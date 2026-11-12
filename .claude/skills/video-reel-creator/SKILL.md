---
name: video-reel-creator
description: Creates short vertical marketing reels (Instagram/TikTok/YouTube Shorts, 9:16) for Vehicle Transport, an auto transport / vehicle shipping company (moves customers' cars coast-to-coast and locally via carrier truck — not a passenger car service), and similar transport/logistics businesses — turns user-supplied photos/clips into a rendered rough-cut video with optional voiceover narration, plus a shot-by-shot script and storyboard. Use whenever the user asks to "make a reel," "turn these photos/clips into a reel," "create a short-form video," wants voiceover/narration added, or wants a promo video ending in a CTA like "call now," "get a free quote," or targeting a specific customer segment (military PCS, dealers, snowbirds, students, corporate relocation, online vehicle buyers). Also use for just the script/storyboard/voiceover script (no footage yet), or editing an existing video into a highlight reel. Trigger proactively for any short-form vertical marketing video request, even without the word "reel."
---

# Video Reel Creator

Turns a handful of photos/clips (and, optionally, no footage at all yet)
into two deliverables for a transportation/travel business's marketing:

1. **A rendered rough-cut vertical video** (1080x1920 mp4) with Ken Burns
   motion on photos, burned-in captions, and a call-to-action end-card.
2. **A shot-by-shot script/storyboard** (markdown) the user can hand to a
   videographer, editor, or use themselves — useful on its own even when
   no rendering happens.

Always produce the storyboard. Only render video when the user has
supplied actual photos/clips (uploaded files) — don't fabricate or
stock-source imagery.

**Default brand:** unless told otherwise, the business is **Vehicle
Transport**, an auto transport / vehicle shipping company (moves cars
via carrier truck, coast-to-coast and locally — customers don't ride in
the vehicle). Read `references/brand_profile.md` before writing any
storyboard or copy — it has the real tagline, phone number, audience
segments, per-segment messaging, tone, and default CTAs pulled from the
business's actual lead-gen plan and live ad creative. Don't default to
generic "Book Now" chauffeur-service language; this brand's CTA is
"Call Now" / "Get a Free Quote."

## Workflow

### 1. Figure out what the user has and wants

Check `/mnt/user-data/uploads` for supplied photos/clips first — don't
ask the user to describe files that are already there.

Clarify only what's missing and needed:
- **Business/service being promoted**, **which audience segment** this
  reel targets (see `references/brand_profile.md` — military, dealers,
  households, students, snowbirds, corporate, or online buyers each get
  different messaging), and the **CTA** to end on. Don't ask if it's
  obvious from context.
- **Do they have footage to work with, or do they want a script only**
  (for footage that doesn't exist yet)?
- If they have footage: is it photos, video clips, or both?

Don't over-ask — if the request is specific enough to proceed (e.g. "make
a reel from these 5 photos, CTA is 'Get a Free Quote'"), just go.

### 2. Write the storyboard/script first

Always do this step, even when rendering. Use the template in
`references/storyboard_template.md`. This forces a clear shot order,
timing, and copy before touching ffmpeg — much faster to revise text in
markdown than to re-render video.

Deliver this as a markdown file via the docx or md artifact convention
(a standalone document the user will reuse/share — save it as a file,
don't just paste it inline).

### 3. Voiceover (if the user wants narration)

This sandbox has no network access and no TTS engine, so Claude cannot
generate spoken audio directly. Instead:

1. The storyboard (step 2) already includes a per-shot narration column
   and a continuous voiceover script block — write real narration lines
   there, don't leave them as placeholders.
2. Tell the user they need to turn that script into an audio file
   themselves: record it (phone voice memo is fine), or generate it in
   a TTS tool (ElevenLabs, CapCut's voice generator, Descript, etc.),
   then upload the resulting audio file.
3. Once they've uploaded a voiceover file, set `voiceover_path` in
   `reel_config.json` to it and re-render (step 4). Background music
   automatically ducks to a lower volume when a voiceover is present —
   see `references/config_schema.md` for the mixing details.

Don't block rendering the visual-only version while waiting on a
voiceover — render captions/music first, then re-render with voice once
the audio file is in hand.

### 4. Render the rough-cut (only if footage was supplied)

1. Read `references/config_schema.md` for the full JSON schema.
2. Build a `reel_config.json` that mirrors the approved storyboard:
   one segment per shot, with `text` matching the on-screen text column,
   durations matching the timing column, and an `endcard` block using
   the chosen CTA.
3. Run:
   ```bash
   python3 scripts/render_reel.py --config reel_config.json --out /mnt/user-data/outputs/reel.mp4
   ```
4. Sanity-check the render before presenting it:
   ```bash
   ffprobe -v error -show_entries format=duration -show_entries stream=width,height -of default=noprint_wrappers=1 /mnt/user-data/outputs/reel.mp4
   ```
   Confirm it's 1080x1920 and the duration matches the sum of segment
   durations + endcard. Optionally extract a frame or two with
   `ffmpeg -ss <t> -frames:v 1 frame.png` and view it to confirm text is
   legible and not clipped off-frame.
5. Present both the storyboard file and the rendered video with
   `present_files`.

If something looks wrong (jittery zoom, clipped text, wrong crop), see
`references/ffmpeg_notes.md` before hand-rolling a different ffmpeg
command — it covers the common failure modes and how the script already
handles them.

### 5. Editing an existing longer video into a highlight reel

If the user supplies one existing video (not photos) and wants it cut
down:
1. Use `ffprobe` to check duration/resolution first.
2. Ask (or infer from the user's framing) which moments matter — or, if
   they just say "make it a highlight reel," use `ffmpeg` to inspect at
   a few evenly-spaced timestamps (extract frames) to identify likely
   good moments (arrivals, close-ups, action) rather than guessing
   blindly.
3. Build `reel_config.json` with `"type": "clip"` segments, each with a
   `start` timestamp and `duration` pulled from the source video, plus
   the same text-overlay and end-card treatment as above.

## Things this skill does NOT do

- **Cannot source stock music, footage, or synthesize voiceover audio.**
  No network access and no TTS engine in this environment. Music and
  voiceover both require the user to supply an audio file (`music_path`
  / `voiceover_path`); Claude's role is writing the narration script,
  not producing the audio itself.
- **Cannot post directly to social platforms.** Deliver the file; the
  user uploads it themselves.
- **Does not fabricate photos/video of the user's business.** If they
  don't have footage yet, produce the storyboard only and say so.

## Reference files

- `references/brand_profile.md` — Vehicle Transport's real tagline, phone
  number, audience segments, messaging, tone, and default CTAs; read this
  before writing any storyboard
- `references/config_schema.md` — full JSON schema for `reel_config.json`,
  read before building a config
- `references/storyboard_template.md` — the markdown template for the
  script/storyboard deliverable
- `references/ffmpeg_notes.md` — how the render pipeline works internally,
  common failure modes, and how to extend it (transitions, keeping clip
  audio, etc.)
