import datetime, sys, re
import os
SEO = os.environ.get("SEO_DIR", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # _seo-campaign/
sys.path.insert(0,'.')
from data import DAYS, B
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
assert len(DAYS)==30, len(DAYS)
wb=Workbook(); ws=wb.active; ws.title="Calendario 30 días"
hdr=["Día","Fecha","Día sem.","Tipo","Segmento","Keyword principal","Keywords secundarias","Título (H1)","URL sugerida","Meta description","Estructura (H2)","Enlaces internos","CTA de conversión","Facebook / Instagram","Google Business Profile","LinkedIn (dealers)","Email (asunto)","Borrador listo","Estado"]
ws.append(hdr)
dias=["Lun","Mar","Mié","Jue","Vie","Sáb","Dom"]
start=datetime.date(2026,10,19)
fills={"Ruta":"E8F1FB","Dealers":"FDF0E1","Dealers (pilar)":"FBDDB8","Guía":"EAF6EC","Segmento":"F3E9F8","Hub (enlaces)":"EEEEEE"}
for i,d in enumerate(DAYS):
    dt=start+datetime.timedelta(days=i)
    tipo,seg,kw,kw2,t,slug,meta,outl,links,cta,fb,gbp,li,em=d
    assert len(meta)<=160,(i+1,len(meta))
    ws.append([i+1,dt,dias[dt.weekday()],tipo,seg,kw,kw2,t,B+"blog/"+slug+".html",meta,outl.replace(" | ","\n"),re.sub(r"(/blog/[a-z0-9-]+)(?=;|$)",r"\1.html",links).replace("; ","\n"),cta,fb,gbp,li or "—",em,"Sí (semana-1/ + html/blog/)" if i<7 else ("Sí (semana-2/ + html/blog/)" if i<14 else "No"),"Pendiente"])
    for c in ws[i+2]:
        c.fill=PatternFill("solid",fgColor=fills.get(tipo,"FFFFFF"))
widths=[5,11,7,13,20,26,30,40,40,45,45,45,28,45,40,45,32,13,11]
thin=Side(style="thin",color="BBBBBB")
for i,w in enumerate(widths,1): ws.column_dimensions[get_column_letter(i)].width=w
for row in ws.iter_rows():
    for c in row:
        c.alignment=Alignment(wrap_text=True,vertical="top"); c.border=Border(top=thin,bottom=thin,left=thin,right=thin)
for c in ws[1]:
    c.font=Font(bold=True,color="FFFFFF"); c.fill=PatternFill("solid",fgColor="1F3A5F")
for r in range(2,32): ws.cell(r,2).number_format="yyyy-mm-dd"
ws.freeze_panes="D2"; ws.auto_filter.ref=f"A1:S31"

s=wb.create_sheet("Estrategia")
rows=[
["Estrategia SEO 30 días · United Auto Transport"],
[""],
["Hallazgos del sitio (revisado 15-oct-2026)"],
["• El sitio no tiene blog todavía: /blog/ no responde. Hay que crear la sección /blog/ antes del Día 1 (las URLs sugeridas asumen esa ruta)."],
["• Solo existe 1 página de ruta: /routes/california-to-new-york-car-shipping.html. No hay página para dealers."],
["• Páginas para enlazar: Open, Enclosed, How it works, Get a quote, Carrier liability, #specialized (inoperable, door-to-door, expedited), #callback."],
["• No se ven teléfono, MC/DOT, reseñas ni dirección en la home. Mostrar MC/DOT y reseñas reales aumenta la confianza y el CTR desde Google."],
[""],
["Rutas priorizadas (inferidas: el sitio no publica volumen por ruta; confirmar con tus datos de reservas)"],
["1. Noreste → Florida (NY, NJ, MA, PA): temporada snowbird oct–ene, la más fuerte ahora mismo."],
["2. Medio Oeste → Florida/Arizona (MI, OH, IL): snowbirds."],
["3. California ↔ Nueva York (ya tiene página de ruta, reforzarla)."],
["4. Texas ↔ California y California → Texas: mudanzas de alto volumen."],
["5. Texas → Florida y California → Florida."],
[""],
["Dealers (≈1 de cada 3 posts)"],
["Pilar: 'Dealer Auto Transport' (Día 2) + posts satélite: subastas, dealer trades, ventas a otros estados, lujo/enclosed, inoperables, Q4, expedited, cómo elegir partner."],
["Recomendación: crear una landing /dealers.html con formulario 'Dealer account' y enlazarla desde cada post de dealers."],
["LinkedIn: publicar los posts de dealers desde la página de empresa y el perfil del equipo comercial; email a lista de dealers con el asunto sugerido."],
[""],
["Mezcla de canales por día"],
["Blog (1 post diario) → Facebook/Instagram (mismo día) → Google Business Profile (mismo día) → LinkedIn (solo posts de dealers/B2B) → Email (resumen semanal con los 2–3 mejores asuntos)."],
[""],
["Medición (revisar cada viernes)"],
["Google Search Console: impresiones, clics y CTR por URL del blog. GA4: conversiones 'get-a-quote' y clics en 'Call now' desde /blog/. Redes: CTR, CPC, CPM y costo por lead si se promocionan posts."],
["Acción recomendada: promocionar en Meta los posts de ruta snowbird (Días 1, 3, 7) con audiencia 55+ en NY/NJ/MA/PA, objetivo Leads, y medir costo por cotización."],
[""],
["Notas"],
["• Todo el contenido publicable (posts, redes, emails) está en inglés porque el sitio y el público son de EE.UU.; la planificación está en español."],
["• Los tiempos de tránsito son rangos típicos de la industria; validarlos con operaciones antes de publicar. No se incluyen precios porque el sitio no los publica."],
]
for r in rows: s.append(r)
s.column_dimensions["A"].width=140
for r in (1,3,9,16,21,24,28): s.cell(r,1).font=Font(bold=True,size=12 if r>1 else 14)
for row in s.iter_rows():
    for c in row: c.alignment=Alignment(wrap_text=True,vertical="top")
wb.save(os.path.join(SEO, "calendario-seo-30-dias.xlsx"))
print("ok")
