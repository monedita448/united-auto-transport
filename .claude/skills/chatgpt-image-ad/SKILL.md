---
name: "chatgpt-image-ad"
description: "Generates static Meta image-ad creatives with ChatGPT Image 2 (gpt-image-2) via the Arcads API: typography-heavy, dense-text and UI-mimicry ads (chat threads, comparison tables, iOS dialogs, notes lists)."
---

# chatgpt-image-ad (Arcads)

Generate one or more **standalone Meta ad image creatives** via Arcads' `POST /v2/images/generate` with `model: "gpt-image-2"`. Hands the image paths off to the `meta-ad-builder` skill — this skill does not upload to Meta itself.

## Bundled files (read first)

This skill comes from **https://github.com/krusemediallc/arcads-claude-code**. If the files below are not available locally, clone the repo (`git clone --depth 1 https://github.com/krusemediallc/arcads-claude-code`) and resolve paths against it:

- The helper script is at `arcads-claude-code/skills/chatgpt-image-ad/scripts/generate_image.py` (use that path wherever this file says `~/.claude/skills/chatgpt-image-ad/scripts/generate_image.py`).
- Links that start with `shared/...` or `../../shared/...` resolve to `arcads-claude-code/shared/...`.
- The Arcads API host (`external-api.arcads.ai`) must be reachable. If the shell gets a proxy/403 or connection error, run the script on the user's own computer (device shell or Claude Code locally) and say so plainly.

## Read order

1. **This file** — Arcads-specific endpoint, auth, presigned upload flow, workflow phases.
2. **[shared/skills/chatgpt-image-ad/prompting/guide.md](../../shared/skills/chatgpt-image-ad/prompting/guide.md)** — model-specific prompting (what gpt-image-2 is good/bad at, when to switch to nano-banana).
3. **[shared/skills/image-ad-prompting/prompting/prompt-library.md](../../shared/skills/image-ad-prompting/prompting/prompt-library.md)** — 30+ validated templates with per-model notes.
4. **[shared/skills/image-ad-prompting/prompting/safety-suffixes.md](../../shared/skills/image-ad-prompting/prompting/safety-suffixes.md)** — the 3 always-on guards.
5. **[scripts/generate_image.py](scripts/generate_image.py)** — the helper script (Python stdlib only).

## Hard rules — never relax

1. **Model is `gpt-image-2`.** The script refuses any other value. If the user asks for nano-banana, use the `arcads-external-api` skill's Nano Banana flow instead.
2. **No platform/screenshot chrome in output.** `NO_CHROME_SUFFIX` is always on (override with `--allow-chrome` only when the ad's concept *requires* chrome — rare).
3. **Edge-safe + glyph-safety suffixes always on** unless `--no-safe-zone` is explicit. They fix real failures; don't remove silently.
4. **Max 5 reference images.** Hard Arcads cap for gpt-image-2 (observed `400 Max 5 reference image(s) allowed`). The script enforces.
5. **No Meta upload from this skill.** Image generation only. Hand off to `meta-ad-builder` via filesystem paths.
6. **Always present a credit-cost estimate before generating** (see `arcads-external-api` skill conventions). Each gpt-image-2 call is one image; multiply by `--n` variants.

## Prerequisites

- `.env` containing `ARCADS_BASIC_AUTH` (preferred, pre-encoded) OR `ARCADS_API_KEY`
- Optional: `PRODUCT_ID`, `PROJECT_ID` in `.env` so generated assets land in the right Arcads dashboard folder (see `arcads-external-api` SKILL.md for the session-folder pattern)
- Reference images on local disk (PNG/JPG/JPEG/WEBP/GIF). The script handles the Arcads presigned-upload flow internally — you pass local paths.

## Configuration

- **Base URL:** `https://external-api.arcads.ai` (or `ARCADS_BASE_URL`).
- **Auth:** HTTP Basic. The script prefers a pre-encoded `ARCADS_BASIC_AUTH` env var (e.g. `Basic ZXhhbXBsZTo=`); falls back to encoding `ARCADS_API_KEY` with an empty password.
- **Endpoint:** `POST /v2/images/generate` (request); `GET /v1/assets/{id}` (poll until `status: generated`); image URL fetched once status flips.
- **Reference uploads:** `POST /v1/file-upload/get-presigned-url` returns `{presignedUrl, filePath}`; `PUT` the bytes to `presignedUrl`; pass the `filePath` string in `referenceImages`. **Each filePath is single-use** — the script re-uploads per variant so parallel runs don't collide.

## Generation modes

| Mode | When to use | Required | Optional |
|---|---|---|---|
| `image` (default) | Generate a brand-new ad image. | `--prompt`, `--aspect-ratio` | `--image-ref` (up to 5) |
| `image_edit` | Modify an existing image (swap colors, change background, add element). | `--prompt`, `--source` | `--image-ref` (up to 5) |

## Supported aspect ratios

`1:1`, `16:9`, `9:16`. **Only these three are accepted by Arcads' `/v2/images/generate` endpoint** (confirmed live: `aspectRatio must be one of the following values: 1:1, 16:9, 9:16`). Templates in the shared library that use `2:3`, `3:2`, `4:5`, etc. won't render at their native ratio on this backend — fall back to `1:1` and crop.

## Inputs the user must provide

| Input | Notes |
|---|---|
| Seed prompt | The creative direction in their words. You will rewrite it (see Phase 3). |
| Aspect ratio | One of the 3 above. Reject anything else. |
| Reference image(s) | Optional but strongly recommended when the ad features a specific product. Up to 5. |
| Variant count `N` | Default 1. Cap at 5. |
| Mode | `image` (default) or `image_edit`. |
| Source image | Required only for `image_edit`. |

## Workflow

### Phase 1: Preflight

1. `.env` exists with `ARCADS_BASIC_AUTH` or `ARCADS_API_KEY`.
2. (Optional) `arcads-external-api` session folder is set up (see that skill's "Session setup" section). If `PRODUCT_ID` / `PROJECT_ID` aren't set, generated assets land in the default project — you can fix later via `POST /v1/assets/add-to-project`.
3. Health-check: `curl -sf -H "$AUTH" "$BASE_URL/v1/products"` returns 200.

### Phase 2: Gather inputs

Collect: seed prompt, mode, source (if edit), reference paths, variant count, aspect ratio.

### Phase 3: Prompt rewrite

Read [shared/skills/image-ad-prompting/prompting/prompt-library.md](../../shared/skills/image-ad-prompting/prompting/prompt-library.md). If the user's brief maps onto a template, **check the Model notes block** — only proceed if `gpt-image-2` is marked clean or preferred. If nano-banana is preferred, suggest switching before generating.

Fill the `{placeholders}` and show the user the rewritten prompt. Ask "Use this, edit it, or start over?" Loop until approved.

For fresh prompts (no template match), follow the structure in [shared/skills/chatgpt-image-ad/prompting/guide.md § Phase 3b](../../shared/skills/chatgpt-image-ad/prompting/guide.md).

### Phase 4: Credit cost confirmation (MANDATORY)

Per `arcads-external-api` conventions: present an estimated credit cost (read from `logs/arcads-api.jsonl` for matching past calls, or `MASTER_CONTEXT.md` rate table). Wait for explicit confirmation before firing.

### Phase 5: Generate

```bash
~/.claude/skills/chatgpt-image-ad/scripts/generate_image.py \
  --prompt "<rewritten>" \
  --aspect-ratio <ratio> \
  --n <N> \
  --image-ref <product.png> \
  [--image-ref <style-board.png>] \
  --out ./generated \
  --env-file .env

# For an edit run:
~/.claude/skills/chatgpt-image-ad/scripts/generate_image.py \
  --mode image_edit \
  --prompt "<edit-instruction>" \
  --source <existing.png> \
  [--image-ref <guidance.png>] \
  --n <N> \
  --out ./generated \
  --env-file .env
```

Each line on stdout is one JSON variant (`variant`, `path`, `asset_id`, `width`, `height`, `prompt`, `mode`, `aspect_ratio`, `model`).

Log each call to `logs/arcads-api.jsonl` with `model=gpt-image-2`, the variant count, `referenceImages` count, and the returned `asset_id`s, per `arcads-external-api` skill conventions.

### Phase 6: Visual QA (MANDATORY)

For each completed variant, **read the image** and inspect for:
- Garbled small text (most common gpt-image-2 failure on dense body text)
- Wordmark drift (if a brand wordmark wasn't passed as `--image-ref`)
- Wrong text count (e.g. 4 Slack messages instead of 3)
- iOS dialog / UI proportion drift

If defects: regenerate with a revised prompt explicitly correcting the issue (see [shared/skills/chatgpt-image-ad/prompting/guide.md § Retry mode](../../shared/skills/chatgpt-image-ad/prompting/guide.md)). Cap at 2 retries per variant.

### Phase 7: Confirm and hand off

Show all paths to the user. Ask "Use all / use these specific ones / regenerate / cancel."

Selected variants are now ready for the **`meta-ad-builder`** skill (copy and upload). Print the paths so the user can pipe them.

Optionally, write the selected paths to `./generated/run-<ts>.jsonl` (one path per line, JSON-wrapped) for downstream consumption.

## Out of scope — fail clearly

- **Meta upload** — use `meta-ad-builder`.
- **Nano Banana / Gemini image generation** — use `arcads-external-api` (Nano Banana flow).
- **Video, carousel, DCO ads** — image only.
- **Ad copy writing** — use `meta-ad-builder` Phase 2.

## Common errors

- **401/403** → fix `.env` per `arcads-external-api` setup flow.
- **400 Max 5 reference image(s) allowed** → reduce `--image-ref` count to ≤5.
- **422 validation/moderation** → tighten the prompt; check that `aspectRatio` is in the supported set.
- **500 UNKNOWN_ERROR** → usually a stale presigned filePath being reused. The script re-uploads per variant; if you still see this, report the `asset_id` from the response.