# Memoria del proyecto (exportada de Claude Projects, 2026-11-11)

Decisiones que ya tomó Camilo. No hace falta volver a preguntarlas.

## Sitio
- https://www.united-autotransport.com: GitHub Pages desde la rama `main` de `monedita448/united-auto-transport`. Sin CI. Cada push a `main` sale en vivo en ~1–3 min.
- Broker de transporte de vehículos (property broker), carriers verificados por FMCSA. Teléfono en todo el contenido: (972) 833-2614.
- Publicación DIRECTA a `main` (decidido 2026-10-20), sin PR por día.
- El HTML del blog también se edita a mano en el sitio (títulos SEO cortos, enlaces a `car-shipping-cost.html`, páginas nuevas). `site_build.py` y `es_build.py` regeneran TODOS los posts y deshacen esas ediciones: después de correrlos, `git checkout --` de todo archivo existente que cambió (excepto `sitemap.xml`) y conservar solo los posts nuevos, sus tarjetas en `blog/index.html` y `es/blog/index.html`, y el sitemap. Usar `<title>` corto (sin paréntesis) en posts nuevos.

## Plan de 30 días (19-oct a 17-nov 2026)
- Calendario: `_seo-campaign/calendario-seo-30-dias.xlsx`. Datos de cada día: `scripts/data.py` (`DAYS[día-1]`).
- Blog en INGLÉS (audiencia EE. UU.) + versión en ESPAÑOL como post separado (aprobado 2026-11-06) en `/es/blog/<slug>.html` con hreflang.
- Rutas prioritarias (inferidas, no de datos de reservas): NE→FL snowbird, Midwest→FL/AZ, CA↔NY, TX↔CA, TX→FL, CA→FL. ~1 de cada 3 posts va para dealers; pilar: `dealer-auto-transport`.
- `SEO30day plan.txt` (export de AIPRM) era de otro negocio (investigación privada). Ignorar.
- Estado al 2026-11-11: días 1–24 publicados en EN; ES desde el día 19. Borradores EN listos hasta el día 30; ES hasta el 24. El 18-nov se cierra la rutina.

## Redes (vía Zapier)
- Facebook: página "United Auto-Transport", id `957859070906091`.
- Instagram: @unitedautotransport_ (en Zapier aparece como "Auto transport"), id `17841404272923516`.
- LinkedIn: perfil PERSONAL de Camilo (no es admin de la página de empresa), acción `share`. No acepta video, así que LinkedIn lleva la imagen.
- Reel diario (aprobado 2026-11-06) en FB + IG. IG `publish_video` puede decir "still processing": esperar 2 min y reintentar una vez. IG foto puede decir "media is not ready": esperar 120 s y reintentar.
- Zapier cobra 1 tarea por post/reel (~10 al día EN+ES). Camilo subió de plan el 2026-11-09.

## Voces (Higgsfield `generate_audio`, model `seed_audio`, voice_type `preset`, `use_unlim:false`)
- Inglés: Mark `27c04473-84a9-4b60-a41f-c8e8458bd4f1`.
- Español (Camilo quiere acento colombiano/latino): Elena `ca83ca7f-c186-493d-bd69-0d765fa861b2` (mujer, por defecto); Leo `73a45c18-0c56-4642-a61e-f6b303f8ded1` (hombre, posts de dealers; habla lento, guion de ~28 palabras).
- Descartadas: Isabella, Xavier, Marisol, Ines, Julian, Andre.
- El audio llega como WAV desde `d8j0ntlcm91z4.cloudfront.net`.

## Preferencias de Camilo
- Responder en español. Terminología del sector: carrier, door-to-door / puerta a puerta, open/enclosed, Bill of Lading (BOL). No es transporte de pasajeros.
- CTAs de conversión: cotización gratis, llama ahora, reserva tu envío. Tono confiable y urgente, sin ser agresivo. Nada de precios inventados.
- Segmentos: snowbirds, militares PCS, compradores online, concesionarios, estudiantes, relocalización corporativa.
