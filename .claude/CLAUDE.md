# United Auto Transport: sitio + campaña SEO

Este repo es el sitio en vivo https://www.united-autotransport.com (GitHub Pages, HTML estático). **Cada push a `main` sale publicado en 1–3 minutos.** No hay CI.

Dueño: Camilo (marketing, transporte de vehículos por carrier). Respóndele en español. Contenido publicado en inglés (audiencia EE. UU.) y, desde el día 19, también en español como posts separados en `/es/`.

## Reglas
- Sector: transporte de vehículos por carrier (no pasajeros). Usa carrier, door-to-door / puerta a puerta, terminal-to-terminal, open/enclosed, Bill of Lading (BOL).
- CTAs de conversión directa ("Get your free quote", "Call (972) 833-2614"). Tono confiable y urgente, sin ser agresivo. No inventes precios.
- Hay HTML editado a mano en el sitio (títulos SEO cortos, enlaces a `car-shipping-cost.html`). Los builds del blog lo sobrescriben: lee la sección 4 de la skill `rutina-seo-diaria` antes de correrlos.
- Nunca hagas commit de llaves ni tokens. El repo es público.

## Dónde está cada cosa
| Qué | Dónde |
|---|---|
| Campaña SEO (no se publica: Jekyll ignora carpetas con `_`) | `_seo-campaign/` |
| Datos de los 30 días (títulos, slugs, textos de redes, GBP, email) | `_seo-campaign/scripts/data.py` |
| Borradores EN / ES | `_seo-campaign/semana-N/dia-XX-<slug>.md` y `semana-N/es/` |
| Calendario | `_seo-campaign/calendario-seo-30-dias.xlsx` |
| Scripts (blog EN, blog ES, imagen, reel, xlsx) | `_seo-campaign/scripts/` |
| Decisiones tomadas (cuentas, IDs, voces, preferencias) | `_seo-campaign/docs/memoria-proyecto.md` |
| Historial de la rutina diaria | `_seo-campaign/docs/TRASPASO-rutina-diaria.md` |
| Posts publicados | `blog/`, `es/blog/` |
| Imágenes y reels publicados | `assets/images/social/`, `assets/video/reels/` |

Las salidas locales de los scripts (copias de reels, imágenes, HTML de prueba) van a `_seo-campaign/out/` y los WAV a `_seo-campaign/voz/`; las dos carpetas están en `.gitignore`.

## Rutina diaria
Usa la skill `/rutina-seo-diaria` (en `.claude/skills/`). Necesita los conectores **Higgsfield** (voz) y **Zapier** (Facebook, Instagram, LinkedIn). En Claude Code, los conectores de claude.ai aparecen al iniciar sesión con la misma cuenta; revísalos con `/mcp`.

Requisitos locales: Python 3 con `pip install -r _seo-campaign/requirements.txt`, `ffmpeg` y Google Chrome o Chromium (o exporta `CHROME=/ruta`).

## Otras skills incluidas
`.claude/skills/`: `video-reel-creator`, `meta-ad-builder`, `arcads-external-api`, `chatgpt-image-ad`, `video-to-action`. Las que usan API piden la llave en un `.env` local (nunca en el repo).
