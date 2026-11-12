# reel_config.json schema

Passed to `scripts/render_reel.py --config <this file> --out <output.mp4>`.

```json
{
  "segments": [
    {
      "type": "photo",              // "photo" or "clip"
      "path": "path/to/file.jpg",   // absolute or relative to cwd
      "duration": 2.5,              // seconds this segment is on screen
      "zoom": "in",                 // photos only: "in" or "out" (Ken Burns)
      "start": 0,                   // clips only: trim start point (seconds)
      "text": "Reliable rides, every time",   // optional caption
      "subtext": "",                          // optional second line
      "text_size": 64,
      "subtext_size": 42,
      "text_position": "bottom"     // "bottom" | "top" | "center"
    }
  ],
  "endcard": {
    "duration": 3.0,
    "cta_text": "Call Now (972) 833-2614",
    "sub_text": "Call or tap the link to reserve",
    "brand_text": "@YourTransportCo",
    "bg_color": "0x1a1a2e"          // hex color, ffmpeg lavfi format
  },
  "music_path": "assets/background_music.mp3",  // optional, omit if none
  "music_volume": 0.5,           // ignored default (0.15) auto-applies if voiceover_path is set
  "voiceover_path": "assets/voiceover.mp3",  // optional narration track, full volume
  "voice_volume": 1.0
}
```

## Notes

- **Segment order = playback order.** Total reel length = sum of segment
  durations + endcard duration.
- **Photos** get an automatic slow zoom (Ken Burns effect) so a static
  image doesn't feel dead on screen. Alternate `"in"`/`"out"` across
  segments so the motion doesn't feel repetitive.
- **Clips** are cropped/scaled to fill the 1080x1920 frame (center-crop).
  If a clip has useful audio (e.g. ambient sound, testimonial dialogue),
  don't set `music_path`, or lower `music_volume` — the current script
  strips clip audio by default (`-an`) to keep the mix clean and
  predictable; see `ffmpeg_notes.md` if the user wants to preserve
  original clip audio instead.
- **`music_path`**: this environment cannot fetch royalty-free music from
  the web (no network access in the sandbox). If the user hasn't
  uploaded a music file themselves, omit `music_path` — the reel renders
  silent, and you should tell the user to add music in CapCut/Instagram/
  TikTok's native editor after downloading, which have built-in licensed
  audio libraries. Never source or embed music from an unverified origin.
- **Recommended total length** for a marketing reel: 15–30 seconds
  (roughly 5-9 segments at 2-3s each, plus a 3s end-card). Shorter reels
  generally get better completion rates.

## Voiceover (`voiceover_path`)

This sandbox has no network access and no text-to-speech engine, so
Claude cannot synthesize narration audio directly. The workflow is:

1. Claude writes a timed narration script (see the "Voiceover script"
   section of `storyboard_template.md`), matched to segment timing.
2. The user turns that into an audio file themselves — recording it,
   or generating it in a TTS tool (ElevenLabs, CapCut's voice generator,
   Descript, etc.) — and uploads the resulting audio file.
3. Claude sets `voiceover_path` to that file and re-renders. The script
   automatically pads short voiceovers with silence and trims long ones
   to the video length, and ducks `music_volume` down to 0.15 by default
   so the voice stays intelligible.

If no voiceover file is supplied, just omit `voiceover_path` — the reel
renders with captions/music only, which is a perfectly good deliverable
on its own.
