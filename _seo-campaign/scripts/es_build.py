"""Build the Spanish blog (es/blog/) and link it to the English posts with hreflang.

Usage: CUTOFF=YYYY-MM-DD python3 es_build.py /path/to/united-auto-transport
Run AFTER site_build.py (it rewrites the English pages and the sitemap's blog entries).
Reads _seo-campaign/semana-*/es/dia-*.md (same format as the English drafts, Spanish text).
Writes es/blog/<slug>.html and es/blog/index.html, adds hreflang en/es to both versions,
and appends the Spanish URLs to sitemap.xml.
"""
import datetime, glob, html, json, os, re, sys
import markdown
SEO = os.environ.get("SEO_DIR", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # _seo-campaign/

REPO = sys.argv[1]
SRC = SEO
B = "https://www.united-autotransport.com/"
START = datetime.date(2026, 10, 19)
CUT = datetime.date.fromisoformat(os.environ.get("CUTOFF", datetime.date.today().isoformat()))
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
e = html.escape

tpl = open(os.path.join(REPO, "routes/california-to-new-york-car-shipping.html"), encoding="utf-8").read()
deeper = lambda s: s.replace('href="../', 'href="../../').replace('src="../', 'src="../../')
SVG_TO_HEADER = deeper(tpl[tpl.index('<a href="#main" class="skip-link">'):tpl.index('<main id="main">')])
FOOTER_TO_END = deeper(tpl[tpl.index("</main>") + len("</main>"):tpl.index("</body>")])
FONTS = deeper(tpl[tpl.index('<link rel="preconnect"'):tpl.index('<!-- PROGRAMMATIC')].strip())


def fecha(d):
    return f"{d.day} de {MESES[d.month - 1]} de {d.year}"


def parse(path):
    t = open(path, encoding="utf-8").read()
    _, fm, body = t.split("---\n", 2)
    meta = {}
    for line in fm.strip().splitlines():
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip().strip('"')
    return meta, body.strip()


def split_faq(body):
    m = re.search(r"\n## FAQ\n(.*?)(?=\n---\n|\Z)", body, re.S)
    if not m:
        return body, []
    qa = re.findall(r"\*\*(.+?)\*\*\n(.+?)(?:\n\n|\Z)", m.group(1).strip() + "\n\n", re.S)
    return body[:m.start()] + body[m.end():], [(q.strip(), a.strip()) for q, a in qa]


def md(s):
    s = re.sub(r"(?m)^((?!- |\d+\. ).+)\n(- |\d+\. )", r"\1\n\n\2", s)
    s = re.sub(r"(united-autotransport\.com/blog/[a-z0-9-]+)\)", r"\1.html)", s)
    return markdown.markdown(s, extensions=["tables"])


def alternates(en_url, es_url):
    return (f'<link rel="alternate" hreflang="en" href="{en_url}">\n'
            f'<link rel="alternate" hreflang="es" href="{es_url}">\n'
            f'<link rel="alternate" hreflang="x-default" href="{en_url}">')


def head(title, desc, url, og_type, ld, alt):
    lds = "\n".join(f'<script type="application/ld+json">\n{json.dumps(x, ensure_ascii=False, indent=1)}\n</script>' for x in ld)
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} | United Auto Transport</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
{alt}
<meta property="og:type" content="{og_type}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="es_US">
<meta property="og:title" content="{e(title)} | United Auto Transport">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{B}assets/images/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)} | United Auto Transport">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{B}assets/images/og-image.jpg">
{FONTS}
{lds}
</head>
<body>
{SVG_TO_HEADER}<main id="main">
"""


BTNS = """<a href="../../get-a-quote.html" class="btn btn-primary btn-lg">Cotización gratis</a>
      <a data-phone-tel data-track-call class="btn btn-lg" style="border:1.5px solid rgba(255,255,255,0.4);color:#fff;"><svg class="icon" width="18" height="18"><use href="#i-phone"/></svg> <span>Llama ahora</span></a>"""


def cta_band(heading):
    return f"""<section class="section-tight" style="background:var(--navy);">
  <div class="container center" style="color:#fff;">
    <h2 style="color:#fff;">{e(heading)}</h2>
    <p style="color:#B9CBDF;margin-bottom:22px;">Pide tu cotización gratis, llámanos o déjanos tu número y te llamamos.</p>
    <div style="display:flex;justify-content:center;gap:12px;flex-wrap:wrap;">
      {BTNS}
    </div>
  </div>
</section>
"""


def end():
    return f"</main>\n{FOOTER_TO_END}</body>\n</html>\n"


posts = []
outdir = os.path.join(REPO, "es", "blog")
os.makedirs(outdir, exist_ok=True)
for f in sorted(glob.glob(f"{SRC}/semana-*/es/dia-*.md")):
    meta, body = parse(f)
    day = int(re.match(r"(\d+)", meta["day"]).group(1))
    date = START + datetime.timedelta(days=day - 1)
    if date > CUT:
        continue
    slug = meta["slug"].rsplit("/", 1)[-1]
    url, en_url = f"{B}es/blog/{slug}.html", f"{B}blog/{slug}.html"
    title, desc = meta["title"], meta["meta_description"]
    body = re.sub(r"^# .+\n", "", body)
    main_md, _, _ = body.rpartition("\n---\n")
    main_md, faqs = split_faq(main_md)
    ld = [
        {"@context": "https://schema.org", "@type": "BlogPosting", "headline": title, "description": desc,
         "inLanguage": "es", "datePublished": date.isoformat(), "mainEntityOfPage": url,
         "image": B + "assets/images/og-image.jpg",
         "author": {"@type": "Organization", "name": "United Auto Transport"},
         "publisher": {"@type": "Organization", "name": "United Auto Transport", "url": B}},
    ]
    if faqs:
        ld.append({"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": "es", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]})
    faq_html = ""
    if faqs:
        items = "\n".join(
            f'      <div class="faq-item{" open" if i == 0 else ""}"><button class="faq-q">{e(q)} <svg class="icon chev" width="16" height="16"><use href="#i-chevron"/></svg></button><div class="faq-a"><p>{md(a)[3:-4]}</p></div></div>'
            for i, (q, a) in enumerate(faqs))
        faq_html = f"""<section class="section section-alt">
  <div class="container" style="max-width:780px;">
    <h2>Preguntas frecuentes</h2>
    <div class="faq-list">
{items}
    </div>
  </div>
</section>
"""
    page = head(title, desc, url, "article", ld, alternates(en_url, url)) + f"""<section class="hero-navy section-tight">
  <div class="container" style="max-width:760px;">
    <a href="index.html" class="route-badge">Blog en español · {fecha(date)}</a>
    <h1 style="margin-top:16px;">{e(title)}</h1>
    <p class="lede mx-auto">{e(desc)}</p>
    <div class="cta-row">
      {BTNS}
    </div>
    <p style="margin-top:14px;"><a href="../../blog/{slug}.html" style="color:#B9CBDF;" hreflang="en">Read in English</a></p>
  </div>
</section>

<section class="section">
  <div class="container blog-prose" style="max-width:780px;">
{md(main_md)}
  </div>
</section>

{faq_html}{cta_band("¿Listo para enviar tu auto?")}""" + end()
    open(os.path.join(outdir, slug + ".html"), "w", encoding="utf-8").write(page)
    posts.append((date, title, slug, desc))
    # hreflang + "Leer en español" link on the English page
    en_path = os.path.join(REPO, "blog", slug + ".html")
    if os.path.exists(en_path):
        en = open(en_path, encoding="utf-8").read()
        if 'hreflang="es"' not in en:
            en = en.replace(f'<link rel="canonical" href="{en_url}">',
                            f'<link rel="canonical" href="{en_url}">\n{alternates(en_url, url)}', 1)
            en = en.replace('<p class="lede mx-auto">', f'<p style="margin:0 0 10px;"><a href="../es/blog/{slug}.html" hreflang="es" style="color:#B9CBDF;">Leer en español</a></p>\n    <p class="lede mx-auto">', 1)
            open(en_path, "w", encoding="utf-8").write(en)

posts.sort(reverse=True)
cards = "\n".join(
    f'      <a class="card blog-card" href="{s}.html"><span class="blog-date">{fecha(d)}</span><h3>{e(t)}</h3><p>{e(ds)}</p></a>'
    for d, t, s, ds in posts)
idx = head("Blog de envío de autos en español", "Guías de envío de autos, rutas, consejos para snowbirds y transporte para concesionarios, en español. Cotización gratis.",
           B + "es/blog/", "website", [], f'<link rel="alternate" hreflang="en" href="{B}blog/">\n<link rel="alternate" hreflang="es" href="{B}es/blog/">') + f"""<section class="hero-navy section-tight">
  <div class="container" style="max-width:760px;">
    <h1>Blog de envío de autos</h1>
    <p class="lede mx-auto">Guías de rutas, consejos para snowbirds y transporte para concesionarios, del equipo de United Auto Transport.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid-3 blog-grid">
{cards}
    </div>
  </div>
</section>

{cta_band("Pide tu cotización gratis")}""" + end()
open(os.path.join(outdir, "index.html"), "w", encoding="utf-8").write(idx)

sm_path = os.path.join(REPO, "sitemap.xml")
sm = open(sm_path, encoding="utf-8").read()
sm = re.sub(r"  <url>\n    <loc>[^<]*/es/blog/[^<]*</loc>.*?</url>\n", "", sm, flags=re.S)
entries = [f"  <url>\n    <loc>{B}es/blog/</loc>\n    <changefreq>daily</changefreq>\n    <priority>0.6</priority>\n  </url>\n"]
entries += [f"  <url>\n    <loc>{B}es/blog/{s}.html</loc>\n    <lastmod>{d.isoformat()}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.5</priority>\n  </url>\n" for d, t, s, ds in sorted(posts)]
sm = sm.replace("</urlset>", "".join(entries) + "</urlset>")
open(sm_path, "w", encoding="utf-8").write(sm)
print(f"{len(posts)} Spanish posts published (cutoff {CUT})")
