# -*- coding: utf-8 -*-
"""Genera la web estática (ES en la raíz, EN en /en, CA en /ca).
Uso:  python3 fuente/build.py      (desde la raíz del repositorio)
Requiere Pillow (solo para leer el tamaño de las imágenes).
"""
import os, html, sys, json, math
from urllib.parse import urlparse
from PIL import Image
sys.path.insert(0, os.path.dirname(__file__))
from contenido import SITE, T, SOBRE, PROYECTOS

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LANGS = ["es", "en", "ca"]
BASE_DIR = {"es": "", "en": "en/", "ca": "ca/"}
PROY_DIR = {"es": "proyectos", "en": "projects", "ca": "projectes"}
LANG_NAME = {"es": "ES", "en": "EN", "ca": "CA"}
OG_LOCALE = {"es": "es_ES", "en": "en_GB", "ca": "ca_ES"}
# Dirección pública de la web. Cambiar aquí si cambia el usuario o el dominio.
SITE_URL = "https://raulgartav.github.io/raulgarciatavera.github.io/"
BASE_PATH = urlparse(SITE_URL).path          # "/raulgarciatavera.github.io/"
OG_IMG = "assets/og.png"

e = html.escape


def tx(v, l):
    """Texto traducido: dict {es,en,ca} o cadena fija."""
    return v[l] if isinstance(v, dict) else v


def num(v, l, dec=1):
    from decimal import Decimal, ROUND_HALF_UP
    s = str(Decimal(str(v)).quantize(Decimal(1).scaleb(-dec), rounding=ROUND_HALF_UP))
    return s if l == "en" else s.replace(".", ",")


def path_home(l):
    return BASE_DIR[l] + "index.html"


def path_proy(l, slug):
    return f"{BASE_DIR[l]}{PROY_DIR[l]}/{slug}.html"


def url_publica(ruta):
    """URL absoluta sin 'index.html'."""
    return SITE_URL + (ruta[:-10] if ruta.endswith("index.html") else ruta)


def rel(desde, hacia):
    """Ruta relativa entre dos archivos de la web."""
    d = os.path.dirname(desde)
    return os.path.relpath(hacia, d or ".").replace(os.sep, "/")


_TAM = {}
def tam(archivo):
    if archivo not in _TAM:
        with Image.open(os.path.join(RAIZ, archivo)) as im:
            _TAM[archivo] = im.size
    return _TAM[archivo]


FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
           "%3Crect width='32' height='32' fill='%231c3faa'/%3E%3Cpath d='M6 26V6h20v20z' fill='none' stroke='white' stroke-width='1.5'/%3E"
           "%3Ctext x='16' y='21' font-family='Arial' font-weight='700' font-size='12' fill='white' text-anchor='middle'%3ERG%3C/text%3E%3C/svg%3E")


# ───────────────────────────── Plantilla de página

def pagina(l, ruta, titulo, descripcion, cuerpo, alternos, og_img=None, extra_head="", scripts=True):
    r = lambda destino: rel(ruta, destino)
    alt_links = "\n".join(
        f'<link rel="alternate" hreflang="{x}" href="{url_publica(alternos[x])}">' for x in LANGS)
    alt_links += f'\n<link rel="alternate" hreflang="x-default" href="{url_publica(alternos["es"])}">'
    idiomas = "".join(
        f'<a href="{r(alternos[x])}" hreflang="{x}" lang="{x}"{" aria-current=\"true\"" if x == l else ""}>{LANG_NAME[x]}</a>'
        for x in LANGS)
    home = r(path_home(l))
    og = SITE_URL + (og_img or OG_IMG)
    textos_js = {k: T[k][l] for k in ("cerrar", "anterior", "posterior", "pausa", "reproducir")}
    script = (f'<script>window.TXT={json.dumps(textos_js, ensure_ascii=False)}</script>\n'
              f'<script src="{r("assets/sitio.js")}" defer></script>') if scripts else ""
    return f"""<!doctype html>
<html lang="{l}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(titulo)}</title>
<meta name="description" content="{e(descripcion)}">
<meta name="author" content="{e(SITE['nombre'])}">
<link rel="canonical" href="{url_publica(ruta)}">
{alt_links}
<meta property="og:type" content="website">
<meta property="og:site_name" content="{e(SITE['nombre'])}">
<meta property="og:title" content="{e(titulo)}">
<meta property="og:description" content="{e(descripcion)}">
<meta property="og:url" content="{url_publica(ruta)}">
<meta property="og:image" content="{og}">
<meta property="og:locale" content="{OG_LOCALE[l]}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#f4f6f9" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0c1322" media="(prefers-color-scheme: dark)">
<link rel="icon" href="{FAVICON}">
<link rel="preload" href="{r('assets/fuentes/archivo-var.woff2')}" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{r('assets/fuentes/plex-sans-400.woff2')}" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{r('assets/estilo.css')}">
{extra_head}</head>
<body>
<a class="saltar" href="#contenido">{e(T['saltar'][l])}</a>
<header class="barra">
  <div class="barra-in">
    <a class="marca" href="{home}" aria-label="{e(SITE['nombre'])}"><span class="marca-c" aria-hidden="true">RG</span><span class="marca-n">{e(SITE['nombre'])}</span></a>
    <nav class="nav" aria-label="{e(T['contenido'][l])}">
      <a href="{home}#proyectos">{e(T['proyectos'][l])}</a>
      <a href="{home}#sobre">{e(T['sobre'][l])}</a>
      <a href="{home}#contacto">{e(T['contacto'][l])}</a>
      <span class="idiomas" role="group" aria-label="{e(T['otros_idiomas'][l])}">{idiomas}</span>
    </nav>
  </div>
</header>
{cuerpo}
<footer class="pie">
  <div class="envoltura pie-in">
    <span>© 2026 {e(SITE['nombre'])}</span>
    <span>{e(T['pie'][l])}</span>
  </div>
</footer>
{script}
</body>
</html>
"""


# ───────────────────────────── Piezas comunes

def etiquetas(p, l):
    return "".join(f'<li>{e(tx(t, l))}</li>' for t in p["etiquetas"])


def chip_estado(p, l):
    return f'<span class="estado estado-{p["estado"]}">{e(T[p["estado"]][l])}</span>'


def portada(p, l, desde, clase="portada", prioridad=False):
    if p.get("portada"):
        w, h = tam(p["portada"])
        carga = ' fetchpriority="high"' if prioridad else ' loading="lazy"'
        return (f'<div class="{clase} con-foto"><img src="{rel(desde, p["portada"])}" width="{w}" height="{h}" '
                f'alt="{e(tx(p["titulo"], l))}"{carga} decoding="async"></div>')
    return (f'<div class="{clase}" aria-hidden="true"><span class="portada-ref">{p["num"]}</span>'
            f'<span class="portada-cota"></span>'
            f'<span class="portada-caj"><b>REF. {p["num"]}</b><i>{e(tx(p["etiquetas"][0], l))}</i></span></div>')


def cifras(p, l):
    if not p.get("cifras"):
        return ""
    items = "".join(f'<div><dt>{e(c["v"])}</dt><dd>{e(tx(c["l"], l))}</dd></div>' for c in p["cifras"])
    return f'<dl class="cifras">{items}</dl>'


def figura(g, l, ruta, estilo=""):
    pie = e(tx(g["pie"], l))
    w, h = tam(g["img"])
    st = f' style="{estilo}"' if estilo else ""
    if g.get("video"):
        media = (f'<video controls preload="none" playsinline width="{w}" height="{h}" poster="{rel(ruta, g["img"])}">'
                 f'<source src="{rel(ruta, g["video"])}" type="video/mp4"></video>')
        return f'<figure class="fig fig-video"{st}>{media}<figcaption>{pie}</figcaption></figure>'
    src = rel(ruta, g["img"])
    media = (f'<a href="{src}" data-visor aria-label="{e(T["ampliar"][l])}: {pie}">'
             f'<img src="{src}" width="{w}" height="{h}" alt="{pie}" loading="lazy" decoding="async"></a>')
    return f'<figure class="fig"{st}>{media}<figcaption>{pie}</figcaption></figure>'


def fila_figuras(fila, l, ruta):
    """Fila justificada: todas las figuras a la misma altura, sin ampliar demasiado las pequeñas."""
    tams = [tam(g["img"]) for g in fila]
    ancho_nat = sum(w for w, _ in tams)
    figs = "".join(figura(g, l, ruta, f"flex:{w / h:.4f} 1 0%") for g, (w, h) in zip(fila, tams))
    return f'<div class="fila-figs n{len(fila)}" style="max-width:{int(ancho_nat * 1.2)}px">{figs}</div>'


def barras(b, l):
    filas = []
    for x in b["barras"]:
        pct = 100 * x["v"] / b["max"]
        valor = f'{num(x["v"], l, b["dec"])} {b["unidad"]}'
        clases = "bar" + (" bar-b" if x.get("serie") == "b" else "") + (" bar-sep" if x.get("sep") else "")
        filas.append(f'<div class="{clases}"><dt>{e(tx(x["l"], l))}</dt>'
                     f'<dd><span class="bar-pista"><span class="bar-v" style="width:{pct:.1f}%"></span></span>'
                     f'<span class="bar-n">{e(valor)}</span></dd></div>')
    limite = ""
    if b.get("limite"):
        pct = 100 * b["limite"]["v"] / b["max"]
        limite = f'<div class="bar-lim" style="--lim:{pct:.1f}%"><span>{e(tx(b["limite"]["l"], l))}</span></div>'
    return (f'<figure class="barras{" con-limite" if limite else ""}"><figcaption>{e(tx(b["titulo"], l))}</figcaption>'
            f'<dl>{"".join(filas)}</dl>{limite}</figure>')


# ───────────────────────────── Cruz de Malta (geometría real, 4 ranuras)

def _pol(r, grados):
    a = math.radians(grados)
    return r * math.cos(a), r * math.sin(a)


def _pt(p):
    return f"{p[0]:.2f} {p[1]:.2f}"


def ginebra_svg(l):
    a = 100.0                       # distancia entre centros
    r = a / math.sqrt(2)            # radio de la manivela (pivote)
    R = a / math.sqrt(2)            # radio exterior de la cruz
    pin = 4.2                       # radio del pivote
    w = pin + 0.8                   # semiancho de ranura
    c = a - r                       # fondo de ranura (posición mínima del pivote)
    rho = 52.0                      # radio del rebaje de bloqueo en la cruz
    rho_d = rho - 1.2               # radio del disco de bloqueo
    Rc = R + 2.0                    # radio del rebaje del disco
    eps = math.degrees(math.asin(w / R))
    delta = math.degrees(math.acos((R * R + a * a - rho * rho) / (2 * a * R)))

    # Contorno de la cruz (ranuras a 0°, 90°, 180°, 270°; rebajes a 45° + k·90°)
    d = [f"M{_pt(_pol(R, eps))}"]
    for k in range(4):
        b0 = 90 * k
        d.append(f"A{R:.2f} {R:.2f} 0 0 1 {_pt(_pol(R, b0 + 45 - delta))}")
        d.append(f"A{rho:.2f} {rho:.2f} 0 0 0 {_pt(_pol(R, b0 + 45 + delta))}")
        d.append(f"A{R:.2f} {R:.2f} 0 0 1 {_pt(_pol(R, b0 + 90 - eps))}")
        th = math.radians(b0 + 90)
        u = (math.cos(th), math.sin(th)); n = (-math.sin(th), math.cos(th))
        cerca = (c * u[0] - w * n[0], c * u[1] - w * n[1])
        lejos = (c * u[0] + w * n[0], c * u[1] + w * n[1])
        d.append(f"L{_pt(cerca)}")
        d.append(f"A{w:.2f} {w:.2f} 0 0 0 {_pt(lejos)}")
        d.append(f"L{_pt(_pol(R, b0 + 90 + eps))}")
    cruz = " ".join(d) + "Z"

    # Disco de bloqueo de la rueda motriz (pivote en +x local)
    gam = math.degrees(math.acos((rho_d ** 2 + a * a - Rc * Rc) / (2 * a * rho_d)))
    pts = [_pol(rho_d, gam + (360 - 2 * gam) * k / 80) for k in range(81)]          # borde del disco
    psi = math.degrees(math.atan2(rho_d * math.sin(math.radians(gam)), a - rho_d * math.cos(math.radians(gam))))
    for k in range(41):                                                              # rebaje: arco centrado en (a, 0)
        ang = math.radians(180 + psi - 2 * psi * k / 40)
        pts.append((a + Rc * math.cos(ang), Rc * math.sin(ang)))
    disco = "M" + " L".join(_pt(q) for q in pts) + "Z"

    # Pose inicial (sin JavaScript): mitad del arrastre
    phi = 18.0
    px, py = a - r * math.cos(math.radians(phi)), r * math.sin(math.radians(phi))
    theta = math.degrees(math.atan2(py, px))
    beta = 180 - phi
    marcas = "".join(
        f'<circle cx="{_pol(34, 45 + 90 * k)[0]:.2f}" cy="{_pol(34, 45 + 90 * k)[1]:.2f}" r="3.2" class="{"gin-m1" if k == 0 else "gin-m"}"/>'
        for k in range(4))
    datos = json.dumps({"a": a, "r": r})
    return f"""<figure class="ginebra" data-ginebra='{datos}' data-gira="{e(T['gin_gira'][l])}" data-bloq="{e(T['gin_bloq'][l])}">
  <div class="gin-lamina">
    <svg viewBox="-86 -96 280 192" role="img" aria-label="{e(T['gin_alt'][l])}">
      <line class="gin-eje" x1="-84" y1="0" x2="192" y2="0"/>
      <line class="gin-eje" x1="0" y1="-84" x2="0" y2="84"/>
      <line class="gin-eje" x1="{a:.0f}" y1="-84" x2="{a:.0f}" y2="84"/>
      <circle class="gin-tray" cx="{a:.0f}" cy="0" r="{r:.2f}"/>
      <g class="gin-cruz" transform="rotate({theta:.2f})"><path d="{cruz}"/>{marcas}<circle class="gin-arbol" r="5"/></g>
      <g class="gin-motriz" transform="translate({a:.0f} 0) rotate({beta:.2f})">
        <path class="gin-disco" d="{disco}"/>
        <line class="gin-brazo" x1="0" y1="0" x2="{r:.2f}" y2="0"/>
        <circle class="gin-pivote" cx="{r:.2f}" cy="0" r="{pin}"/>
        <circle class="gin-arbol" r="5"/>
      </g>
      <text class="gin-rot" x="0" y="-86" text-anchor="middle">{e(T['gin_cruz'][l])}</text>
      <text class="gin-rot" x="{a:.0f}" y="-86" text-anchor="middle">{e(T['gin_motriz'][l])}</text>
    </svg>
  </div>
  <div class="gin-panel">
    <span class="gin-estado" aria-live="off">{e(T['gin_gira'][l])}</span>
    <div class="gin-ciclo" title="{e(T['gin_ciclo'][l])}"><span class="gin-tramo"></span><span class="gin-cursor"></span></div>
    <button type="button" class="gin-btn" hidden>{e(T['pausa'][l])}</button>
  </div>
  <figcaption>{e(T['gin_pie'][l])} {e(T['gin_ciclo'][l])}.</figcaption>
</figure>"""


# ───────────────────────────── Página de inicio

def boton_cv(l, ruta):
    f = SITE["cv"].get(l)
    if not f:
        return ""
    return f'<a class="btn" href="{rel(ruta, f)}" download>{e(T["descargar_cv"][l])}</a>'


def contacto(l, ruta):
    items = [f'<li><span class="k">LinkedIn</span><a href="{SITE["linkedin"]}" rel="me">linkedin.com/in/raulgarciatavera</a></li>']
    if SITE["email"]:
        items.append(f'<li><span class="k">Email</span><a href="mailto:{e(SITE["email"])}">{e(SITE["email"])}</a></li>')
    return f"""<section class="contacto envoltura" id="contacto">
  <h2 class="sec-t">{e(T['contacto'][l])}</h2>
  <div class="contacto-in">
    <p>{e(T['disp'][l])}. {e(T['zona'][l])}.</p>
    <ul class="contacto-l">{''.join(items)}</ul>
    {boton_cv(l, ruta)}
  </div>
</section>"""


def lista_cv(items, l):
    out = []
    for it in items:
        out.append(f'<li><div class="cv-f">{e(it["f"])}</div><div class="cv-c"><h4>{e(tx(it["t"], l))}</h4><p>{e(tx(it["d"], l))}</p></div></li>')
    return f'<ol class="cv-l">{"".join(out)}</ol>'


def home(l):
    ruta = path_home(l)
    alternos = {x: path_home(x) for x in LANGS}
    tarjetas = []
    for i, p in enumerate(PROYECTOS):
        href = rel(ruta, path_proy(l, p["slug"]))
        tarjetas.append(f"""<li class="tarjeta">
  <a href="{href}" class="tarjeta-a">
    {portada(p, l, ruta, prioridad=(i == 0))}
    <div class="tarjeta-c">
      <div class="tarjeta-meta"><span class="mono">REF. {p['num']} · {e(tx(p['periodo'], l))}</span>{chip_estado(p, l)}</div>
      <h3>{e(tx(p['titulo'], l))}</h3>
      <p>{e(tx(p['resumen'], l))}</p>
      <ul class="tags">{etiquetas(p, l)}</ul>
      <span class="leer">{e(T['leer'][l])} <span aria-hidden="true">→</span></span>
    </div>
  </a>
</li>""")
    herr = "".join(
        f'<div class="herr-f"><dt>{e(tx(cat, l))}</dt><dd>{" · ".join(e(tx(x, l)) for x in items)}</dd></div>'
        for cat, items in SOBRE["herramientas"])
    cuerpo = f"""<main id="contenido">
<section class="hero">
  <div class="envoltura hero-in">
    <div class="hero-txt">
      <p class="eyebrow">{e(T['titular'][l])} · ETSEIB–UPC</p>
      <h1>{e(SITE['nombre'])}</h1>
      <p class="lema">{e(T['lema'][l])}</p>
      <p class="intro">{e(T['intro'][l])}</p>
      <div class="acciones"><a class="btn btn-p" href="#proyectos">{e(T['ver_proy'][l])}</a>{boton_cv(l, ruta)}<a class="btn" href="{SITE['linkedin']}" rel="me">LinkedIn</a></div>
    </div>
    <dl class="cajetin">
      <div><dt>{e(T['disp_t'][l])}</dt><dd>{e(T['disp'][l])}</dd></div>
      <div><dt>{e(T['zona_t'][l])}</dt><dd>{e(T['zona'][l])}</dd></div>
      <div><dt>CAD</dt><dd>SOLIDWORKS · CSWP</dd></div>
      <div><dt>{e(T['proyectos'][l])}</dt><dd>{len(PROYECTOS):02d}</dd></div>
    </dl>
  </div>
</section>

<section class="envoltura bloque" id="proyectos">
  <h2 class="sec-t">{e(T['proyectos'][l])}</h2>
  <ul class="tarjetas">{''.join(tarjetas)}</ul>
</section>

<section class="envoltura bloque" id="sobre">
  <h2 class="sec-t">{e(T['sobre'][l])}</h2>
  <div class="sobre">
    <div>
      <h3 class="sub-t">{e(T['formacion'][l])}</h3>{lista_cv(SOBRE['formacion'], l)}
      <h3 class="sub-t">{e(T['experiencia'][l])}</h3>{lista_cv(SOBRE['experiencia'], l)}
    </div>
    <div>
      <h3 class="sub-t">{e(T['certs'][l])}</h3>{lista_cv(SOBRE['certs'], l)}
      <h3 class="sub-t">{e(T['herramientas'][l])}</h3><dl class="herr">{herr}</dl>
    </div>
  </div>
</section>
{contacto(l, ruta)}
</main>"""
    titulo = f"{SITE['nombre']} · {T['lema'][l].rstrip('.')}"
    persona = {
        "@context": "https://schema.org", "@type": "Person", "name": SITE["nombre"], "url": SITE_URL,
        "jobTitle": T["titular"][l], "sameAs": [SITE["linkedin"]],
        "alumniOf": {"@type": "CollegeOrUniversity", "name": "ETSEIB, Universitat Politècnica de Catalunya"},
        "knowsAbout": ["Mechanical design", "SOLIDWORKS", "Finite element analysis", "Robotics", "Automation"],
    }
    extra = f'<script type="application/ld+json">{json.dumps(persona, ensure_ascii=False)}</script>\n'
    return ruta, pagina(l, ruta, titulo, T["intro"][l], cuerpo, alternos, extra_head=extra)


# ───────────────────────────── Página de proyecto

def seccion(s, i, l, ruta):
    partes = []
    if "p" in s:
        partes.append(f'<p>{e(s["p"][l])}</p>')
    if "l" in s:
        partes.append("<ul class=\"guiones\">" + "".join(f"<li>{e(x)}</li>" for x in s["l"][l]) + "</ul>")
    if s.get("anim") == "ginebra":
        partes.append(ginebra_svg(l))
    for fila in s.get("filas", []):
        partes.append(fila_figuras(fila, l, ruta))
    if s.get("barras"):
        partes.append(barras(s["barras"], l))
    for fila in s.get("filas2", []):
        partes.append(fila_figuras(fila, l, ruta))
    return f'<section class="psec" id="s{i + 1}"><h2>{e(s["h"][l])}</h2>{"".join(partes)}</section>'


def proyecto(l, i):
    p = PROYECTOS[i]
    ruta = path_proy(l, p["slug"])
    alternos = {x: path_proy(x, p["slug"]) for x in LANGS}
    secs = "".join(seccion(s, k, l, ruta) for k, s in enumerate(p["secciones"]))
    indice = "".join(f'<li><a href="#s{k + 1}">{e(s["h"][l])}</a></li>' for k, s in enumerate(p["secciones"]))
    galeria = ""
    if p["galeria"]:
        figs = "".join(figura(g, l, ruta) for g in p["galeria"])
        galeria = f'<section class="galeria"><h2 class="sec-t">{e(T["galeria"][l])}</h2><div class="gal">{figs}</div></section>'
    sig = PROYECTOS[(i + 1) % len(PROYECTOS)]
    home_r = rel(ruta, path_home(l))
    cuerpo = f"""<main class="envoltura proy" id="contenido">
  <a class="volver" href="{home_r}#proyectos"><span aria-hidden="true">←</span> {e(T['volver'][l])}</a>
  <header class="proy-cab">
    <div class="proy-tit">
      <p class="eyebrow">REF. {p['num']} · {e(tx(p['tipo'], l))}</p>
      <h1>{e(tx(p['titulo'], l))}</h1>
      <p class="lema">{e(tx(p['resumen'], l))}</p>
    </div>
    <dl class="cajetin">
      <div><dt>{e(T['periodo'][l])}</dt><dd>{e(tx(p['periodo'], l))}</dd></div>
      <div><dt>{e(T['papel'][l])}</dt><dd>{e(tx(p['papel'], l))}</dd></div>
      <div><dt>{e(T['estado'][l])}</dt><dd>{chip_estado(p, l)}</dd></div>
      <div><dt>{e(T['herramientas'][l])}</dt><dd><ul class="tags">{etiquetas(p, l)}</ul></dd></div>
    </dl>
  </header>
  {portada(p, l, ruta, "portada portada-g", prioridad=True)}
  {cifras(p, l)}
  <div class="proy-cuerpo">
    <nav class="proy-lat" aria-label="{e(T['contenido'][l])}"><h2 class="mini">{e(T['contenido'][l])}</h2><ol class="indice">{indice}</ol></nav>
    <div class="proy-txt">{secs}</div>
  </div>
  {galeria}
  <a class="siguiente" href="{rel(ruta, path_proy(l, sig['slug']))}">
    <span class="mini">{e(T['siguiente'][l])} · REF. {sig['num']}</span>
    <span class="sig-t">{e(tx(sig['titulo'], l))} <span aria-hidden="true">→</span></span>
  </a>
</main>"""
    titulo = f"{tx(p['titulo'], l)} · {SITE['nombre']}"
    return ruta, pagina(l, ruta, titulo, tx(p["resumen"], l), cuerpo, alternos, og_img=p.get("portada"))


# ───────────────────────────── 404, sitemap y robots

def pagina_404():
    bloques = "".join(
        f'<p lang="{x}"><strong>{e(T["e404_t"][x])}.</strong> {e(T["e404_p"][x])} '
        f'<a href="{BASE_PATH}{BASE_DIR[x]}">{e(T["inicio"][x])}</a></p>' for x in LANGS)
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>404 · {e(SITE['nombre'])}</title>
<meta name="robots" content="noindex">
<link rel="icon" href="{FAVICON}">
<link rel="stylesheet" href="{BASE_PATH}assets/estilo.css">
</head>
<body>
<main class="envoltura e404">
  <p class="eyebrow">REF. 404</p>
  <h1>404</h1>
  {bloques}
</main>
</body>
</html>
"""


def main():
    for i, p in enumerate(PROYECTOS):
        p["num"] = f"{i + 1:02d}"
    escritos = []
    for l in LANGS:
        paginas = [home(l)] + [proyecto(l, i) for i in range(len(PROYECTOS))]
        for ruta, contenido in paginas:
            destino = os.path.join(RAIZ, ruta)
            os.makedirs(os.path.dirname(destino) or RAIZ, exist_ok=True)
            with open(destino, "w", encoding="utf-8") as f:
                f.write(contenido)
            escritos.append(ruta)
    with open(os.path.join(RAIZ, "404.html"), "w", encoding="utf-8") as f:
        f.write(pagina_404())
    urls = "".join(f"<url><loc>{url_publica(r)}</loc></url>\n" for r in escritos)
    with open(os.path.join(RAIZ, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    with open(os.path.join(RAIZ, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}sitemap.xml\n")
    open(os.path.join(RAIZ, ".nojekyll"), "w").close()
    print(f"{len(escritos)} páginas generadas")


if __name__ == "__main__":
    main()
