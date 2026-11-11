# Handoff: daily SEO routine (United Auto Transport), from 2026-11-07

Camilo approved moving the daily routine to a new thread on 2026-11-06, so the reels can get voiceover. The new cloud environment allows the Higgsfield audio host, and the old thread can't use it.

## First steps in the new thread
1. Check the network: `curl -sS -o /dev/null -w "%{http_code}" https://d8j0ntlcm91z4.cloudfront.net/<un WAV de Higgsfield>` should return 200. If it doesn't, tell Camilo that the project still needs the new environment selected in Project settings > Cloud environment.
2. Clone `monedita448/united-auto-transport` to `/home/claude/united-auto-transport`. The repo is GitHub Pages, with no CI and no PRs. Push directly to `main`.
3. Read the current scheduled task with `get_trigger trig_01D63Vc3aBW7ufK37ULpLYuR`. Its prompt is the full daily recipe in English and Spanish: Zapier targets, IDs, scripts and the reply format.
4. Create a new daily scheduled task bound to this thread with the same prompt: `CRON_TZ=America/New_York 57 7 * * *`. Add the voiceover step below and remove the line that says "Audio can't be mixed yet".
5. Then disable the old one: `update_trigger trig_01D63Vc3aBW7ufK37ULpLYuR enabled=false`. That way nothing gets published twice.
6. Post in the thread that the routine continues there, and show Camilo a reel with voiceover before it joins the daily routine. He asked to see a sample first.

## Voiceover (new)
- English voice: Higgsfield `generate_audio`, model `seed_audio`, voice_type `preset`, voice "Mark" `27c04473-84a9-4b60-a41f-c8e8458bd4f1`.
- Spanish voices (Colombian paisa accent wanted): Isabella (female) `80924413-1ea8-4e64-9719-e00b86796f05`, Xavier (male) `43173c95-3ec8-446a-a162-6504332c578b`. Camilo didn't say how to alternate them. Use Isabella by default, since he said the woman is the main voice, and Xavier for dealer posts, or ask him.
- Pass `use_unlim:false`. It costs about 1.3 credits per clip. Wait for the job with `jobs_wait`. The audio comes back as a WAV on d8j0ntlcm91z4.cloudfront.net.
- Script: about 30 to 35 words (around 13 seconds), following the reel's 4 scenes (hook, key points, Why United, CTA with "Call 972-833-2614"). Day 19 EN: "Wintering in Arizona? Skip the drive. We ship your car door-to-door with FMCSA-verified carriers, and every inspection goes on the Bill of Lading. Get your free quote today. Call 972-833-2614." Spanish uses "carro".
- Mix (example): `ffmpeg -i reel.mp4 -i voice.wav -filter_complex "[1:a]aresample=44100,adelay=300:all=1,apad[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 160k -shortest -movflags +faststart out.mp4`. Overwrite `assets/video/reels/<slug>.mp4` (and `-es.mp4`) before committing. Or, better, add a `--voice <wav>` option to `scripts/reel.py`.

## Where things are
- Plan, scripts and drafts: `/mnt/project-files/seo/` (scripts in `scripts/`: data.py, site_build.py, es_build.py, social_image.py [`LANG_ES=1` for Spanish], reel.py [`<day> es` for Spanish], tohtml.py, build.py).
- Spanish drafts: `semana-N/es/dia-XX-<slug>.md`, using day 19 as the model.
- Project memory: `MEMORY.md` has the account decisions (FB page, IG, Camilo's personal LinkedIn, why LinkedIn doesn't take video).
- Days 2 to 19 are published in English. Day 19 is also in Spanish (blog, FB, IG and LinkedIn).
- Still to do: drafts for days 29 and 30 (semana-5). On Nov 18, close the routine and delete the scheduled task.
- The old thread hit the 24-attachment limit. If the new thread can use `attached_outputs` again, attach normally.

## Status 2026-11-06 (new thread)
- Done: network OK, new scheduled task trig_01X61dP4keNmjABej4Z7xHF9 bound to the new thread, old one disabled, reel.py has --voice, Chrome path auto-detected in reel.py and social_image.py.
- Voice samples (day 19): seo/reels/voz/muestra-dia19-en-mark.mp4, -es-isabella.mp4, -es-xavier.mp4. Voice joins the routine once Camilo approves.
- 2026-11-06 21:27Z: Camilo asked for more Hispanic/Colombian voices. Extra Spanish samples (seed_audio preset ids): Marisol 75e72cd5-011b-4130-a474-e8b1ab341f04, Ines 023ebf5e-1970-40d8-825c-a5ef6a1dd4ff, Elena ca83ca7f-c186-493d-bd69-0d765fa861b2 (female); Julian 95429266-c0ac-4137-a209-63b8812b0f23, Andre f1e8226e-2248-4d5f-b43c-0a79e9949dbf, Leo 73a45c18-0c56-4642-a61e-f6b303f8ded1 (male). Files: seo/reels/voz/muestra-dia19-es-<name>.mp4. Waiting for his pick.
- 2026-11-06 21:47Z: Camilo chose Elena (ES female, default) and Leo (ES male, dealer posts). Scheduled task updated; voice on from day 20.

- 2026-11-10 (día 23): el hilo "Rutina SEO diaria con reels con voz" llegó al máximo de 24 adjuntos. Desde el día 24, enlazar imágenes y reels con sus URLs públicas (assets/images/social/<slug>[-es].jpg, assets/video/reels/<slug>[-es].mp4) en lugar de attached_outputs. Instagram también puede responder "media is not ready" en la foto: esperar 120 s y reintentar.

- 2026-11-11 (día 24): otro hilo está editando directamente el HTML publicado (títulos SEO cortos, enlaces a car-shipping-cost.html, páginas nuevas). site_build.py/es_build.py regeneran TODOS los posts y revierten esas ediciones. Desde ahora: después de los builds, `git checkout --` de todos los archivos existentes modificados excepto sitemap.xml, y solo agregar los 2 posts nuevos + su tarjeta en blog/index.html y es/blog/index.html. Usar un <title> corto (sin paréntesis) para el post nuevo.
