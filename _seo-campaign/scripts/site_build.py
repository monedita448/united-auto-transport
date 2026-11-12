"""Build blog pages into the united-auto-transport site repo using the site's own template.

Usage: CUTOFF=YYYY-MM-DD python3 site_build.py /path/to/united-auto-transport
Publishes every draft in _seo-campaign/semana-*/ whose plan date is <= CUTOFF:
writes blog/<slug>.html, blog/index.html and refreshes the blog entries in sitemap.xml.
"""
import datetime, glob, html, json, os, re, sys
import markdown
SEO = os.environ.get("SEO_DIR", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # _seo-campaign/

REPO = sys.argv[1]
SRC = SEO
B = "https://www.united-autotransport.com/"
START = datetime.date(2026, 10, 19)
CUT = datetime.date.fromisoformat(os.environ.get("CUTOFF", datetime.date.today().isoformat()))

tpl = open(os.path.join(REPO, "routes/california-to-new-york-car-shipping.html"), encoding="utf-8").read()
# shared chrome from the route page (paths are already ../ relative, which matches /blog/)
SVG_TO_HEADER = tpl[tpl.index('<a href="#main" class="skip-link">'):tpl.index('<main id="main">')]
FOOTER_TO_END = tpl[tpl.index("</main>") + len("</main>"):tpl.index("</body>")]
FONTS = tpl[tpl.index('<link rel="preconnect"'):tpl.index('<!-- PROGRAMMATIC')].strip()
e = html.escape


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
    s = re.sub(r"^- \[ \] ", "- ☐ ", s, flags=re.M)
    s = re.sub(r"(?m)^((?!- |\d+\. ).+)\n(- |\d+\. )", r"\1\n\n\2", s)  # blank line before lists
    s = re.sub(r"(united-autotransport\.com/blog/[a-z0-9-]+)\)", r"\1.html)", s)
    return markdown.markdown(s, extensions=["tables"])


def head(title, desc, url, og_type, ld):
    lds = "\n".join(f'<script type="application/ld+json">\n{json.dumps(x, ensure_ascii=False, indent=1)}\n</script>' for x in ld)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} | United Auto Transport</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{og_type}">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{e(title)} | United Auto Transport">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{B}assets/images/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
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


def cta_band(heading):
    return f"""<section class="section-tight" style="background:var(--navy);">
  <div class="container center" style="color:#fff;">
    <h2 style="color:#fff;">{e(heading)}</h2>
    <p style="color:#B9CBDF;margin-bottom:22px;">Get a free quote, call now, or leave your number and we'll call you back.</p>
    <div style="display:flex;justify-content:center;gap:12px;flex-wrap:wrap;">
      <a href="../get-a-quote.html" class="btn btn-primary btn-lg">Get a free quote</a>
      <a data-phone-tel data-track-call class="btn btn-lg" style="border:1.5px solid rgba(255,255,255,0.4);color:#fff;"><svg class="icon" width="18" height="18"><use href="#i-phone"/></svg> <span data-cta-call-copy>Call now</span></a>
    </div>
  </div>
</section>
"""


def end():
    return f"</main>\n{FOOTER_TO_END}</body>\n</html>\n"


posts = []
for f in sorted(glob.glob(f"{SRC}/semana-*/dia-*.md")):
    meta, body = parse(f)
    day = int(re.match(r"(\d+)", meta["day"]).group(1))
    date = START + datetime.timedelta(days=day - 1)
    if date > CUT:
        continue
    slug = meta["slug"].rsplit("/", 1)[-1]
    url = f"{B}blog/{slug}.html"
    title, desc = meta["title"], meta["meta_description"]
    body = re.sub(r"^# .+\n", "", body)  # H1 goes in the hero
    main_md, _, cta_md = body.rpartition("\n---\n")
    main_md, faqs = split_faq(main_md)
    ld = [
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": B},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": B + "blog/"},
            {"@type": "ListItem", "position": 3, "name": title}]},
        {"@context": "https://schema.org", "@type": "BlogPosting", "headline": title, "description": desc,
         "datePublished": date.isoformat(), "mainEntityOfPage": url, "image": B + "assets/images/og-image.jpg",
         "author": {"@type": "Organization", "name": "United Auto Transport"},
         "publisher": {"@type": "Organization", "name": "United Auto Transport", "url": B}},
    ]
    if faqs:
        ld.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]})
    faq_html = ""
    if faqs:
        items = "\n".join(
            f'      <div class="faq-item{" open" if i == 0 else ""}"><button class="faq-q">{e(q)} <svg class="icon chev" width="16" height="16"><use href="#i-chevron"/></svg></button><div class="faq-a"><p>{md(a)[3:-4]}</p></div></div>'
            for i, (q, a) in enumerate(faqs))
        faq_html = f"""<section class="section section-alt">
  <div class="container" style="max-width:780px;">
    <h2>Frequently Asked Questions</h2>
    <div class="faq-list">
{items}
    </div>
  </div>
</section>
"""
    page = head(title, desc, url, "article", ld) + f"""<section class="hero-navy section-tight">
  <div class="container" style="max-width:760px;">
    <a href="index.html" class="route-badge">Blog · {date.strftime('%B %-d, %Y')}</a>
    <h1 style="margin-top:16px;">{e(title)}</h1>
    <p class="lede mx-auto">{e(desc)}</p>
    <div class="cta-row">
      <a href="../get-a-quote.html" class="btn btn-primary btn-lg">Get a free quote</a>
      <a data-phone-tel data-track-call class="btn btn-lg" style="border:1.5px solid rgba(255,255,255,0.4);color:#fff;"><svg class="icon" width="18" height="18"><use href="#i-phone"/></svg> <span data-cta-call-copy>Call now</span></a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container blog-prose" style="max-width:780px;">
{md(main_md)}
  </div>
</section>

{faq_html}{cta_band("Ready to ship your car?")}""" + end()
    os.makedirs(os.path.join(REPO, "blog"), exist_ok=True)
    open(os.path.join(REPO, "blog", slug + ".html"), "w", encoding="utf-8").write(page)
    posts.append((date, title, slug, desc))

posts.sort(reverse=True)
cards = "\n".join(
    f'      <a class="card blog-card" href="{s}.html"><span class="blog-date">{d.strftime("%B %-d, %Y")}</span><h3>{e(t)}</h3><p>{e(ds)}</p></a>'
    for d, t, s, ds in posts)
idx_title = "Car Shipping Blog: Route Guides, Snowbird Tips & Dealer Transport"
idx_desc = "Car shipping guides, route timelines, snowbird tips and dealer transport advice from United Auto Transport. Get a free quote anytime."
idx = head(idx_title, idx_desc, B + "blog/", "website", [
    {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": B},
        {"@type": "ListItem", "position": 2, "name": "Blog"}]}]) + f"""<section class="hero-navy section-tight">
  <div class="container" style="max-width:760px;">
    <h1>Car Shipping Blog</h1>
    <p class="lede mx-auto">Route guides, snowbird tips and dealer transport advice from the United Auto Transport team.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid-3 blog-grid">
{cards}
    </div>
  </div>
</section>

{cta_band("Get your free car shipping quote")}""" + end()
open(os.path.join(REPO, "blog", "index.html"), "w", encoding="utf-8").write(idx)

# sitemap: drop old blog entries, add current ones
sm_path = os.path.join(REPO, "sitemap.xml")
sm = open(sm_path, encoding="utf-8").read()
sm = re.sub(r"  <url>\n    <loc>[^<]*/blog/[^<]*</loc>.*?</url>\n", "", sm, flags=re.S)
entries = [f"  <url>\n    <loc>{B}blog/</loc>\n    <changefreq>daily</changefreq>\n    <priority>0.7</priority>\n  </url>\n"]
entries += [f"  <url>\n    <loc>{B}blog/{s}.html</loc>\n    <lastmod>{d.isoformat()}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.6</priority>\n  </url>\n" for d, t, s, ds in sorted(posts)]
sm = sm.replace("</urlset>", "".join(entries) + "</urlset>")
open(sm_path, "w", encoding="utf-8").write(sm)
print(f"{len(posts)} posts published (cutoff {CUT})")
