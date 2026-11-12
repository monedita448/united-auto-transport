#!/usr/bin/env python3
"""
render_reel.py — Build a vertical (9:16) marketing reel from a mix of
photos and video clips, with Ken Burns motion on photos, per-segment
text overlays, and an end-card call-to-action.

Usage:
  python render_reel.py --config reel_config.json --out /path/to/output.mp4

See references/config_schema.md for the full JSON schema and
references/ffmpeg_notes.md for how the ffmpeg graph is built.
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile

W, H = 1080, 1920  # vertical 9:16
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def run(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("CMD FAILED:", " ".join(cmd), file=sys.stderr)
        print(result.stderr, file=sys.stderr)
        raise SystemExit(1)
    return result


def escape_text(s):
    # ffmpeg drawtext needs these escaped
    return (
        s.replace("\\", "\\\\")
        .replace(":", "\\:")
        .replace("'", "\u2019")
        .replace("%", "\\%")
    )


def build_photo_segment(photo_path, duration, zoom_direction, tmpdir, idx):
    """Ken Burns: slow zoom/pan on a still photo, output as a silent clip."""
    out = os.path.join(tmpdir, f"seg_{idx:02d}.mp4")
    fps = 30
    frames = int(duration * fps)
    # zoompan needs an oversized input to avoid jitter; scale up first
    if zoom_direction == "in":
        zexpr = "zoom+0.0018"
        z_start = 1.0
    else:  # "out"
        zexpr = "if(lte(zoom\\,1.0)\\,1.15\\,zoom-0.0018)"
        z_start = 1.15
    vf = (
        f"scale=3240:5760:force_original_aspect_ratio=increase,"
        f"crop=3240:5760,"
        f"zoompan=z='{zexpr}':d={frames}:s={W}x{H}:fps={fps},"
        f"setsar=1"
    )
    run([
        "ffmpeg", "-y", "-loop", "1", "-i", photo_path,
        "-vf", vf, "-t", str(duration),
        "-c:v", "libx264", "-pix_fmt", "yuv420p", out,
    ])
    return out


def build_clip_segment(clip_path, duration, tmpdir, idx, start=0):
    """Trim/crop a video clip to fill the vertical frame."""
    out = os.path.join(tmpdir, f"seg_{idx:02d}.mp4")
    vf = (
        f"scale={W}:{H}:force_original_aspect_ratio=increase,"
        f"crop={W}:{H},setsar=1,fps=30"
    )
    cmd = ["ffmpeg", "-y", "-ss", str(start), "-i", clip_path,
           "-t", str(duration), "-vf", vf, "-an",
           "-c:v", "libx264", "-pix_fmt", "yuv420p", out]
    run(cmd)
    return out


def add_text_overlay(seg_path, tmpdir, idx, lines, position="bottom",
                      is_endcard=False, bg_box=True):
    """Burn text onto a segment. `lines` is a list of (text, fontsize)."""
    out = os.path.join(tmpdir, f"seg_{idx:02d}_txt.mp4")
    filters = []
    if position == "bottom":
        base_y = "h-h*0.22"
    elif position == "top":
        base_y = "h*0.08"
    else:  # center (used for end-card)
        base_y = "(h-text_h)/2"

    for i, (text, size) in enumerate(lines):
        esc = escape_text(text)
        y_expr = f"{base_y}+{i*int(size*1.25)}" if position != "center" \
            else f"{base_y}+{(i-len(lines)/2)*int(size*1.3)}"
        box = "1" if bg_box else "0"
        filters.append(
            f"drawtext=fontfile={FONT}:text='{esc}':fontsize={size}:"
            f"fontcolor=white:box={box}:boxcolor=black@0.45:boxborderw=18:"
            f"x=(w-text_w)/2:y={y_expr}"
        )
    vf = ",".join(filters)
    run(["ffmpeg", "-y", "-i", seg_path, "-vf", vf,
         "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "copy", out])
    return out


def build_endcard(tmpdir, idx, duration, cta_text, sub_text, brand_text,
                   bg_color="0x1a1a2e"):
    out = os.path.join(tmpdir, f"seg_{idx:02d}.mp4")
    run([
        "ffmpeg", "-y", "-f", "lavfi",
        "-i", f"color=c={bg_color}:s={W}x{H}:d={duration}:r=30",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", out,
    ])
    lines = [(cta_text, 88), (sub_text, 52)]
    if brand_text:
        lines.append((brand_text, 40))
    return add_text_overlay(out, tmpdir, idx, lines, position="center",
                             is_endcard=True)


def concat_segments(segment_paths, out_path, tmpdir):
    list_file = os.path.join(tmpdir, "concat_list.txt")
    with open(list_file, "w") as f:
        for p in segment_paths:
            f.write(f"file '{os.path.abspath(p)}'\n")
    run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", list_file,
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
        out_path,
    ])


def add_audio_tracks(video_path, out_path, music_path=None, voice_path=None,
                      music_volume=0.5, voice_volume=1.0):
    """Mix an optional voiceover (full volume, foreground) with optional
    background music (ducked lower) onto the (silent) rendered video.
    If neither is supplied, just copies the video through unchanged."""
    if not music_path and not voice_path:
        shutil.copy(video_path, out_path)
        return

    inputs = ["-i", video_path]
    filter_parts = []
    audio_labels = []
    next_idx = 1

    if voice_path:
        inputs += ["-i", voice_path]
        # apad extends with silence if the voiceover is shorter than the
        # video; global -shortest below caps total output to video length
        filter_parts.append(f"[{next_idx}:a]volume={voice_volume},apad[voice]")
        audio_labels.append("[voice]")
        next_idx += 1

    if music_path:
        inputs += ["-stream_loop", "-1", "-i", music_path]
        filter_parts.append(f"[{next_idx}:a]volume={music_volume}[music]")
        audio_labels.append("[music]")
        next_idx += 1

    if len(audio_labels) == 2:
        filter_parts.append(
            f"{audio_labels[0]}{audio_labels[1]}amix=inputs=2:"
            f"duration=first:dropout_transition=0[a]"
        )
    else:
        filter_parts.append(f"{audio_labels[0]}anull[a]")

    filter_complex = ";".join(filter_parts)
    run([
        "ffmpeg", "-y", *inputs,
        "-filter_complex", filter_complex,
        "-map", "0:v", "-map", "[a]", "-shortest",
        "-c:v", "copy", "-c:a", "aac", "-movflags", "+faststart",
        out_path,
    ])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    with open(args.config) as f:
        cfg = json.load(f)

    tmpdir = tempfile.mkdtemp(prefix="reel_")
    segment_paths = []

    try:
        for idx, seg in enumerate(cfg["segments"]):
            duration = seg.get("duration", 2.5)
            if seg["type"] == "photo":
                raw = build_photo_segment(
                    seg["path"], duration,
                    seg.get("zoom", "in"), tmpdir, idx,
                )
            elif seg["type"] == "clip":
                raw = build_clip_segment(
                    seg["path"], duration, tmpdir, idx,
                    start=seg.get("start", 0),
                )
            else:
                raise ValueError(f"Unknown segment type: {seg['type']}")

            if seg.get("text"):
                lines = [(seg["text"], seg.get("text_size", 64))]
                if seg.get("subtext"):
                    lines.append((seg["subtext"], seg.get("subtext_size", 42)))
                raw = add_text_overlay(
                    raw, tmpdir, idx, lines,
                    position=seg.get("text_position", "bottom"),
                )
            segment_paths.append(raw)

        if cfg.get("endcard"):
            ec = cfg["endcard"]
            idx = len(cfg["segments"])
            ec_path = build_endcard(
                tmpdir, idx, ec.get("duration", 3.0),
                ec["cta_text"], ec.get("sub_text", ""),
                ec.get("brand_text", ""),
                ec.get("bg_color", "0x1a1a2e"),
            )
            segment_paths.append(ec_path)

        silent_out = os.path.join(tmpdir, "silent_full.mp4")
        concat_segments(segment_paths, silent_out, tmpdir)

        music_path = cfg.get("music_path")
        if music_path and not os.path.exists(music_path):
            print(f"WARNING: music_path not found, skipping: {music_path}", file=sys.stderr)
            music_path = None

        voice_path = cfg.get("voiceover_path")
        if voice_path and not os.path.exists(voice_path):
            print(f"WARNING: voiceover_path not found, skipping: {voice_path}", file=sys.stderr)
            voice_path = None

        # default music lower when a voiceover is present so it doesn't compete
        default_music_vol = 0.15 if voice_path else 0.5
        add_audio_tracks(
            silent_out, args.out,
            music_path=music_path, voice_path=voice_path,
            music_volume=cfg.get("music_volume", default_music_vol),
            voice_volume=cfg.get("voice_volume", 1.0),
        )

        print(f"Rendered reel: {args.out}")
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


if __name__ == "__main__":
    main()
