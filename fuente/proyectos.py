# -*- coding: utf-8 -*-
# Proyectos de la web. Cada texto en es / en / ca.
# galeria: imágenes {"img": ruta, "pie": {...}} o vídeos {"video": ruta, "img": póster, "pie": {...}}
# cifras: datos clave {"v": valor, "l": {...}}

I3D = {"es": "Impresión 3D", "en": "3D printing", "ca": "Impressió 3D"}

# Del más reciente al más antiguo. Un proyecto nuevo se añade al principio.
ORDEN = ["brazo-robotico", "clasificador-color", "viga-impresa", "abridor-fem"]

PROYECTOS = [
# ───────────────────────────── Clasificador
{
    "slug": "clasificador-color",
    "estado": "acabado",
    "portada": "img/clasificador-color/maquina-funcionando.jpg",
    "periodo": {"es": "01/2026 – 05/2026", "en": "01/2026 – 05/2026", "ca": "01/2026 – 05/2026"},
    "tipo": {"es": "Proyecto II · ETSEIB · equipo de 4", "en": "Project II · ETSEIB · team of 4", "ca": "Projecte II · ETSEIB · equip de 4"},
    "papel": {"es": "Coordinación, programación, electrónica e impresión 3D", "en": "Coordination, programming, electronics and 3D printing", "ca": "Coordinació, programació, electrònica i impressió 3D"},
    "titulo": {"es": "Clasificador automático por colores con Cruz de Malta", "en": "Automatic colour sorter with a Geneva drive", "ca": "Classificador automàtic per colors amb creu de Malta"},
    "resumen": {
        "es": "Máquina que clasifica piezas por colores. Una cinta las lleva a una plataforma que gira a pasos exactos de 90° gracias a una Cruz de Malta. En cada parada, un sensor lee el color y tres servomotores empujan cada pieza a su caja.",
        "en": "A machine that sorts parts by colour. A conveyor feeds them onto a platform that turns in exact 90° steps thanks to a Geneva drive. At each stop a sensor reads the colour and three servos push each part into its bin.",
        "ca": "Màquina que classifica peces per colors. Una cinta les porta a una plataforma que gira a passos exactes de 90° gràcies a una creu de Malta. A cada parada, un sensor llegeix el color i tres servomotors empenyen cada peça a la seva caixa.",
    },
    "etiquetas": ["SOLIDWORKS", "Arduino (C++)", I3D, {"es": "Mecanismos", "en": "Mechanisms", "ca": "Mecanismes"}],
    "cifras": [],
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
         "p": {"es": "Todas las piezas propias se modelaron de forma paramétrica en SOLIDWORKS con criterios de diseño para fabricación y se imprimieron en PLA: la rueda motriz, la Cruz de Malta, la plataforma superior, la bancada que sujeta el sensor y los servos, y los toboganes que llevan cada pieza a su caja. Antes de imprimir, comprobamos el ensamblaje con detección de interferencias y un estudio de movimiento, para que los brazos de los servos no chocaran con el soporte del sensor.",
               "en": "All custom parts were modelled parametrically in SOLIDWORKS following design-for-manufacturing criteria and printed in PLA: the drive wheel, the Geneva wheel, the top platform, the frame that holds the sensor and the servos, and the chutes that take each part to its bin. Before printing, we checked the assembly with interference detection and a motion study so the servo arms would not hit the sensor mount.",
               "ca": "Totes les peces pròpies es van modelar de manera paramètrica en SOLIDWORKS amb criteris de disseny per a fabricació i es van imprimir en PLA: la roda motriu, la creu de Malta, la plataforma superior, la bancada que subjecta el sensor i els servos, i els tobogans que porten cada peça a la seva caixa. Abans d'imprimir, vam comprovar el muntatge amb detecció d'interferències i un estudi de moviment, perquè els braços dels servos no xoquessin amb el suport del sensor."}},
        {"h": {"es": "Control", "en": "Control", "ca": "Control"},
         "p": {"es": "El programa en C++ sincroniza tres cosas: la lectura del sensor, el giro de la plataforma y el disparo de los servos. Para que ninguna tarea bloquee a las demás, el avance del motor paso a paso se temporiza con millis() en lugar de pausas fijas. Antes de cada uso se calibra el sensor con piezas de referencia de cada color.",
               "en": "The C++ program synchronises three things: the sensor reading, the platform rotation and the servo actuation. To keep any task from blocking the others, the stepper is timed with millis() instead of fixed delays. The sensor is calibrated with reference parts of each colour before use.",
               "ca": "El programa en C++ sincronitza tres coses: la lectura del sensor, el gir de la plataforma i l'accionament dels servos. Perquè cap tasca bloquegi les altres, l'avanç del motor pas a pas es temporitza amb millis() en lloc de pauses fixes. Abans de cada ús es calibra el sensor amb peces de referència de cada color."},
         "l": {"es": ["La cinta avanza y deja una pieza en la estación de lectura. El sensor la lee y la pantalla muestra el color detectado.",
                      "La cinta se para, para que no caiga otra pieza durante la maniobra, y la plataforma avanza 90°.",
                      "El programa desplaza una posición su registro de cuatro estaciones. Así, el color de cada pieza viaja en memoria a la vez que la pieza gira en la plataforma.",
                      "Si el color guardado en una estación coincide con el de su caja, el servo de esa estación empuja la pieza, vuelve a su posición de reposo y el contador de ese color suma uno. Si hace falta, actúan varios servos a la vez."],
               "en": ["The conveyor runs and drops a part at the reading station. The sensor reads it and the display shows the detected colour.",
                      "The conveyor stops, so no other part falls during the move, and the platform advances 90°.",
                      "The program shifts its four-station register by one position. This way the colour of each part travels in memory while the part turns on the platform.",
                      "If the colour stored for a station matches its bin, that station's servo pushes the part, returns to rest and the counter for that colour goes up by one. Several servos can act at once if needed."],
               "ca": ["La cinta avança i deixa una peça a l'estació de lectura. El sensor la llegeix i la pantalla mostra el color detectat.",
                      "La cinta s'atura, perquè no caigui una altra peça durant la maniobra, i la plataforma avança 90°.",
                      "El programa desplaça una posició el seu registre de quatre estacions. Així, el color de cada peça viatja en memòria alhora que la peça gira a la plataforma.",
                      "Si el color desat en una estació coincideix amb el de la seva caixa, el servo d'aquella estació empeny la peça, torna a la posició de repòs i el comptador d'aquell color suma un. Si cal, actuen diversos servos alhora."]}},
        {"h": {"es": "Lectura del color", "en": "Reading the colour", "ca": "Lectura del color"},
         "p": {"es": "Las piezas son caramelos Sugus rojos, verdes y azules. El TCS3200 no devuelve un color, sino una señal por cada uno de sus filtros (rojo, verde y azul). El programa mide los tres canales y se queda con el dominante. Si la lectura es demasiado débil o los tres canales salen casi iguales, entiende que la estación está vacía y no guarda nada. Las cajas están a 90°, 180° y 270° de la estación de lectura: rojo, verde y azul, en ese orden.",
               "en": "The parts are red, green and blue Sugus sweets. The TCS3200 does not return a colour but one signal for each of its filters (red, green and blue). The program measures the three channels and keeps the dominant one. If the reading is too weak or the three channels come out almost equal, it takes the station as empty and stores nothing. The bins sit 90°, 180° and 270° from the reading station: red, green and blue, in that order.",
               "ca": "Les peces són caramels Sugus vermells, verds i blaus. El TCS3200 no retorna un color, sinó un senyal per cadascun dels seus filtres (vermell, verd i blau). El programa mesura els tres canals i es queda amb el dominant. Si la lectura és massa feble o els tres canals surten gairebé iguals, entén que l'estació és buida i no desa res. Les caixes són a 90°, 180° i 270° de l'estació de lectura: vermell, verd i blau, en aquest ordre."}},
        {"h": {"es": "Mi papel", "en": "My role", "ca": "El meu paper"},
         "p": {"es": "Coordiné al equipo de cuatro personas porque era quien estaba metido en más partes del proyecto. Hice toda la programación y las conexiones electrónicas, e imprimí las piezas, que diseñamos entre todo el equipo. Participé en todas las fases, desde la propuesta hasta el prototipo final y el póster.",
               "en": "I coordinated the team of four because I was the one involved in most parts of the project. I wrote all the code and did all the electronic wiring, and I printed the parts, which we designed together as a team. I took part in every phase, from the proposal to the final prototype and the poster.",
               "ca": "Vaig coordinar l'equip de quatre persones perquè era qui estava ficat en més parts del projecte. Vaig fer tota la programació i les connexions electròniques, i vaig imprimir les peces, que vam dissenyar entre tot l'equip. Vaig participar en totes les fases, des de la proposta fins al prototip final i el pòster."}},
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
         "p": {"es": "El abridor tenía que permitir abrir una botella con comodidad, romperse con la mano en un ensayo destructivo controlado, tener un brazo de menos de 150 mm y un coeficiente de seguridad de entre 1,5 y 2. La eficiencia a maximizar era la carga última dividida por el peso de la pieza.",
               "en": "The opener had to open a bottle comfortably, break by hand in a controlled destructive test, have a lever arm under 150 mm and a safety factor between 1.5 and 2. The efficiency to maximise was the ultimate load divided by the weight of the part.",
               "ca": "L'obridor havia de permetre obrir una ampolla còmodament, trencar-se amb la mà en un assaig destructiu controlat, tenir un braç de menys de 150 mm i un coeficient de seguretat d'entre 1,5 i 2. L'eficiència a maximitzar era la càrrega última dividida pel pes de la peça."}},
        {"h": {"es": "Las fuerzas de diseño", "en": "Design forces", "ca": "Les forces de disseny"},
         "l": {"es": ["Para abrir: el profesorado sitúa en unos 100 N la fuerza necesaria para desprender una chapa. Con la palanca del primer diseño (23 mm del gancho al apoyo y 100 mm del apoyo a la mano), eso son 23 N en el mango. Contando la dispersión, 37,4 N cubren el 95 % de los casos, y esa fue la fuerza nominal.",
                      "Lo que puede hacer el usuario: partimos de un estudio de fuerza de agarre con 211 adultos y supusimos que al empujar el mango se aplica un 30 % de esa fuerza. El percentil 5 son 49,7 N, por encima de la fuerza nominal, así que casi cualquier persona puede usarlo.",
                      "Para romper: con el coeficiente de seguridad pedido, el primer diseño tenía que fallar con una carga de entre 56 y 75 N."],
               "en": ["To open: the teaching staff put the force needed to pull off a cap at about 100 N. With the lever of the first design (23 mm from hook to fulcrum and 100 mm from fulcrum to hand), that is 23 N at the handle. Allowing for scatter, 37.4 N covers 95% of cases, and that became the nominal force.",
                      "What the user can do: we started from a grip-strength study of 211 adults and assumed that pushing on the handle uses 30% of that force. The 5th percentile is 49.7 N, above the nominal force, so almost anyone can use it.",
                      "To break: with the required safety factor, the first design had to fail under a load between 56 and 75 N."],
               "ca": ["Per obrir: el professorat situa en uns 100 N la força necessària per desprendre un tap de corona. Amb la palanca del primer disseny (23 mm del ganxo al suport i 100 mm del suport a la mà), això són 23 N al mànec. Comptant la dispersió, 37,4 N cobreixen el 95 % dels casos, i aquesta va ser la força nominal.",
                      "El que pot fer l'usuari: vam partir d'un estudi de força de presa amb 211 adults i vam suposar que en empènyer el mànec s'aplica un 30 % d'aquesta força. El percentil 5 són 49,7 N, per sobre de la força nominal, així que gairebé qualsevol persona el pot fer servir.",
                      "Per trencar: amb el coeficient de seguretat demanat, el primer disseny havia de fallar amb una càrrega d'entre 56 i 75 N."]}},
        {"h": {"es": "Material", "en": "Material", "ca": "Material"},
         "p": {"es": "Con un diagrama de Ashby comparamos acero inoxidable, aluminio 6061, polímeros rígidos y madera. Descartamos el acero por su densidad y su límite elástico, demasiado altos, y la madera porque es anisótropa y difícil de modelar. Empezamos estudiando el aluminio, pero con fuerza manual no se podía llegar a su límite elástico y costaba unas cinco veces más. Elegimos metacrilato (PMMA, E = 3.000 MPa, límite elástico de 70 MPa), que además era fácil de conseguir y de cortar.",
               "en": "Using an Ashby chart we compared stainless steel, 6061 aluminium, rigid polymers and wood. We ruled out steel because its density and yield strength were too high, and wood because it is anisotropic and hard to model. We started by studying aluminium, but its yield point could not be reached by hand and it cost about five times more. We chose acrylic (PMMA, E = 3,000 MPa, 70 MPa yield strength), which was also easy to source and to cut.",
               "ca": "Amb un diagrama d'Ashby vam comparar acer inoxidable, alumini 6061, polímers rígids i fusta. Vam descartar l'acer per la densitat i el límit elàstic, massa alts, i la fusta perquè és anisòtropa i difícil de modelitzar. Vam començar estudiant l'alumini, però amb força manual no es podia arribar al seu límit elàstic i costava unes cinc vegades més. Vam triar metacrilat (PMMA, E = 3.000 MPa, límit elàstic de 70 MPa), que a més era fàcil d'aconseguir i de tallar."}},
        {"h": {"es": "Modelo de elementos finitos", "en": "Finite element model", "ca": "Model d'elements finits"},
         "p": {"es": "El modelo se hizo en ANSYS APDL como un problema de tensión plana, con elementos cuadráticos de 8 nodos (PLANE183) y material elástico, lineal e isótropo. El apoyo sobre la chapa se fija en vertical, el punto de contacto del gancho queda fijo y la mano es una fuerza vertical sobre el mango. Refinamos la malla en los puntos con concentración de tensiones y dejamos fuera los elementos pegados a los contactos puntuales, que dan picos de tensión sin sentido físico. Como el metacrilato es frágil, usamos el criterio de Rankine: comprobamos por separado la tensión principal de tracción y la de compresión, y el coeficiente de seguridad es el menor de los dos.",
               "en": "The model was built in ANSYS APDL as a plane-stress problem, with 8-node quadratic elements (PLANE183) and a linear elastic isotropic material. The fulcrum on the cap is fixed vertically, the hook contact point is fully fixed and the hand is a vertical force on the handle. We refined the mesh at stress concentrations and left out the elements next to the point contacts, which give stress peaks with no physical meaning. Because acrylic is brittle we used the Rankine criterion: we checked principal tension and principal compression separately, and the safety factor is the lower of the two.",
               "ca": "El model es va fer en ANSYS APDL com un problema de tensió plana, amb elements quadràtics de 8 nodes (PLANE183) i material elàstic, lineal i isòtrop. El suport sobre el tap es fixa en vertical, el punt de contacte del ganxo queda fix i la mà és una força vertical sobre el mànec. Vam refinar la malla als punts amb concentració de tensions i vam deixar fora els elements enganxats als contactes puntuals, que donen pics de tensió sense sentit físic. Com que el metacrilat és fràgil, vam fer servir el criteri de Rankine: vam comprovar per separat la tensió principal de tracció i la de compressió, i el coeficient de seguretat és el menor dels dos."},
         "l": {"es": ["Hipótesis de linealidad: repetimos el cálculo con un análisis no lineal y el desplazamiento máximo cambió un 3,9 %.",
                      "Pequeños desplazamientos: el desplazamiento máximo era el 3,4 % de la longitud de la pieza."],
               "en": ["Linearity: we repeated the calculation with a non-linear analysis and the maximum displacement changed by 3.9%.",
                      "Small displacements: the maximum displacement was 3.4% of the length of the part."],
               "ca": ["Hipòtesi de linealitat: vam repetir el càlcul amb una anàlisi no lineal i el desplaçament màxim va canviar un 3,9 %.",
                      "Petits desplaçaments: el desplaçament màxim era el 3,4 % de la longitud de la peça."]}},
        {"h": {"es": "Optimización en cuatro versiones", "en": "Four design iterations", "ca": "Optimització en quatre versions"},
         "l": {"es": ["Diseño inicial macizo, de 10 mm de espesor: 21,5 g. Con la carga de rotura objetivo, la tensión máxima era de 44,9 MPa, en el radio interior del gancho, lejos de los 70 MPa del material. Sobraba material.",
                      "Versión 1: dos vaciados interiores siguiendo el contorno, 15,5 g. Carga última prevista de 65 N y eficiencia de 429.",
                      "Versión 2: un tercer vaciado, 14,5 g y eficiencia de 464. La ensayamos y rompió a 82 N por compresión, junto al vaciado central. Hasta entonces solo habíamos vigilado la tracción, porque en el diseño macizo la compresión no importaba. Al reproducir el ensayo en el modelo, la compresión en ese punto era de 92,5 MPa, y ese valor pasó a ser nuestro límite a compresión.",
                      "Versión final: acortamos el brazo de 100 a 63 mm y bajamos el espesor de 10 a 8 mm, con lo que la masa quedó en 10,0 g. Con el brazo más corto hace falta más fuerza para abrir (59,4 N nominales), pero la pieza aguanta más. Las tensiones son de 45,9 MPa a tracción y 55,9 MPa a compresión, con coeficientes de seguridad de 1,53 y 1,65: los dos límites se alcanzan casi a la vez. La carga última prevista es de 91 N y la eficiencia teórica de 922, el doble que la de la versión 2."],
               "en": ["Solid initial design, 10 mm thick: 21.5 g. Under the target failure load, the peak stress was 44.9 MPa, at the inner radius of the hook, far from the 70 MPa of the material. There was material to spare.",
                      "Version 1: two internal cut-outs following the outline, 15.5 g. Predicted ultimate load of 65 N and efficiency of 429.",
                      "Version 2: a third cut-out, 14.5 g and efficiency of 464. We tested it and it broke at 82 N in compression, next to the middle cut-out. Until then we had only watched tension, because compression did not matter in the solid design. When we reproduced the test in the model, compression at that point was 92.5 MPa, and that value became our compressive limit.",
                      "Final version: we shortened the lever arm from 100 to 63 mm and reduced the thickness from 10 to 8 mm, which brought the mass down to 10.0 g. A shorter arm needs more force to open a bottle (59.4 N nominal), but the part holds more. Stresses are 45.9 MPa in tension and 55.9 MPa in compression, with safety factors of 1.53 and 1.65: both limits are reached almost together. The predicted ultimate load is 91 N and the theoretical efficiency 922, twice that of version 2."],
               "ca": ["Disseny inicial massís, de 10 mm de gruix: 21,5 g. Amb la càrrega de trencament objectiu, la tensió màxima era de 44,9 MPa, al radi interior del ganxo, lluny dels 70 MPa del material. Sobrava material.",
                      "Versió 1: dos buidats interiors seguint el contorn, 15,5 g. Càrrega última prevista de 65 N i eficiència de 429.",
                      "Versió 2: un tercer buidat, 14,5 g i eficiència de 464. La vam assajar i es va trencar a 82 N per compressió, al costat del buidat central. Fins aleshores només havíem vigilat la tracció, perquè al disseny massís la compressió no importava. En reproduir l'assaig al model, la compressió en aquell punt era de 92,5 MPa, i aquest valor va passar a ser el nostre límit a compressió.",
                      "Versió final: vam escurçar el braç de 100 a 63 mm i vam baixar el gruix de 10 a 8 mm, de manera que la massa va quedar en 10,0 g. Amb el braç més curt cal més força per obrir (59,4 N nominals), però la peça aguanta més. Les tensions són de 45,9 MPa a tracció i 55,9 MPa a compressió, amb coeficients de seguretat d'1,53 i 1,65: els dos límits s'assoleixen gairebé alhora. La càrrega última prevista és de 91 N i l'eficiència teòrica de 922, el doble que la de la versió 2."]}},
        {"h": {"es": "Fabricación", "en": "Manufacturing", "ca": "Fabricació"},
         "p": {"es": "Todas las piezas se cortaron por láser en Servei Estació, en Barcelona: cuatro de los dos primeros prototipos, en plancha de 10 mm, y tres de la versión final, en plancha de 8 mm (una para el ensayo de uso, otra para el destructivo y otra para la presentación). En total fueron siete abridores y dos botellas para los ensayos: 33,8 €.",
               "en": "All parts were laser-cut at Servei Estació in Barcelona: four of the first two prototypes, from 10 mm sheet, and three of the final version, from 8 mm sheet (one for the functional test, one for the destructive test and one for the presentation). In total, seven openers and two bottles for the tests: €33.80.",
               "ca": "Totes les peces es van tallar per làser a Servei Estació, a Barcelona: quatre dels dos primers prototips, en planxa de 10 mm, i tres de la versió final, en planxa de 8 mm (una per a l'assaig d'ús, una altra per al destructiu i una altra per a la presentació). En total van ser set obridors i dues ampolles per als assaigs: 33,8 €."}},
        {"h": {"es": "Ensayo final y lo que aprendí", "en": "Final test and what I learned", "ca": "Assaig final i què en vaig aprendre"},
         "p": {"es": "En el ensayo de uso, la versión final abrió la botella sin problema. En el ensayo destructivo aguantó 177 N, casi el doble de lo previsto, con un comportamiento elástico y frágil hasta la rotura. El modelo lineal resultó conservador por tres motivos: predice el fallo con la tensión pico de un solo nodo, no recoge la redistribución local de tensiones del PMMA y el punto de contacto real era distinto del simulado. El coeficiente de seguridad real fue de 3,3, fuera del rango pedido. La lección es que un modelo de elementos finitos hay que contrastarlo con ensayos y ajustar bien las condiciones de contorno.",
               "en": "In the functional test the final version opened the bottle without trouble. In the destructive test it held 177 N, almost twice the prediction, behaving elastically and brittle up to failure. The linear model proved conservative for three reasons: it predicts failure from a single-node peak stress, it ignores local stress redistribution in PMMA, and the real contact point differed from the simulated one. The real safety factor was 3.3, outside the required range. The lesson is that a finite element model has to be checked against tests and its boundary conditions tuned carefully.",
               "ca": "A l'assaig d'ús, la versió final va obrir l'ampolla sense problema. A l'assaig destructiu va aguantar 177 N, gairebé el doble del previst, amb un comportament elàstic i fràgil fins al trencament. El model lineal va resultar conservador per tres motius: prediu la fallada amb la tensió pic d'un sol node, no recull la redistribució local de tensions del PMMA i el punt de contacte real era diferent del simulat. El coeficient de seguretat real va ser de 3,3, fora del rang demanat. La lliçó és que un model d'elements finits s'ha de contrastar amb assaigs i ajustar bé les condicions de contorn."}},
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
         "p": {"es": "La forma de la viga venía condicionada por dos obstáculos de 50 mm que hay entre los apoyos. Para esquivarlos, la viga baja 120 mm entre sus dos tramos horizontales, y la carga de 250 N actúa en el tramo inferior. Iteramos el ángulo del tramo inclinado y la longitud del primer tramo, y elegimos 65° y 185 mm. Es un compromiso entre momento flector bajo, un reparto razonable entre axil y cortante, y uniones fáciles de fabricar.",
               "en": "The shape of the beam was dictated by two 50 mm obstacles between the supports. To clear them, the beam drops 120 mm between its two horizontal segments, and the 250 N load acts on the lower one. We iterated the angle of the inclined segment and the length of the first segment, and chose 65° and 185 mm. It balances a low bending moment, a reasonable split between axial and shear force, and joints that are easy to make.",
               "ca": "La forma de la biga venia condicionada per dos obstacles de 50 mm que hi ha entre els suports. Per esquivar-los, la biga baixa 120 mm entre els dos trams horitzontals, i la càrrega de 250 N actua al tram inferior. Vam iterar l'angle del tram inclinat i la longitud del primer tram, i vam triar 65° i 185 mm. És un compromís entre moment flector baix, un repartiment raonable entre axial i tallant, i unions fàcils de fabricar."},
         "l": {"es": ["Reacciones en los apoyos: 96,9 N en A y 153,1 N en B. El momento flector máximo, 29,7 N·m, está en el punto de aplicación de la carga.",
                      "Con un ángulo de 80° el momento del tramo inclinado bajaba solo 1,9 N·m, pero ese tramo trabajaba casi todo a compresión, con riesgo de pandeo, y las uniones quedaban casi en ángulo recto.",
                      "Tramos resultantes: 185 mm el superior, 132,4 mm el inclinado y 259 mm el inferior."],
               "en": ["Support reactions: 96.9 N at A and 153.1 N at B. The maximum bending moment, 29.7 N·m, is at the load point.",
                      "At 80° the moment in the inclined segment dropped by only 1.9 N·m, but that segment worked almost entirely in compression, with a risk of buckling, and the joints became nearly right angles.",
                      "Resulting segments: 185 mm upper, 132.4 mm inclined and 259 mm lower."],
               "ca": ["Reaccions als suports: 96,9 N a A i 153,1 N a B. El moment flector màxim, 29,7 N·m, és al punt d'aplicació de la càrrega.",
                      "Amb un angle de 80° el moment del tram inclinat baixava només 1,9 N·m, però aquest tram treballava gairebé tot a compressió, amb risc de vinclament, i les unions quedaven gairebé en angle recte.",
                      "Trams resultants: 185 mm el superior, 132,4 mm l'inclinat i 259 mm l'inferior."]}},
        {"h": {"es": "Material y sección", "en": "Material and cross-section", "ca": "Material i secció"},
         "p": {"es": "Con diagramas de Ashby elegimos PLA (E = 2.800 MPa, límite de 60 MPa) impreso al 100 % de relleno: es barato, accesible y permite una geometría a medida. Elegimos una sección en doble T porque es simétrica y aprovecha igual las alas a tracción y a compresión. La dimensionamos iterando con la ley de Navier, el criterio de Rankine y el teorema de Castigliano, buscando la mínima masa que cumpliera todo. El resultado fue una sección de 18 × 30 mm, con alas de 2 mm y alma de 3 mm. Con ella, la tensión máxima calculada es de 24,0 MPa (coeficiente de seguridad de 2,50), la flecha de 13,8 mm y la masa teórica de 107 g.",
               "en": "Using Ashby charts we chose PLA (E = 2,800 MPa, 60 MPa strength) printed at 100% infill: it is cheap, accessible and allows a custom geometry. We chose an I-section because it is symmetric and uses both flanges equally in tension and compression. We sized it iteratively with Navier's law, the Rankine criterion and Castigliano's theorem, looking for the lowest mass that met every limit. The result was an 18 × 30 mm section with 2 mm flanges and a 3 mm web. With it, the calculated peak stress is 24.0 MPa (safety factor 2.50), the deflection 13.8 mm and the theoretical mass 107 g.",
               "ca": "Amb diagrames d'Ashby vam triar PLA (E = 2.800 MPa, límit de 60 MPa) imprès al 100 % de farciment: és barat, accessible i permet una geometria a mida. Vam triar una secció en doble T perquè és simètrica i aprofita igual les ales a tracció i a compressió. La vam dimensionar iterant amb la llei de Navier, el criteri de Rankine i el teorema de Castigliano, buscant la mínima massa que ho complís tot. El resultat va ser una secció de 18 × 30 mm, amb ales de 2 mm i ànima de 3 mm. Amb ella, la tensió màxima calculada és de 24,0 MPa (coeficient de seguretat de 2,50), la fletxa de 13,8 mm i la massa teòrica de 107 g."},
         "l": {"es": ["Material: el PLA Basic de eSUN resiste 64 MPa a lo largo de los cordones, pero solo 28 MPa entre capas. Por eso las capas tenían que seguir la dirección de la tensión.",
                      "Restricciones de la sección: alto no mayor que el doble del ancho (para que no vuelque), ancho de 35 mm como máximo y alto de 38 mm como máximo, por el obstáculo.",
                      "Probamos todas las combinaciones de alma (2–5 mm), alas (2–5 mm), ancho (10–30 mm) y alto (16–32 mm). Una sección de 22 × 28 mm pesaba 10 g menos, pero su flecha, 14,9 mm, quedaba al borde del límite.",
                      "Comprobamos también la unión entre ala y alma (20,9 MPa) y el eje neutro, donde el cortante es máximo (1,3 MPa): los puntos críticos son las caras superior e inferior."],
               "en": ["Material: eSUN PLA Basic withstands 64 MPa along the extruded lines but only 28 MPa between layers. That is why the layers had to follow the stress direction.",
                      "Section limits: height no more than twice the width (so it does not tip over), width up to 35 mm and height up to 38 mm because of the obstacle.",
                      "We tried every combination of web (2–5 mm), flanges (2–5 mm), width (10–30 mm) and height (16–32 mm). A 22 × 28 mm section was 10 g lighter, but its 14.9 mm deflection sat right at the limit.",
                      "We also checked the flange-to-web junction (20.9 MPa) and the neutral axis, where shear peaks (1.3 MPa): the critical points are the top and bottom faces."],
               "ca": ["Material: el PLA Basic d'eSUN resisteix 64 MPa al llarg dels cordons, però només 28 MPa entre capes. Per això les capes havien de seguir la direcció de la tensió.",
                      "Restriccions de la secció: alçada no més gran que el doble de l'amplada (perquè no bolqui), amplada de 35 mm com a màxim i alçada de 38 mm com a màxim, per l'obstacle.",
                      "Vam provar totes les combinacions d'ànima (2–5 mm), ales (2–5 mm), amplada (10–30 mm) i alçada (16–32 mm). Una secció de 22 × 28 mm pesava 10 g menys, però la seva fletxa, 14,9 mm, quedava al límit.",
                      "Vam comprovar també la unió entre ala i ànima (20,9 MPa) i l'eix neutre, on el tallant és màxim (1,3 MPa): els punts crítics són les cares superior i inferior."]}},
        {"h": {"es": "Fabricación", "en": "Manufacturing", "ca": "Fabricació"},
         "p": {"es": "La viga mide 500 mm y la placa de la impresora (Bambu Lab A1) solo 256 mm, así que la imprimimos en dos piezas unidas con un empalme a solape y un tornillo M4 de acero. En la zona de la unión reforzamos el alma hasta 10 mm, con lo que el coeficiente de seguridad ahí pasó a 3,5. Ajustamos los parámetros de impresión (230 °C, capas de 0,16 mm, 5 perímetros, relleno rectilíneo al 100 %) para que las propiedades se acercaran a las de la ficha técnica.",
               "en": "The beam is 500 mm long and the printer bed (Bambu Lab A1) is only 256 mm, so we printed it in two parts joined by a lap splice with a steel M4 bolt. Around the joint we thickened the web to 10 mm, which raised the safety factor there to 3.5. We tuned the print settings (230 °C, 0.16 mm layers, 5 perimeters, 100% rectilinear infill) so the properties would match the datasheet.",
               "ca": "La biga fa 500 mm i la placa de la impressora (Bambu Lab A1) només 256 mm, així que la vam imprimir en dues peces unides amb un empalmament a solapa i un cargol M4 d'acer. A la zona de la unió vam reforçar l'ànima fins a 10 mm, de manera que el coeficient de seguretat allà va passar a 3,5. Vam ajustar els paràmetres d'impressió (230 °C, capes de 0,16 mm, 5 perímetres, farciment rectilini al 100 %) perquè les propietats s'acostessin a les de la fitxa tècnica."},
         "l": {"es": ["El corte está en el tramo inclinado, a 73 mm de la esquina superior. Ahí el momento es de 20,9 N·m, y cada ala transmite unos 770 N al tornillo.",
                      "Con el alma de 3 mm, el tornillo aplastaba el PLA a 56,9 MPa, casi en el límite de 60 MPa. Con el alma de 10 mm la presión baja a 17,1 MPa.",
                      "La sección con el agujero queda a 16,4 MPa, con un coeficiente de seguridad de 3,7."],
               "en": ["The cut is in the inclined segment, 73 mm from the upper corner. The moment there is 20.9 N·m, and each flange passes about 770 N to the bolt.",
                      "With the 3 mm web, the bolt crushed the PLA at 56.9 MPa, almost at the 60 MPa limit. With a 10 mm web the bearing stress drops to 17.1 MPa.",
                      "The section through the hole sits at 16.4 MPa, a safety factor of 3.7."],
               "ca": ["El tall és al tram inclinat, a 73 mm de la cantonada superior. Allà el moment és de 20,9 N·m, i cada ala transmet uns 770 N al cargol.",
                      "Amb l'ànima de 3 mm, el cargol aixafava el PLA a 56,9 MPa, gairebé al límit de 60 MPa. Amb l'ànima de 10 mm la pressió baixa a 17,1 MPa.",
                      "La secció amb el forat queda a 16,4 MPa, amb un coeficient de seguretat de 3,7."]}},
        {"h": {"es": "El primer prototipo falló", "en": "The first prototype failed", "ca": "El primer prototip va fallar"},
         "p": {"es": "La primera viga la imprimimos en PLA Matte, que resultó tener un módulo de Young bastante más bajo que el usado en los cálculos. La probamos en casa y se rompió mucho antes de lo esperado, separándose entre capas en el tramo inclinado. Habíamos impreso todas las capas en horizontal, y en el tramo diagonal la tensión normal actuaba en parte perpendicular a ellas. Volvimos a imprimir en PLA Basic, orientando cada tramo para que las fibras siguieran la dirección de la tensión.",
               "en": "We printed the first beam in PLA Matte, which turned out to have a much lower Young's modulus than the one used in the calculations. We tested it at home and it broke far earlier than expected, splitting between layers in the inclined segment. All layers had been printed horizontally, so in the diagonal segment the normal stress acted partly across them. We reprinted in PLA Basic, orienting each segment so the fibres followed the stress direction.",
               "ca": "La primera biga la vam imprimir en PLA Matte, que va resultar tenir un mòdul de Young força més baix que el fet servir als càlculs. La vam provar a casa i es va trencar molt abans del que esperàvem, separant-se entre capes al tram inclinat. Havíem imprès totes les capes en horitzontal, i al tram diagonal la tensió normal actuava en part perpendicular a elles. Vam tornar a imprimir en PLA Basic, orientant cada tram perquè les fibres seguissin la direcció de la tensió."}},
        {"h": {"es": "Verificación por elementos finitos", "en": "Finite element check", "ca": "Verificació per elements finits"},
         "p": {"es": "Contrastamos el cálculo a mano con SOLIDWORKS Simulation, con una malla de unos 58.000 nodos. La simulación dio una flecha de 11,3 mm, frente a los 13,8 mm de Castigliano. La diferencia es razonable: el modelo 3D recoge la rigidez extra de los codos y de la unión, que el cálculo analítico no considera. Las dos cifras quedan por debajo del límite de 15 mm.",
               "en": "We checked the hand calculation with SOLIDWORKS Simulation, using a mesh of about 58,000 nodes. The simulation gave an 11.3 mm deflection, against 13.8 mm from Castigliano. The difference makes sense: the 3D model captures the extra stiffness of the corners and the joint, which the analytical model leaves out. Both values are below the 15 mm limit.",
               "ca": "Vam contrastar el càlcul a mà amb SOLIDWORKS Simulation, amb una malla d'uns 58.000 nodes. La simulació va donar una fletxa d'11,3 mm, davant dels 13,8 mm de Castigliano. La diferència és raonable: el model 3D recull la rigidesa extra dels colzes i de la unió, que el càlcul analític no considera. Les dues xifres queden per sota del límit de 15 mm."},
         "l": {"es": ["Malla sólida de elementos cuadráticos: 58.182 nodos y 29.672 elementos. La unión atornillada no se modeló, porque sus coeficientes de seguridad eran mucho más altos.",
                      "Tensiones máximas en la sección de la carga: 20,9 MPa a tracción y 18,3 MPa a compresión, frente a los 24,0 MPa del cálculo a mano. El cálculo a mano queda del lado de la seguridad."],
               "en": ["Solid mesh of quadratic elements: 58,182 nodes and 29,672 elements. The bolted joint was not modelled, because its safety factors were much higher.",
                      "Peak stresses at the load section: 20.9 MPa in tension and 18.3 MPa in compression, against 24.0 MPa from the hand calculation. The hand calculation is on the safe side."],
               "ca": ["Malla sòlida d'elements quadràtics: 58.182 nodes i 29.672 elements. La unió cargolada no es va modelar, perquè els seus coeficients de seguretat eren molt més alts.",
                      "Tensions màximes a la secció de la càrrega: 20,9 MPa a tracció i 18,3 MPa a compressió, davant dels 24,0 MPa del càlcul a mà. El càlcul a mà queda del costat de la seguretat."]}},
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
    "brazo-robotico": {1: {"anim": "brazo"}},
    "clasificador-color": {
        0: {"anim": "ginebra"},
        1: {"filas": [["funcionamiento"]]},
        2: {"filas": [["ensamblaje-cad"], ["simulacion-solidworks"]]},
        3: {"filas": [["diagrama-flujo"]]},
    },
    "abridor-fem": {
        3: {"filas": [["fem-traccion", "fem-compresion-detalle"]]},
        4: {"filas": [["diseno-inicial", "optimizacion-1"], ["optimizacion-2", "diseno-final"]], "barras": MASA,
            "filas2": [["ensayo-82N", "plano"]]},
        6: {"filas": [["ensayo-fuerza-desplazamiento"]], "barras": CARGA},
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


# ───────────────────────────── Portada de la web
# Frase con la que cada proyecto se presenta en la página de inicio.
GANCHOS = {
    "brazo-robotico": {
        "es": "El primer objetivo es que coja un objeto y lo deje en las coordenadas que se le indican.",
        "en": "The first goal is to pick up an object and place it at the coordinates it is given.",
        "ca": "El primer objectiu és que agafi un objecte i el deixi a les coordenades que se li indiquen.",
    },
    "clasificador-color": {
        "es": "La plataforma avanza 90°, se bloquea y, mientras está quieta, un sensor lee el color de la pieza.",
        "en": "The platform advances 90°, locks and, while it is still, a sensor reads the colour of the part.",
        "ca": "La plataforma avança 90°, es bloqueja i, mentre està quieta, un sensor llegeix el color de la peça.",
    },
    "abridor-fem": {
        "es": "El modelo predecía la rotura a 91 N. En el ensayo aguantó 177 N.",
        "en": "The model predicted failure at 91 N. In the test it held 177 N.",
        "ca": "El model preveia el trencament a 91 N. A l'assaig va aguantar 177 N.",
    },
    "viga-impresa": {
        "es": "Diseñada para soportar 250 N entre apoyos a 500 mm, con una flecha calculada de 13,8 mm.",
        "en": "Designed to carry 250 N between supports 500 mm apart, with a calculated deflection of 13.8 mm.",
        "ca": "Dissenyada per suportar 250 N entre suports a 500 mm, amb una fletxa calculada de 13,8 mm.",
    },
}
# Cómo se compone cada proyecto en la página de inicio.
#   forma "a": imagen a la izquierda · "b": imagen a la derecha · "c": foto a todo el ancho
#   "esquema": dibujo animado para los proyectos que aún no tienen fotos · "video": bucle corto · "extra": segunda imagen
DESTACADOS = {
    "brazo-robotico": {"forma": "a", "esquema": "brazo"},
    "clasificador-color": {"forma": "b", "video": "img/clasificador-color/funcionamiento-corto.mp4"},
    "viga-impresa": {"forma": "c"},
    "abridor-fem": {"forma": "b", "extra": "img/abridor-fem/fem-traccion.jpg",
                    "extra_alt": {"es": "Tensiones principales de tracción del diseño final en ANSYS.",
                                  "en": "Maximum principal (tensile) stress of the final design in ANSYS.",
                                  "ca": "Tensions principals de tracció del disseny final a ANSYS."}},
}
