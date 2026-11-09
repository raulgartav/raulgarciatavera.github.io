# -*- coding: utf-8 -*-
"""Genera la web estática (ES en la raíz, EN en /en, CA en /ca).
Uso:  python3 fuente/build.py      (desde la raíz del repositorio)
"""
import os, html, shutil, sys
sys.path.insert(0, os.path.dirname(__file__))
from contenido import SITE, T, SOBRE, PROYECTOS

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LANGS = ["es", "en", "ca"]
BASE_DIR = {"es": "", "en": "en/", "ca": "ca/"}
PROY_DIR = {"es": "proyectos", "en": "projects", "ca": "projectes"}
LANG_NAME = {"es": "ES", "en": "EN", "ca": "CA"}
HTML_LANG = {"es": "es", "en": "en", "ca": "ca"}
SITE_URL = "https://raulgartav.github.io/"

e = html.escape

def tx(v, l):
    """Texto traducido: dict {es,en,ca} o cadena fija."""
    return v[l] if isinstance(v, dict) else v

def path_home(l):
    return BASE_DIR[l] + "index.html"

def path_proy(l, slug):
    return f"{BASE_DIR[l]}{PROY_DIR[l]}/{slug}.html"

def rel(desde, hacia):
    """Ruta relativa entre dos archivos de la web."""
    d = os.path.dirname(desde)
    r = os.path.relpath(hacia, d or ".")
    return r.replace(os.sep, "/")

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
           "%3Crect width='32' height='32' fill='%231c3faa'/%3E%3Cpath d='M6 26V6h20v20z' fill='none' stroke='white' stroke-width='1.5'/%3E"
           "%3Ctext x='16' y='21' font-family='Arial' font-weight='700' font-size='12' fill='white' text-anchor='middle'%3ERG%3C/text%3E%3C/svg%3E")

def pagina(l, ruta, titulo, descripcion, cuerpo, alternos):
    css = rel(ruta, "assets/estilo.css")
    alt_links = "\n".join(
        f'<link rel="alternate" hreflang="{HTML_LANG[x]}" href="{SITE_URL}{alternos[x]}">' for x in LANGS)
    idiomas = "".join(
        f'<a href="{rel(ruta, alternos[x])}" hreflang="{x}" lang="{x}"{" aria-current=\"true\"" if x == l else ""}>{LANG_NAME[x]}</a>'
        for x in LANGS)
    home = rel(ruta, path_home(l))
    return f"""<!doctype html>
<html lang="{HTML_LANG[l]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(titulo)}</title>
<meta name="description" content="{e(descripcion)}">
<meta property="og:title" content="{e(titulo)}">
<meta property="og:description" content="{e(descripcion)}">
<meta property="og:type" content="website">
{alt_links}
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@75..100,500..800&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="{css}">
</head>
<body>
<header class="barra">
  <div class="barra-in">
    <a class="marca" href="{home}"><span class="marca-c">RG</span><span class="marca-n">{e(SITE['nombre'])}</span></a>
    <nav class="nav" aria-label="Principal">
      <a href="{home}#proyectos">{e(T['proyectos'][l])}</a>
      <a href="{home}#sobre">{e(T['sobre'][l])}</a>
      <a href="{home}#contacto">{e(T['contacto'][l])}</a>
      <span class="idiomas" aria-label="{e(T['otros_idiomas'][l])}">{idiomas}</span>
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
</body>
</html>
"""

def etiquetas(p, l):
    return "".join(f'<li>{e(tx(t, l))}</li>' for t in p["etiquetas"])

def chip_estado(p, l):
    return f'<span class="estado estado-{p["estado"]}">{e(T[p["estado"]][l])}</span>'

def portada(p, l, desde, clase="portada"):
    if p["galeria"]:
        g = p["galeria"][0]
        return (f'<div class="{clase} con-foto"><img src="{rel(desde, g["archivo"])}" '
                f'alt="{e(tx(g["pie"], l))}" loading="lazy"></div>')
    return (f'<div class="{clase}" aria-hidden="true"><span class="portada-ref">{p["num"]}</span>'
            f'<span class="portada-cota"></span>'
            f'<span class="portada-caj"><b>REF. {p["num"]}</b><i>{e(tx(p["etiquetas"][0], l))}</i></span></div>')

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
    for p in PROYECTOS:
        href = rel(ruta, path_proy(l, p["slug"]))
        tarjetas.append(f"""<li class="tarjeta">
  <a href="{href}" class="tarjeta-a">
    {portada(p, l, ruta)}
    <div class="tarjeta-c">
      <div class="tarjeta-meta"><span class="mono">{e(tx(p['periodo'], l))}</span>{chip_estado(p, l)}</div>
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
    cuerpo = f"""<main>
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
    return ruta, pagina(l, ruta, titulo, T["intro"][l], cuerpo, alternos)

def proyecto(l, i):
    p = PROYECTOS[i]
    ruta = path_proy(l, p["slug"])
    alternos = {x: path_proy(x, p["slug"]) for x in LANGS}
    secs = []
    for s in p["secciones"]:
        contenido = ""
        if "p" in s:
            contenido += f'<p>{e(s["p"][l])}</p>'
        if "l" in s:
            contenido += "<ul>" + "".join(f"<li>{e(x)}</li>" for x in s["l"][l]) + "</ul>"
        secs.append(f'<section class="psec"><h2>{e(s["h"][l])}</h2>{contenido}</section>')
    galeria = ""
    if p["galeria"]:
        figs = "".join(
            f'<figure><img src="{rel(ruta, g["archivo"])}" alt="{e(tx(g["pie"], l))}" loading="lazy"><figcaption>{e(tx(g["pie"], l))}</figcaption></figure>'
            for g in p["galeria"])
        galeria = f'<section class="galeria"><h2 class="sec-t">{e(T["galeria"][l])}</h2><div class="gal">{figs}</div></section>'
    sig = PROYECTOS[(i + 1) % len(PROYECTOS)]
    home_r = rel(ruta, path_home(l))
    cuerpo = f"""<main class="envoltura proy">
  <a class="volver" href="{home_r}#proyectos"><span aria-hidden="true">←</span> {e(T['volver'][l])}</a>
  <header class="proy-cab">
    <div class="proy-tit">
      <p class="eyebrow">REF. {p['num']} · {e(tx(p['tipo'], l))}</p>
      <h1>{e(tx(p['titulo'], l))}</h1>
      <p class="lema">{e(tx(p['resumen'], l))}</p>
    </div>
    <dl class="cajetin">
      <div><dt>{e(T['periodo'][l])}</dt><dd>{e(tx(p['periodo'], l))}</dd></div>
      <div><dt>{e(T['tipo'][l])}</dt><dd>{e(tx(p['tipo'], l))}</dd></div>
      <div><dt>{e(T['papel'][l])}</dt><dd>{e(tx(p['papel'], l))}</dd></div>
      <div><dt>{e(T['estado'][l])}</dt><dd>{chip_estado(p, l)}</dd></div>
    </dl>
  </header>
  {portada(p, l, ruta, "portada portada-g")}
  <div class="proy-cuerpo">
    <aside class="proy-lat"><h2 class="mini">{e(T['herramientas'][l])}</h2><ul class="tags">{etiquetas(p, l)}</ul></aside>
    <div class="proy-txt">{''.join(secs)}</div>
  </div>
  {galeria}
  <a class="siguiente" href="{rel(ruta, path_proy(l, sig['slug']))}">
    <span class="mini">{e(T['siguiente'][l])}</span>
    <span class="sig-t">{e(tx(sig['titulo'], l))} <span aria-hidden="true">→</span></span>
  </a>
</main>"""
    titulo = f"{tx(p['titulo'], l)} · {SITE['nombre']}"
    return ruta, pagina(l, ruta, titulo, tx(p["resumen"], l), cuerpo, alternos)

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
    # comprobar imágenes referenciadas
    for p in PROYECTOS:
        for g in p["galeria"]:
            if not os.path.exists(os.path.join(RAIZ, g["archivo"])):
                print("FALTA IMAGEN:", g["archivo"])
    open(os.path.join(RAIZ, ".nojekyll"), "w").close()
    print(f"{len(escritos)} páginas generadas")

if __name__ == "__main__":
    main()
