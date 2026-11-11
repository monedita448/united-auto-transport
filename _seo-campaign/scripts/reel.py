"""Render a branded 1080x1920 vertical reel (MP4, ~15s) for one blog post.

Usage: python3 reel.py /path/to/united-auto-transport <day-number>
Writes <repo>/assets/video/reels/<slug>.mp4 (public URL for Instagram/Facebook/LinkedIn)
and a copy in _seo-campaign/reels/. Four scenes (hook, key points, trust, CTA)
rendered with headless Chrome, stitched by ffmpeg with slow zoom and crossfades.
"""
import html, os, re, shutil, subprocess, sys, tempfile
SEO = os.environ.get("SEO_DIR", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # _seo-campaign/

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import data

# Optional voiceover: --voice <wav> (mixed in with a 0.3 s lead-in, padded/trimmed to the video length)
VOICE = None
if "--voice" in sys.argv:
    i = sys.argv.index("--voice")
    VOICE = sys.argv[i + 1]
    del sys.argv[i:i + 2]
REPO, DAY = sys.argv[1], int(sys.argv[2])
ES = len(sys.argv) > 3 and sys.argv[3] == "es"  # Spanish: reads img_*/reel_points from semana-*/es/dia-XX-*.md
CHROME = os.environ.get("CHROME") or next((p for p in [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",  # macOS
    "C:/Program Files/Google/Chrome/Application/chrome.exe",  # Windows
    "/opt/pw-browsers/chromium", *__import__("glob").glob("/opt/pw-browsers/chromium-*/chrome-linux*/chrome"),
] if os.path.isfile(p) and os.access(p, os.X_OK)), shutil.which("google-chrome") or shutil.which("chromium") or "chromium")
PHONE = "(972) 833-2614"
OUT_REPO = os.path.join(REPO, "assets/video/reels")
OUT_SHARED = os.path.join(SEO, "out", "reels")
SITE = "united-autotransport.com"
SCENE_SEC = [4.0, 5.0, 3.5, 4.5]
FADE = 0.5


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
        return m.group(1) + ("?" if m.group(2) == "?" else ""), m.group(3)
    return t, ""


LOGO = """<svg width="110" height="110" viewBox="0 0 32 32">
<rect x="1" y="1" width="30" height="30" rx="7" fill="#0B2A4A" stroke="#E8871E" stroke-width="1.5"/>
<path d="M11,8 L11,19 A6,6 0 0 0 23,19 L23,8" fill="none" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/>
<path d="M11,8 L11,19 A6,6 0 0 0 23,19 L23,8" fill="none" stroke="#E8871E" stroke-width="1" stroke-dasharray="2 1.5"/>
</svg>"""

CSS = """*{margin:0;padding:0;box-sizing:border-box}
html{width:1080px;height:2140px;background:#050B16}body{width:1080px;height:1920px}
body{font-family:'Inter Display','Inter',sans-serif;color:#F5F7FA;
background:radial-gradient(circle at 85% 8%,rgba(232,135,30,.25),transparent 40%),linear-gradient(180deg,#0B2A4A 0%,#050B16 100%);
padding:150px 90px 300px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.brand{display:flex;align-items:center;gap:24px}
.brand b{display:block;font-size:46px;font-weight:800;letter-spacing:1px}
.brand i{display:block;font-style:normal;font-size:24px;font-weight:700;color:#E8871E;letter-spacing:2px}
.mid{margin:auto 0;display:flex;flex-direction:column}
.tag{display:inline-block;align-self:flex-start;background:rgba(232,135,30,.15);color:#F2941F;
border:2px solid rgba(232,135,30,.5);border-radius:999px;padding:14px 30px;font-size:36px;font-weight:700;letter-spacing:2px;text-transform:uppercase}
h1{margin-top:40px;font-weight:800;letter-spacing:-1px;line-height:1.06}
p.sub{margin-top:40px;font-size:54px;line-height:1.3;color:#B6C2D6;font-weight:500}
ul{list-style:none;margin-top:50px}
li{font-size:62px;font-weight:700;line-height:1.2;padding:40px 0 40px 96px;position:relative;border-bottom:2px solid rgba(255,255,255,.08)}
li:before{content:"";position:absolute;left:0;top:50px;width:56px;height:56px;border-radius:50%;background:#E8871E}
li:after{content:"";position:absolute;left:19px;top:60px;width:12px;height:22px;border:solid #402400;border-width:0 6px 6px 0;transform:rotate(45deg)}
.btn{margin-top:70px;align-self:flex-start;background:#E8871E;color:#402400;font-weight:800;font-size:62px;padding:34px 54px;border-radius:18px}
.phone{margin-top:48px;font-size:72px;font-weight:800}
.site{margin-top:20px;font-size:44px;color:#93A1B8;font-weight:600}
.road{position:absolute;right:-80px;top:360px;width:560px;height:10px;background:repeating-linear-gradient(90deg,#E8871E 0 50px,transparent 50px 90px);opacity:.35;transform:rotate(-30deg)}"""


def shell(inner):
    return (f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="road"></div><div class="brand">{LOGO}<div><b>UNITED</b><i>AUTO TRANSPORT</i></div></div>'
            f'<div class="mid">{inner}</div></body></html>')


def h1(text):
    n = len(text)
    size = 132 if n <= 30 else 116 if n <= 46 else 98 if n <= 64 else 84
    return f'<h1 style="font-size:{size}px">{html.escape(text)}</h1>'


def points(outline):
    """Up to 3 short lines from the outline's H2s, skipping CTA/FAQ boilerplate."""
    out = []
    for part in outline.split("|"):
        t = re.sub(r"^\s*H2\s*", "", part).strip()
        if not t or re.search(r"cta|faq|quote|get started|set up", t, re.I):
            continue
        t = re.sub(r"\s*\(.*?\)", "", t)
        if len(t) > 42:
            t = t[:40].rsplit(" ", 1)[0] + "…"
        out.append(t)
    return out[:3]


def es_meta(day):
    import glob
    f = glob.glob(f"{SEO}/semana-*/es/dia-{day:02d}-*.md")[0]
    fm = dict(l.split(":", 1) for l in open(f, encoding="utf-8").read().split("---\n")[1].strip().splitlines())
    return {k.strip(): v.strip().strip('"') for k, v in fm.items()}


def scenes_es(d):
    m = es_meta(DAY)
    e = html.escape
    pts = [p.strip() for p in m["reel_points"].split("|")][:3]
    dealer = d[0].startswith("Dealers")
    sub = m.get("img_sub", "")
    return [
        shell(f'<span class="tag">{e(m["img_tag"])}</span>{h1(m["img_title"])}' + (f'<p class="sub">{e(sub)}</p>' if sub else "")),
        shell(f'<span class="tag">Lo que debes saber</span><ul>{"".join(f"<li>{e(p)}</li>" for p in pts)}</ul>'),
        shell('<span class="tag">Por qué United</span><ul><li>Carriers verificados por la FMCSA</li>'
              '<li>Servicio puerta a puerta</li><li>Inspección registrada en el Bill of Lading</li></ul>'),
        shell(f'{h1("Concesionarios: abre tu cuenta" if dealer else "Envía tu auto con confianza")}'
              f'<span class="btn">{"Llama ahora" if dealer else "Cotización gratis"}</span>'
              f'<div class="phone">{PHONE}</div><div class="site">{SITE}</div>'),
    ]


def scenes(d):
    if ES:
        return scenes_es(d)
    tipo, seg, titulo, outline = d[0], d[1], d[4], d[7]
    head, sub = split_title(titulo)
    e = html.escape
    pts = points(outline) or ["Door-to-door pickup & delivery", "Open or enclosed carriers", "Inspection on the BOL"]
    dealer = tipo.startswith("Dealers")
    return [
        shell(f'<span class="tag">{e(eyebrow(tipo, seg))}</span>{h1(head)}'
              + (f'<p class="sub">{e(sub)}</p>' if sub else "")),
        shell(f'<span class="tag">What to know</span><ul>{"".join(f"<li>{e(p)}</li>" for p in pts)}</ul>'),
        shell('<span class="tag">Why United</span><ul><li>FMCSA-verified carriers</li>'
              '<li>Door-to-door service</li><li>Vehicle inspected and noted on the Bill of Lading</li></ul>'),
        shell(f'{h1("Dealers: set up your account" if dealer else "Ship your car with confidence")}'
              f'<span class="btn">{"Call now" if dealer else "Get a free quote"}</span>'
              f'<div class="phone">{PHONE}</div><div class="site">{SITE}</div>'),
    ]


def render_png(src_html, png):
    src = png + ".html"
    open(src, "w", encoding="utf-8").write(src_html)
    full = png + ".full.png"
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                    "--force-device-scale-factor=1", "--window-size=1080,2140",
                    f"--screenshot={full}", f"file://{src}"], check=True, capture_output=True, timeout=60)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", full, "-vf", "crop=1080:1920:0:0", png], check=True)


def build(pngs, out):
    global SCENE_SEC
    fps = 30
    if VOICE:  # stretch the CTA scene so the voice (plus 0.3 s lead-in and 0.5 s tail) always fits
        vlen = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                     VOICE], capture_output=True, text=True, check=True).stdout.strip())
        need = vlen + 0.8 - (sum(SCENE_SEC) - FADE * (len(pngs) - 1))
        if need > 0:
            SCENE_SEC = [*SCENE_SEC[:-1], SCENE_SEC[-1] + need]
    inputs, filt = [], []
    for i, (p, sec) in enumerate(zip(pngs, SCENE_SEC)):
        inputs += ["-loop", "1", "-framerate", str(fps), "-t", str(sec), "-i", p]
        frames = int(sec * fps)
        filt.append(f"[{i}:v]scale=1188:2112,zoompan=z='1+0.06*on/{frames}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
                    f":d=1:s=1080x1920:fps={fps},format=yuv420p,setsar=1[v{i}]")
    last, offset = "v0", 0.0
    for i in range(1, len(pngs)):
        offset += SCENE_SEC[i - 1] - FADE
        filt.append(f"[{last}][v{i}]xfade=transition=fade:duration={FADE}:offset={offset:.2f}[x{i}]")
        last = f"x{i}"
    total = sum(SCENE_SEC) - FADE * (len(pngs) - 1)
    if VOICE:
        inputs += ["-i", VOICE]
        filt.append(f"[{len(pngs)}:a]aresample=44100,aformat=channel_layouts=stereo,adelay=300:all=1,apad,"
                    f"atrim=0:{total:.2f}[a]")
        amap = "[a]"
    else:
        inputs += ["-f", "lavfi", "-t", f"{total:.2f}", "-i", "anullsrc=r=44100:cl=stereo"]
        amap = f"{len(pngs)}:a"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *inputs, "-filter_complex", ";".join(filt),
                    "-map", f"[{last}]", "-map", amap, "-c:v", "libx264", "-profile:v", "high",
                    "-preset", "medium", "-crf", "21", "-r", str(fps), "-pix_fmt", "yuv420p",
                    "-c:a", "aac", "-b:a", "160k", "-t", f"{total:.2f}", "-movflags", "+faststart", out], check=True)


d = data.DAYS[DAY - 1]
slug = d[5] + ("-es" if ES else "")
os.makedirs(OUT_REPO, exist_ok=True)
os.makedirs(OUT_SHARED, exist_ok=True)
out = os.path.join(OUT_REPO, slug + ".mp4")
with tempfile.TemporaryDirectory() as tmp:
    pngs = []
    for i, s in enumerate(scenes(d)):
        p = os.path.join(tmp, f"s{i}.png")
        render_png(s, p)
        pngs.append(p)
    build(pngs, out)
    for i, p in enumerate(pngs):
        shutil.copy(p, os.path.join(OUT_SHARED, f"{slug}-scene{i}.png"))
shutil.copy(out, os.path.join(OUT_SHARED, slug + ".mp4"))
print(f"reel rendered: {out} ({os.path.getsize(out) // 1024} KB)")
