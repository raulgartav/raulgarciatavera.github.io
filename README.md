# raulgartav.github.io

Portfolio de proyectos de Raúl García Tavera (ES / EN / CA): https://raulgartav.github.io

La web solo explica proyectos, del más reciente al más antiguo (el orden está en `ORDEN`). Los datos de currículum no van aquí.

Web estática sin dependencias: un generador en Python escribe el HTML, y el diseño y la interacción están en un CSS y un JS propios.

## Cómo está organizada

| Qué | Dónde |
|---|---|
| Textos de la web | `fuente/contenido.py` |
| Contenido de cada proyecto, orden, figuras por sección y portada | `fuente/proyectos.py` (`PROYECTOS`, `ORDEN`, `MAQUETA`, `GANCHOS`, `DESTACADOS`) |
| Plantillas HTML | `fuente/build.py` |
| Diseño | `assets/estilo.css` |
| Animaciones e interacción | `assets/sitio.js` |
| Fotos y vídeos | `img/<proyecto>/` (las versiones WebP se generan solas en `img/<proyecto>/web/`) |

## Publicar un cambio

1. Editar el contenido o añadir fotos en `img/<proyecto>/`.
2. Generar las páginas: `python3 fuente/build.py` (Python 3 con Pillow).
3. Subir a `main`. GitHub Pages publica la rama tal cual.

## Notas de diseño

- Tipografía: Mona Sans variable (SIL Open Font License), alojada en `assets/fuentes/`.
- La Cruz de Malta de la portada y de la página del clasificador se dibuja a partir de su geometría y se mueve con su cinemática real.
- Las animaciones respetan `prefers-reduced-motion`, y sin JavaScript la web se lee completa.
