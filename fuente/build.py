# -*- coding: utf-8 -*-
"""Genera la web estática (ES en la raíz, EN en /en, CA en /ca).
Uso:  python3 fuente/build.py      (desde la raíz del repositorio)
Requiere Pillow (lee el tamaño de las imágenes y genera sus versiones WebP).

Estructura:
  contenido.py   textos de la web y datos de "Sobre mí"
  proyectos.py   contenido de cada proyecto y su maquetación
  build.py       plantillas HTML (este archivo)
  ../assets/     estilo.css, sitio.js, fuentes
"""
import os, html, sys, json, math
from urllib.parse import urlparse, quote
from PIL import Image
sys.path.insert(0, os.path.dirname(__file__))
from contenido import SITE, T, SOBRE, PROYECTOS, GANCHOS, DESTACADOS

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LANGS = ["es", "en", "ca"]
BASE_DIR = {"es": "", "en": "en/", "ca": "ca/"}
PROY_DIR = {"es": "proyectos", "en": "projects", "ca": "projectes"}
LANG_NAME = {"es": "ES", "en": "EN", "ca": "CA"}
OG_LOCALE = {"es": "es_ES", "en": "en_GB", "ca": "ca_ES"}
# Dirección pública de la web. Cambiar aquí si cambia el usuario o el dominio.
SITE_URL = "https://raulgartav.github.io/"
BASE_PATH = urlparse(SITE_URL).path          # "/"
OG_IMG = "assets/og.png"
ANCHOS_WEBP = (640, 1100)                    # versiones reducidas de cada imagen

e = html.escape


# ───────────────────────────── Utilidades

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


_VAR = {}
def variantes(archivo):
    """Versiones WebP de una imagen (las crea si faltan). Devuelve [(ruta, ancho)]."""
    if archivo in _VAR:
        return _VAR[archivo]
    w, h = tam(archivo)
    carpeta = os.path.join(os.path.dirname(archivo), "web")
    nombre = os.path.splitext(os.path.basename(archivo))[0]
    os.makedirs(os.path.join(RAIZ, carpeta), exist_ok=True)
    origen = os.path.join(RAIZ, archivo)
    out = []
    for ancho in [a for a in ANCHOS_WEBP if a < w] + [w]:
        ruta = f"{carpeta}/{nombre}-{ancho}.webp"
        destino = os.path.join(RAIZ, ruta)
        if not os.path.exists(destino) or os.path.getmtime(destino) < os.path.getmtime(origen):
            with Image.open(origen) as im:
                im = im.convert("RGB")
                if ancho < w:
                    im = im.resize((ancho, round(h * ancho / w)), Image.LANCZOS)
                im.save(destino, "WEBP", quality=80, method=6)
        out.append((ruta, ancho))
    _VAR[archivo] = out
    return out


def pic(archivo, alt, ruta, sizes="100vw", lazy=True, attrs=""):
    """<picture> con WebP en varios anchos y el JPG original de reserva."""
    w, h = tam(archivo)
    srcset = ", ".join(f"{rel(ruta, v)} {a}w" for v, a in variantes(archivo))
    carga = 'loading="lazy"' if lazy else 'fetchpriority="high"'
    return (f'<picture><source type="image/webp" srcset="{srcset}" sizes="{sizes}">'
            f'<img src="{rel(ruta, archivo)}" width="{w}" height="{h}" alt="{e(alt)}" {carga} decoding="async"{attrs}></picture>')


ICONO = {
    "flecha": '<svg class="ico ico-der" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "atras": '<svg class="ico ico-izq" viewBox="0 0 24 24" aria-hidden="true"><path d="M19 12H5M11 6l-6 6 6 6"/></svg>',
    "fuera": '<svg class="ico ico-fuera" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17L17 7M9 7h8v8"/></svg>',
    "abajo": '<svg class="ico ico-abajo" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M6 13l6 6 6-6"/></svg>',
}


# ───────────────────────────── Cruz de Malta (geometría real, 4 ranuras)

def _pol(r, grados):
    a = math.radians(grados)
    return r * math.cos(a), r * math.sin(a)


def _pt(p):
    return f"{p[0]:.2f} {p[1]:.2f}"


def _geometria():
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
    return {"a": a, "r": r, "pin": pin, "cruz": cruz, "disco": disco,
            "theta": math.degrees(math.atan2(py, px)), "beta": 180 - phi}


GEO = _geometria()
MARCA = f'<svg class="marca-i" viewBox="-72 -72 144 144" aria-hidden="true"><path d="{GEO["cruz"]}"/></svg>'
FAVICON = "data:image/svg+xml," + quote(
    f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='-84 -84 168 168'><path fill='#d0282e' d='{GEO['cruz']}'/></svg>")


def _mecanismo_svg(l, rotulos):
    g = GEO
    a, r = g["a"], g["r"]
    px, py = _pol(34, 45)
    textos = ""
    if rotulos:
        textos = (f'<text class="gin-rot" x="0" y="-84" text-anchor="middle">{e(T["gin_cruz"][l])}</text>'
                  f'<text class="gin-rot" x="{a:.0f}" y="-84" text-anchor="middle">{e(T["gin_motriz"][l])}</text>')
    caja = "-86 -96 280 192" if rotulos else "-80 -80 262 160"
    return f"""<svg viewBox="{caja}" role="img" aria-label="{e(T['gin_alt'][l])}">
      <line class="gin-eje" x1="-78" y1="0" x2="180" y2="0"/>
      <line class="gin-eje" x1="0" y1="-78" x2="0" y2="78"/>
      <line class="gin-eje" x1="{a:.0f}" y1="-78" x2="{a:.0f}" y2="78"/>
      <circle class="gin-tray" cx="{a:.0f}" cy="0" r="{r:.2f}"/>
      <g class="gin-cruz" transform="rotate({g['theta']:.2f})"><path d="{g['cruz']}"/><circle class="gin-m" cx="{px:.2f}" cy="{py:.2f}" r="3.4"/><circle class="gin-arbol" r="5"/></g>
      <g class="gin-motriz" transform="translate({a:.0f} 0) rotate({g['beta']:.2f})">
        <path class="gin-disco" d="{g['disco']}"/>
        <line class="gin-brazo" x1="0" y1="0" x2="{r:.2f}" y2="0"/>
        <circle class="gin-pivote" cx="{r:.2f}" cy="0" r="{g['pin']}"/>
        <circle class="gin-arbol" r="5"/>
      </g>{textos}
    </svg>"""


def _datos_ginebra(l):
    datos = json.dumps({"a": GEO["a"], "r": GEO["r"]})
    return f"data-ginebra='{datos}' data-gira=\"{e(T['gin_gira'][l])}\" data-bloq=\"{e(T['gin_bloq'][l])}\""


def ginebra_figura(l):
    """Animación completa, para la página del proyecto."""
    return f"""<figure class="ginebra rv" {_datos_ginebra(l)}>
  <div class="gin-lamina">
    {_mecanismo_svg(l, True)}
  </div>
  <div class="gin-panel">
    <span class="gin-estado" aria-live="off">{e(T['gin_gira'][l])}</span>
    <div class="gin-ciclo" title="{e(T['gin_ciclo'][l])}"><span class="gin-tramo"></span><span class="gin-cursor"></span></div>
    <button type="button" class="gin-btn" hidden>{e(T['pausa'][l])}</button>
  </div>
  <figcaption>{e(T['gin_pie'][l])} {e(T['gin_ciclo'][l])}.</figcaption>
</figure>"""


def ginebra_hero(l, href):
    """El mismo mecanismo, como imagen de entrada de la web."""
    return f"""<figure class="mec" {_datos_ginebra(l)}>
      {_mecanismo_svg(l, False)}
      <figcaption>
        <span class="mec-estado"><span class="gin-estado" aria-live="off">{e(T['gin_gira'][l])}</span><button type="button" class="gin-btn" hidden>{e(T['pausa'][l])}</button></span>
        <span class="mec-pie">{e(T['mec_pie'][l])} <a href="{href}">{e(T['ver'][l])}</a></span>
      </figcaption>
    </figure>"""


# ───────────────────────────── Plantilla de página

def pagina(l, ruta, titulo, descripcion, cuerpo, alternos, og_img=None, extra_head="", clase=""):
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
<meta name="theme-color" content="#f4f6f7" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0c1322" media="(prefers-color-scheme: dark)">
<link rel="icon" href="{FAVICON}">
<link rel="preload" href="{r('assets/fuentes/mona-sans-latin.woff2')}" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{r('assets/estilo.css')}">
<script>document.documentElement.classList.add("js");window.TXT={json.dumps(textos_js, ensure_ascii=False)}</script>
<script src="{r('assets/sitio.js')}" defer></script>
{extra_head}</head>
<body{f' class="{clase}"' if clase else ''}>
<a class="saltar" href="#contenido">{e(T['saltar'][l])}</a>
<header class="barra">
  <div class="ancho barra-in">
    <a class="marca" href="{home}">{MARCA}<span>{e(SITE['nombre'])}</span></a>
    <button type="button" class="menu-btn" aria-expanded="false" aria-controls="nav" hidden>{e(T['menu'][l])}</button>
    <nav class="nav" id="nav" aria-label="{e(T['contenido'][l])}">
      <a href="{home}#proyectos">{e(T['proyectos'][l])}</a>
      <a href="{home}#sobre">{e(T['sobre'][l])}</a>
      <a href="{home}#contacto">{e(T['contacto'][l])}</a>
      <span class="idiomas" role="group" aria-label="{e(T['otros_idiomas'][l])}">{idiomas}</span>
    </nav>
  </div>
</header>
{cuerpo}
<footer class="pie">
  <div class="ancho pie-in">
    <span>© 2026 {e(SITE['nombre'])}</span>
    <span>{e(T['pie'][l])}</span>
    <span class="pie-enl"><a href="{SITE['linkedin']}" rel="me">LinkedIn</a><a href="{SITE['github']}" rel="me">GitHub</a></span>
  </div>
</footer>
</body>
</html>
"""


# ───────────────────────────── Piezas comunes

def etiquetas(p, l):
    return "".join(f'<li>{e(tx(t, l))}</li>' for t in p["etiquetas"])


def chip_estado(p, l):
    return f'<span class="estado estado-{p["estado"]}">{e(T[p["estado"]][l])}</span>'


def cifras(p, l, clase="cifras", maximo=None):
    if not p.get("cifras"):
        return ""
    lista = p["cifras"][:maximo] if maximo else p["cifras"]
    items = "".join(f'<div><dt>{e(c["v"])}</dt><dd>{e(tx(c["l"], l))}</dd></div>' for c in lista)
    return f'<dl class="{clase}">{items}</dl>'


def figura(g, l, ruta, estilo="", sizes="(min-width: 1100px) 780px, 92vw"):
    pie = e(tx(g["pie"], l))
    w, h = tam(g["img"])
    st = f' style="{estilo}"' if estilo else ""
    if g.get("video"):
        media = (f'<video controls preload="none" playsinline width="{w}" height="{h}" poster="{rel(ruta, g["img"])}">'
                 f'<source src="{rel(ruta, g["video"])}" type="video/mp4"></video>')
        return f'<figure class="fig fig-video"{st}>{media}<figcaption>{pie}</figcaption></figure>'
    src = rel(ruta, g["img"])
    media = (f'<a href="{src}" data-visor aria-label="{e(T["ampliar"][l])}: {pie}">'
             f'{pic(g["img"], tx(g["pie"], l), ruta, sizes)}</a>')
    return f'<figure class="fig"{st}>{media}<figcaption>{pie}</figcaption></figure>'


def fila_figuras(fila, l, ruta):
    """Fila justificada: todas las figuras a la misma altura, sin ampliar demasiado las pequeñas."""
    tams = [tam(g["img"]) for g in fila]
    ancho_nat = sum(w for w, _ in tams)
    sizes = "(min-width: 1100px) 780px, 92vw" if len(fila) == 1 else "(min-width: 1100px) 390px, 46vw"
    figs = "".join(figura(g, l, ruta, f"flex:{w / h:.4f} 1 0%", sizes) for g, (w, h) in zip(fila, tams))
    return f'<div class="fila-figs n{len(fila)} rv" style="max-width:{int(ancho_nat * 1.2)}px">{figs}</div>'


def barras(b, l):
    filas = []
    for i, x in enumerate(b["barras"]):
        pct = 100 * x["v"] / b["max"]
        valor = f'{num(x["v"], l, b["dec"])} {b["unidad"]}'
        clases = "bar" + (" bar-b" if x.get("serie") == "b" else "") + (" bar-sep" if x.get("sep") else "")
        filas.append(f'<div class="{clases}" style="--i:{i}"><dt>{e(tx(x["l"], l))}</dt>'
                     f'<dd><span class="bar-pista"><span class="bar-v" style="width:{pct:.1f}%"></span></span>'
                     f'<span class="bar-n">{e(valor)}</span></dd></div>')
    limite, estilo = "", ""
    if b.get("limite"):
        estilo = f' style="--lim:{100 * b["limite"]["v"] / b["max"]:.1f}%"'
        limite = f'<p class="bar-ley"><span aria-hidden="true"></span>{e(tx(b["limite"]["l"], l))}</p>'
    return (f'<figure class="barras rv{" con-limite" if limite else ""}"{estilo}><figcaption>{e(tx(b["titulo"], l))}</figcaption>'
            f'<dl>{"".join(filas)}</dl>{limite}</figure>')


# ───────────────────────────── Página de inicio

def palabras(texto):
    """Envuelve cada palabra para que el titular aparezca palabra a palabra."""
    return " ".join(f'<span class="pal"><span style="--i:{i}">{e(w)}</span></span>' for i, w in enumerate(texto.split()))


def meta_obra(p, l):
    return f'{e(tx(p["tipo"], l))} · {e(tx(p["periodo"], l))}'


def obra(p, l, ruta, primera):
    """Proyecto destacado de la portada. Cada uno tiene su propia composición."""
    d = DESTACADOS[p["slug"]]
    href = rel(ruta, path_proy(l, p["slug"]))
    titulo = tx(p["titulo"], l)
    vt = f' style="view-transition-name:foto-{p["slug"]}"'
    sizes = "(min-width: 1000px) 1160px, 92vw" if d["forma"] == "c" else "(min-width: 1000px) 680px, 92vw"
    foto = pic(p["portada"], titulo, ruta, sizes, lazy=not primera)
    if d.get("video"):
        w, h = tam(p["portada"])
        media = (f'<div class="obra-foto"{vt}><video class="obra-video" muted loop playsinline preload="none" width="{w}" height="{h}" '
                 f'poster="{rel(ruta, p["portada"])}" aria-label="{e(T["video_alt"][l])}" data-auto>'
                 f'<source src="{rel(ruta, d["video"])}" type="video/mp4"></video>'
                 f'<button type="button" class="video-btn" hidden>{e(T["pausa"][l])}</button></div>')
    else:
        media = f'<div class="obra-foto"{vt}>{foto}</div>'
    if d.get("extra"):
        media += f'<div class="obra-extra">{pic(d["extra"], tx(d["extra_alt"], l), ruta, "(min-width: 1000px) 300px, 40vw")}</div>'
    return f"""<article class="obra obra-{d['forma']}">
    <div class="obra-media rv-foto">{media}</div>
    <div class="obra-txt rv">
      <p class="obra-meta">{meta_obra(p, l)}</p>
      <h3><a href="{href}">{e(titulo)}</a></h3>
      <p class="obra-gancho">{e(GANCHOS[p['slug']][l])}</p>
      {cifras(p, l, "obra-cifras", 3)}
      <span class="ver" aria-hidden="true">{e(T['ver'][l])}{ICONO['flecha']}</span>
    </div>
  </article>"""


def otro(p, l, ruta):
    href = rel(ruta, path_proy(l, p["slug"]))
    return f"""<li class="otro rv">
      <p class="obra-meta">{e(tx(p['tipo'], l))}{chip_estado(p, l)}</p>
      <h3><a href="{href}">{e(tx(p['titulo'], l))}</a></h3>
      <p>{e(tx(p['resumen'], l))}</p>
      <ul class="tags">{etiquetas(p, l)}</ul>
      <span class="ver" aria-hidden="true">{e(T['ver'][l])}{ICONO['flecha']}</span>
    </li>"""


def fila_cv(titulo, items, l):
    filas = "".join(
        f'<li><span class="cv-f">{e(it["f"])}</span><div><h4>{e(tx(it["t"], l))}</h4><p>{e(tx(it["d"], l))}</p></div></li>'
        for it in items)
    return f'<div class="cv-fila rv"><h3>{e(titulo)}</h3><ol class="cv-l">{filas}</ol></div>'


def home(l):
    ruta = path_home(l)
    alternos = {x: path_home(x) for x in LANGS}
    con_foto = [p for p in PROYECTOS if p["slug"] in DESTACADOS and p.get("portada")]
    resto = [p for p in PROYECTOS if p not in con_foto]
    obras = "\n  ".join(obra(p, l, ruta, i == 0) for i, p in enumerate(con_foto))
    otros = "".join(otro(p, l, ruta) for p in resto)
    herr = "".join(
        f'<div><dt>{e(tx(cat, l))}</dt><dd>{", ".join(e(tx(x, l)) for x in items)}</dd></div>'
        for cat, items in SOBRE["herramientas"])
    cv_boton = ""
    if SITE["cv"].get(l):
        cv_boton = f'<a class="btn" href="{rel(ruta, SITE["cv"][l])}" download>{e(T["descargar_cv"][l])}</a>'
    correo = ""
    if SITE["email"]:
        correo = f'<li><a href="mailto:{e(SITE["email"])}">{e(SITE["email"])}</a></li>'
    cuerpo = f"""<main id="contenido">
<section class="hero">
  <div class="ancho hero-in">
    <div class="hero-txt">
      <p class="hero-quien">{e(T['titular'][l])}, ETSEIB (UPC)</p>
      <h1>{palabras(T['lema'][l])}</h1>
      <p class="hero-intro">{e(T['intro_hero'][l])}</p>
      <div class="acciones">
        <a class="btn btn-p" href="#proyectos">{e(T['ver_proy'][l])}{ICONO['abajo']}</a>{cv_boton}
        <a class="btn" href="{SITE['linkedin']}" rel="me">LinkedIn{ICONO['fuera']}</a>
        <a class="btn" href="{SITE['github']}" rel="me">GitHub{ICONO['fuera']}</a>
      </div>
    </div>
    {ginebra_hero(l, rel(ruta, path_proy(l, 'clasificador-color')))}
  </div>
  <dl class="ancho hero-datos">
    <div><dt>{e(T['disp_t'][l])}</dt><dd>{e(T['disp'][l])}</dd></div>
    <div><dt>{e(T['zona_t'][l])}</dt><dd>{e(T['zona'][l])}</dd></div>
    <div><dt>{e(T['cert_t'][l])}</dt><dd>SOLIDWORKS CSWP</dd></div>
    <div><dt>{e(T['idiomas_t'][l])}</dt><dd>{e(T['idiomas'][l])}</dd></div>
  </dl>
</section>

<section class="ancho bloque" id="proyectos">
  <header class="bloque-cab rv">
    <h2>{e(T['proyectos'][l])}</h2>
    <p>{e(T['proy_intro'][l])}</p>
  </header>
  {obras}
  <div class="otros">
    <h2 class="otros-t rv">{e(T['otros'][l])}</h2>
    <ul class="otros-l">{otros}</ul>
  </div>
</section>

<section class="ancho bloque sobre" id="sobre">
  <h2 class="rv">{e(T['sobre'][l])}</h2>
  <div class="sobre-c">
    {fila_cv(T['formacion'][l], SOBRE['formacion'], l)}
    {fila_cv(T['experiencia'][l], SOBRE['experiencia'], l)}
    {fila_cv(T['certs'][l], SOBRE['certs'], l)}
    <div class="cv-fila rv"><h3>{e(T['herramientas'][l])}</h3><dl class="herr">{herr}</dl></div>
  </div>
</section>

<section class="contacto" id="contacto">
  <div class="ancho contacto-in rv">
    <h2>{e(T['contacto_t'][l])}</h2>
    <div class="contacto-c">
      <p>{e(T['contacto_p'][l])} {e(T['zona'][l])}.</p>
      <ul class="contacto-l">
        <li><a href="{SITE['linkedin']}" rel="me">LinkedIn{ICONO['fuera']}</a></li>
        <li><a href="{SITE['github']}" rel="me">GitHub{ICONO['fuera']}</a></li>{correo}
      </ul>
    </div>
  </div>
</section>
</main>"""
    titulo = f"{SITE['nombre']} · {T['lema'][l].rstrip('.')}"
    persona = {
        "@context": "https://schema.org", "@type": "Person", "name": SITE["nombre"], "url": SITE_URL,
        "jobTitle": T["titular"][l], "sameAs": [SITE["linkedin"], SITE["github"]],
        "alumniOf": {"@type": "CollegeOrUniversity", "name": "ETSEIB, Universitat Politècnica de Catalunya"},
        "knowsAbout": ["Mechanical design", "SOLIDWORKS", "Finite element analysis", "Robotics", "Automation"],
    }
    extra = f'<script type="application/ld+json">{json.dumps(persona, ensure_ascii=False)}</script>\n'
    return ruta, pagina(l, ruta, titulo, T["intro"][l], cuerpo, alternos, extra_head=extra, clase="inicio")


# ───────────────────────────── Página de proyecto

def seccion(s, i, l, ruta):
    partes = []
    if "p" in s:
        partes.append(f'<p class="rv">{e(s["p"][l])}</p>')
    if "l" in s:
        partes.append('<ul class="guiones rv">' + "".join(f"<li>{e(x)}</li>" for x in s["l"][l]) + "</ul>")
    if s.get("anim") == "ginebra":
        partes.append(ginebra_figura(l))
    for fila in s.get("filas", []):
        partes.append(fila_figuras(fila, l, ruta))
    if s.get("barras"):
        partes.append(barras(s["barras"], l))
    for fila in s.get("filas2", []):
        partes.append(fila_figuras(fila, l, ruta))
    return f'<section class="psec" id="s{i + 1}"><h2 class="rv">{e(s["h"][l])}</h2>{"".join(partes)}</section>'


def proyecto(l, i):
    p = PROYECTOS[i]
    ruta = path_proy(l, p["slug"])
    alternos = {x: path_proy(x, p["slug"]) for x in LANGS}
    secs = "".join(seccion(s, k, l, ruta) for k, s in enumerate(p["secciones"]))
    indice = "".join(f'<li><a href="#s{k + 1}">{e(s["h"][l])}</a></li>' for k, s in enumerate(p["secciones"]))
    galeria = ""
    if p["galeria"]:
        figs = "".join(figura(g, l, ruta) for g in p["galeria"])
        galeria = f'<section class="galeria"><h2>{e(T["galeria"][l])}</h2><div class="gal">{figs}</div></section>'
    portada = ""
    if p.get("portada"):
        portada = (f'<div class="ancho-g proy-portada" style="view-transition-name:foto-{p["slug"]}">'
                   f'{pic(p["portada"], tx(p["titulo"], l), ruta, "(min-width: 1400px) 1320px, 96vw", lazy=False)}</div>')
    sig = PROYECTOS[(i + 1) % len(PROYECTOS)]
    home_r = rel(ruta, path_home(l))
    cuerpo = f"""<div class="progreso" role="progressbar" aria-label="{e(T['progreso'][l])}" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0"><span></span></div>
<main class="proy" id="contenido">
  <header class="ancho proy-cab">
    <a class="volver" href="{home_r}#proyectos">{ICONO['atras']}{e(T['volver'][l])}</a>
    <p class="obra-meta">{e(tx(p['tipo'], l))}</p>
    <h1>{e(tx(p['titulo'], l))}</h1>
    <p class="proy-lema">{e(tx(p['resumen'], l))}</p>
  </header>
  {portada}
  <div class="ancho">
    <dl class="ficha{'' if portada else ' ficha-sola'}">
      <div><dt>{e(T['periodo'][l])}</dt><dd>{e(tx(p['periodo'], l))}</dd></div>
      <div><dt>{e(T['papel'][l])}</dt><dd>{e(tx(p['papel'], l))}</dd></div>
      <div><dt>{e(T['estado'][l])}</dt><dd>{chip_estado(p, l)}</dd></div>
      <div class="ficha-herr"><dt>{e(T['herramientas'][l])}</dt><dd><ul class="tags">{etiquetas(p, l)}</ul></dd></div>
    </dl>
    {cifras(p, l, "cifras rv")}
    <div class="proy-cuerpo">
      <nav class="proy-lat" aria-label="{e(T['contenido'][l])}"><h2>{e(T['contenido'][l])}</h2><ol class="indice">{indice}</ol></nav>
      <div class="proy-txt">{secs}</div>
    </div>
    {galeria}
  </div>
  <a class="siguiente" href="{rel(ruta, path_proy(l, sig['slug']))}">
    <span class="ancho siguiente-in">
      <span class="siguiente-k">{e(T['siguiente'][l])}</span>
      <span class="siguiente-t">{e(tx(sig['titulo'], l))}{ICONO['flecha']}</span>
    </span>
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
<main class="ancho e404">
  <a class="marca" href="{BASE_PATH}">{MARCA}<span>{e(SITE['nombre'])}</span></a>
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
