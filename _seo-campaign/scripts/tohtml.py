import re, json, glob, os, html, datetime, markdown
SEO = os.environ.get("SEO_DIR", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # _seo-campaign/
SRC=SEO; OUT=os.path.join(SEO, "out", "html", "blog")
os.makedirs(OUT, exist_ok=True)
B="https://www.united-autotransport.com/"
START=datetime.date(2026,10,19)
CSS="""<style>
/* Estilos mínimos para que la página se vea bien sola. Si el sitio ya tiene su CSS, borra este bloque. */
*{box-sizing:border-box}
article table{display:block;overflow-x:auto}
:root{--ink:#1b2430;--muted:#5b6675;--brand:#1f3a5f;--accent:#e8731a;--bg:#ffffff;--soft:#f4f6f9}
body{margin:0;font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:var(--ink);background:var(--bg);line-height:1.65}
.site-bar{background:var(--brand);color:#fff;padding:12px 16px;display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap}
.site-bar a{color:#fff;text-decoration:none;font-weight:600}
.btn{display:inline-block;background:var(--accent);color:#fff!important;padding:10px 18px;border-radius:6px;text-decoration:none;font-weight:700}
.btn.alt{background:transparent;border:2px solid currentColor}
article{max-width:760px;margin:0 auto;padding:24px 16px 48px}
article h1{font-size:2rem;line-height:1.25;margin:.5em 0}
article h2{margin-top:1.8em;color:var(--brand)}
article a{color:var(--brand)}
article table{border-collapse:collapse;width:100%;margin:1em 0;font-size:.95rem}
article th,article td{border:1px solid #d5dbe3;padding:8px;text-align:left;vertical-align:top}
article th{background:var(--soft)}
.meta{color:var(--muted);font-size:.9rem}
.cta-box{background:var(--soft);border-left:4px solid var(--accent);padding:20px;margin-top:2em;border-radius:6px}
.cta-box .btn{margin:8px 8px 0 0}
footer{background:var(--soft);color:var(--muted);font-size:.85rem;padding:20px 16px;text-align:center}
.post-list{list-style:none;padding:0}.post-list li{padding:16px 0;border-bottom:1px solid #e3e7ec}
.post-list a{font-weight:700;font-size:1.1rem;text-decoration:none}
</style>"""
HEADER=f"""<!-- REEMPLAZAR por el header/nav real del sitio -->
<header class="site-bar"><a href="{B}index.html">United Auto Transport</a>
<span><a class="btn" href="{B}get-a-quote.html">Get a free quote</a></span></header>"""
FOOTER=f"""<!-- REEMPLAZAR por el footer real del sitio -->
<footer>United Auto Transport is a licensed property broker connecting customers with FMCSA-verified, independently licensed and insured motor carriers.<br>
© 2026 United Auto Transport · <a href="{B}legal/terms.html">Terms</a> · <a href="{B}legal/privacy.html">Privacy</a></footer>"""

def parse(path):
    t=open(path,encoding="utf-8").read()
    _,fm,body=t.split("---\n",2)
    meta={}
    for line in fm.strip().splitlines():
        k,v=line.split(":",1); meta[k.strip()]=v.strip().strip('"')
    return meta, body.strip()

def faqs(body):
    m=re.search(r"## FAQ\n(.*?)(\n---|\Z)",body,re.S)
    if not m: return []
    out=[]
    for q,a in re.findall(r"\*\*(.+?)\*\*\n(.+?)(?:\n\n|\Z)",m.group(1),re.S):
        out.append({"@type":"Question","name":q.strip(),"acceptedAnswer":{"@type":"Answer","text":a.strip()}})
    return out

posts=[]
for f in sorted(glob.glob(f"{SRC}/semana-*/dia-*.md")):
    meta,body=parse(f)
    day=int(re.match(r"(\d+)",meta["day"]).group(1))
    date=START+datetime.timedelta(days=day-1)
    slug=meta["slug"].rsplit("/",1)[-1]
    url=f"{B}blog/{slug}.html"
    # split final CTA (after last ---) into a styled box
    parts=body.rsplit("\n---\n",1)
    main_md=parts[0]; cta_md=parts[1] if len(parts)>1 else ""
    main_md=re.sub(r"^- \[ \] ","- ☐ ",main_md,flags=re.M)
    # python-markdown needs a blank line before a list
    main_md=re.sub(r"(?m)^((?!- |\d+\. ).+)\n(- |\d+\. )",r"\1\n\n\2",main_md)
    # rewrite internal blog links to .html
    fix=lambda s: re.sub(r"(united-autotransport\.com/blog/[a-z0-9-]+)(\))",r"\1.html\2",s)
    main_html=markdown.markdown(fix(main_md),extensions=["tables"])
    cta_html=markdown.markdown(fix(cta_md))
    cta_html=re.sub(r'<a href="([^"]+get-a-quote[^"]*)">',r'<a class="btn" href="\1">',cta_html)
    cta_html=re.sub(r'<a href="([^"]+#callback)">',r'<a class="btn alt" href="\1">',cta_html)
    title=meta["title"]; desc=meta["meta_description"]
    ld=[{"@context":"https://schema.org","@type":"BlogPosting","headline":title,"description":desc,
         "datePublished":date.isoformat(),"mainEntityOfPage":url,"image":B+"assets/images/og-image.jpg",
         "author":{"@type":"Organization","name":"United Auto Transport"},
         "publisher":{"@type":"Organization","name":"United Auto Transport","url":B}}]
    fq=faqs(body)
    if fq: ld.append({"@context":"https://schema.org","@type":"FAQPage","mainEntity":fq})
    e=html.escape
    page=f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} | United Auto Transport</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{B}assets/images/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{B}assets/images/og-image.jpg">
<meta property="article:published_time" content="{date.isoformat()}">
{''.join(f'<script type="application/ld+json">{json.dumps(x,ensure_ascii=False)}</script>' + chr(10) for x in ld)}{CSS}
</head>
<body>
{HEADER}
<main id="main">
<article>
<p class="meta"><a href="{B}blog/index.html">Blog</a> · {date.strftime('%B %-d, %Y')}</p>
{main_html}
<div class="cta-box">
{cta_html}
</div>
</article>
</main>
{FOOTER}
</body>
</html>
"""
    open(f"{OUT}/{slug}.html","w",encoding="utf-8").write(page)
    first_p=re.search(r"<p>(.*?)</p>",main_html,re.S).group(1)
    posts.append((date,title,slug,desc))

CUT=os.environ.get("CUTOFF")
if CUT: posts=[p for p in posts if p[0]<=datetime.date.fromisoformat(CUT)]
posts.sort(reverse=True)
items="\n".join(f'<li><a href="{s}.html">{html.escape(t)}</a><div class="meta">{d.strftime("%B %-d, %Y")}</div><p>{html.escape(ds)}</p></li>' for d,t,s,ds in posts)
idx=f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Car Shipping Blog: Guides, Routes & Dealer Tips | United Auto Transport</title>
<meta name="description" content="Car shipping guides, route timelines, snowbird tips and dealer transport advice from United Auto Transport. Get a free quote anytime.">
<link rel="canonical" href="{B}blog/index.html">
{CSS}
</head>
<body>
{HEADER}
<main id="main"><article>
<h1>Car Shipping Blog</h1>
<p>Route guides, snowbird tips and dealer transport advice from the United Auto Transport team.</p>
<!-- Lista solo los posts publicados hasta la fecha. Se regenera cada día. -->
<ul class="post-list">
{items}
</ul>
<div class="cta-box"><p><strong>Ready to ship?</strong></p><a class="btn" href="{B}get-a-quote.html">Get your free quote</a><a class="btn alt" href="{B}index.html#callback">Request a callback</a></div>
</article></main>
{FOOTER}
</body></html>
"""
open(f"{OUT}/index.html","w",encoding="utf-8").write(idx)
print(len(posts),"posts ->",OUT)
