"""Render a branded 1080x1080 social image for each blog post up to CUTOFF.

Usage: CUTOFF=YYYY-MM-DD python3 social_image.py /path/to/united-auto-transport
Writes <repo>/assets/images/social/<slug>.jpg (public URL for Instagram/Facebook/LinkedIn)
and a copy in _seo-campaign/social/. Existing images are kept unless FORCE=1.
"""
import datetime, html, os, re, shutil, subprocess, sys, tempfile
from PIL import Image
SEO = os.environ.get("SEO_DIR", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # _seo-campaign/

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import data

REPO = sys.argv[1]
START = datetime.date(2026, 10, 19)
CUT = datetime.date.fromisoformat(os.environ.get("CUTOFF", datetime.date.today().isoformat()))
FORCE = os.environ.get("FORCE") == "1"
ES = os.environ.get("LANG_ES") == "1"  # Spanish: reads img_* fields from semana-*/es/dia-XX-<slug>.md, writes <slug>-es.jpg
CHROME = os.environ.get("CHROME") or next((p for p in [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",  # macOS
    "C:/Program Files/Google/Chrome/Application/chrome.exe",  # Windows
    "/opt/pw-browsers/chromium", *__import__("glob").glob("/opt/pw-browsers/chromium-*/chrome-linux*/chrome"),
] if os.path.isfile(p) and os.access(p, os.X_OK)), shutil.which("google-chrome") or shutil.which("chromium") or "chromium")
OUT_REPO = os.path.join(REPO, "assets/images/social")
OUT_SHARED = os.path.join(SEO, "out", "social")
PHONE = "(972) 833-2614"
TRUST = ("Carriers verificados por la FMCSA &nbsp;·&nbsp; Puerta a puerta &nbsp;·&nbsp; Abierto y cerrado" if os.environ.get("LANG_ES") == "1"
         else "FMCSA-verified carriers &nbsp;·&nbsp; Door-to-door &nbsp;·&nbsp; Open &amp; enclosed")
BTN, OR_CALL = ("Cotización gratis", "o llama al") if os.environ.get("LANG_ES") == "1" else ("Get a free quote", "or call")


def eyebrow(tipo, seg):
    s = seg.lower()
    if tipo.startswith("Dealers"):
        return "For dealers"
    if "pcs" in s or "milit" in s:
        return "Military PCS moves"
    if "estudiant" in s:
        return "College car shipping"
    if "corporativa" in s:
        return "Corporate relocation"
    if tipo == "Guía":
        return "Car shipping guide"
    if "snowbird" in s:
        return "Snowbird route guide"
    return "Route guide"


def split_title(t):
    m = re.match(r"(.+?)([:?])\s+(.+)", t)
    if m:
        head = m.group(1) + ("?" if m.group(2) == "?" else "")
        return head, m.group(3)
    return t, ""


def page(title, sub, tag):
    n = len(title)
    size = 84 if n <= 34 else 72 if n <= 48 else 62 if n <= 64 else 54
    e = html.escape
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0;box-sizing:border-box}}
html{{width:1080px;height:1300px;background:#050B16}}body{{width:1080px;height:1080px}}
body{{font-family:'Inter Display','Inter',sans-serif;color:#F5F7FA;
background:radial-gradient(circle at 85% 10%,rgba(232,135,30,.22),transparent 45%),linear-gradient(180deg,#0B2A4A 0%,#050B16 100%);
padding:84px;display:flex;flex-direction:column;position:relative;overflow:hidden}}
.brand{{display:flex;align-items:center;gap:22px}}
.brand b{{display:block;font-size:40px;font-weight:800;letter-spacing:1px}}
.brand i{{display:block;font-style:normal;font-size:21px;font-weight:700;color:#E8871E;letter-spacing:2px}}
.tag{{margin-top:auto;display:inline-block;align-self:flex-start;background:rgba(232,135,30,.15);color:#F2941F;
border:2px solid rgba(232,135,30,.5);border-radius:999px;padding:12px 26px;font-size:26px;font-weight:700;letter-spacing:2px;text-transform:uppercase}}
h1{{margin-top:34px;font-size:{size}px;line-height:1.08;font-weight:800;letter-spacing:-1px}}
p.sub{{margin-top:26px;font-size:34px;line-height:1.3;color:#B6C2D6;font-weight:500}}
.trust{{margin-top:40px;font-size:26px;color:#93A1B8;font-weight:500}}
.cta{{margin-top:44px;display:flex;gap:20px;align-items:center}}
.btn{{background:#E8871E;color:#402400;font-weight:800;font-size:32px;padding:24px 38px;border-radius:14px}}
.phone{{font-size:32px;font-weight:700;color:#F5F7FA}}
.road{{position:absolute;right:-60px;top:250px;width:420px;height:8px;background:repeating-linear-gradient(90deg,#E8871E 0 40px,transparent 40px 70px);opacity:.35;transform:rotate(-30deg)}}
</style></head><body>
<div class="road"></div>
<div class="brand"><svg width="96" height="96" viewBox="0 0 32 32">
<rect x="1" y="1" width="30" height="30" rx="7" fill="#0B2A4A" stroke="#E8871E" stroke-width="1.5"/>
<path d="M11,8 L11,19 A6,6 0 0 0 23,19 L23,8" fill="none" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/>
<path d="M11,8 L11,19 A6,6 0 0 0 23,19 L23,8" fill="none" stroke="#E8871E" stroke-width="1" stroke-dasharray="2 1.5"/>
</svg><div><b>UNITED</b><i>AUTO TRANSPORT</i></div></div>
<span class="tag">{e(tag)}</span>
<h1>{e(title)}</h1>
{f'<p class="sub">{e(sub)}</p>' if sub else ''}
<div class="trust">{TRUST}</div>
<div class="cta"><span class="btn">{BTN}</span><span class="phone">{OR_CALL} {PHONE}</span></div>
</body></html>"""


def render(html_src, out_jpg):
    with tempfile.TemporaryDirectory() as d:
        src, png = os.path.join(d, "card.html"), os.path.join(d, "card.png")
        open(src, "w", encoding="utf-8").write(html_src)
        subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                        "--force-device-scale-factor=1", "--window-size=1080,1300",
                        f"--screenshot={png}", f"file://{src}"], check=True, capture_output=True, timeout=60)
        Image.open(png).convert("RGB").crop((0, 0, 1080, 1080)).save(out_jpg, "JPEG", quality=88, optimize=True)


os.makedirs(OUT_REPO, exist_ok=True)
os.makedirs(OUT_SHARED, exist_ok=True)
made = 0
for i, d in enumerate(data.DAYS, 1):
    if START + datetime.timedelta(days=i - 1) > CUT:
        break
    tipo, seg, titulo, slug = d[0], d[1], d[4], d[5]
    name = slug + ("-es" if ES else "") + ".jpg"
    out = os.path.join(OUT_REPO, name)
    if os.path.exists(out) and not FORCE:
        continue
    if ES:
        import glob
        fs = glob.glob(f"{SEO}/semana-*/es/dia-{i:02d}-*.md")
        if not fs:
            continue
        fm = dict(l.split(":", 1) for l in open(fs[0], encoding="utf-8").read().split("---\n")[1].strip().splitlines())
        fm = {k.strip(): v.strip().strip('"') for k, v in fm.items()}
        head, sub, tag = fm["img_title"], fm.get("img_sub", ""), fm["img_tag"]
    else:
        head, sub = split_title(titulo)
        tag = eyebrow(tipo, seg)
    render(page(head, sub, tag), out)
    shutil.copy(out, os.path.join(OUT_SHARED, name))
    made += 1
print(f"{made} social images rendered (cutoff {CUT})")
