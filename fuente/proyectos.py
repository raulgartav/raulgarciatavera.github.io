# -*- coding: utf-8 -*-
# Proyectos de la web. Cada texto en es / en / ca.
# galeria: imágenes {"img": ruta, "pie": {...}} o vídeos {"video": ruta, "img": póster, "pie": {...}}
# cifras: datos clave {"v": valor, "l": {...}}

I3D = {"es": "Impresión 3D", "en": "3D printing", "ca": "Impressió 3D"}

ORDEN = ["clasificador-color", "abridor-fem", "viga-impresa", "brazo-robotico", "motor-dc"]

PROYECTOS = [
# ───────────────────────────── Clasificador
{
    "slug": "clasificador-color",
    "estado": "acabado",
    "portada": "img/clasificador-color/maquina-funcionando.jpg",
    "periodo": {"es": "01/2026 – 05/2026", "en": "01/2026 – 05/2026", "ca": "01/2026 – 05/2026"},
    "tipo": {"es": "Proyecto II · ETSEIB · equipo de 4", "en": "Project II · ETSEIB · team of 4", "ca": "Projecte II · ETSEIB · equip de 4"},
    "papel": {"es": "Coordinador del equipo", "en": "Team coordinator", "ca": "Coordinador de l'equip"},
    "titulo": {"es": "Clasificador automático por colores con Cruz de Malta", "en": "Automatic colour sorter with a Geneva drive", "ca": "Classificador automàtic per colors amb creu de Malta"},
    "resumen": {
        "es": "Máquina que clasifica piezas por colores. Una cinta las lleva a una plataforma que gira a pasos exactos de 90° gracias a una Cruz de Malta. En cada parada, un sensor lee el color y tres servomotores empujan cada pieza a su caja.",
        "en": "A machine that sorts parts by colour. A conveyor feeds them onto a platform that turns in exact 90° steps thanks to a Geneva drive. At each stop a sensor reads the colour and three servos push each part into its bin.",
        "ca": "Màquina que classifica peces per colors. Una cinta les porta a una plataforma que gira a passos exactes de 90° gràcies a una creu de Malta. A cada parada, un sensor llegeix el color i tres servomotors empenyen cada peça a la seva caixa.",
    },
    "etiquetas": ["SOLIDWORKS", "Arduino (C++)", I3D, {"es": "Mecanismos", "en": "Mechanisms", "ca": "Mecanismes"}],
    "cifras": [
        {"v": "4 × 90°", "l": {"es": "estaciones de la Cruz de Malta", "en": "Geneva drive stations", "ca": "estacions de la creu de Malta"}},
        {"v": "3", "l": {"es": "colores clasificados", "en": "colours sorted", "ca": "colors classificats"}},
        {"v": "0,2 mm", "l": {"es": "holgura pivote–ranura", "en": "pin–slot clearance", "ca": "joc pivot–ranura"}},
        {"v": "5", "l": {"es": "motores coordinados", "en": "coordinated motors", "ca": "motors coordinats"}},
    ],
    "secciones": [
        {"h": {"es": "El reto", "en": "The challenge", "ca": "El repte"},
         "p": {"es": "Coordinar una alimentación continua (la cinta) con una lectura de color que necesita la pieza quieta y con una clasificación física posterior. La solución fue un mecanismo clásico: la Cruz de Malta convierte el giro continuo del motor en avances intermitentes de 90°, y durante cada pausa la plataforma queda bloqueada mecánicamente.",
               "en": "Coordinating a continuous feed (the conveyor) with a colour reading that needs the part to stand still, followed by physical sorting. The answer was a classic mechanism: a Geneva drive turns the motor's continuous rotation into intermittent 90° steps, and during each pause the platform is mechanically locked.",
               "ca": "Coordinar una alimentació contínua (la cinta) amb una lectura de color que necessita la peça quieta i amb una classificació física posterior. La solució va ser un mecanisme clàssic: la creu de Malta converteix el gir continu del motor en avanços intermitents de 90°, i durant cada pausa la plataforma queda bloquejada mecànicament."}},
        {"h": {"es": "Cómo funciona", "en": "How it works", "ca": "Com funciona"},
         "l": {"es": ["Una cinta transportadora, con un motor de corriente continua con reductora y piezas LEGO, deja cada pieza en la estación de lectura.",
                      "El sensor TCS3200 lee el color dentro de una carcasa opaca que lo aísla de la luz ambiente.",
                      "Un motor paso a paso (driver A3967) mueve la rueda motriz. Cada vuelta hace girar la plataforma 90°, y durante los 270° restantes la mantiene bloqueada.",
                      "El Arduino guarda el color de la pieza que hay en cada estación y activa el servo HS-422 de la estación que le corresponde.",
                      "Una pantalla LCD muestra el color detectado y el recuento por colores. Hay un pulsador de marcha/paro y una parada de emergencia."],
               "en": ["A conveyor driven by a geared DC motor, with LEGO parts, drops each part at the reading station.",
                      "A TCS3200 sensor reads the colour inside an opaque housing that shields it from ambient light.",
                      "A stepper motor (A3967 driver) turns the drive wheel. Each turn rotates the platform 90° and keeps it locked for the remaining 270°.",
                      "The Arduino tracks the colour of the part at each station and fires the HS-422 servo at the matching one.",
                      "An LCD shows the detected colour and a count per colour. There is a start/stop button and an emergency stop."],
               "ca": ["Una cinta transportadora, amb un motor de corrent continu amb reductora i peces LEGO, deixa cada peça a l'estació de lectura.",
                      "El sensor TCS3200 llegeix el color dins d'una carcassa opaca que l'aïlla de la llum ambient.",
                      "Un motor pas a pas (driver A3967) mou la roda motriu. Cada volta fa girar la plataforma 90°, i durant els 270° restants la manté bloquejada.",
                      "L'Arduino desa el color de la peça que hi ha a cada estació i activa el servo HS-422 de l'estació que li correspon.",
                      "Una pantalla LCD mostra el color detectat i el recompte per colors. Hi ha un polsador de marxa/paro i una parada d'emergència."]}},
        {"h": {"es": "Diseño y fabricación", "en": "Design and manufacturing", "ca": "Disseny i fabricació"},
         "p": {"es": "Todas las piezas propias se modelaron de forma paramétrica en SOLIDWORKS con criterios de diseño para fabricación y se imprimieron en PLA. Entre el pivote y las ranuras de la cruz se dejó una holgura de 0,2 mm para que el encaje fuera suave. Antes de imprimir, comprobamos el ensamblaje con detección de interferencias y un estudio de movimiento, para que los brazos de los servos no chocaran con el soporte del sensor.",
               "en": "All custom parts were modelled parametrically in SOLIDWORKS following design-for-manufacturing criteria and printed in PLA. A 0.2 mm clearance between the pin and the Geneva slots gives a smooth engagement. Before printing, we checked the assembly with interference detection and a motion study so the servo arms would not hit the sensor mount.",
               "ca": "Totes les peces pròpies es van modelar de manera paramètrica en SOLIDWORKS amb criteris de disseny per a fabricació i es van imprimir en PLA. Entre el pivot i les ranures de la creu es va deixar un joc de 0,2 mm perquè l'encaix fos suau. Abans d'imprimir, vam comprovar el muntatge amb detecció d'interferències i un estudi de moviment, perquè els braços dels servos no xoquessin amb el suport del sensor."}},
        {"h": {"es": "Control", "en": "Control", "ca": "Control"},
         "p": {"es": "El programa en C++ sincroniza tres cosas: la lectura del sensor, el giro de la plataforma y el disparo de los servos. Para que ninguna tarea bloquee a las demás, el avance del motor paso a paso se temporiza con millis() en lugar de pausas fijas. Antes de cada uso se calibra el sensor con piezas de referencia de cada color.",
               "en": "The C++ program synchronises three things: the sensor reading, the platform rotation and the servo actuation. To keep any task from blocking the others, the stepper is timed with millis() instead of fixed delays. The sensor is calibrated with reference parts of each colour before use.",
               "ca": "El programa en C++ sincronitza tres coses: la lectura del sensor, el gir de la plataforma i l'accionament dels servos. Perquè cap tasca bloquegi les altres, l'avanç del motor pas a pas es temporitza amb millis() en lloc de pauses fixes. Abans de cada ús es calibra el sensor amb peces de referència de cada color."}},
        {"h": {"es": "Mi papel", "en": "My role", "ca": "El meu paper"},
         "p": {"es": "Coordiné al equipo de cuatro personas durante todo el proyecto, desde la propuesta hasta el prototipo final y el póster.",
               "en": "I coordinated the four-person team throughout the project, from the proposal to the final prototype and poster.",
               "ca": "Vaig coordinar l'equip de quatre persones durant tot el projecte, des de la proposta fins al prototip final i el pòster."}},
    ],
    "galeria": [
        {"video": "img/clasificador-color/funcionamiento.mp4", "img": "img/clasificador-color/maquina-funcionando.jpg",
         "pie": {"es": "El prototipo clasificando piezas en el laboratorio.", "en": "The prototype sorting parts in the lab.", "ca": "El prototip classificant peces al laboratori."}},
        {"img": "img/clasificador-color/ensamblaje-cad.jpg",
         "pie": {"es": "Ensamblaje general en SOLIDWORKS: cinta, Cruz de Malta, plataforma, servos y cajas.", "en": "Full SOLIDWORKS assembly: conveyor, Geneva drive, platform, servos and bins.", "ca": "Muntatge general en SOLIDWORKS: cinta, creu de Malta, plataforma, servos i caixes."}},
        {"video": "img/clasificador-color/simulacion-solidworks.mp4", "img": "img/clasificador-color/simulacion-solidworks.jpg",
         "pie": {"es": "Estudio de movimiento en SOLIDWORKS para comprobar la sincronización.", "en": "SOLIDWORKS motion study used to check the timing.", "ca": "Estudi de moviment en SOLIDWORKS per comprovar la sincronització."}},
        {"img": "img/clasificador-color/pantalla-lcd.jpg",
         "pie": {"es": "La pantalla muestra el estado y el recuento por colores.", "en": "The display shows the status and the count per colour.", "ca": "La pantalla mostra l'estat i el recompte per colors."}},
        {"img": "img/clasificador-color/diagrama-flujo.jpg", "ancho": True,
         "pie": {"es": "Diagrama de flujo del programa de control.", "en": "Flowchart of the control program.", "ca": "Diagrama de flux del programa de control."}},
    ],
},
# ───────────────────────────── Abridor
{
    "slug": "abridor-fem",
    "estado": "acabado",
    "portada": "img/abridor-fem/abridor-botella.jpg",
    "periodo": {"es": "Otoño 2025", "en": "Autumn 2025", "ca": "Tardor 2025"},
    "tipo": {"es": "Mecánica de Medios Continuos · equipo de 3", "en": "Continuum Mechanics · team of 3", "ca": "Mecànica dels Medis Continus · equip de 3"},
    "papel": {"es": "Diseño, simulación y ensayos", "en": "Design, simulation and testing", "ca": "Disseny, simulació i assaigs"},
    "titulo": {"es": "Abridor de botellas optimizado con elementos finitos", "en": "Bottle opener optimised with finite elements", "ca": "Obridor d'ampolles optimitzat amb elements finits"},
    "resumen": {
        "es": "Diseño, simulación, fabricación y ensayo de un abridor de chapas de metacrilato. El objetivo era maximizar la relación entre la carga de rotura y el peso, con un coeficiente de seguridad de entre 1,5 y 2. Pasamos por cuatro versiones y dos ensayos a rotura.",
        "en": "Design, simulation, manufacture and testing of an acrylic bottle-cap opener. The goal was to maximise the ratio between failure load and weight, with a safety factor between 1.5 and 2. It went through four versions and two destructive tests.",
        "ca": "Disseny, simulació, fabricació i assaig d'un obridor de taps de metacrilat. L'objectiu era maximitzar la relació entre la càrrega de trencament i el pes, amb un coeficient de seguretat d'entre 1,5 i 2. Vam passar per quatre versions i dos assaigs a trencament.",
    },
    "etiquetas": ["ANSYS APDL", "FEM", "SOLIDWORKS", {"es": "Ensayos", "en": "Testing", "ca": "Assaigs"}],
    "cifras": [
        {"v": "21,5 → 10,0 g", "l": {"es": "masa, del primer diseño al final", "en": "mass, first to final design", "ca": "massa, del primer disseny al final"}},
        {"v": "91 N", "l": {"es": "rotura prevista por el modelo", "en": "failure load predicted by FEM", "ca": "trencament previst pel model"}},
        {"v": "177 N", "l": {"es": "rotura real en el ensayo", "en": "measured failure load", "ca": "trencament real a l'assaig"}},
        {"v": "33,8 €", "l": {"es": "coste de 7 prototipos", "en": "cost of 7 prototypes", "ca": "cost de 7 prototips"}},
    ],
    "secciones": [
        {"h": {"es": "Requisitos", "en": "Requirements", "ca": "Requisits"},
         "p": {"es": "El abridor tenía que permitir abrir una botella con comodidad, romperse con la mano en un ensayo destructivo controlado, tener un brazo de menos de 150 mm y un coeficiente de seguridad de entre 1,5 y 2. La fuerza nominal la estimamos a partir de datos de fuerza de agarre de la población, tomando el percentil 5 para que casi cualquier persona pudiera usarlo. La eficiencia a maximizar era la carga última dividida por el peso.",
               "en": "The opener had to open a bottle comfortably, break by hand in a controlled destructive test, have a lever arm under 150 mm and a safety factor between 1.5 and 2. We estimated the nominal force from population grip-strength data, using the 5th percentile so almost anyone could use it. The efficiency to maximise was ultimate load divided by weight.",
               "ca": "L'obridor havia de permetre obrir una ampolla còmodament, trencar-se amb la mà en un assaig destructiu controlat, tenir un braç de menys de 150 mm i un coeficient de seguretat d'entre 1,5 i 2. La força nominal la vam estimar a partir de dades de força de presa de la població, prenent el percentil 5 perquè gairebé qualsevol persona el pogués fer servir. L'eficiència a maximitzar era la càrrega última dividida pel pes."}},
        {"h": {"es": "Material", "en": "Material", "ca": "Material"},
         "p": {"es": "Primero estudiamos el aluminio, pero con fuerza manual no se podía llegar a su límite elástico y costaba unas cinco veces más. Elegimos metacrilato (PMMA, E = 3.000 MPa, límite elástico de 70 MPa), cortado por láser en Servei Estació, en Barcelona.",
               "en": "We first studied aluminium, but its yield point could not be reached by hand and it cost about five times more. We chose acrylic (PMMA, E = 3,000 MPa, 70 MPa yield strength), laser-cut at Servei Estació in Barcelona.",
               "ca": "Primer vam estudiar l'alumini, però amb força manual no es podia arribar al seu límit elàstic i costava unes cinc vegades més. Vam triar metacrilat (PMMA, E = 3.000 MPa, límit elàstic de 70 MPa), tallat per làser a Servei Estació, a Barcelona."}},
        {"h": {"es": "Modelo de elementos finitos", "en": "Finite element model", "ca": "Model d'elements finits"},
         "p": {"es": "El modelo se hizo en ANSYS APDL con elementos sólidos cuadráticos (SOLID183) y material elástico, lineal e isótropo. Refinamos la malla en los puntos con concentración de tensiones. Para cada versión comprobamos la tracción y la compresión principales, calculamos el coeficiente de seguridad y, a partir de él, la carga última.",
               "en": "The model was built in ANSYS APDL with quadratic solid elements (SOLID183) and a linear elastic isotropic material, with mesh refinement at stress concentrations. For each version we checked principal tension and compression, computed the safety factor and, from it, the ultimate load.",
               "ca": "El model es va fer en ANSYS APDL amb elements sòlids quadràtics (SOLID183) i material elàstic, lineal i isòtrop. Vam refinar la malla als punts amb concentració de tensions. Per a cada versió vam comprovar la tracció i la compressió principals, vam calcular el coeficient de seguretat i, a partir d'ell, la càrrega última."}},
        {"h": {"es": "Optimización en cuatro versiones", "en": "Four design iterations", "ca": "Optimització en quatre versions"},
         "l": {"es": ["Diseño inicial macizo: 21,5 g, con tensiones muy por debajo del límite. Sobraba material.",
                      "Versión 1: dos vaciados interiores siguiendo el contorno, 15,5 g.",
                      "Versión 2: un tercer vaciado, 14,5 g. La ensayamos y rompió a 82 N por compresión, justo donde el modelo marcaba la tensión máxima. Con ese dato fijamos el límite real a compresión del material en 92,5 MPa.",
                      "Versión final: brazo de 63 mm y espesor de 8 mm, 10,0 g. Coeficiente de seguridad de 1,53, carga última prevista de 91 N y eficiencia teórica de 922."],
               "en": ["Solid initial design: 21.5 g, with stresses well below the limit. There was material to spare.",
                      "Version 1: two internal cut-outs following the outline, 15.5 g.",
                      "Version 2: a third cut-out, 14.5 g. We tested it and it broke at 82 N in compression, exactly where the model showed peak stress. That gave us the real compressive limit of the material: 92.5 MPa.",
                      "Final version: 63 mm lever arm and 8 mm thickness, 10.0 g. Safety factor 1.53, predicted ultimate load 91 N and theoretical efficiency of 922."],
               "ca": ["Disseny inicial massís: 21,5 g, amb tensions molt per sota del límit. Sobrava material.",
                      "Versió 1: dos buidats interiors seguint el contorn, 15,5 g.",
                      "Versió 2: un tercer buidat, 14,5 g. La vam assajar i es va trencar a 82 N per compressió, just on el model marcava la tensió màxima. Amb aquesta dada vam fixar el límit real a compressió del material en 92,5 MPa.",
                      "Versió final: braç de 63 mm i gruix de 8 mm, 10,0 g. Coeficient de seguretat d'1,53, càrrega última prevista de 91 N i eficiència teòrica de 922."]}},
        {"h": {"es": "Ensayo final y lo que aprendí", "en": "Final test and what I learned", "ca": "Assaig final i què en vaig aprendre"},
         "p": {"es": "En el ensayo destructivo, la versión final aguantó 177 N, casi el doble de lo previsto, con un comportamiento elástico y frágil hasta la rotura. El modelo lineal resultó conservador por tres motivos: predice el fallo con la tensión pico de un solo nodo, no recoge la redistribución local de tensiones del PMMA y el punto de contacto real era distinto del simulado. El coeficiente de seguridad real fue de 3,3, fuera del rango pedido. La lección es que un modelo de elementos finitos hay que contrastarlo con ensayos y ajustar bien las condiciones de contorno.",
               "en": "In the destructive test the final version held 177 N, almost twice the prediction, behaving elastically and brittle up to failure. The linear model proved conservative for three reasons: it predicts failure from a single-node peak stress, it ignores local stress redistribution in PMMA, and the real contact point differed from the simulated one. The real safety factor was 3.3, outside the required range. The lesson is that a finite element model has to be checked against tests and its boundary conditions tuned carefully.",
               "ca": "A l'assaig destructiu, la versió final va aguantar 177 N, gairebé el doble del previst, amb un comportament elàstic i fràgil fins al trencament. El model lineal va resultar conservador per tres motius: prediu la fallada amb la tensió pic d'un sol node, no recull la redistribució local de tensions del PMMA i el punt de contacte real era diferent del simulat. El coeficient de seguretat real va ser de 3,3, fora del rang demanat. La lliçó és que un model d'elements finits s'ha de contrastar amb assaigs i ajustar bé les condicions de contorn."}},
    ],
    "galeria": [
        {"img": "img/abridor-fem/diseno-final.jpg", "pie": {"es": "Versión final: brazo más corto, 10,0 g.", "en": "Final version: shorter arm, 10.0 g.", "ca": "Versió final: braç més curt, 10,0 g."}},
        {"img": "img/abridor-fem/fem-traccion.jpg", "pie": {"es": "Tensiones principales de tracción del diseño final en ANSYS.", "en": "Principal tensile stresses of the final design in ANSYS.", "ca": "Tensions principals de tracció del disseny final en ANSYS."}},
        {"img": "img/abridor-fem/fem-compresion-detalle.jpg", "pie": {"es": "Detalle de la zona crítica a compresión, con la malla refinada.", "en": "Close-up of the critical compression zone with refined mesh.", "ca": "Detall de la zona crítica a compressió, amb la malla refinada."}},
        {"img": "img/abridor-fem/optimizacion-1.jpg", "pie": {"es": "Versión 1: dos vaciados, 15,5 g.", "en": "Version 1: two cut-outs, 15.5 g.", "ca": "Versió 1: dos buidats, 15,5 g."}},
        {"img": "img/abridor-fem/optimizacion-2.jpg", "pie": {"es": "Versión 2: tres vaciados, 14,5 g.", "en": "Version 2: three cut-outs, 14.5 g.", "ca": "Versió 2: tres buidats, 14,5 g."}},
        {"img": "img/abridor-fem/ensayo-82N.jpg", "pie": {"es": "Ensayo de la versión 2: rotura a 82 N.", "en": "Test of version 2: failure at 82 N.", "ca": "Assaig de la versió 2: trencament a 82 N."}},
        {"img": "img/abridor-fem/ensayo-fuerza-desplazamiento.jpg", "pie": {"es": "Curva fuerza–desplazamiento del ensayo final: lineal hasta romper a 177 N.", "en": "Force–displacement curve of the final test: linear up to failure at 177 N.", "ca": "Corba força–desplaçament de l'assaig final: lineal fins a trencar a 177 N."}},
        {"img": "img/abridor-fem/plano.jpg", "pie": {"es": "Plano acotado del diseño definitivo.", "en": "Dimensioned drawing of the final design.", "ca": "Plànol acotat del disseny definitiu."}},
        {"img": "img/abridor-fem/diseno-inicial.jpg", "pie": {"es": "Diseño inicial macizo con sus cotas principales.", "en": "Solid initial design with its main dimensions.", "ca": "Disseny inicial massís amb les cotes principals."}},
    ],
},
# ───────────────────────────── Viga
{
    "slug": "viga-impresa",
    "estado": "acabado",
    "portada": "img/viga-impresa/viga-final.jpg",
    "periodo": {"es": "02/2026 – 05/2026", "en": "02/2026 – 05/2026", "ca": "02/2026 – 05/2026"},
    "tipo": {"es": "Resistencia de Materiales · equipo de 3", "en": "Strength of Materials · team of 3", "ca": "Resistència de Materials · equip de 3"},
    "papel": {"es": "Cálculo, diseño e impresión", "en": "Calculation, design and printing", "ca": "Càlcul, disseny i impressió"},
    "titulo": {"es": "Viga de PLA impresa en 3D", "en": "3D-printed PLA beam", "ca": "Biga de PLA impresa en 3D"},
    "resumen": {
        "es": "Diseño, cálculo, fabricación y ensayo de un elemento resistente que salva dos obstáculos y soporta 250 N entre apoyos separados 500 mm. La flecha tenía que ser como máximo de 15 mm y el coeficiente de seguridad de entre 1,5 y 2,5. Lo resolvimos con una sección en doble T impresa en PLA.",
        "en": "Design, calculation, manufacture and testing of a load-bearing element that clears two obstacles and carries 250 N between supports 500 mm apart. Deflection had to stay at or below 15 mm and the safety factor between 1.5 and 2.5. We solved it with a 3D-printed PLA I-section.",
        "ca": "Disseny, càlcul, fabricació i assaig d'un element resistent que salva dos obstacles i suporta 250 N entre suports separats 500 mm. La fletxa havia de ser com a màxim de 15 mm i el coeficient de seguretat d'entre 1,5 i 2,5. Ho vam resoldre amb una secció en doble T impresa en PLA.",
    },
    "etiquetas": [{"es": "Resistencia de materiales", "en": "Strength of materials", "ca": "Resistència de materials"}, "SOLIDWORKS Simulation", I3D, "Castigliano"],
    "cifras": [
        {"v": "250 N", "l": {"es": "carga de servicio", "en": "service load", "ca": "càrrega de servei"}},
        {"v": "13,8 mm", "l": {"es": "flecha calculada (límite 15 mm)", "en": "calculated deflection (15 mm limit)", "ca": "fletxa calculada (límit 15 mm)"}},
        {"v": "2,50", "l": {"es": "coeficiente de seguridad", "en": "safety factor", "ca": "coeficient de seguretat"}},
        {"v": "107 g", "l": {"es": "masa teórica", "en": "theoretical mass", "ca": "massa teòrica"}},
    ],
    "secciones": [
        {"h": {"es": "Geometría", "en": "Geometry", "ca": "Geometria"},
         "p": {"es": "La forma de la viga venía condicionada por dos obstáculos. Iteramos el ángulo del tramo inclinado y la longitud del primer tramo, y elegimos 65° y 185 mm. Es un compromiso entre momento flector bajo, un reparto razonable entre axil y cortante, y uniones fáciles de fabricar.",
               "en": "The shape of the beam was dictated by two obstacles. We iterated the angle of the inclined segment and the length of the first segment, and chose 65° and 185 mm. It balances a low bending moment, a reasonable split between axial and shear force, and joints that are easy to make.",
               "ca": "La forma de la biga venia condicionada per dos obstacles. Vam iterar l'angle del tram inclinat i la longitud del primer tram, i vam triar 65° i 185 mm. És un compromís entre moment flector baix, un repartiment raonable entre axial i tallant, i unions fàcils de fabricar."}},
        {"h": {"es": "Material y sección", "en": "Material and cross-section", "ca": "Material i secció"},
         "p": {"es": "Con diagramas de Ashby elegimos PLA (E = 2.800 MPa, límite de 60 MPa) impreso al 100 % de relleno: es barato, accesible y permite una geometría a medida. Elegimos una sección en doble T porque es simétrica y aprovecha igual las alas a tracción y a compresión. La dimensionamos iterando con la ley de Navier, el criterio de Rankine y el teorema de Castigliano, buscando la mínima masa que cumpliera todo. El resultado fue una sección de 18 × 30 mm con paredes de 2 y 3 mm.",
               "en": "Using Ashby charts we chose PLA (E = 2,800 MPa, 60 MPa strength) printed at 100% infill: it is cheap, accessible and allows a custom geometry. We chose an I-section because it is symmetric and uses both flanges equally in tension and compression. We sized it iteratively with Navier's law, the Rankine criterion and Castigliano's theorem, looking for the lowest mass that met every limit. The result was an 18 × 30 mm section with 2 and 3 mm walls.",
               "ca": "Amb diagrames d'Ashby vam triar PLA (E = 2.800 MPa, límit de 60 MPa) imprès al 100 % de farciment: és barat, accessible i permet una geometria a mida. Vam triar una secció en doble T perquè és simètrica i aprofita igual les ales a tracció i a compressió. La vam dimensionar iterant amb la llei de Navier, el criteri de Rankine i el teorema de Castigliano, buscant la mínima massa que ho complís tot. El resultat va ser una secció de 18 × 30 mm amb parets de 2 i 3 mm."}},
        {"h": {"es": "Fabricación", "en": "Manufacturing", "ca": "Fabricació"},
         "p": {"es": "La viga mide 500 mm y la placa de la impresora (Bambu Lab A1) solo 256 mm, así que la imprimimos en dos piezas unidas con un empalme a solape y un tornillo M4 de acero. En la zona de la unión reforzamos el alma hasta 10 mm, con lo que el coeficiente de seguridad ahí pasó a 3,5. Ajustamos los parámetros de impresión (230 °C, capas de 0,16 mm, 5 perímetros, relleno rectilíneo al 100 %) para que las propiedades se acercaran a las de la ficha técnica.",
               "en": "The beam is 500 mm long and the printer bed (Bambu Lab A1) is only 256 mm, so we printed it in two parts joined by a lap splice with a steel M4 bolt. Around the joint we thickened the web to 10 mm, which raised the safety factor there to 3.5. We tuned the print settings (230 °C, 0.16 mm layers, 5 perimeters, 100% rectilinear infill) so the properties would match the datasheet.",
               "ca": "La biga fa 500 mm i la placa de la impressora (Bambu Lab A1) només 256 mm, així que la vam imprimir en dues peces unides amb un empalmament a solapa i un cargol M4 d'acer. A la zona de la unió vam reforçar l'ànima fins a 10 mm, de manera que el coeficient de seguretat allà va passar a 3,5. Vam ajustar els paràmetres d'impressió (230 °C, capes de 0,16 mm, 5 perímetres, farciment rectilini al 100 %) perquè les propietats s'acostessin a les de la fitxa tècnica."}},
        {"h": {"es": "El primer prototipo falló", "en": "The first prototype failed", "ca": "El primer prototip va fallar"},
         "p": {"es": "La primera viga la imprimimos en PLA Matte, que resultó tener un módulo de Young bastante más bajo que el usado en los cálculos. La probamos en casa y se rompió mucho antes de lo esperado, separándose entre capas en el tramo inclinado. Habíamos impreso todas las capas en horizontal, y en el tramo diagonal la tensión normal actuaba en parte perpendicular a ellas. Volvimos a imprimir en PLA Basic, orientando cada tramo para que las fibras siguieran la dirección de la tensión.",
               "en": "We printed the first beam in PLA Matte, which turned out to have a much lower Young's modulus than the one used in the calculations. We tested it at home and it broke far earlier than expected, splitting between layers in the inclined segment. All layers had been printed horizontally, so in the diagonal segment the normal stress acted partly across them. We reprinted in PLA Basic, orienting each segment so the fibres followed the stress direction.",
               "ca": "La primera biga la vam imprimir en PLA Matte, que va resultar tenir un mòdul de Young força més baix que el fet servir als càlculs. La vam provar a casa i es va trencar molt abans del que esperàvem, separant-se entre capes al tram inclinat. Havíem imprès totes les capes en horitzontal, i al tram diagonal la tensió normal actuava en part perpendicular a elles. Vam tornar a imprimir en PLA Basic, orientant cada tram perquè les fibres seguissin la direcció de la tensió."}},
        {"h": {"es": "Verificación por elementos finitos", "en": "Finite element check", "ca": "Verificació per elements finits"},
         "p": {"es": "Contrastamos el cálculo a mano con SOLIDWORKS Simulation, con una malla de unos 58.000 nodos. La simulación dio una flecha de 11,3 mm, frente a los 13,8 mm de Castigliano. La diferencia es razonable: el modelo 3D recoge la rigidez extra de los codos y de la unión, que el cálculo analítico no considera. Las dos cifras quedan por debajo del límite de 15 mm.",
               "en": "We checked the hand calculation with SOLIDWORKS Simulation, using a mesh of about 58,000 nodes. The simulation gave an 11.3 mm deflection, against 13.8 mm from Castigliano. The difference makes sense: the 3D model captures the extra stiffness of the corners and the joint, which the analytical model leaves out. Both values are below the 15 mm limit.",
               "ca": "Vam contrastar el càlcul a mà amb SOLIDWORKS Simulation, amb una malla d'uns 58.000 nodes. La simulació va donar una fletxa d'11,3 mm, davant dels 13,8 mm de Castigliano. La diferència és raonable: el model 3D recull la rigidesa extra dels colzes i de la unió, que el càlcul analític no considera. Les dues xifres queden per sota del límit de 15 mm."}},
    ],
    "galeria": [
        {"img": "img/viga-impresa/esquema.jpg", "pie": {"es": "Planteamiento: apoyos a 500 mm, carga de 250 N y dos obstáculos.", "en": "Problem set-up: supports 500 mm apart, 250 N load and two obstacles.", "ca": "Plantejament: suports a 500 mm, càrrega de 250 N i dos obstacles."}},
        {"img": "img/viga-impresa/seccion.jpg", "pie": {"es": "Sección en doble T elegida y sus resultados.", "en": "Chosen I-section and its results.", "ca": "Secció en doble T triada i els seus resultats."}},
        {"img": "img/viga-impresa/fem-tensiones.jpg", "pie": {"es": "Tensiones en SOLIDWORKS Simulation.", "en": "Stresses in SOLIDWORKS Simulation.", "ca": "Tensions en SOLIDWORKS Simulation."}},
        {"img": "img/viga-impresa/fem-desplazamientos.jpg", "pie": {"es": "Desplazamiento vertical: 11,3 mm en el punto de carga.", "en": "Vertical displacement: 11.3 mm at the load point.", "ca": "Desplaçament vertical: 11,3 mm al punt de càrrega."}},
        {"img": "img/viga-impresa/impresion.jpg", "pie": {"es": "Impresión de las piezas en la Bambu Lab A1.", "en": "Printing the parts on the Bambu Lab A1.", "ca": "Impressió de les peces a la Bambu Lab A1."}},
        {"img": "img/viga-impresa/primer-prototipo-roto.jpg", "pie": {"es": "Primer prototipo: rotura entre capas en el tramo inclinado.", "en": "First prototype: delamination in the inclined segment.", "ca": "Primer prototip: trencament entre capes al tram inclinat."}},
        {"img": "img/viga-impresa/orientacion-incorrecta.jpg", "pie": {"es": "Orientación inicial: capas cruzadas con la tensión en el tramo diagonal.", "en": "Initial orientation: layers crossing the stress in the diagonal segment.", "ca": "Orientació inicial: capes creuades amb la tensió al tram diagonal."}},
        {"img": "img/viga-impresa/orientacion-correcta.jpg", "pie": {"es": "Orientación corregida: fibras alineadas en todos los tramos.", "en": "Corrected orientation: fibres aligned in every segment.", "ca": "Orientació corregida: fibres alineades a tots els trams."}},
    ],
},
# ───────────────────────────── Brazo
{
    "slug": "brazo-robotico",
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
    "etiquetas": ["Arduino", I3D, {"es": "Servos", "en": "Servos", "ca": "Servos"}, {"es": "Cinemática", "en": "Kinematics", "ca": "Cinemàtica"}],
    "cifras": [],
    "secciones": [
        {"h": {"es": "Objetivo", "en": "Goal", "ca": "Objectiu"},
         "p": {"es": "Construir un brazo de cinco grados de libertad que, a partir de una posición en coordenadas, mueva cada articulación para coger un objeto y dejarlo en otro punto. He elegido un camino de bajo coste para poder iterar rápido. Si funciona bien, mejoraré los componentes.",
               "en": "Build a five-degree-of-freedom arm that, given a target position in coordinates, moves each joint to pick up an object and place it somewhere else. I chose a low-cost route so I can iterate quickly. If it works well, I will upgrade the components.",
               "ca": "Construir un braç de cinc graus de llibertat que, a partir d'una posició en coordenades, mogui cada articulació per agafar un objecte i deixar-lo en un altre punt. He triat un camí de baix cost per poder iterar ràpid. Si funciona bé, milloraré els components."}},
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
# ───────────────────────────── Motor
{
    "slug": "motor-dc",
    "estado": "acabado",
    "periodo": {"es": "2026", "en": "2026", "ca": "2026"},
    "tipo": {"es": "Parte práctica de un trabajo universitario", "en": "Practical part of a university assignment", "ca": "Part pràctica d'un treball universitari"},
    "papel": {"es": "Diseño, fabricación y pruebas", "en": "Design, manufacturing and testing", "ca": "Disseny, fabricació i proves"},
    "titulo": {"es": "Motor de corriente continua casero", "en": "Home-built DC motor", "ca": "Motor de corrent continu casolà"},
    "resumen": {
        "es": "Motor de corriente continua construido desde cero con dos imanes de neodimio, tres bobinas y un conmutador. Las piezas están diseñadas en SOLIDWORKS e impresas en 3D. Es la parte práctica de un trabajo sobre motores eléctricos.",
        "en": "A DC motor built from scratch with two neodymium magnets, three coils and a commutator. The parts are designed in SOLIDWORKS and 3D-printed. It is the practical part of an assignment on electric motors.",
        "ca": "Motor de corrent continu construït des de zero amb dos imants de neodimi, tres bobines i un commutador. Les peces estan dissenyades en SOLIDWORKS i impreses en 3D. És la part pràctica d'un treball sobre motors elèctrics.",
    },
    "etiquetas": ["SOLIDWORKS", I3D, {"es": "Electromagnetismo", "en": "Electromagnetism", "ca": "Electromagnetisme"}],
    "cifras": [],
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
         "p": {"es": "Primero probé el principio con una sola bobina y, cuando funcionó, monté las tres y el conmutador hasta tener el motor completo girando.",
               "en": "I first tested the principle with a single coil and, once it worked, assembled all three coils and the commutator until the complete motor was running.",
               "ca": "Primer vaig provar el principi amb una sola bobina i, quan va funcionar, vaig muntar les tres bobines i el commutador fins a tenir el motor complet girant."}},
    ],
    "galeria": [],
},
]


# ───────────────────────────── Maquetación
# Qué figuras, gráficos y animaciones acompañan a cada sección (por índice de sección).
# "filas": filas de figuras (claves = nombre del archivo sin extensión). Las no usadas quedan en la galería final.

MASA = {
    "titulo": {"es": "Masa en cada versión", "en": "Mass of each version", "ca": "Massa a cada versió"},
    "unidad": "g", "dec": 1, "max": 21.47,
    "barras": [
        {"l": {"es": "Inicial", "en": "Initial", "ca": "Inicial"}, "v": 21.47},
        {"l": {"es": "Versión 1", "en": "Version 1", "ca": "Versió 1"}, "v": 15.52},
        {"l": {"es": "Versión 2", "en": "Version 2", "ca": "Versió 2"}, "v": 14.45},
        {"l": {"es": "Final", "en": "Final", "ca": "Final"}, "v": 10.04, "serie": "b"},
    ],
}
CARGA = {
    "titulo": {"es": "Carga de rotura: modelo frente a ensayo", "en": "Failure load: model vs test", "ca": "Càrrega de trencament: model davant d'assaig"},
    "unidad": "N", "dec": 0, "max": 177,
    "barras": [
        {"l": {"es": "Versión 2 · modelo", "en": "Version 2 · model", "ca": "Versió 2 · model"}, "v": 65.77},
        {"l": {"es": "Versión 2 · ensayo", "en": "Version 2 · test", "ca": "Versió 2 · assaig"}, "v": 82, "serie": "b"},
        {"l": {"es": "Final · modelo", "en": "Final · model", "ca": "Final · model"}, "v": 90.81, "sep": True},
        {"l": {"es": "Final · ensayo", "en": "Final · test", "ca": "Final · assaig"}, "v": 177, "serie": "b"},
    ],
}
FLECHA = {
    "titulo": {"es": "Flecha en el punto de carga", "en": "Deflection at the load point", "ca": "Fletxa al punt de càrrega"},
    "unidad": "mm", "dec": 1, "max": 16,
    "limite": {"v": 15, "l": {"es": "Límite: 15 mm", "en": "Limit: 15 mm", "ca": "Límit: 15 mm"}},
    "barras": [
        {"l": {"es": "Cálculo (Castigliano)", "en": "Hand calculation (Castigliano)", "ca": "Càlcul (Castigliano)"}, "v": 13.84},
        {"l": {"es": "Simulación (FEM)", "en": "Simulation (FEM)", "ca": "Simulació (FEM)"}, "v": 11.32, "serie": "b"},
    ],
}

MAQUETA = {
    "clasificador-color": {
        0: {"anim": "ginebra"},
        1: {"filas": [["funcionamiento"]]},
        2: {"filas": [["ensamblaje-cad"], ["simulacion-solidworks"]]},
        3: {"filas": [["diagrama-flujo"]]},
    },
    "abridor-fem": {
        2: {"filas": [["fem-traccion", "fem-compresion-detalle"]]},
        3: {"filas": [["diseno-inicial", "optimizacion-1"], ["optimizacion-2", "diseno-final"]], "barras": MASA,
            "filas2": [["ensayo-82N", "plano"]]},
        4: {"filas": [["ensayo-fuerza-desplazamiento"]], "barras": CARGA},
    },
    "viga-impresa": {
        0: {"filas": [["esquema"]]},
        1: {"filas": [["seccion"]]},
        2: {"filas": [["impresion"]]},
        3: {"filas": [["primer-prototipo-roto"], ["orientacion-incorrecta", "orientacion-correcta"]]},
        4: {"filas": [["fem-tensiones", "fem-desplazamientos"]], "barras": FLECHA},
    },
}
DESCARTAR = {"clasificador-color": ["pantalla-lcd"]}   # redundante con la portada y el vídeo

def _clave(g):
    import os
    return os.path.splitext(os.path.basename(g.get("video") or g["img"]))[0]

for _p in PROYECTOS:
    _lib = {_clave(g): g for g in _p["galeria"]}
    _usadas = set(DESCARTAR.get(_p["slug"], []))
    for _i, _m in MAQUETA.get(_p["slug"], {}).items():
        _s = _p["secciones"][_i]
        for _k in ("filas", "filas2"):
            if _k in _m:
                _s[_k] = [[_lib[c] for c in fila] for fila in _m[_k]]
                _usadas.update(c for fila in _m[_k] for c in fila)
        for _k in ("barras", "anim"):
            if _k in _m:
                _s[_k] = _m[_k]
    _p["galeria"] = [g for g in _p["galeria"] if _clave(g) not in _usadas]
