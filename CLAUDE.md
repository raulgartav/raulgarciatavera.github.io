# Portfolio de proyectos de Raúl García Tavera

Web publicada en https://raulgartav.github.io (GitHub Pages sirve la rama `main` tal cual).

## Qué es y qué no es

- Es un sitio para ver los proyectos de Raúl **con detalle**. No es un currículum: nada de formación, experiencia, certificaciones ni disponibilidad.
- Los proyectos van **del más reciente al más antiguo** (`ORDEN` en `fuente/proyectos.py`). Uno nuevo se añade al principio.
- La web está en construcción y lo dice en la cabecera de «Proyectos».
- **No inventar** datos, resultados ni características. Si falta un dato, se pregunta a Raúl. No incluir datos irrelevantes.
- Todo texto existe en castellano, inglés y catalán (`es`, `en`, `ca`).
- Contacto: solo LinkedIn y correo.

## Cómo está hecha

Web estática sin dependencias. No se edita el HTML generado: se edita la fuente y se vuelve a generar.

| Qué | Dónde |
|---|---|
| Textos generales | `fuente/contenido.py` |
| Proyectos: contenido, orden, figuras por sección, portada | `fuente/proyectos.py` (`PROYECTOS`, `ORDEN`, `MAQUETA`, `GANCHOS`, `DESTACADOS`) |
| Plantillas HTML y esquemas SVG | `fuente/build.py` |
| Diseño | `assets/estilo.css` |
| Animaciones e interacción | `assets/sitio.js` |
| Fotos y vídeos | `img/<proyecto>/` (los WebP de `web/` se generan solos) |

## Flujo de trabajo

1. Editar la fuente o añadir material en `img/<proyecto>/`.
2. `python3 fuente/build.py` (necesita Pillow).
3. Revisar en local: `python3 -m http.server 8765` y abrir http://localhost:8765. Mirar ordenador y móvil.
4. Commit y push a `main` cuando Raúl dé el visto bueno.

## Diseño

- Una sola tipografía (Mona Sans variable), papel frío, tinta azul marino y rojo PLA como único acento. Tema oscuro automático.
- Cada proyecto tiene su propia composición en la portada (`DESTACADOS`). Los que no tienen fotos usan un esquema animado; cuando haya fotos, se sustituye.
- Animaciones sobrias, siempre con `prefers-reduced-motion`, y la web debe leerse completa sin JavaScript.
- Responder a Raúl en castellano.

## Pendiente

- Fotos o vídeo del brazo robótico.
- Resultado del ensayo de la viga en el laboratorio.
