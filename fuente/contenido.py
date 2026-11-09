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
        ({"es": "Simulación", "en": "Simulation", "ca": "Simulació"}, ["ANSYS APDL", "FEM"]),
        ({"es": "Programación", "en": "Programming", "ca": "Programació"}, ["Python", "C++", "Arduino"]),
        ({"es": "Control", "en": "Control", "ca": "Control"}, ["MATLAB", "Simulink"]),
        ({"es": "Fabricación", "en": "Manufacturing", "ca": "Fabricació"}, [{"es": "Impresión 3D (FDM)", "en": "3D printing (FDM)", "ca": "Impressió 3D (FDM)"}]),
        ({"es": "Gestión", "en": "Business", "ca": "Gestió"}, ["SAP ERP / CRM", "Excel"]),
    ],
}

# Orden = orden en la web
PROYECTOS = [
    {
        "slug": "brazo-robotico",
        "num": "01",
        "estado": "en_curso",
        "periodo": {"es": "2026 – en curso", "en": "2026 – ongoing", "ca": "2026 – en curs"},
        "tipo": {"es": "Proyecto personal", "en": "Personal project", "ca": "Projecte personal"},
        "papel": {"es": "Todo el proyecto", "en": "Whole project", "ca": "Tot el projecte"},
        "titulo": {"es": "Brazo robótico de 5 grados de libertad", "en": "5-DOF robotic arm", "ca": "Braç robòtic de 5 graus de llibertat"},
        "resumen": {
            "es": "Brazo robótico de bajo coste que estoy construyendo en casa con piezas impresas en 3D, servos de modelismo y un Arduino UNO. El primer objetivo es que coja objetos y los deje en unas coordenadas indicadas.",
            "en": "A low-cost robotic arm I am building at home with 3D-printed parts, hobby servos and an Arduino UNO. The first goal is for it to pick up objects and place them at given coordinates.",
            "ca": "Braç robòtic de baix cost que estic construint a casa amb peces impreses en 3D, servos de modelisme i un Arduino UNO. El primer objectiu és que agafi objectes i els deixi en unes coordenades indicades.",
        },
        "etiquetas": ["Arduino", {"es": "Impresión 3D", "en": "3D printing", "ca": "Impressió 3D"}, {"es": "Servos", "en": "Servos", "ca": "Servos"}, {"es": "Cinemática", "en": "Kinematics", "ca": "Cinemàtica"}],
        "secciones": [
            {"h": {"es": "Objetivo", "en": "Goal", "ca": "Objectiu"},
             "p": {"es": "Construir un brazo de cinco grados de libertad que, a partir de una posición en coordenadas, mueva cada articulación para coger un objeto y dejarlo en otro punto. He elegido un camino de bajo coste para poder iterar rápido: si funciona bien, mejoraré los componentes.",
                   "en": "Build a five-degree-of-freedom arm that, given a target position in coordinates, moves each joint to pick up an object and place it somewhere else. I chose a low-cost route so I can iterate quickly; if it works well, I will upgrade the components.",
                   "ca": "Construir un braç de cinc graus de llibertat que, a partir d'una posició en coordenades, mogui cada articulació per agafar un objecte i deixar-lo en un altre punt. He triat un camí de baix cost per poder iterar ràpid: si funciona bé, milloraré els components."}},
            {"h": {"es": "Cómo está hecho", "en": "How it is built", "ca": "Com està fet"},
             "l": {"es": ["Estructura de piezas impresas en 3D con una Bambu Lab A1.", "Cinco articulaciones movidas por servos de modelismo.", "Control con un Arduino UNO."],
                   "en": ["Structure made of parts 3D-printed on a Bambu Lab A1.", "Five joints driven by hobby servos.", "Controlled by an Arduino UNO."],
                   "ca": ["Estructura de peces impreses en 3D amb una Bambu Lab A1.", "Cinc articulacions mogudes per servos de modelisme.", "Control amb un Arduino UNO."]}},
            {"h": {"es": "Próximos pasos", "en": "Next steps", "ca": "Propers passos"},
             "p": {"es": "Cuando el brazo coloque objetos de forma fiable, quiero añadirle visión artificial para que localice los objetos por sí mismo en lugar de recibir sus coordenadas.",
                   "en": "Once the arm places objects reliably, I want to add computer vision so it can locate objects by itself instead of receiving their coordinates.",
                   "ca": "Quan el braç col·loqui objectes de manera fiable, vull afegir-hi visió artificial perquè localitzi els objectes per si mateix en lloc de rebre'n les coordenades."}},
        ],
        "galeria": [],
    },
    {
        "slug": "clasificador-color",
        "num": "02",
        "estado": "acabado",
        "periodo": {"es": "01/2026 – 05/2026", "en": "01/2026 – 05/2026", "ca": "01/2026 – 05/2026"},
        "tipo": {"es": "Proyecto académico en equipo", "en": "Academic team project", "ca": "Projecte acadèmic en equip"},
        "papel": {"es": "Coordinador del equipo", "en": "Team coordinator", "ca": "Coordinador de l'equip"},
        "titulo": {"es": "Clasificador automatizado de piezas por color", "en": "Automated colour-sorting machine", "ca": "Classificador automàtic de peces per color"},
        "resumen": {
            "es": "Máquina que detecta el color de cada pieza con un sensor y la clasifica según ese color. Junta mecánica, electrónica y programación en un mismo sistema. Coordiné al equipo durante todo el proyecto.",
            "en": "A machine that detects the colour of each part with a sensor and sorts it accordingly. It brings mechanics, electronics and programming together in one system. I coordinated the team throughout the project.",
            "ca": "Màquina que detecta el color de cada peça amb un sensor i la classifica segons aquest color. Ajunta mecànica, electrònica i programació en un mateix sistema. Vaig coordinar l'equip durant tot el projecte.",
        },
        "etiquetas": ["Arduino (C++)", "SOLIDWORKS", {"es": "Impresión 3D", "en": "3D printing", "ca": "Impressió 3D"}, {"es": "Motores paso a paso", "en": "Stepper motors", "ca": "Motors pas a pas"}],
        "secciones": [
            {"h": {"es": "El reto", "en": "The challenge", "ca": "El repte"},
             "p": {"es": "Diseñar y construir un sistema automático que reconozca piezas de distintos colores y las separe sin intervención manual, integrando sensores, actuadores y mecanismos propios.",
                   "en": "Design and build an automatic system that recognises parts of different colours and separates them without manual intervention, integrating sensors, actuators and custom mechanisms.",
                   "ca": "Dissenyar i construir un sistema automàtic que reconegui peces de diferents colors i les separi sense intervenció manual, integrant sensors, actuadors i mecanismes propis."}},
            {"h": {"es": "Qué hicimos", "en": "What we did", "ca": "Què vam fer"},
             "l": {"es": ["Lectura del color de cada pieza con sensores de color.", "Programa de control en Arduino, escrito en C++.", "Accionamiento con motores paso a paso y de corriente continua.", "Mecanismos diseñados en SOLIDWORKS y fabricados con impresión 3D."],
                   "en": ["Colour reading of each part with colour sensors.", "Control program on Arduino, written in C++.", "Actuation with stepper and DC motors.", "Mechanisms designed in SOLIDWORKS and 3D-printed."],
                   "ca": ["Lectura del color de cada peça amb sensors de color.", "Programa de control en Arduino, escrit en C++.", "Accionament amb motors pas a pas i de corrent continu.", "Mecanismes dissenyats en SOLIDWORKS i fabricats amb impressió 3D."]}},
            {"h": {"es": "Mi papel", "en": "My role", "ca": "El meu paper"},
             "p": {"es": "Coordiné al equipo: organicé el trabajo entre los miembros y me encargué de que la parte mecánica, la electrónica y el programa encajaran en una sola máquina.",
                   "en": "I coordinated the team: I organised the work among the members and made sure the mechanical design, the electronics and the program came together as one machine.",
                   "ca": "Vaig coordinar l'equip: vaig organitzar la feina entre els membres i em vaig encarregar que la part mecànica, l'electrònica i el programa encaixessin en una sola màquina."}},
        ],
        "galeria": [],
    },
    {
        "slug": "motor-dc",
        "num": "03",
        "estado": "acabado",
        "periodo": {"es": "2026", "en": "2026", "ca": "2026"},
        "tipo": {"es": "Parte práctica de un trabajo universitario", "en": "Practical part of a university assignment", "ca": "Part pràctica d'un treball universitari"},
        "papel": {"es": "Diseño, fabricación y pruebas", "en": "Design, manufacturing and testing", "ca": "Disseny, fabricació i proves"},
        "titulo": {"es": "Motor de corriente continua casero", "en": "Home-built DC motor", "ca": "Motor de corrent continu casolà"},
        "resumen": {
            "es": "Motor de corriente continua construido desde cero con dos imanes de neodimio, tres bobinas y un conmutador, con piezas diseñadas en SOLIDWORKS e impresas en 3D. Es la parte práctica de un trabajo sobre motores eléctricos.",
            "en": "A DC motor built from scratch with two neodymium magnets, three coils and a commutator, with parts designed in SOLIDWORKS and 3D-printed. It is the practical part of an assignment on electric motors.",
            "ca": "Motor de corrent continu construït des de zero amb dos imants de neodimi, tres bobines i un commutador, amb peces dissenyades en SOLIDWORKS i impreses en 3D. És la part pràctica d'un treball sobre motors elèctrics.",
        },
        "etiquetas": ["SOLIDWORKS", {"es": "Impresión 3D", "en": "3D printing", "ca": "Impressió 3D"}, {"es": "Electromagnetismo", "en": "Electromagnetism", "ca": "Electromagnetisme"}],
        "secciones": [
            {"h": {"es": "Contexto", "en": "Context", "ca": "Context"},
             "p": {"es": "El motor acompaña un trabajo universitario sobre motores eléctricos que parte de las ecuaciones de Maxwell. Quería comprobar en una máquina real lo que el trabajo explica sobre el papel.",
                   "en": "The motor accompanies a university assignment on electric motors that starts from Maxwell's equations. I wanted to check on a real machine what the assignment explains on paper.",
                   "ca": "El motor acompanya un treball universitari sobre motors elèctrics que parteix de les equacions de Maxwell. Volia comprovar en una màquina real el que el treball explica sobre el paper."}},
            {"h": {"es": "Cómo está hecho", "en": "How it is built", "ca": "Com està fet"},
             "l": {"es": ["Dos imanes de neodimio que crean el campo magnético.", "Tres bobinas situadas entre los imanes.", "Conmutador que invierte la corriente para mantener el giro.", "Soportes y piezas diseñados en SOLIDWORKS e impresos en 3D."],
                   "en": ["Two neodymium magnets that create the magnetic field.", "Three coils placed between the magnets.", "A commutator that reverses the current to keep it turning.", "Supports and parts designed in SOLIDWORKS and 3D-printed."],
                   "ca": ["Dos imants de neodimi que creen el camp magnètic.", "Tres bobines situades entre els imants.", "Commutador que inverteix el corrent per mantenir el gir.", "Suports i peces dissenyats en SOLIDWORKS i impresos en 3D."]}},
            {"h": {"es": "Proceso", "en": "Process", "ca": "Procés"},
             "p": {"es": "Primero probé el principio con una sola bobina y, una vez funcionaba, monté las tres y el conmutador hasta tener el motor completo girando.",
                   "en": "I first tested the principle with a single coil and, once it worked, assembled all three coils and the commutator until the complete motor was running.",
                   "ca": "Primer vaig provar el principi amb una sola bobina i, un cop funcionava, vaig muntar les tres bobines i el commutador fins a tenir el motor complet girant."}},
        ],
        "galeria": [],
    },
    {
        "slug": "abrelatas-fem",
        "num": "04",
        "estado": "acabado",
        "periodo": {"es": "09/2025 – 11/2025", "en": "09/2025 – 11/2025", "ca": "09/2025 – 11/2025"},
        "tipo": {"es": "Proyecto académico", "en": "Academic project", "ca": "Projecte acadèmic"},
        "papel": {"es": "Diseño, simulación y validación", "en": "Design, simulation and validation", "ca": "Disseny, simulació i validació"},
        "titulo": {"es": "Optimización estructural de un abrelatas", "en": "Structural optimisation of a can opener", "ca": "Optimització estructural d'un obrellaunes"},
        "resumen": {
            "es": "Análisis por elementos finitos de un abrelatas para mejorar su comportamiento estructural: modelo en ANSYS APDL, optimización del diseño y comprobación con ensayos reales.",
            "en": "Finite element analysis of a can opener to improve its structural behaviour: an ANSYS APDL model, design optimisation and verification with real tests.",
            "ca": "Anàlisi per elements finits d'un obrellaunes per millorar-ne el comportament estructural: model en ANSYS APDL, optimització del disseny i comprovació amb assajos reals.",
        },
        "etiquetas": ["ANSYS APDL", "FEM", {"es": "Optimización", "en": "Optimisation", "ca": "Optimització"}, {"es": "Ensayos", "en": "Testing", "ca": "Assajos"}],
        "secciones": [
            {"h": {"es": "Objetivo", "en": "Goal", "ca": "Objectiu"},
             "p": {"es": "Estudiar cómo trabaja la estructura de un abrelatas al usarlo y mejorar su diseño a partir de la simulación.",
                   "en": "Study how the structure of a can opener behaves in use and improve its design based on simulation.",
                   "ca": "Estudiar com treballa l'estructura d'un obrellaunes quan s'utilitza i millorar-ne el disseny a partir de la simulació."}},
            {"h": {"es": "Qué hice", "en": "What I did", "ca": "Què vaig fer"},
             "l": {"es": ["Modelo de elementos finitos de la pieza en ANSYS APDL.", "Optimización de la geometría a partir de los resultados.", "Validación experimental del diseño.", "Documentación técnica del proceso y los resultados."],
                   "en": ["Finite element model of the part in ANSYS APDL.", "Geometry optimisation based on the results.", "Experimental validation of the design.", "Technical documentation of the process and results."],
                   "ca": ["Model d'elements finits de la peça en ANSYS APDL.", "Optimització de la geometria a partir dels resultats.", "Validació experimental del disseny.", "Documentació tècnica del procés i els resultats."]}},
        ],
        "galeria": [],
    },
]

# Orden en la web (de más a menos relevante)
ORDEN = ["clasificador-color", "brazo-robotico", "abrelatas-fem", "motor-dc"]
PROYECTOS.sort(key=lambda p: ORDEN.index(p["slug"]))
