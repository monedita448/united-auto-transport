---
name: rutina-seo-diaria
description: Publica el paquete SEO del día de United Auto Transport (blog EN+ES, imagen, reel con voz, posts en Facebook, Instagram y LinkedIn). Úsala cuando Camilo pida "el post de hoy", "corre la rutina", "publica el día X" o /rutina-seo-diaria.
---

# Rutina SEO diaria (United Auto Transport)

Plan de 30 días: 19-oct a 17-nov 2026, en INGLÉS y ESPAÑOL. Todo se hace desde la raíz del repo (`united-auto-transport`). Carpeta de la campaña: `_seo-campaign/` (abreviada `$SEO`). Responde a Camilo en español.

Si hoy es antes del 2026-10-19, no hagas nada. Si es después del 2026-11-17, avisa que el plan terminó. Si el argumento trae un número de día, usa ese día.

## 0. Preparar
- `git fetch origin main && git checkout main && git pull --ff-only origin main`.
- `pip install -r _seo-campaign/requirements.txt`. Hace falta `ffmpeg` y Google Chrome o Chromium (o `CHROME=/ruta/al/binario`).
- Revisa con `/mcp` que estén conectados **Higgsfield** y **Zapier**. Si falta uno, sigue sin él y dilo al final.

## 1. Datos del día
Día = (hoy − 2026-10-19) + 1. Lee `DAYS[día-1]` en `$SEO/scripts/data.py` (tipo, segmento, kw, kw_sec, titulo, slug, meta, outline, links, cta, fb_ig, gbp, linkedin, email).

## 2. Borradores
- Inglés: que existan los borradores del resto de esta semana y la siguiente en `$SEO/semana-N/dia-XX-<slug>.md` (mismo front-matter + FAQ + '---' CTA final que las semanas 1–2). Sin precios inventados; términos carrier, door-to-door, open/enclosed, BOL.
- Español (post separado): escribe `$SEO/semana-N/es/dia-XX-<slug>.md` con el mismo cuerpo, español hispano de EE. UU., manteniendo carrier, Bill of Lading (BOL), puerta a puerta, transporte abierto/cerrado; enlaces internos solo en inglés llevan "(en inglés)". Modelo: `$SEO/semana-3/es/dia-19-snowbird-car-shipping-to-arizona.md`. Mismo slug, más `img_tag`, `img_title`, `img_sub`, `reel_points` (3 puntos con " | "), `fb_ig` (con "link en la bio o llama al (972) 833-2614" + hashtags en español) y `linkedin`.
- Si cambia el estado de borradores: `cd $SEO/scripts && python3 build.py` (rehace el xlsx).

## 3. Voz
Dos guiones de ~30–35 palabras (~13 s) que sigan las 4 escenas del reel: gancho, puntos clave, por qué United (puerta a puerta, carriers verificados por FMCSA, inspección en el Bill of Lading) y CTA que termina en "Call 972-833-2614." / "Llama al 972-833-2614.". En español se dice "carro".
Higgsfield `generate_audio`: model `seed_audio`, voice_type `preset`, `use_unlim:false`.
- EN: Mark `27c04473-84a9-4b60-a41f-c8e8458bd4f1`.
- ES: Elena `ca83ca7f-c186-493d-bd69-0d765fa861b2` (por defecto) o Leo `73a45c18-0c56-4642-a61e-f6b303f8ded1` para posts de dealers (guion de ~28 palabras, habla lento).
Espera con `jobs_wait`, descarga los WAV a `$SEO/voz/<slug>.wav` y `$SEO/voz/<slug>-es.wav`. Si falla, renderiza sin voz y dilo.

## 4. Publicar en el sitio (directo a main)
Desde `$SEO/scripts/`, con `CUTOFF=<hoy ISO>` y la ruta del repo como primer argumento, en este orden:
```
python3 site_build.py ../..
python3 es_build.py ../..
python3 social_image.py ../..
LANG_ES=1 python3 social_image.py ../..
python3 reel.py ../.. <día> --voice ../voz/<slug>.wav
python3 reel.py ../.. <día> es --voice ../voz/<slug>-es.wav
```
**Importante:** los builds regeneran todos los posts y deshacen las ediciones hechas a mano en el sitio. Después de correrlos, `git checkout --` de todo archivo que ya existía y cambió, excepto `sitemap.xml`. Quedan solo: los 2 posts nuevos, su tarjeta en `blog/index.html` y `es/blog/index.html`, el sitemap, las imágenes y los reels. Usa un `<title>` corto (sin paréntesis) en el post nuevo.
Mira las imágenes EN y ES y una escena de cada reel (`$SEO/out/reels/`). Commit con el mensaje "Publish blog post: <title>" y `git push origin main`. Espera ~3 min y confirma que `https://www.united-autotransport.com/blog/<slug>.html?v=<día>` y `/es/blog/<slug>.html?v=<día>es` cargan.

## 5. Redes vía Zapier
Todo DOS veces: EN (textos de data.py, blog/<slug>.html, <slug>.jpg, <slug>.mp4) y ES (front-matter del md en español, es/blog/<slug>.html, <slug>-es.jpg, <slug>-es.mp4).
URLs públicas: imagen `https://www.united-autotransport.com/assets/images/social/<slug>[-es].jpg`, video `https://www.united-autotransport.com/assets/video/reels/<slug>[-es].mp4`.
- Facebook `page_stream` (FacebookV2CLIAPI), página `957859070906091`: message = fb_ig cambiando "link in bio"/"link en la bio" por "Read the full guide: <URL>" / "Lee la guía completa: <URL>" + hashtags; source = imagen.
- Instagram `publish_media_v2` (InstagramBusinessCLIAPI), instagramPageId `17841404272923516`: media = [imagen]; caption = fb_ig (EN: + " link in bio or call (972) 833-2614.") + hashtags, sin URL. Si dice "media is not ready", espera 120 s y reintenta.
- LinkedIn perfil personal `share` (LinkedInCLIAPI): visibility__code "anyone", comment = texto linkedin + 2–3 hashtags, content__submitted_url = blog, content__title = título, content__submitted_image_url = imagen.
- Reel en FB `page_video` (página `957859070906091`, title corto, source = video, description = texto del post de FB) e IG `publish_video` (video = URL, caption igual a la foto). Si IG dice "Video is still processing", espera 2 min y reintenta una vez (no duplica).
Si una red falla o pide autenticación, sáltala y dilo.

## 6. Resumen para Camilo (en español, corto)
Empieza con "No necesito nada de tu parte hoy." cuando sea cierto. Incluye: "Día X: <título>", URLs EN y ES en vivo, qué redes recibieron post y reel en cada idioma, qué voz usó cada reel, y pega el texto de Google Business Profile y el asunto del email de data.py (en inglés, sin "Asunto:"), porque esos siguen siendo manuales.
