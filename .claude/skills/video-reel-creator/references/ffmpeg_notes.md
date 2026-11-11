# ffmpeg implementation notes

Background on how `scripts/render_reel.py` works, for when you need to
debug a failure or extend it.

## Pipeline

1. Each segment (photo or clip) is rendered to its own short silent
   `.mp4` in a temp dir.
   - Photos: oversampled 3x then `zoompan` for a smooth Ken Burns
     zoom in/out, cropped/scaled to fill 1080x1920.
   - Clips: scaled+cropped to fill 1080x1920 (center-crop), trimmed to
     the requested duration, audio stripped (`-an`).
2. If the segment has `text`/`subtext`, `drawtext` burns it in with a
   semi-transparent box behind it for legibility over any background.
3. An optional end-card is generated from a solid color background
   (`lavfi color=`) with centered CTA/subtext/brand text.
4. All segments are concatenated with the ffmpeg `concat` demuxer
   (`-f concat`) — this requires every segment to have matching codec/
   resolution/pix_fmt, which is why every stage re-encodes to
   `libx264` / `yuv420p` at 1080x1920.
5. If `music_path` is set, it's looped under the full video with
   `-stream_loop -1` and mixed at `music_volume`, trimmed to match
   video length with `-shortest`.

## Common issues

- **"Unrecognized option" / filter errors on drawtext**: text containing
  `:`, `'`, or `%` must go through `escape_text()` — this is already
  handled in the script, but if you hand-edit ffmpeg commands directly,
  remember to escape these.
- **Jittery zoompan**: caused by zoompan operating on the native
  (small) input resolution. The script oversamples to 3240x5760 first
  — don't remove that scale step.
- **Clip has useful audio the user wants to keep**: change
  `build_clip_segment` to drop `-an`, and instead of the global
  `add_music` step, mix per-segment audio in the concat step. This is a
  bigger change — for a one-off, simplest is to render without music
  and tell the user to layer clip audio + music in CapCut/Premiere.
- **Render is slow**: each photo re-encode is the slow part (zoompan +
  libx264). For a quick draft/preview, drop resolution to 540x960 in
  the script's `W, H` constants, render, then re-render at full res
  once the user approves the cut.
- **Vertical crop cuts off the subject**: `crop=W:H` center-crops by
  default. For off-center subjects, add explicit `x`/`y` crop offsets
  per-segment (would need a config field like `"crop_focus": "top"` —
  not currently in the schema; add it if a user needs it repeatedly).

## Extending

If a user wants transitions (crossfade, wipe) between segments instead
of hard cuts, replace the `concat` demuxer step with `xfade` filter
chains — but note this requires knowing exact segment durations up
front and re-timing the whole chain, so it's meaningfully more complex.
Only build this if a user specifically asks for it.
