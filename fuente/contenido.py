# -*- coding: utf-8 -*-
# Textos de la web. Cada texto tiene versión es / en / ca.
# La web solo explica proyectos: los datos de currículum están en el CV, no aquí.
# Para añadir fotos: copiar los archivos en img/<slug>/ y listarlos en "galeria".

SITE = {
    "nombre": "Raúl García Tavera",
    "linkedin": "https://www.linkedin.com/in/raulgarciatavera/",
    "github": "https://github.com/raulgartav",
    "email": None,          # p. ej. "raulgarciatavera123@gmail.com" — pendiente de confirmar
    "cv": {                 # PDF del CV por idioma (ruta dentro de la web); None = no se muestra
        "es": None, "en": None, "ca": None,
    },
}

T = {
    "titular": {
        "es": "Estudiante de Ingeniería en Tecnologías Industriales",
        "en": "Industrial Technology Engineering student",
        "ca": "Estudiant d'Enginyeria en Tecnologies Industrials",
    },
    "lema": {
        "es": "Diseño mecánico, robótica y automatización.",
        "en": "Mechanical design, robotics and automation.",
        "ca": "Disseny mecànic, robòtica i automatització.",
    },
    "intro": {
        "es": "Estudio cuarto curso en la ETSEIB (UPC). Me interesan la robótica, la mecatrónica y la automatización, y quiero trabajar en un departamento de I+D, un equipo de diseño o una oficina técnica. Aquí explico con detalle los proyectos que he hecho en la carrera y en casa.",
        "en": "I am a fourth-year student at ETSEIB (UPC). I am interested in robotics, mechatronics and automation, and I want to work in an R&D department, a design team or a technical office. This site explains in detail the projects I have built at university and at home.",
        "ca": "Estudio quart curs a l'ETSEIB (UPC). M'interessen la robòtica, la mecatrònica i l'automatització, i vull treballar en un departament d'R+D, un equip de disseny o una oficina tècnica. Aquí explico amb detall els projectes que he fet a la carrera i a casa.",
    },
    "intro_hero": {
        "es": "Aquí explico con detalle los proyectos que hago en la carrera y en casa: qué problema había, qué decisiones tomé y qué resultado dieron.",
        "en": "This is where I explain in detail the projects I build at university and at home: the problem, the decisions I made and the results.",
        "ca": "Aquí explico amb detall els projectes que faig a la carrera i a casa: quin problema hi havia, quines decisions vaig prendre i quin resultat van donar.",
    },
    "proy_intro": {
        "es": "Ordenados del más reciente al más antiguo. La web está en construcción: iré añadiendo proyectos a medida que los termine.",
        "en": "Newest first. This site is a work in progress: I will add projects as I finish them.",
        "ca": "Ordenats del més recent al més antic. La web està en construcció: aniré afegint projectes a mesura que els acabi.",
    },
    "otros": {"es": "Otros proyectos", "en": "Other projects", "ca": "Altres projectes"},
    "ver": {"es": "Ver el proyecto", "en": "View project", "ca": "Veure el projecte"},
    "mec_pie": {
        "es": "La Cruz de Malta de mi clasificador de colores, dibujada con su geometría real.",
        "en": "The Geneva drive from my colour sorter, drawn from its real geometry.",
        "ca": "La creu de Malta del meu classificador de colors, dibuixada amb la seva geometria real.",
    },
    "cert_t": {"es": "Certificación", "en": "Certification", "ca": "Certificació"},
    "idiomas_t": {"es": "Idiomas", "en": "Languages", "ca": "Idiomes"},
    "idiomas": {"es": "Inglés C1, español y catalán nativos", "en": "English C1, native Spanish and Catalan", "ca": "Anglès C1, castellà i català natius"},
    "contacto_t": {
        "es": "¿Quieres más detalle de algún proyecto?",
        "en": "Want more detail on a project?",
        "ca": "Vols més detall d'algun projecte?",
    },
    "contacto_p": {
        "es": "Escríbeme por LinkedIn.",
        "en": "Message me on LinkedIn.",
        "ca": "Escriu-me per LinkedIn.",
    },
    "esq_brazo": {
        "es": "Esquema: cinco articulaciones en serie, de la base al extremo que coge los objetos.",
        "en": "Diagram: five joints in series, from the base to the end that picks up objects.",
        "ca": "Esquema: cinc articulacions en sèrie, de la base a l'extrem que agafa els objectes.",
    },
    "esq_motor": {
        "es": "Esquema del principio: tres bobinas giran entre dos imanes y el conmutador invierte la corriente para mantener el giro.",
        "en": "Principle diagram: three coils turn between two magnets, and the commutator reverses the current to keep them turning.",
        "ca": "Esquema del principi: tres bobines giren entre dos imants i el commutador inverteix el corrent per mantenir el gir.",
    },
    "menu": {"es": "Menú", "en": "Menu", "ca": "Menú"},
    "video_alt": {"es": "Vídeo del prototipo en funcionamiento", "en": "Video of the prototype running", "ca": "Vídeo del prototip en funcionament"},
    "progreso": {"es": "Progreso de lectura", "en": "Reading progress", "ca": "Progrés de lectura"},
    "disp_t": {"es": "Disponibilidad", "en": "Availability", "ca": "Disponibilitat"},
    "disp": {
        "es": "Prácticas a media jornada desde enero de 2027",
        "en": "Part-time internship from January 2027",
        "ca": "Pràctiques a mitja jornada des de gener de 2027",
    },
    "zona_t": {"es": "Zona", "en": "Location", "ca": "Zona"},
    "zona": {"es": "Barcelona y Baix Llobregat", "en": "Barcelona area, Spain", "ca": "Barcelona i Baix Llobregat"},
    "ver_proy": {"es": "Ver proyectos", "en": "See projects", "ca": "Veure projectes"},
    "descargar_cv": {"es": "Descargar CV", "en": "Download CV", "ca": "Descarregar CV"},
    "proyectos": {"es": "Proyectos", "en": "Projects", "ca": "Projectes"},
    "sobre": {"es": "Sobre mí", "en": "About", "ca": "Sobre mi"},
    "contacto": {"es": "Contacto", "en": "Contact", "ca": "Contacte"},
    "formacion": {"es": "Formación", "en": "Education", "ca": "Formació"},
    "experiencia": {"es": "Experiencia", "en": "Experience", "ca": "Experiència"},
    "certs": {"es": "Certificaciones e idiomas", "en": "Certifications and languages", "ca": "Certificacions i idiomes"},
    "herramientas": {"es": "Herramientas", "en": "Tools", "ca": "Eines"},
    "leer": {"es": "Leer el proyecto", "en": "Read the project", "ca": "Llegir el projecte"},
    "volver": {"es": "Todos los proyectos", "en": "All projects", "ca": "Tots els projectes"},
    "periodo": {"es": "Periodo", "en": "Period", "ca": "Període"},
    "tipo": {"es": "Tipo", "en": "Type", "ca": "Tipus"},
    "papel": {"es": "Mi papel", "en": "My role", "ca": "El meu paper"},
    "estado": {"es": "Estado", "en": "Status", "ca": "Estat"},
    "acabado": {"es": "Terminado", "en": "Completed", "ca": "Acabat"},
    "en_curso": {"es": "En desarrollo", "en": "In progress", "ca": "En desenvolupament"},
    "galeria": {"es": "Imágenes", "en": "Images", "ca": "Imatges"},
    "siguiente": {"es": "Siguiente proyecto", "en": "Next project", "ca": "Següent projecte"},
    "pie": {
        "es": "Se actualiza con cada proyecto nuevo.",
        "en": "Updated with every new project.",
        "ca": "S'actualitza amb cada projecte nou.",
    },
    "contenido": {"es": "Contenido", "en": "Contents", "ca": "Contingut"},
    "saltar": {"es": "Saltar al contenido", "en": "Skip to content", "ca": "Salta al contingut"},
    "ampliar": {"es": "Ampliar imagen", "en": "Enlarge image", "ca": "Amplia la imatge"},
    "cerrar": {"es": "Cerrar", "en": "Close", "ca": "Tanca"},
    "anterior": {"es": "Anterior", "en": "Previous", "ca": "Anterior"},
    "posterior": {"es": "Siguiente", "en": "Next", "ca": "Següent"},
    "pausa": {"es": "Pausar", "en": "Pause", "ca": "Pausa"},
    "reproducir": {"es": "Reproducir", "en": "Play", "ca": "Reprodueix"},
    "gin_gira": {"es": "Girando 90°", "en": "Turning 90°", "ca": "Girant 90°"},
    "gin_bloq": {"es": "Bloqueada: el sensor lee el color", "en": "Locked: the sensor reads the colour", "ca": "Bloquejada: el sensor llegeix el color"},
    "gin_motriz": {"es": "Rueda motriz", "en": "Drive wheel", "ca": "Roda motriu"},
    "gin_cruz": {"es": "Cruz de Malta", "en": "Geneva wheel", "ca": "Creu de Malta"},
    "gin_ciclo": {"es": "Una vuelta del motor: ¼ de giro, ¾ de bloqueo", "en": "One motor turn: ¼ moving, ¾ locked", "ca": "Una volta del motor: ¼ de gir, ¾ de bloqueig"},
    "gin_pie": {
        "es": "El mecanismo, dibujado a partir de su geometría. La rueda motriz gira de forma continua; su pivote entra en una ranura, arrastra la cruz 90° y sale. El resto de la vuelta, el disco de bloqueo impide que la cruz se mueva.",
        "en": "The mechanism, drawn from its geometry. The drive wheel turns continuously; its pin enters a slot, drags the wheel through 90° and leaves. For the rest of the turn, the locking disc keeps the wheel from moving.",
        "ca": "El mecanisme, dibuixat a partir de la seva geometria. La roda motriu gira de manera contínua; el seu pivot entra en una ranura, arrossega la creu 90° i surt. La resta de la volta, el disc de bloqueig impedeix que la creu es mogui.",
    },
    "gin_alt": {"es": "Animación de un mecanismo de Cruz de Malta de cuatro ranuras", "en": "Animation of a four-slot Geneva drive", "ca": "Animació d'un mecanisme de creu de Malta de quatre ranures"},
    "e404_t": {"es": "Página no encontrada", "en": "Page not found", "ca": "Pàgina no trobada"},
    "e404_p": {"es": "Esta página no existe o ha cambiado de sitio.", "en": "This page does not exist or has moved.", "ca": "Aquesta pàgina no existeix o ha canviat de lloc."},
    "inicio": {"es": "Ir al inicio", "en": "Go to home page", "ca": "Vés a l'inici"},
    "otros_idiomas": {"es": "Idioma", "en": "Language", "ca": "Idioma"},
}

from proyectos import PROYECTOS, ORDEN, GANCHOS, DESTACADOS
PROYECTOS.sort(key=lambda p: ORDEN.index(p["slug"]))
