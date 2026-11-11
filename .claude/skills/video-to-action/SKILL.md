---
name: "video-to-action"
description: "Extracts actionable steps, procedures, and checklists from a YouTube video by sending the URL to Gemini for multimodal (video+audio) analysis, with an automatic transcript-only fallback. Use this whenever the user pastes a YouTube link and wants the steps, procedure, tutorial content, or key takeaways pulled out — e.g. \"extract the steps from this video\", \"what does this tutorial say to do\", \"turn this into a checklist\", \"summarize the actions in this video\". Also trigger for requests to analyze a YouTube video's content even if the word \"steps\" isn't used."
---


# Video to Action

Turns a YouTube video into an actionable summary (steps, key details, caveats) by sending the URL directly to Gemini, which can natively ingest YouTube links and analyze both the visual and audio content — no need to download the video.

## When to use this

Trigger whenever the user shares a YouTube URL and wants to extract usable content from it: steps in a tutorial, a procedure demonstrated on screen, a checklist, or a summary of what to actually do. This is different from just asking "what is this video about" in the abstract — the goal is actionable output someone could follow to replicate what's shown.

## Prerequisites

- `GEMINI_API_KEY` environment variable must be set. Get a free key at https://aistudio.google.com/apikey. If it's missing, tell the user how to get one and set it rather than guessing or failing silently.
- `pip install google-genai --break-system-packages`
- Optional, only needed for `--quick` mode or as a fallback: `pip install youtube-transcript-api --break-system-packages`

## How to run it

1. Write the script below to a file, e.g. `video_to_action.py`.
2. Run it against the user's URL:
   ```
   python video_to_action.py "<youtube_url>"
   ```
3. For a faster, cheaper, audio-only pass (skips full video analysis), or if the user explicitly wants just the transcript summarized:
   ```
   python video_to_action.py "<youtube_url>" --quick
   ```
4. If full video analysis fails for any reason (private video, region lock, API error), the script automatically falls back to transcript-only analysis and prints a note to stderr saying it did so. Pass that note along to the user so they know the analysis was audio-only (meaning any purely visual steps, like an on-screen setting with no verbal description, may be missing).
5. Present the output to the user as-is — it already follows a clean structure (Summary / Steps / Key Details / Watch Out For). Don't re-summarize it further unless asked.

## The script

```python
#!/usr/bin/env python3
"""
video_to_action.py

Sends a YouTube video to Gemini for multimodal analysis (visual + audio) and
extracts a structured, actionable summary: steps, procedure, key details,
and things to watch out for. Falls back to transcript-only analysis if full
video analysis fails, or if --quick is passed.

Requires:
    pip install google-genai --break-system-packages
    (optional, for --quick / fallback) pip install youtube-transcript-api --break-system-packages

Environment:
    GEMINI_API_KEY must be set (free key: https://aistudio.google.com/apikey)

Usage:
    python video_to_action.py <youtube_url>
    python video_to_action.py <youtube_url> --quick
"""

import argparse
import os
import re
import sys


PROMPT = """You are analyzing a video (or its transcript) to extract actionable content for someone who wants to actually DO what's shown, not just understand it conceptually.

Produce output in this exact structure:

## Summary
2-3 sentences on what this video covers.

## Steps / Procedure
A numbered list of the concrete steps shown or described, in the order they should be performed. Be specific: include exact settings, values, tool names, or commands mentioned. If the video isn't procedural (e.g. a discussion or review), list the key actionable takeaways instead.

## Key Details
Specific numbers, thresholds, tool names, links, or warnings mentioned that someone would need to replicate this correctly.

## Watch Out For
Caveats, common mistakes, or "don't do this" moments the video calls out.

Be concrete and skip filler. If a step depends on something shown visually (a UI element, an on-screen value) that isn't stated verbally, and you only had the transcript, flag that as uncertain.
"""


def extract_video_id(url: str) -> str:
    patterns = [
        r"(?:v=|/videos/|embed/|youtu\.be/|/v/|/shorts/)([0-9A-Za-z_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    raise ValueError(f"Could not extract a YouTube video ID from: {url}")


def analyze_with_video(youtube_url: str, api_key: str) -> str:
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=types.Content(
            parts=[
                types.Part(file_data=types.FileData(file_uri=youtube_url)),
                types.Part(text=PROMPT),
            ]
        ),
    )
    return response.text


def analyze_with_transcript(youtube_url: str, api_key: str) -> str:
    from youtube_transcript_api import YouTubeTranscriptApi
    from google import genai

    video_id = extract_video_id(youtube_url)
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    transcript_text = " ".join(chunk["text"] for chunk in transcript_list)

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"{PROMPT}\n\n--- TRANSCRIPT (audio-only, no visual context) ---\n\n{transcript_text}",
    )
    return response.text


def main():
    parser = argparse.ArgumentParser(description="Extract actionable steps from a YouTube video via Gemini.")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("--quick", action="store_true", help="Skip video analysis, use transcript only (faster, cheaper, audio-only).")
    args = parser.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable is not set.", file=sys.stderr)
        print("Get a free key at https://aistudio.google.com/apikey", file=sys.stderr)
        sys.exit(1)

    if args.quick:
        print(analyze_with_transcript(args.url, api_key))
        return

    try:
        print(analyze_with_video(args.url, api_key))
    except Exception as e:
        print(f"[Full video analysis failed ({e}), falling back to transcript-only]\n", file=sys.stderr)
        try:
            print(analyze_with_transcript(args.url, api_key))
        except Exception as e2:
            print(f"Error: both video analysis and transcript fallback failed.\nVideo error: {e}\nTranscript error: {e2}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
```

## Notes

- Gemini ingests the YouTube URL natively (no download/upload step needed), so this works for any public YouTube video within Gemini's supported length limits.
- Private, unlisted-but-restricted, or region-locked videos may fail full analysis — that's exactly when the transcript fallback kicks in.
- If the user just wants a quick gist rather than a structured breakdown, `--quick` is faster and cheaper since it skips video/audio processing entirely.

