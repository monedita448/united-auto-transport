# Brand profile — Vehicle Transport

Source: `facebook-auto-transport-lead-gen-plan.md` (user-provided) + the
live Facebook reel ad screenshot shared in chat. Use this as the default
context for every reel unless the user says otherwise for a specific one.

## What the business actually does

**Auto transport / vehicle shipping** — moving customers' vehicles by
carrier truck, coast-to-coast and locally within the U.S. This is NOT a
chauffeur/passenger car service — nobody rides in the vehicle; the
vehicle itself is the cargo being shipped on a car carrier.

## Core identity

- **Name:** Vehicle Transport
- **Tagline:** "Simplified | Prioritized | Unparalleled"
- **Phone:** (972) 833-2614
- **Coverage:** Coast-to-coast & local
- **Core message:** "Your vehicle, delivered safely, on time, wherever
  life takes you."
- **Message hierarchy for every ad/reel:** Pain point → Solution (the
  service) → Differentiator (insured, tracked, on-time) → CTA.
- **Bilingual:** produce/caption in English and Spanish where practical —
  the brand's existing live ads run both (e.g. "¿Necesitas transportar tu
  carro en U.S.A.? Llámanos al 972 833 2614").
- **Existing visual style** (match for consistency): dark semi-transparent
  text boxes over photo/video backgrounds, bold white headline text, a
  yellow/gold accent color for emphasis (price, CTA, key phrases), a
  caution-triangle-style icon next to the wordmark.

## Audience segments (pick the segment a reel is for — messaging differs)

| Segment | Trigger/timing | Pain point | Hook style |
|---|---|---|---|
| Auto dealers / fleet & B2B | Ongoing | Reliability, volume pricing, damage-free delivery | "How dealerships move 20 cars at once." |
| Military (PCS moves) | May–Sept peak | Tight deadlines, reimbursement, trust | "Got PCS orders? Here's your car's timeline." |
| Household/residential moves | Home sale/lease dates | Price, safety, timing coordination | "Moving cross-country? Skip the road trip." |
| Snowbirds / seasonal relocators | Oct–Nov, Mar–Apr | Recurring reliable service, flexible windows | "Chasing the sun? Your car should too." |
| Business/corporate relocation | HR-driven, bulk | Simplicity, single point of contact | "Relocating employees? One call handles it all." |
| College students | Aug/Dec/May | Budget-conscious, short timeline | "Why pay for gas AND a flight home?" |
| Online vehicle buyers | Immediate, one-time | Trust, tracking, damage coverage | "Bought a car online? Here's how you know it's safe." |
| Collectors / classic & RV | Event-driven | Specialized/enclosed handling | (needs its own angle, not yet scripted) |

## Supporting messages by segment

- **Dealers:** "Volume shipping with damage-free guarantees and dedicated account support."
- **Military:** "PCS orders in hand? We ship on your timeline — no surprises, no delays."
- **Households:** "Moving is stressful enough. Let us handle the car."
- **Students:** "Affordable, flexible shipping — because your parents shouldn't have to drive it."
- **Corporate:** "One partner for all your employee relocations, with reporting your HR team will love."

## Tone

Professional, reassuring, direct — not jokey. Leans on trust signals
(licensed, insured, tracked, on-time) because the core anxiety being
sold against is "will my car actually arrive safely and on time."
Urgency is used for time-bound segments (military, online buyers) more
than for households/dealers. Bilingual audiences get the same message,
not a watered-down version.

## Default CTA set for this brand

- "Call Now" (paired with the phone number, matches existing live ads)
- "Get a Free Quote"
- Avoid generic "Book Now" language — this brand's existing creative
  uses "Call Now" / "Get a Free Quote," not "Book Now" (that reads more
  like a passenger-ride CTA, which isn't what this business does).

## Default end-card treatment

- `brand_text`: "Vehicle Transport"
- `bg_color`: a dark navy/near-black (e.g. `0x14171f`) to match the
  existing dark-overlay look, with the CTA text able to sit in
  gold/yellow if the renderer supports colored text (current
  `render_reel.py` end-card text is white by default — see
  `ffmpeg_notes.md` if a colored-text variant is wanted).
- Always include the phone number (972) 833-2614 in the end-card
  sub-text unless the reel is dealer/B2B-only and a landing page URL is
  preferred instead.
