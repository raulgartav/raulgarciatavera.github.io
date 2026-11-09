# -*- coding: utf-8 -*-
# Contenido de la web. Cada texto tiene versión es / en / ca.
# Para añadir fotos: copiar los archivos en img/<slug>/ y listarlos en "galeria".

SITE = {
    "nombre": "Raúl García Tavera",
    "linkedin": "https://www.linkedin.com/in/raulgarciatavera/",
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

SOBRE = {
    "formacion": [
        {
            "t": {"es": "Grado en Ingeniería en Tecnologías Industriales", "en": "BSc in Industrial Technology Engineering", "ca": "Grau en Enginyeria en Tecnologies Industrials"},
            "d": {"es": "ETSEIB, Universitat Politècnica de Catalunya · nota media 7,5/10", "en": "ETSEIB, Universitat Politècnica de Catalunya · GPA 7.5/10", "ca": "ETSEIB, Universitat Politècnica de Catalunya · nota mitjana 7,5/10"},
            "f": "2023 – 2027",
        },
    ],
    "experiencia": [
        {
            "t": {"es": "Becario técnico-comercial (HVAC) · Daikin AC Spain", "en": "Technical Sales Engineer Intern (HVAC) · Daikin AC Spain", "ca": "Becari tècnic-comercial (HVAC) · Daikin AC Spain"},
            "d": {
                "es": "Departamento Comercial, Barcelona. Preparo soluciones técnicas y ofertas de climatización para instaladores y distribuidores, y atiendo dudas técnicas, de stock y de plazos. Formación interna en VRV, splits, aerotermia y normativa. SAP (ERP y CRM), Excel y software interno de Daikin.",
                "en": "Sales Department, Barcelona. I prepare technical solutions and HVAC quotations for installers and distributors, and handle technical, stock and lead-time queries. Internal training on VRV, splits, heat pumps and regulations. SAP (ERP and CRM), Excel and Daikin in-house software.",
                "ca": "Departament Comercial, Barcelona. Preparo solucions tècniques i ofertes de climatització per a instal·ladors i distribuïdors, i atenc dubtes tècnics, d'estoc i de terminis. Formació interna en VRV, splits, aerotèrmia i normativa. SAP (ERP i CRM), Excel i programari intern de Daikin.",
            },
            "f": "09/2026 – 01/2027",
        },
        {
            "t": {"es": "Profesor particular", "en": "Private tutor", "ca": "Professor particular"},
            "d": {
                "es": "Preparación de la Selectividad en materias técnicas (2.º de Bachillerato) y clases de Cálculo, Física y Expresión Gráfica a una estudiante de primero de Ingeniería.",
                "en": "University entrance exam preparation in technical subjects, and Calculus, Physics and Technical Drawing lessons for a first-year engineering student.",
                "ca": "Preparació de la Selectivitat en matèries tècniques (2n de Batxillerat) i classes de Càlcul, Física i Expressió Gràfica a una estudiant de primer d'Enginyeria.",
            },
            "f": "2023 –",
        },
    ],
    "certs": [
        {"t": {"es": "SOLIDWORKS Certified Design Professional (CSWP)", "en": "SOLIDWORKS Certified Design Professional (CSWP)", "ca": "SOLIDWORKS Certified Design Professional (CSWP)"},
         "d": {"es": "Dassault Systèmes", "en": "Dassault Systèmes", "ca": "Dassault Systèmes"}, "f": "07/2025"},
        {"t": {"es": "Cambridge C1 Advanced (192)", "en": "Cambridge C1 Advanced (192)", "ca": "Cambridge C1 Advanced (192)"},
         "d": {"es": "Español y catalán nativos", "en": "Native Spanish and Catalan", "ca": "Castellà i català natius"}, "f": "09/2026"},
    ],
    "herramientas": [
        ("CAD", ["SOLIDWORKS (CSWP)"]),
        ({"es": "Simulación", "en": "Simulation", "ca": "Simulació"}, ["ANSYS APDL", "SOLIDWORKS Simulation", "FEM"]),
        ({"es": "Programación", "en": "Programming", "ca": "Programació"}, ["Python", "C++", "Arduino"]),
        ({"es": "Control", "en": "Control", "ca": "Control"}, ["MATLAB", "Simulink"]),
        ({"es": "Fabricación", "en": "Manufacturing", "ca": "Fabricació"}, [{"es": "Impresión 3D (FDM)", "en": "3D printing (FDM)", "ca": "Impressió 3D (FDM)"}]),
        ({"es": "Gestión", "en": "Business", "ca": "Gestió"}, ["SAP ERP / CRM", "Excel"]),
    ],
}

from proyectos import PROYECTOS, ORDEN
PROYECTOS.sort(key=lambda p: ORDEN.index(p["slug"]))
