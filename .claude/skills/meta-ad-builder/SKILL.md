---
name: "meta-ad-builder"
description: "Publishes finished creatives as PAUSED Meta (Facebook/Instagram) ads, writes multi-variant ad copy, and pulls top ads by ROAS or competitor ads from the Ad Library. Use to deploy/launch a creative to Meta."
---

# Meta ad builder

Turn a finished creative — typically the output of a generative-AI skill in this
workspace — into a live Meta ad. The skill covers three phases: **research**
(optional) → **copy** → **deploy**. It talks to the Meta Marketing API directly
via ported, parameterized Python scripts.

## Bundled files and connector (read first)

- This skill comes from **https://github.com/krusemediallc/arcads-claude-code**, folder `shared/skills/meta-ad-builder/`. Every relative path below (`scripts/...`, `prompting/...`, `reference/...`) is inside that folder. If the files are not next to this SKILL.md, clone the repo (`git clone --depth 1 https://github.com/krusemediallc/arcads-claude-code`) and run the scripts from `arcads-claude-code/shared/skills/meta-ad-builder/`.
- **If a Meta Ads connector is connected in the session** (tools such as `ads_get_ad_accounts`, `ads_create_creative`, `ads_create_ad`, `ads_creative_upload_media`, `ads_library_search`, `ads_insights_*`), prefer those tools over the Python scripts and `META_ACCESS_TOKEN`. Keep every safety rule below: ads are created PAUSED, show the full payload and get a go-ahead before creating anything, confirm the ad set and destination URL.

## When to use this skill

Trigger on phrases like:
- "deploy this video to Meta" / "publish this as a Facebook ad"
- "build/launch a Meta ad" / "push this creative into <ad set>"
- "create a Meta ad with this image and copy"
- "pull my top-performing ads" / "what are my best ads by ROAS"
- "research competitor ads" / "pull <brand>'s ads from the Ad Library"

Do **not** use this skill to *generate* creative — that's `arcads-external-api`,
`chatgpt-image-ad`, `pixar-style-ad`, `claymation-ad`, `generate-youtube-thumbnail`, etc. This skill is the
*direct Meta Marketing API* deployment step.

## Read order

1. **This file** — workflow, decision tree, safety rules.
2. **[prompting/copy-guide.md](prompting/copy-guide.md)** — the 5-body / 5-title /
   3-description frameworks and the `--copy-file` JSON shape.
3. **[reference/deploy-patterns.md](reference/deploy-patterns.md)** — creative
   spec mechanics, video polling, retry, failure modes.
4. **[reference/meta-api-cheatsheet.md](reference/meta-api-cheatsheet.md)** — the
   full Meta Marketing API reference (campaigns, ad sets, ads, enums, gotchas,
   Ad Library). Consult as needed; don't read end-to-end.

## Prerequisites

- **Env** (in `.env` — see your repo's `.env.example`):
  - `META_ACCESS_TOKEN` (required) — long-lived token with `ads_management` scope
  - `META_AD_ACCOUNT_ID` (required) — with or without the `act_` prefix
  - `META_PAGE_ID`, `META_IG_USER_ID`, `META_PIXEL_ID` (optional defaults for deploy)
  - `META_API_VERSION` (optional, default `v23.0`)
- **Python deps:** `python3 -m pip install -r scripts/requirements.txt`
- **A target ad set** that already exists. The skill deploys ads into an existing
  ad set — it does not create campaigns or ad sets. If the user needs a new ad
  set, create it in Ads Manager or via the cheatsheet §3–§4 first.
- **The finished creative on disk** — an image or video file path. Chat-pasted
  files are not accessible; ask the user for a real path.

Run `bash scripts/check-meta-env.sh` to verify credentials before anything else.

## Workflow

### Phase 1 — Research (optional, when copy should model winners)

```bash
# Rank the account's ads and pull the winning copy
python scripts/pull-top-ads.py --date-preset last_30d --min-spend 100 --limit 15

# Pull a competitor's ads from the Ad Library
python scripts/pull-competitor-ads.py --pages "BrandName" --limit 50
```

Both write JSON under `OUTPUT_BASE` (or `./outputs/meta-ads/`). Read the top-ad
`copy` fields to identify winning hook/proof/CTA patterns before writing new copy.

### Phase 2 — Copy

Write a `copy.json` following **[copy-guide.md](prompting/copy-guide.md)**:
5 bodies (one per framework angle), 5 titles, 3 descriptions. If Phase 1 ran,
mirror the voice and patterns of the winners — new creative + proven copy DNA.
Save `copy.json` somewhere under `outputs/` so it isn't committed.

### Phase 3 — Deploy

**Always dry-run first** — it prints the full creative payload, makes no API calls:

```bash
python scripts/deploy-ad.py --dry-run \
  --adset-id <AD_SET_ID> --copy-file copy.json --link <DESTINATION_URL> \
  --image path/to/creative.png
```

Review the payload with the user, then deploy for real:

```bash
python scripts/deploy-ad.py \
  --adset-id <AD_SET_ID> --copy-file copy.json --link <DESTINATION_URL> \
  --video clip-a.mp4 --video clip-b.mp4 --cta SIGN_UP --pixel-id <PIXEL_ID>
```

- `--image` / `--video` are repeatable — each becomes its own ad in the ad set.
- Every ad is created **PAUSED**. Tell the user to review and un-pause in Meta
  Ads Manager. The skill never launches a spending ad automatically.
- Results (ad IDs) are written to `deployment_results.json` under `OUTPUT_BASE`.

## Decision tree

| User intent | Phases |
|---|---|
| "Deploy this creative to Meta" + copy provided | Phase 3 only |
| "Build a Meta ad, write the copy too" | Phase 2 → 3 |
| "Make ads modeled on my winners" | Phase 1 → 2 → 3 |
| "What are my best ads / competitor research" | Phase 1 only |

## Safety rules

- **Ads deploy PAUSED.** Never add an `--active` override or un-pause ads without
  an explicit user instruction. Confirm the user knows the ads are paused.
- **Dry-run before every real deploy.** Show the payload; get a go-ahead.
- **Confirm the target ad set and destination URL** with the user before
  deploying — an ad in the wrong ad set spends against the wrong budget.
- **Deploying ads is a shared-state, money-adjacent action.** Treat the live
  `deploy-ad.py` run as something to confirm, not assume.
- The skill creates ads only — it does **not** create or edit campaigns, ad sets,
  budgets, or audiences. Those stay manual.

## Quirks and pitfalls

- **Video processing is async.** `deploy-ad.py` polls the uploaded video until
  Meta finishes processing before creating the ad — a video deploy can take a
  few minutes. See [deploy-patterns.md](reference/deploy-patterns.md).
- **Transient `OAuthException` (code 2).** Retried automatically with backoff.
- **`act_` prefix** is added automatically if missing from `META_AD_ACCOUNT_ID`.
- **Account-specific data stays out of git.** All output routes through
  `outputs/` (gitignored): ad IDs, pulled spend/revenue, competitor data.
- **Special Ad Categories** (credit, employment, housing, social issues) change
  ad-set targeting rules — flag to the user; see cheatsheet §3.5.

## Cost note

The Meta Marketing API itself is free to call. **Ad spend is real money** — but
because every ad deploys PAUSED, nothing spends until the user un-pauses it in
Ads Manager. There are no per-call credits to estimate.