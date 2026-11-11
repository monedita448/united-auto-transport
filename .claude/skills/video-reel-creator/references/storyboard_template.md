# Storyboard / script template

Always produce this as a markdown deliverable alongside (or instead of)
the rendered video. It's the artifact a user hands to a videographer,
freelance editor, or uses to film new footage themselves.

```markdown
# Vehicle Transport — Reel Script: "[Working Title]"

**Segment:** e.g. Household/residential moves
**Goal:** drive calls/quote-requests for cross-country auto shipping
**Platform:** Instagram Reels / TikTok / YouTube Shorts (1080x1920, 9:16)
**Target length:** 20–30 seconds
**CTA:** Call Now / Get a Free Quote (see `brand_profile.md` — this
brand does NOT use "Book Now," it's not a passenger service)

## Shot list

| # | Duration | Shot | On-screen text | Voiceover (narration) | Notes |
|---|----------|------|-----------------|------------------------|-------|
| 1 | 0:00–0:03 | Car carrier truck loaded with vehicles, on the highway | "Moving cross-country?" | "Moving cross-country? Skip the road trip." | Match existing brand look: dark text box, bold white text |
| 2 | 0:03–0:06 | Close-up: vehicle being secured/loaded onto carrier | "Safe. Insured. Tracked." | "Your car, shipped safely and insured, every mile." | |
| 3 | 0:06–0:10 | Empty driveway → car arriving at new home (before/after) | "Coast-to-coast & local" | "Coast to coast, or just across town." | |
| 4 | 0:10–0:14 | Carrier truck driving, wide shot | "" | (let it breathe, no narration) | |
| 5 | 0:14–0:18 | Vehicle delivered, owner relieved/happy | "On time, every time." | "On time, every time — that's the promise." | |
| End card | 0:18–0:22 | Solid dark background + CTA | "Call Now (972) 833-2614" / "Get a Free Quote" | "Call Vehicle Transport today at 972-833-2614." | Match brand end-card defaults in `brand_profile.md` |

## Voiceover script (full narration, read straight through)

> [0:00] Moving cross-country? Skip the road trip. [0:03] Your car,
> shipped safely and insured, every mile. [0:06] Coast to coast, or
> just across town. [0:14] On time, every time — that's the promise.
> [0:18] Call Vehicle Transport today at 972-833-2614.

Once the user has a voiceover audio file (recorded or TTS-generated),
set `voiceover_path` in `reel_config.json` and re-render — see
`config_schema.md` for details.

## Captions (for the platform post, not on-screen text)

- **Hook line (first 125 characters, shown before "more"):** ...
- **Full caption:** ...
- **Hashtags:** 3–8, mix of broad + niche + local, and segment-specific
  where relevant (e.g. #AutoTransport #CarShipping #PCSMove
  #SnowbirdLife — pick per the segment this reel targets)

## Music/audio direction

Describe the mood (upbeat/corporate/chill), not a specific copyrighted
track — e.g. "light acoustic guitar, mid-tempo, optimistic." Suggest the
user pick a licensed track in-app (Instagram/TikTok's audio library)
since we can't source or embed real music here.

## Production notes

- Keep key text/subjects inside the center-safe 1080x1420 area — the top
  and bottom ~250px get covered by platform UI (profile name, captions,
  like/share buttons).
- Vertical 9:16, minimum 1080x1920, 30fps.
- If filming new footage: prioritize the carrier truck/vehicle loading
  process, the vehicle in transit, and the moment of safe
  arrival/relief — these convert better than generic road b-roll. Trust
  signals (insured, tracked, on-time) should be visible or stated, not
  implied.
```

Adapt the shot count and headline copy to the segments actually being
produced (rendered from real assets have real shot descriptions;
purely-planned/unfilmed reels can use production notes instead).
