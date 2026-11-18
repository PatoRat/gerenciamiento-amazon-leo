---
title: "Amazon Leo — Informe de investigación"
subtitle: "Versión resumida"
---

**Trabajo Integrador de Investigación · Dirección de Proyectos 2026 · Facultad de Ingeniería y Ciencias Agrarias (UCA)**

Fecha de corte de la evidencia: 16/11/2026

# Resumen ejecutivo

Amazon Leo, antes llamado Project Kuiper, es el programa con el que Amazon quiere dar internet desde el espacio con una constelación de satélites en órbita baja. La FCC, el regulador de Estados Unidos, autorizó 3.232 satélites y fijó dos plazos: 1.616 satélites operativos al 30/07/2026 y los 3.232 al 30/07/2029. En 2020 Amazon anunció una inversión de más de USD 10.000 millones (#39).

Al 16/11/2026 hay unos 396 satélites lanzados (12,3% del total) en 15 misiones. Una de esas misiones falló: el 15/11/2026 el cohete Vulcan perdió los 40 satélites que llevaba. Amazon no llegó al primer plazo y la FCC le dio solo un permiso parcial (un *waiver*). El servicio comercial todavía no empezó.

Rehicimos la gestión del proyecto con el método de la cátedra: caso de negocio, acta, alcance, cronograma, estimaciones, costos, riesgos y valor ganado. Llegamos a cinco conclusiones:

1. **El cuello de botella es el lanzamiento, no la fábrica.** Se fabrican muchos más satélites de los que se lanzan.
2. **El plazo de 2029 no se cumple con los lanzamientos contratados.** El Monte Carlo, la estimación PERT y el valor ganado coinciden. El fin razonable está entre 2031 y 2038.
3. **El riesgo principal es regulatorio:** que la FCC no conceda otro alivio. Proponemos un plan de recuperación (≈ 08/2031), un pedido de alivio con evidencia y más capacidad de lanzamiento.
4. **Faltó un criterio verificable de inicio del servicio.** El inicio se corrió unos dos años sin incumplir ningún plazo formal.
5. **El alcance crece antes de terminar la primera generación** (Gen2, conexión directa a teléfonos, Globalstar).

El límite principal: Amazon no publica sus costos. No calculamos el CPI ni inventamos montos.

# 1. Introducción y método

## 1.1 Qué investigamos y cómo

Investigamos Amazon Leo para reconstruir cómo podría gestionarse, no para describirlo. Seguimos los cinco pasos de la consigna:

| Paso | Qué hicimos | Dónde está |
|---|---|---|
| 1. Ubicar | Historia, motivos y estado al corte | Sección 2 |
| 2. Buscar evidencia | 47 fuentes, con prioridad para las primarias (Amazon, FCC, SEC, ULA) | Sección 3 y Anexo A |
| 3. Reconstruir | Caso de negocio, acta, alcance, cronograma, estimaciones, costos, riesgos y valor ganado | Secciones 4 a 12 |
| 4. Conectar | Una tabla única de cifras y un control de coherencia | Sección 13 y Anexo C |
| 5. Defender | Tablero ejecutivo y guion de preguntas | Tablero |

El marco teórico es el de la cátedra (clases 1 a 6 y 10, el Paneo y las plantillas). Usamos sus nombres: Acta de Constitución, WBS, Registro de Riesgos, Exposición al Riesgo, Valor Ganado.

## 1.2 Cómo se identifica el origen de cada dato

Cada afirmación importante lleva una de tres etiquetas:

- **[dato real]**: viene de una fuente que se puede verificar. Se cita con el número `#n` de la lista de fuentes.
- **[inferencia del grupo]**: una conclusión razonable a partir de la evidencia, con sus supuestos a la vista.
- **[propuesta de gestión]**: algo que creó el grupo para reconstruir cómo se debería gestionar el proyecto: un documento, una estimación, una decisión o una respuesta.

Lo que no es público no se inventa. Aparece como "No público" o como un límite del análisis.

## 1.3 Convenciones

- La fecha de corte es el 16/11/2026. No incorporamos hechos posteriores.
- **Medimos con satélites lanzados**, como aproximación de los operativos. La FCC mide operativos y Amazon solo publica lanzados. Como los operativos son menos o igual que los lanzados, todos nuestros resultados son optimistas para Amazon.
- Todos los números salen de la tabla de cifras maestras (Anexo C).

## 1.4 Limitaciones generales

Amazon es una empresa privada y no publica su cronograma, su WBS ni su presupuesto. Casi todo lo que sabemos de la empresa son declaraciones propias. Algunas páginas no pudieron consultarse por bloqueo o paywall (SpaceNews y fcc.gov, entre otras). Y el proyecto sigue en marcha: la falla de LV-01 ocurrió un día antes del corte.

# 2. Ubicación del proyecto

## 2.1 Qué problema aborda y quién lo impulsa

Amazon presentó el proyecto en 2020 como un servicio de banda ancha confiable y accesible para comunidades sin servicio o mal atendidas (#39), y en 2025 habla de llevar internet a miles de millones de personas que no lo tienen (#28). El sistema tiene tres partes: los satélites, una red terrestre de antenas y fibra, y terminales para los usuarios (Nano, Pro y Ultra, de 100 Mbps a 1 Gbps; #29, #30) **[dato real]**.

Creemos que la oportunidad tiene dos caras. Una es social: conectar donde no llega la red terrestre. La otra es comercial: aerolíneas, empresas, operadores móviles y servicio directo a teléfonos. Los acuerdos firmados entre 2024 y 2026 (JetBlue, Delta, Apple, DIRECTV, NBN Co y otros) se concentran en la segunda **[inferencia del grupo]**. Suponemos que esos acuerdos reflejan las prioridades del programa.

Leo es un negocio de Amazon dentro de Devices & Services. Lo dirige Rajeev Badyal, vicepresidente de Amazon Leo (#21). La FCC fija las reglas: autorizó 3.236 satélites en 2020 (#6), los redujo a 3.232 en 2024 (#7) y en 2026 concedió un waiver parcial del primer plazo (#8). Cuatro proveedores comparten los lanzamientos: ULA (Atlas V y Vulcan), Arianespace (Ariane 6), Blue Origin (New Glenn) y SpaceX (Falcon 9) **[dato real]**.

## 2.2 Cómo llegó hasta acá

| Etapa | Qué pasó |
|---|---|
| 2019–2020 | Presentaciones ante la FCC; la FCC autoriza el 30/07/2020 y Amazon compromete más de USD 10.000 millones (#42, #6, #39). |
| 2022–2024 | Contratos de lanzamiento que Amazon describe como los más grandes de la historia comercial; abre la fábrica de Kirkland (04/2024); la FCC ajusta la constelación a 3.232 (#4, #26, #7). |
| 2025 | Primera misión de producción, KA-01 (28/04/2025). En noviembre, Project Kuiper pasa a llamarse Amazon Leo (#2, #21). |
| 2026 | Amazon pide una prórroga (30/01) y la FCC concede un waiver parcial (05/06). El primer plazo no se cumple. En abril anuncia la compra de Globalstar (#8, #22). |
| 15/11/2026 | La misión LV-01 falla unos 10 minutos después del despegue y se pierden 40 satélites (#2, #11). |

## 2.3 Estado al 16/11/2026

| Indicador | Valor |
|---|---|
| Satélites lanzados | ≈ 396 de 3.232 (12,3%) **[inferencia del grupo]**, suma de #2 |
| Primer plazo (1.616 al 30/07/2026) | No cumplido: 24,5% **[inferencia del grupo]** |
| Plazo final | 3.232 al 30/07/2029 **[dato real]** (#8) |
| Misiones | 15: 14 con despliegue y 1 fallida **[dato real]** |
| Satélites fabricados | 1.000 a inicios de 09/2026 **[dato real]** (#3) |
| Servicio comercial | No lanzado; hay pruebas con empresas **[dato real]** |

**[inferencia del grupo]** El proyecto tiene la capacidad industrial montada (fábrica, instalaciones en Florida, más de 100 lanzamientos contratados), pero no consigue convertirla en satélites en órbita al ritmo que pide el regulador. El cuello de botella es el lanzamiento, y la falla del 15/11 lo agravó. Mientras tanto, Amazon amplía el programa (Gen2, conexión directa a teléfonos, Globalstar) antes de terminar la primera generación.

# 3. Evidencia y fuentes

## 3.1 Qué usamos

Reunimos 47 fuentes, consultadas el 15 y el 16/11/2026 (lista completa en el Anexo A). Unas 30 son comunicados oficiales de Amazon, que son declaraciones propias. Las más importantes son las regulatorias primarias: las órdenes FCC 20-102 (2020), DA 24-224 (2024) y DA 26-553 (2026), y un comunicado de la SEC (2026). Las demás son del proveedor ULA y prensa especializada, que usamos para ubicar y confirmar hechos pero nunca como única fuente de un dato duro. Wikipedia se usó solo para navegar y no se cita.

## 3.2 Cómo evaluamos

Priorizamos las fuentes primarias. Se consultó el texto original de las órdenes DA 24-224 y DA 26-553. Cuando dos fuentes se contradicen, lo registramos y no promediamos. Por ejemplo, la fecha del plazo final aparece como 20/07/2029 en una orden y como 30/07/2029 en otra; usamos la de 2026, que es la más reciente. Las cifras que cambian, como contratos y satélites, se citan siempre con fecha.

## 3.3 Qué no es público

| Dato | Cómo lo tratamos |
|---|---|
| Inversión total actualizada | Usamos el compromiso inicial de 2020 (más de USD 10.000 millones) como piso |
| Costo por satélite y por lanzamiento, monto de la fianza | No público; damos la estructura de costos sin montos |
| Cronograma interno, WBS, presupuesto | Los reconstruimos como propuesta de gestión (secciones 6 a 10) |
| Satélites operativos | Usamos lanzados como aproximación |
| Causa de la falla de LV-01 | No publicada; queda como tema abierto |

**[inferencia del grupo]** Lo que no es público define el trabajo. La parte investigable (plazos, contratos, regulación) es sólida y la económica es débil. Por eso ponemos el peso en el plazo y el alcance, que se pueden medir con evidencia, más que en el costo.

# 4. Actores e interesados

## 4.1 Quién es quién

| Grupo | Actores | Qué papel tienen |
|---|---|---|
| Dirección | Amazon (Devices & Services); vicepresidente de Amazon Leo (R. Badyal) | Financian, dirigen y deciden (#21, #22, #28) |
| Equipo visible | Negocio y producto (C. Weber), sistemas de lanzamiento (M. Wuerl), producción (S. Metayer), legal y regulatorio (D. Zapolsky) | Gestionan cada frente (#24, #3, #27, #33) |
| Regulador | FCC; reguladores de otros países (por ejemplo Kenia) | Autoriza, fija plazos y sanciones (#6, #7, #8, #18) |
| Lanzamientos | ULA, Arianespace, Blue Origin, SpaceX | Son el cuello de botella |
| Infraestructura pública | NASA, Space Force, Space Florida | Sitios y coordinación de lanzamiento (#27, #23) |
| Clientes y socios | JetBlue, Delta, Apple, DIRECTV, NBN Co, Herotel y otros; Globalstar (compra) | Demanda y distribución |
| Competidores | SpaceX (Starlink), OneWeb, Telesat | Se opusieron ante la FCC en 2019 (#45) |

**[inferencia del grupo]** SpaceX es competidor y proveedor a la vez: se opuso a Amazon ante la FCC en 2019 (#45) y hoy le vende lanzamientos (#38, #23). No encontramos acuerdos públicos que concilien las dos posiciones.

## 4.2 Poder e interés

**[propuesta de gestión]** Clasificamos a los interesados según su poder sobre el proyecto y su interés en el resultado, con la matriz poder/interés (un criterio externo a la cátedra, que usamos como complemento).

- **Gestionar de cerca** (poder e interés altos): la FCC, ULA y Blue Origin (66% de los lanzamientos que quedan) y la dirección de Amazon.
- **Mantener satisfechos** (poder alto, interés bajo): reguladores nacionales, NASA y Space Force.
- **Mantener informados** (poder bajo, interés alto): socios de distribución, aerolíneas y Apple.
- **Monitorear:** competidores y prensa.

El poder sale de la evidencia: la FCC puede reducir la autorización (#8 ¶12) y los lanzadores definen el ritmo (riesgo R-02).

## 4.3 Plan de comunicaciones básico

**[propuesta de gestión]** Usa los instrumentos de seguimiento de la Clase 6.

| Interesado | Qué necesita saber | Cómo y cada cuánto |
|---|---|---|
| FCC | Avance contra los plazos, certificación del 50% | Reportes formales, por plazo |
| Lanzadores | Manifiesto y fechas de retorno al vuelo | Reunión de avance, mensual y por misión |
| Dirección de Amazon | Valor ganado, riesgos rojos, temas abiertos | Informe de situación, mensual |
| Socios | Fecha y criterio de inicio del servicio | Comunicación con margen, trimestral |
| Equipo interno | Avance y problemas | Reunión semanal |

**[inferencia del grupo]** Las promesas de inicio del servicio que se fueron corriendo (sección 8) muestran un problema de gestión de expectativas. La Clase 2 advierte que un proyecto bien administrado puede fracasar si no cumple las expectativas iniciales. Por eso el plan propone comunicar fechas con margen y con un criterio de inicio verificable.

# 5. Caso de negocio (reconstruido)

**[propuesta de gestión]** con base en datos reales. Seguimos la plantilla de la cátedra.

## 5.1 Resumen

Amazon quiere entrar al mercado de banda ancha satelital en órbita baja para llevar conectividad donde no llegan las redes actuales y abrir negocios nuevos: empresas, aviación, operadores y teléfonos. Eligió una integración vertical, con fabricación, terminales y operación propias (#22), y lanzamiento tercerizado en cuatro proveedores. El caso sigue siendo deseable, porque los acuerdos comerciales crecen, pero su viabilidad en plazo está comprometida: al ritmo actual no se llega al plazo de 2029.

## 5.2 El problema

**[dato real]** Amazon lo plantea como un problema de acceso: miles de millones de personas sin internet de alta velocidad (#28).

**[inferencia del grupo]** Para Amazon también es estratégico. Sin red propia depende de terceros para conectar dispositivos, clientes empresariales y la nube. El proyecto crea un negocio nuevo dentro de Devices & Services, con procesos que la empresa no tenía, como fabricar equipo aeroespacial en serie y operar lanzamientos. Suponemos que la integración con AWS y con los dispositivos es parte de la motivación, aunque Amazon no la presenta como problema.

## 5.3 Objetivos, premisas y restricciones

| Objetivo | Indicador de éxito |
|---|---|
| Cumplir la autorización de la FCC | 3.232 satélites operativos al 30/07/2029 (#8) **[dato real]** |
| Iniciar el servicio comercial | Criterio a definir y comunicar con margen **[propuesta de gestión]** |
| Aprovechar los acuerdos firmados | JetBlue en 2027, Delta en 2028, servicio directo a teléfonos en 2028 (#36, #31, #22) **[dato real]** |
| Ingresos y suscriptores | No público |

Premisas **[propuesta de gestión]**: los contratos de lanzamiento siguen vigentes, la fábrica alcanza su capacidad declarada y la demanda se sostiene. Restricciones **[dato real]**: los plazos de la FCC y la pérdida de la fianza si no se cumplen (#8 ¶3, ¶12, ¶18), la prohibición de desplegar directo a la órbita operativa (#7 ¶43) y la capacidad de lanzamiento de terceros.

Amazon no publica un plan estratégico de Leo. La alineación con Devices & Services, AWS y el mercado empresarial es una lectura del grupo sobre declaraciones verificables (#22, #34, #4, #29).

## 5.4 Costos y beneficios

Los costos con fuente son pocos **[dato real]**: el compromiso inicial de más de USD 10.000 millones (#39), más de USD 140 millones en la instalación de procesamiento de Kennedy Space Center (#27), más de USD 200 millones en instalaciones de Cabo Cañaveral (#23) y un costo de fabricación esperado de menos de USD 400 por terminal (#30). Los lanzamientos (unos 108 contratados) y la fianza no tienen monto público.

Los beneficios son cualitativos **[inferencia del grupo]**: ingresos por servicio a empresas, aviación (500 aviones de Delta desde 2028, #31) y operadores, sinergias con AWS y una posición en un mercado con pocos operadores de órbita baja. Sin ingresos ni costo total públicos, el análisis solo puede ser cualitativo. Lo relevante para la gestión es que los costos ya comprometidos son altos y en gran parte fijos, mientras que los beneficios dependen de iniciar un servicio que se corrió unos dos años.

## 5.5 Alternativas

**[propuesta de gestión]** Descartamos cuatro alternativas:

- **No entrar al mercado:** dejaría a Amazon dependiendo de terceros, y los competidores ya se movían (#45).
- **Comprar capacidad a un operador existente:** menos control y menos margen. Amazon eligió diseñar, fabricar y operar por su cuenta (#22).
- **Una constelación más chica:** reduciría la cobertura prometida. Amazon rechazó resignar satélites ante la FCC (#8 ¶8, ¶11).
- **Solo conexión directa a teléfonos:** no cubre banda ancha fija ni empresas. Amazon lo suma desde 2028 como línea adicional (#34).

Se eligió la constelación propia con lanzamiento diversificado: da control de la cadena y reparte el riesgo de lanzamiento, a cambio de un plazo exigente.

## 5.6 Actualización 2026

**[inferencia del grupo]** La cátedra dice que el caso de negocio no es estático. Al corte conviene reevaluarlo: el plazo de 2029 no es alcanzable, el inicio del servicio se corrió unos dos años y el alcance creció. Recomendamos separar el caso de la primera generación (cumplir la autorización e iniciar el servicio) del de las líneas nuevas, para no justificar el atraso de uno con el potencial del otro.

# 6. Acta de Constitución (reconstruida)

**[propuesta de gestión]** Proponemos reconstruir el acta al **30/07/2020**, el día en que la FCC autorizó la constelación y Amazon anunció la inversión (#6, #39). Es el momento en que el proyecto queda formalmente habilitado. En ese momento se llamaba Project Kuiper.

## 6.1 Qué sabemos y qué suponemos

Es explícito en la evidencia **[dato real]**: los 3.236 satélites autorizados (#6), los plazos del 50% al 30/07/2026 y del 100% al 30/07/2029 (#7, #8), la inversión de más de USD 10.000 millones y el propósito declarado (#39). No se conoce el presupuesto detallado, el organigrama de 2020, el cronograma interno ni el costo de los lanzamientos. Suponemos que el vicepresidente del programa actúa como gerente, que los lanzamientos se contratan a terceros y que la fabricación es propia **[propuesta de gestión]**.

## 6.2 El acta

| Campo | Contenido |
|---|---|
| Proyecto | Project Kuiper: despliegue de la constelación de primera generación (desde el 13/11/2025, Amazon Leo) |
| Objetivo | Desplegar y operar 3.236 satélites (3.232 desde 2024) con su red terrestre y sus terminales, cumpliendo el 50% al 30/07/2026 y el 100% al 30/07/2029, y habilitar el servicio comercial de banda ancha |
| Propósito | Servicio de banda ancha confiable y accesible para comunidades sin servicio (#39), y una oportunidad de negocio |
| Producto | Constelación a 590, 610 y 630 km de altura, estaciones terrestres y fibra, y terminales de bajo costo (#6, #28, #30) |
| Criterios de éxito | (1) 1.616 satélites operativos al 30/07/2026; (2) 3.232 al 30/07/2029; (3) servicio comercial con criterio verificable: cobertura mínima por región, satélites operativos mínimos y primeros clientes pagos. El (3) es propuesta del grupo |
| Entregables | Satélites fabricados, instalaciones de procesamiento, campañas de lanzamiento, constelación operativa, segmento terrestre, terminales y servicio habilitado |
| Requisitos | Cumplir las condiciones de la FCC (desechos orbitales, no desplegar directo a la órbita operativa, #7 ¶43); terminales de menos de USD 400 (#30) |
| Equipo y gerente | Roles visibles: sistemas de lanzamiento, producción, legal y regulatorio, negocio y producto (#3, #24, #27, #33). Gerente: el vicepresidente a cargo (en 2025, R. Badyal, #21) |
| Autoridad del gerente | Asignar presupuesto dentro de la línea base, contratar lanzamientos dentro del marco aprobado, priorizar el manifiesto y escalar a la dirección los cambios de alcance y los pedidos a la FCC **[propuesta de gestión]** |
| Plazo | 30/07/2020 a 30/07/2029 (9 años), con un plazo intermedio el 30/07/2026 |
| Presupuesto | Compromiso de más de USD 10.000 millones (#39); el detalle no es público |
| Restricciones | Plazos de la FCC con sanción (reducción de la autorización y pérdida de la fianza), dependencia de lanzadores de terceros y coordinación de espectro (#8) |
| Riesgos iniciales | Confiabilidad de lanzadores nuevos, atraso regulatorio, oposición de competidores y escalado de la fabricación. Se materializaron en 2025–2026 **[inferencia del grupo]** |
| Sponsor | Dirección de Amazon (en 2020 anunció el proyecto Dave Limp, vicepresidente senior, #39) |
| Aprobación | Reconstrucción académica, sin firmas |

## 6.3 Revisión con el checklist de la cátedra

El acta explica el porqué, define qué se autoriza, distingue hechos de supuestos, identifica responsables, incluye límites y no se convierte en el plan (la WBS, el cronograma y los costos van en las secciones 7 a 10).

**[inferencia del grupo]** El criterio de éxito (3) no existía en forma pública. Eso explica que el inicio del servicio pudiera correrse cuatro veces sin que se incumpliera un plazo formal. Con ese campo, el riesgo R-03 tendría un disparador verificable.

# 7. Alcance y WBS

## 7.1 Declaración del alcance

**[propuesta de gestión]** con base en datos reales.

- **Producto:** un sistema de banda ancha satelital en órbita baja. Incluye la constelación de primera generación (3.232 satélites, #7), la red terrestre (#17, #28) y los terminales Nano, Pro y Ultra (#29, #30).
- **Proyecto:** fabricar, procesar, lanzar y poner en operación los 3.232 satélites, desplegar el segmento terrestre, producir terminales, habilitar el servicio comercial y cumplir las obligaciones de la FCC.
- **Criterios de aceptación:** satélites "deployed and operating" (#8 ¶3), 3.232 al 30/07/2029 y servicio comercial según el criterio del acta.
- **Quedan afuera:** Gen2 (3.212 satélites), el sistema Polar (1.292) (#8 ¶3), el servicio directo a teléfonos (hasta 5.105 satélites desde 2028, #34), la integración de Globalstar (#22) y la operación comercial posterior al inicio del servicio.
- **Supuestos:** los contratos de lanzamiento siguen vigentes, la capacidad de fábrica declarada es alcanzable y lanzados es aproximadamente operativos.

Dejamos afuera las líneas nuevas porque Amazon Leo es un programa y el despliegue de la primera generación es el proyecto con línea base pública (Paneo, tema 2). Las líneas nuevas se detallarán cuando haya información, con elaboración progresiva (*rolling wave*, Clase 2). Así el alcance es medible y coincide con el horizonte de riesgos (30/07/2029) y con el total del valor ganado (3.232).

## 7.2 WBS

**[propuesta de gestión]** Ordenamos la WBS por el flujo físico del despliegue. Estos son sus nueve paquetes principales:

1. **Gestión del proyecto:** acta, plan y seguimiento.
2. **Cumplimiento regulatorio:** autorizaciones de la FCC, gestión de plazos (aviso, waiver, certificación del 50%), plan de desechos orbitales y licencias por país.
3. **Satélites:** diseño y prototipos, planta de Kirkland y lotes fabricados.
4. **Procesamiento e integración:** instalaciones de Kennedy Space Center y Cabo Cañaveral, e integración de la carga por misión.
5. **Lanzamientos:** una campaña por cohete (Atlas V, Vulcan, Ariane 6, New Glenn y Falcon 9).
6. **Constelación en órbita:** elevación a órbita operativa y centro de operaciones.
7. **Segmento terrestre:** estaciones, puntos de presencia e integración con AWS, y fibra.
8. **Terminales de usuario:** Nano, Pro y Ultra.
9. **Servicio habilitado:** preview empresarial, inicio comercial según el acta y socios de distribución.

Lo que no tiene fuente pública, como los prototipos y el centro de operaciones, está marcado como reconstrucción.

## 7.3 Cómo se conectan fabricación, lanzamiento y operación

**[inferencia del grupo]** La WBS es una cadena en serie con un cuello de botella claro: el lanzamiento.

| Eslabón | Capacidad o ritmo | Fuente |
|---|---|---|
| Fabricación | Hasta 30 satélites por semana (≈ 130 por mes); 1.000 fabricados a inicios de 09/2026 | #23, #3 |
| Procesamiento | En Kennedy Space Center, más de 100 satélites por mes y tres campañas a la vez | #27 |
| Lanzamiento | ≈ 21 satélites por mes desplegados (promedio de 04/2025 a 11/2026) | Anexo C |
| Operación | Haría falta ≈ 87 por mes para llegar al plazo final | Anexo C |

Amazon mismo dice que ajusta la producción a la disponibilidad de lanzadores (#23). La diferencia entre fabricados (1.000) y lanzados (396) no la presentamos como stock confirmado: puede incluir satélites en pruebas o descartados. Para la gestión, el control tiene que concentrarse en los lanzamientos (manifiesto, proveedores y retorno al vuelo) y no en la fábrica. Eso es la base del riesgo R-02 y de la oportunidad OP-1.

# 8. Cronograma maestro

## 8.1 Plazos y hitos

| Hito | Fecha | Estado al 16/11/2026 |
|---|---|---|
| Autorización de la FCC (3.236 satélites) | 30/07/2020 | Cumplido (#6, #39) |
| Fábrica de Kirkland operativa | 04/2024 | Cumplido (#26) |
| Modificación de la FCC (3.232 satélites) | 08/03/2024 | Cumplido (#7) |
| Primera misión de producción, KA-01 | 28/04/2025 | Cumplido (#2) |
| Instalación de Kennedy Space Center operativa | 24/07/2025 | Cumplido (#27) |
| Preview empresarial | 24/11/2025 | Cumplido (#29) |
| **Plazo del 50%: 1.616 operativos** | 30/07/2026 | **No cumplido** (396) (#8) |
| Aviso de cumplimiento a la FCC | 14/08/2026 | No encontrado (#7 ¶53) |
| Primer vuelo de Vulcan para Leo | 15/11/2026 | **Fallido** (tema T-01) (#2, #11) |
| Inicio del servicio comercial | "later this year" (2026) | Pendiente, sin criterio público (#3) |
| Certificación del 50% construido (acorta la pérdida de espectro) | 30/10/2027 | Futuro (#8 ¶15) |
| Fin de la pérdida de prioridad de espectro | 30/03/2028 | Futuro (#8 ¶15) |
| **Plazo final: 3.232 operativos** | 30/07/2029 | En riesgo (R-04) (#8 ¶3) |

El inicio del servicio se fue corriendo: primeros clientes "later that year" en 2023 (#30), servicio "next year" en 2024 (#26), "broader rollout next year" en 2025 (#29) y "later this year" el 09/11/2026 (#3). Cada promesa corrió el inicio cerca de un año **[inferencia del grupo]**.

## 8.2 Cada misión es un punto de control

**[propuesta de gestión]** La Clase 3 dice que los *inch-pebbles* dividen el avance en puntos más chicos para detectar desvíos a tiempo. Acá la unidad natural es la misión: se sabe el día, el cohete y la cantidad de satélites (#2). Controlamos por trimestre.

| Trimestre | Misiones | Satélites | Acumulado |
|---|---|---|---|
| 2T 2025 | 2 | 54 | 54 |
| 3T 2025 | 3 | 75 | 129 |
| 4T 2025 | 2 | 51 | 180 |
| 1T 2026 | 1 | 32 | 212 |
| 2T 2026 | 5 | 155 | 367 |
| 3T 2026 | 1 | 29 | 396 |
| 4T 2026 (al 16/11) | 1 (fallida) | 0 | 396 |

Para llegar a 3.232 el 30/07/2029 hacen falta unos 262 satélites por trimestre (87 por mes) **[inferencia del grupo]**. El mejor trimestre real fue el 2T 2026, con 155.

## 8.3 Secuencia y dependencias

**[propuesta de gestión]** La secuencia es en serie: fabricar el lote, procesarlo e integrar la carga, lanzar la misión y elevar los satélites a su órbita operativa (no se despliega directo, #7 ¶43). El lanzamiento depende de un recurso externo, el cohete del proveedor. Las estaciones terrestres se instalan en paralelo y dependen de las licencias por país. El servicio inicia en cada región cuando están listos satélites, estaciones y terminales, según el criterio del acta.

## 8.4 Cuando el plazo manda: acortar, nivelar y la zona inalcanzable

**[inferencia del grupo]** Según la Clase 3, si el plazo es fijo se puede acortar (más recursos en paralelo) o nivelar (ajustar al recurso escaso), y existe una zona inalcanzable donde ningún acortamiento razonable cumple la fecha. Aplicado a Amazon Leo:

- **Acortar:** sumar lanzadores (Ariane 6 pasó de 18 a 24 lanzamientos y se contrataron 10 Falcon 9 más, #24, #23). Es la oportunidad OP-1.
- **Nivelar:** Amazon ajusta la fábrica a los lanzadores disponibles (#23). La fábrica no es el recurso escaso.
- **Zona inalcanzable:** hacen falta unas 35 misiones por año. El plan de Amazon es de 20 y el ritmo observado, de unas 11. El Monte Carlo y el PERT dan casi 0% de llegar a tiempo. Con los recursos contratados, el plazo de 2029 está en la zona inalcanzable.

## 8.5 Dos líneas base y una reserva

**[propuesta de gestión]** Proponemos dos líneas base. La **A (regulatoria)** es la que fija la FCC: 1.616 al 30/07/2026 y 3.232 al 30/07/2029. Es una restricción y sirve para medir el valor ganado. La **R (recuperación)** sostiene el plan declarado de Amazon, 20 misiones por año con 30 satélites cada una, es decir 50 satélites por mes. Termina hacia **08/2031**. No cumple 2029, pero es el compromiso más exigente que tiene respaldo en una declaración de la empresa (#23), y presentarlo con evidencia de avance mejora las chances de un nuevo alivio.

Sumamos una reserva de unos 4 meses por el riesgo R-02 (un lanzador en tierra), lo que lleva el fin a **≈ 12/2031**. La contamos una sola vez: el atraso de los riesgos R-03 y R-04 es el mismo atraso visto desde otro lado.

# 9. Estimaciones

## 9.1 Qué se estima y cómo

| Variable | Método (Clase 4) | Por qué |
|---|---|---|
| Satélites por misión | Análoga: misiones ya voladas por cohete (24 en Falcon 9, 27–29 en Atlas V, 32–36 en Ariane 64, 40 en Vulcan) | Hay historia real por vehículo (#2, #3) |
| Ritmo de lanzamiento | Tres valores (PERT) | Hay mucha incertidumbre: fallas, retornos al vuelo y cohetes nuevos |
| Duración del despliegue restante | Paramétrica (satélites que faltan ÷ ritmo) y PERT | Hay una relación cuantitativa directa |
| Producción | Dato declarado | No es el cuello de botella |

## 9.2 Estimación PERT

**[propuesta de gestión]** Estimamos cuánto tardaría en desplegarse lo que falta (2.836 satélites), con 30 satélites por misión. Usamos los mismos tres valores que el Monte Carlo de la sección 11, para que las dos herramientas sean coherentes.

| Valor | Ritmo | Duración | Fin |
|---|---|---|---|
| Optimista | 2,0 misiones por mes (24 por año), por encima del plan "20+" de Amazon | 47,3 meses | ≈ 10/2030 |
| Más probable | 0,92 por mes (≈ 11 por año), el ritmo observado desde el 28/04/2026 | 102,8 meses | ≈ 06/2035 |
| Pesimista | 0,5 por mes (6 por año), con lanzadores clave en tierra buena parte del período | 189,1 meses | ≈ 08/2042 |

**[inferencia del grupo]** El tiempo esperado es de 107,9 meses, es decir hasta ≈ 11/2035, con un desvío de 23,6 meses. Hasta el 30/07/2029 quedan 32,4 meses, así que la probabilidad de terminar a tiempo es de ≈ 0,07% (aproximación normal). Es un número pequeño que depende de los tres valores que elegimos nosotros.

## 9.3 Tres herramientas, una conclusión

| Herramienta | Resultado | Por qué difiere |
|---|---|---|
| Monte Carlo (sección 11) | Mediana de ≈ 1.513 satélites al 30/07/2029; llegar a 3.232, ≈ 0% | Distribución triangular sobre el ritmo |
| PERT (esta sección) | Fin ≈ 11/2035; ≈ 0,07% | Los casos pesimistas pesan más, porque la duración es inversa al ritmo |
| Valor ganado (sección 12) | Fin ≈ 2031 (plan) o ≈ 2038 (ritmo observado) | Proyección lineal de un solo escenario |

**[inferencia del grupo]** Con supuestos distintos, las tres llegan a lo mismo: el plazo de 2029 no se cumple con la capacidad contratada. El fin razonable está entre 2031 y 2038.

## 9.4 Cuándo reestimar y qué sesgos hay

**[propuesta de gestión]** Proponemos reestimar al volver a volar Vulcan (cierre del tema T-01), al primer vuelo de New Glenn para Leo y cada trimestre con los puntos de control de la sección 8.

**[inferencia del grupo]** Hay dos sesgos visibles. Uno es el optimismo de la fuente: la capacidad de 30 por semana, las "20+ misiones" y los "≈ 700 al 30/07/2026" son declaraciones de Amazon, y lo proyectado ante la FCC terminó en 396. El otro es confundir capacidad instalada con ritmo efectivo. Por eso el valor más probable salió del ritmo observado y no del plan.

# 10. Costos y presupuesto

Amazon no publica su presupuesto ni sus costos unitarios. Esta sección reconstruye la estructura y el método de la gestión de costos. Solo usamos montos con fuente, y donde no hay, decimos "No público". No inventamos cifras.

## 10.1 Lo que sí es público

| Concepto | Monto |
|---|---|
| Compromiso de inversión inicial (30/07/2020) | Más de USD 10.000 millones (#39) |
| Inversión total actualizada (14/04/2026) | "Multibillion-dollar", sin cifra (#5) |
| Instalación de procesamiento en Kennedy Space Center | Más de USD 140 millones (#27) |
| Instalaciones en Cabo Cañaveral | Más de USD 200 millones (#23) |
| Terminal estándar (costo de fabricación esperado) | Menos de USD 400 por unidad (#30) |
| Lanzamientos, costo por satélite, monto de la fianza | No público |

**[inferencia del grupo]** Las dos inversiones en Florida suman más de USD 340 millones, alrededor del 3,4% del compromiso inicial. Suponemos que ya están dentro de ese compromiso y que no son adicionales, aunque no se sabe.

## 10.2 Estructura por elementos de la WBS

**[propuesta de gestión]** Clasificar los costos es posible aunque falten los montos, y eso es lo que defendemos. La planta de satélites, las instalaciones y la gestión son costos **fijos**. Los satélites, los lanzamientos, las estaciones terrestres y las terminales son **variables**, porque dependen de la cantidad. Estimaríamos los variables con el método paramétrico: costo unitario por 3.232 satélites, precio por misión por unos 108 lanzamientos y costo por estación por más de 300. Hoy esos montos son "No público".

**[inferencia del grupo]** Lo que más pesa en el total es variable por unidad. Por eso perder una misión cuesta dos veces (los 40 satélites y el lanzamiento), y por eso acelerar el ritmo no abarata: adelanta costos variables. Los fijos ya están pagados. Suponemos que los satélites y los lanzamientos dominan el total, como pasa en constelaciones comparables, pero es un supuesto sin cifra.

## 10.3 Presupuesto, reservas y control

**[propuesta de gestión]** Seguimos la estructura de la Clase 5: los costos estimados más la reserva de contingencia forman la línea base de costos, y con la reserva gerencial se llega al presupuesto total. Con los datos públicos solo se puede decir que los costos estimados son de al menos USD 10.000 millones. La contingencia se compondría de reponer 40 satélites, la fianza y los lanzamientos adicionales de recuperación. Todo lo demás es "No calculable". La reserva gerencial la fija el sponsor.

Sin costo real, el CPI no se puede calcular. Tampoco el índice de riesgo ni el apalancamiento de la sección 11, porque no hay costo total ni costo de las respuestas. Si se usaran los USD 10.000 millones como costo total, habría que expresar las exposiciones en dólares, y esos impactos tampoco son públicos.

**[inferencia del grupo]** Lo que sí se puede seguir con datos públicos son señales de costo: inversiones nuevas (Kennedy Space Center, Cabo Cañaveral), contratos adicionales de lanzamiento (Ariane 6 con 6 más y Falcon 9 con 10 más) y eventos de costo no planificado (la pérdida de LV-01). Todas apuntan a un costo que crece con un avance lento. Es la situación que la Clase 6 llama "mucho gasto con poco trabajo realizado", aunque aquí solo se puede afirmar de forma cualitativa.

# 11. Gestión de riesgos

## 11.1 Qué hicimos y qué encontramos

Reconstruimos cómo podrían gestionarse los riesgos del despliegue con el método de la Clase 10: planificar, identificar, analizar de forma cualitativa y cuantitativa, planificar las respuestas y supervisar. Elegimos el **plazo** como objetivo a proteger primero, porque la FCC fijó plazos con consecuencias concretas sobre el espectro, la fianza y la cantidad de satélites autorizados.

El registro tiene cuatro riesgos desarrollados, tres en seguimiento y dos oportunidades. Uno ya ocurrió: la pérdida de 40 satélites del 15/11/2026 (R-01). Dos están en rojo: que la FCC no conceda otro alivio del plazo de 2029 (exposición 0,28) y que un lanzador clave quede en tierra (0,20). Se encadenan: un lanzador en tierra frena el ritmo, eso retrasa el servicio y agranda la brecha con el plazo final, y Amazon queda dependiendo del regulador.

Con el ritmo observado o con el plan de Amazon, llegar a 3.232 satélites antes del 30/07/2029 es prácticamente imposible. Por eso no llegar es una condición prevista y no un riesgo, y el riesgo principal es si la FCC concede otro alivio.

## 11.2 Planificación

**Por qué el plazo.** El regulador fija tres consecuencias con fecha **[dato real]** (DA 26-553): sin 1.616 satélites operativos el 30/07/2026, Amazon pierde prioridad de espectro hasta el 30/03/2028 (¶15) y pierde la fianza (¶18); y sin 3.232 el 30/07/2029, le reducen la autorización a los satélites operativos ese día (¶12). **[propuesta de gestión]** Por eso el plazo arrastra a los demás objetivos, que ordenamos así: plazo, alcance, calidad y costo. Con el costo hay una inferencia: Amazon parece sacrificarlo primero, porque sigue ampliando lanzamientos pese al atraso (Ariane 6 de 18 a 24, #24; 10 Falcon 9 más, #23), aunque atribuye esa ampliación a su confianza en el Ariane 6.

**Apetito al riesgo.** Amazon aceptó incumplir el primer plazo, lanzó el mayor lote hasta la fecha y diversifica los lanzadores **[dato real]**. Lo leemos como una **búsqueda de riesgo moderada** **[inferencia del grupo]**; ninguna fuente declara el apetito de Amazon, es una lectura de su conducta.

**Escalas y umbrales** **[propuesta de gestión]**. Usamos las escalas de la cátedra (probabilidad de 0,10 a 0,90 e impacto de 0,05 a 0,80). La cátedra no fija los colores; los elegimos nosotros: rojo si la exposición es de 0,20 o más, amarillo de 0,10 a 0,19, verde de 0,05 a 0,09 y azul por debajo de 0,05.

## 11.3 Identificación

De una lista inicial de 12 amenazas y 3 oportunidades, fusionamos las que comparten causa y evento y descartamos una inferencia débil. Quedó:

| ID | Riesgo | Tratamiento |
|---|---|---|
| R-01 | Pérdida de satélites por falla de un lanzador (recurrencia; ocurrió el 15/11/2026 y pasó a ser el tema T-01) | Desarrollado |
| R-02 | Un lanzador clave en tierra, con el manifiesto concentrado | Desarrollado |
| R-03 | Desvío del cronograma y del inicio del servicio | Desarrollado |
| R-04 | Que la FCC no conceda un nuevo alivio del plazo de 2029 | Desarrollado |
| R-05 | Pérdida temporal de prioridad de espectro | Seguimiento |
| R-06 | Dependencia de socios locales | Seguimiento |
| R-07 | Aprobaciones regulatorias externas | Seguimiento |
| OP-1 | Más capacidad de lanzamiento, diversificada | Oportunidad |
| OP-2 | Demanda comercial (aerolíneas y servicio a teléfonos) | Solo mencionada |

## 11.4 Cuentas de base

La FCC mide los plazos en satélites "deployed and operating" (¶3), pero Amazon solo informa lanzados ("nearly 400", #2) **[dato real]**. Usamos los **lanzados (≈ 396) como aproximación**; si algún satélite no opera, la brecha real es mayor, así que nuestros resultados son optimistas **[inferencia del grupo]**. Quedan ≈ 93 lanzamientos (21 Ariane 6, 10 Falcon 9, 1 Atlas V, 37 Vulcan y 24 New Glenn), y 61 de ellos, ≈ 66%, dependen de Vulcan y New Glenn. Faltan 2.836 satélites en ≈ 32,5 meses.

## 11.5 Los riesgos desarrollados

### R-04: que la FCC no conceda un nuevo alivio del plazo de 2029

**Por qué lo reformulamos.** Primero lo habíamos escrito como "no cumplir el plazo de 2029". Pero el análisis cuantitativo (11.8) da una probabilidad de no llegar de casi 100%, y un evento casi seguro no es un riesgo: es una condición prevista. Lo incierto es la respuesta del regulador. Si la FCC no da otro alivio, Amazon llegaría al 30/07/2029 con unos 1.500 a 2.000 satélites, le reducen la autorización a los operativos y se expone la fianza (¶3, ¶12, ¶18) **[dato real]**.

**Probabilidad: 0,70** **[propuesta de gestión]**. Es la probabilidad de que la FCC **no** conceda otro alivio, es decir, suponemos un 30% de chances de que sí. A favor: la FCC ya dio un waiver parcial en 2026 (¶11). En contra: fue parcial y dejó intactos el plazo de 2029 y la fianza (¶11, ¶18), y la brecha es grande (hacen falta ≈ 35 misiones por año, el plan es de 20 y lo observado, de ≈ 11). Ningún dato permite predecir a la FCC: el 30% es un juicio del grupo basado en el único precedente. Con cualquier probabilidad de 0,50 o más, el riesgo seguiría en rojo.

**Impacto: 0,40 (alto).** Quedar en ≈ 2.050 satélites significaría perder unos 1.180 autorizados (≈ 37%), que en la escala de alcance es "inaceptable". Amazon pidió un waiver en vez de resignar satélites (¶8, ¶11), de donde inferimos que no vería aceptable una constelación parcial.

**Exposición: 0,70 × 0,40 = 0,28 (rojo).**

**Respuesta (mitigar).** Evitar implicaría resignar alcance, y transferir no aplica a un plazo regulatorio. Proponemos presentar a tiempo un nuevo pedido de extensión o waiver con evidencia de avance (la respuesta principal), acelerar el ritmo aunque no alcance, porque achica la brecha y fortalece el pedido, e informar a la FCC la capacidad construida y los lanzamientos contratados. Responsable propuesto: el director legal de Amazon (#33). Disparadores: un ritmo de 6 meses por debajo del necesario, un nuevo atraso de un lanzador o un cambio de política de la FCC.

**Después de responder: 0,50 × 0,40 = 0,20, sigue en rojo.** Un pedido bien fundado mejora las chances, pero decide el regulador y la brecha de ritmo sigue siendo grande.

### R-02 y R-03: el lanzador en tierra y el desvío del servicio

| | R-02: lanzador clave en tierra | R-03: desvío del cronograma y del servicio |
|---|---|---|
| Qué pasaría | Vulcan o New Glenn quedan fuera de servicio seis meses o más y el ritmo se frena | El inicio del servicio se posterga una vez más y se demoran ingresos y acuerdos |
| Probabilidad | 0,50 | 0,70 |
| Impacto | 0,40 (alto) | 0,20 (moderado) |
| Exposición | **0,20, rojo** (justo en el corte) | **0,14, amarillo** |
| Respuesta (mitigar) | Priorizar Ariane 6 y Falcon 9, pedir fechas de retorno al vuelo a ULA y Blue Origin, evaluar más contratos | Iniciar el servicio por regiones, definir un criterio de inicio y comunicar fechas con margen |
| Responsable | Sistemas de lanzamiento (#3) | Negocio y producto (#24) |
| Después de responder | 0,50 × 0,20 = **0,10, amarillo** | 0,70 × 0,10 = **0,07, verde** |

**R-02.** Vulcan y New Glenn concentran ≈ 66% de lo que queda por lanzar. Vulcan estuvo unos 9 meses en tierra antes de LV-01 (#12), y New Glenn explotó en su plataforma el 28/05/2026 (#47) y todavía no voló para Leo **[dato real]**. Seis meses fuera de servicio de ≈ 66% de la capacidad equivalen a ≈ 4 meses de ritmo total, alrededor del 12% del horizonte, que la escala de plazo califica como alto. Con una probabilidad de 0,40 pasaría a amarillo. Reservamos unos 4 meses en el cronograma.

**R-03.** Amazon tiene ≈ 396 satélites contra ≈ 700 proyectados al 30/07/2026 (¶8), y el inicio del servicio se corrió cuatro veces (sección 8). El impacto es moderado porque cada postergación previa fue de ≈ 1 año, ≈ 10% de un horizonte de ≈ 10 años, y otra podría ser menor.

### R-01: pérdida de satélites por falla de un lanzador (recurrencia)

El 15/11/2026 la misión LV-01 falló y se perdieron 40 satélites (#2, #11). Lo ocurrido pasó a ser un **tema** (un problema a resolver, T-01, sección 11.10). La ficha mide ahora la **recurrencia**: que vuelva a pasar en las 37 misiones Vulcan que quedan.

**Probabilidad: 0,30 por misión** **[propuesta de gestión]**. La frecuencia observada es 0,20 (1 en 5 vuelos, #11), pero la muestra es muy chica y, sin causa raíz, la incertidumbre técnica sigue.

**Impacto: 0,10 (bajo).** Los 40 satélites son el 1,2% de los 3.232, y reponerlos equivale a ≈ 1,3 semanas de la capacidad de fábrica, contra ≈ 140 semanas hasta el plazo. El costo de un satélite no es público y suponemos la franja baja.

**Exposición: 0,30 × 0,10 = 0,03 (azul).** Está en azul aunque ya ocurrió porque el mayor daño, el cohete en tierra, se mide en R-02, y sumarlo acá sería contarlo dos veces. El punto débil que el grupo tiene que poder defender es el costo: con un costo unitario alto el impacto subiría a moderado y R-01 pasaría a verde (0,06).

**Respuesta (aceptar de forma activa).** Con exposición muy baja la cátedra indica aceptar. Elegimos la forma activa porque el riesgo ya ocurrió y hay disparadores concretos: una anomalía en un vuelo Vulcan o que ULA no publique la causa antes del siguiente vuelo. El plan de contingencia es reponer los 40 satélites con producción de Kirkland, reasignar misiones a otros lanzadores y pedirle a ULA su investigación.

## 11.6 Riesgos menores y oportunidades

Los tres riesgos de severidad baja se vigilan sin respuesta completa; si se activa un disparador, pasan al registro. Los valores tienen poca evidencia dura.

| ID | Riesgo | P × I = ER | Qué se vigila |
|---|---|---|---|
| R-05 | Pérdida temporal de prioridad de espectro hasta el 30/03/2028 (¶15) | 0,30 × 0,20 = 0,06 (verde) | Una ronda nueva de la FCC; certificar el 50% construido antes del 30/10/2027 |
| R-06 | Dependencia de socios locales | 0,50 × 0,10 = 0,05 (verde) | Que un socio no confirme fecha |
| R-07 | Aprobaciones externas: compra de Globalstar y licencias por país | 0,30 × 0,20 = 0,06 (verde) | Pedidos de información de un regulador |

**OP-1, más capacidad de lanzamiento:** Amazon sumó 6 lanzamientos de Ariane 6 (#24) y 10 de Falcon 9 (#23), lo que permitiría sostener el ritmo aunque Vulcan o New Glenn estén en tierra. Es la respuesta de mitigación de R-02. **OP-2, demanda comercial:** hay acuerdos con JetBlue, Delta, Apple y Globalstar, pero no la desarrollamos porque no hay datos de ingresos.

## 11.7 Matriz de probabilidad e impacto

| Probabilidad / Impacto | 0,05 | 0,10 | 0,20 | 0,40 | 0,80 |
|---|---|---|---|---|---|
| 0,90 | verde | verde | amarillo | rojo | rojo |
| 0,70 | azul | verde | **R-03** 0,14 amarillo | **R-04** 0,28 rojo | rojo |
| 0,50 | azul | **R-06** 0,05 verde | amarillo | **R-02** 0,20 rojo | rojo |
| 0,30 | azul | **R-01** 0,03 azul | **R-05, R-07** 0,06 verde | amarillo | rojo |
| 0,10 | azul | azul | azul | azul | verde |

**[inferencia del grupo]** El riesgo se concentra en la regulación (suma de exposiciones externas: 0,40) y en los proveedores y el cronograma (0,34), no en lo técnico (0,03) ni en la organización (0,05). Es coherente con el objetivo elegido.

## 11.8 Análisis cuantitativo: Monte Carlo

Amazon no publica su red de actividades, así que no se puede simular su cronograma interno. Con datos públicos sí se puede simular **cuántos satélites habría el 30/07/2029**, que es la medida del plazo de R-04. Simulamos 100.000 futuros posibles (el código está en el Anexo D) a partir de 396 satélites lanzados y 32,5 meses de horizonte **[dato real]**.

**Supuestos** **[propuesta de gestión]**: el ritmo va de 0,5 misiones por mes (lanzadores clave en tierra buena parte del período) a 2,0 (el plan de "20+ misiones" y algo más), con 0,92 como valor más probable (el ritmo observado). Cada misión lleva entre 24 y 40 satélites, con 30 como valor típico. El ritmo se mantiene constante.

| Escenario con 30 satélites por misión | Misiones por año | Satélites al 30/07/2029 | % de 3.232 |
|---|---|---|---|
| Ritmo observado | 11 | ≈ 1.290 | 40% |
| Plan de Amazon | 20 | ≈ 2.020 | 63% |
| Ritmo necesario | 35 | ≈ 3.240 | 100% |

La simulación da P10 ≈ 1.141 (35%), **mediana ≈ 1.513 (47%)** y P90 ≈ 2.046 (63%). La probabilidad de llegar a 3.232 es ≈ 0% **[inferencia del grupo]**: haría falta tres veces el ritmo observado y casi el doble del plan.

**Cuánto depende de nuestros supuestos.** El "≈ 0%" no es una medición: depende de los rangos que elegimos. Con un ritmo máximo de 3,5 misiones por mes, más del triple del observado, la probabilidad sube solo a ≈ 7%, y la conclusión no cambia. El modelo además ignora una aceleración gradual y las fallas de lanzamiento, que empeorarían el resultado.

## 11.9 Respuestas, reservas y efecto

| Riesgo | R-04 | R-02 | R-03 | R-05 | R-06 | R-07 | R-01 | **Suma** |
|---|---|---|---|---|---|---|---|---|
| Exposición antes | 0,28 | 0,20 | 0,14 | 0,06 | 0,05 | 0,06 | 0,03 | **0,82** |
| Exposición después | 0,20 | 0,10 | 0,07 | 0,03 | 0,03 | 0,04 | 0,03 | **0,50** |

**[inferencia del grupo]** Las respuestas bajan la exposición total ≈ 39%, pero R-04 sigue en rojo. Los valores "después" son propuestas, no mediciones.

**Reservas** **[propuesta de gestión]**. Proponemos contingencia en unidades para R-01 (reponer 40 satélites), de tiempo para R-02 (≈ 4 meses, que contamos una sola vez porque alimenta el atraso de R-03 y R-04) y de costo para R-04 (sin monto público). El índice de riesgo y el apalancamiento no se pueden calcular: el impacto está en una escala y no en dólares, y no hay presupuesto público.

## 11.10 Seguimiento y control

**Tema T-01: pérdida de la misión LV-01** **[propuesta de gestión]**. ULA informó una anomalía unos 10 minutos después del despegue y Amazon confirmó que "the payload was lost" (#2, #11). El daño directo es acotado, y el indirecto es el cohete en tierra, que activa R-02 y agrava R-03 y R-04. Proponemos reponer los satélites, reasignar las próximas misiones a Ariane 6 y Falcon 9 (LE-04 sigue programada para no antes del 23/11/2026) y exigirle a ULA la causa raíz antes de volver a cargar satélites en Vulcan. Estado: **abierto**; se cierra cuando ULA publique la causa y Vulcan vuelva a volar sin anomalías.

**Indicadores a vigilar** **[propuesta de gestión]:** una anomalía en un vuelo Vulcan, la fecha de retorno al vuelo de Vulcan y de New Glenn (alerta si no hay fecha a los 3 meses), el ritmo de los últimos 6 meses (alerta por debajo de ≈ 17 misiones) y los satélites operativos por mes (alerta por debajo de ≈ 87). Reestimamos probabilidad e impacto cada trimestre y después de cada evento.

## 11.11 Limitaciones

No son públicos el costo de un satélite, el monto de la fianza ni el costo de las respuestas, y no los completamos con cifras inventadas. No pudimos verificar si la FCC ejecutó la pérdida de la fianza, si NBN Co lanzó su servicio, la causa de la falla de Vulcan ni el estado de las licencias por país y de la compra de Globalstar (búsqueda del 16/11/2026). La mayor parte de las fuentes son comunicados de Amazon, es decir, declaraciones propias.

# 12. Seguimiento y valor ganado

## 12.1 Medir por el resultado

La cátedra pide medir el avance por el resultado, no por el esfuerzo (Clase 6). En Amazon Leo el resultado es público y verificable: los **satélites desplegados**. Por eso calculamos el valor ganado en unidades físicas **[propuesta de gestión]**:

| Concepto | Valor |
|---|---|
| Total (BAC) | 3.232 satélites **[dato real]** (#8 ¶3) |
| Valor planificado (PV) | Línea base A: 1.616 al 30/07/2026 y 3.232 al 30/07/2029, unidos en línea recta. Línea base B: ≈ 700 al 30/07/2026 (plan de Amazon) |
| Valor ganado (EV) | Satélites lanzados acumulados **[inferencia del grupo]**, suma de #2 |
| Costo real (AC) | No público |

Control de consistencia: nuestra serie suma 180 satélites al 16/12/2025, y Amazon declaró ante la FCC "180 satélites lanzados" el 30/01/2026 (#8 ¶8).

## 12.2 Resultados

**[inferencia del grupo]** El SPI es el valor ganado dividido por el planificado: menos de 1 significa que se avanza por debajo del plan.

| Corte | Planificado | Ganado | SPI |
|---|---|---|---|
| Plazo del 50% contra la FCC (30/07/2026) | 1.616 | 396 | **0,25** |
| Plazo del 50% contra el plan de Amazon (30/07/2026) | 700 | 396 | **0,57** |
| Hoy, contra la línea base de la FCC (16/11/2026) | 1.777 | 396 | **0,22** |

Contra su propio plan, Amazon ejecutó el 57%. Contra lo que exige el regulador, el 25%. Entre julio y noviembre el SPI empeora (de 0,25 a 0,22) porque no hubo despliegues exitosos mientras el plan seguía avanzando. Además, que el plan de Amazon (≈ 700) estuviera tan por debajo del plazo de la FCC (1.616) muestra que la empresa nunca planificó cumplir el primer plazo: pidió el waiver con un plan que ya lo daba por perdido (#8 ¶8).

## 12.3 ¿Cuándo termina?

| Escenario | Ritmo | Fin |
|---|---|---|
| Ritmo observado | 21,3 satélites por mes | ≈ 2038 |
| Plan de Amazon (20 misiones por año de 30 satélites) | 50 por mes | ≈ 08/2031 |
| PERT (sección 9) | | ≈ 11/2035 (desvío de 24 meses) |
| Lo necesario para el plazo | 87,5 por mes | 30/07/2029 |

## 12.4 Lo que no se puede calcular

El **CPI** (valor ganado ÷ costo real) y la variación de costo necesitan el costo real, que no es público. No lo estimamos. Podemos decir de forma cualitativa que hay mucho gasto comprometido (más de USD 340 millones en instalaciones y más de 100 lanzamientos contratados) con un avance físico de 12,3%.

## 12.5 Sistema de seguimiento propuesto

**[propuesta de gestión]** Con los instrumentos de la Clase 6: un informe de situación mensual (valor ganado, SPI, ritmo del mes, causas de desvío y estimado para terminar), un registro de temas pendientes (hoy, el T-01), un formulario de resolución por cada tema, reuniones de avance con los proveedores de lanzamiento y reuniones de cierre por plazo (30/10/2027 y 30/07/2029). Ante un desvío, la Clase 6 propone agregar recursos, extender plazos o eliminar funciones. Amazon ya hace las dos primeras (más lanzadores y el pedido a la FCC) y rechazó la tercera (#8 ¶8, ¶11). Nuestra propuesta combina las dos primeras con el plan de recuperación de la sección 8.

# 13. Integración y coherencia

La consigna pide evitar documentos aislados. Esta sección muestra cómo se conecta todo.

## 13.1 La cadena

**[inferencia del grupo]** Las secciones cuentan una sola historia:

1. **Alcance (7):** la cadena fabricar, procesar, lanzar y operar tiene un cuello de botella en el lanzamiento.
2. **Tiempos y estimaciones (8, 9):** el ritmo real (≈ 21 por mes) es un cuarto del necesario (≈ 87). El PERT da ≈ 0,07% de llegar a tiempo.
3. **Valor ganado (12):** el SPI va de 0,22 a 0,57 según la línea base, y el fin, de 2031 a 2038.
4. **Riesgos (11):** como no llegar es casi seguro, el riesgo principal es regulatorio (R-04), alimentado por los lanzadores en tierra (R-02), que el 15/11/2026 se activó con el tema T-01.
5. **Respuesta integrada:** plan de recuperación (≈ 08/2031), pedido de alivio con evidencia y más capacidad de lanzamiento (OP-1).
6. **Costos (10):** esa respuesta adelanta costos variables y deja en riesgo la fianza. La reserva de contingencia tiene que cubrirlos.
7. **Caso de negocio y acta (5, 6):** el caso sigue siendo deseable pero hay que reevaluarlo, y el acta necesitaba un criterio verificable de inicio del servicio.

## 13.2 Controles de coherencia

Todas las secciones usan los mismos números, que salen de la tabla de cifras maestras (Anexo C). Hicimos estos controles:

- Nuestra serie de satélites contra la declaración de Amazon a la FCC: 180 contra 180.
- Monte Carlo, PERT y valor ganado apuntan a la misma conclusión (2029 inalcanzable; fin entre 2031 y 2038).
- La reserva de tiempo del riesgo R-02 se cuenta una sola vez.
- Los contratos figuran igual en todas las secciones (New Glenn, 24; total, ≈ 108).
- La unidad de avance es una sola, lanzados como aproximación de operativos, y está declarada.
- El alcance (primera generación, 3.232, hasta el 30/07/2029) coincide con el total del valor ganado y con el horizonte de riesgos.

## 13.3 Elaboración progresiva

La cátedra dice que "la llave para relacionar temas es la elaboración progresiva". Se ve en tres lugares: el alcance (la primera generación en detalle y las líneas nuevas después), las estimaciones (se reestiman cuando cambia la información) y el caso de negocio (que hay que actualizar con el atraso).

# 14. Conclusiones y limitaciones

## 14.1 Conclusiones

1. **El cuello de botella es el lanzamiento, no la fábrica.** Amazon declara capacidad para hasta 30 satélites por semana y fabricó unos 1.000, pero desplegó 396 a ≈ 21 por mes **[inferencia del grupo]**.
2. **El plazo de 2029 no se alcanza con la capacidad contratada.** Monte Carlo, PERT y valor ganado coinciden. El fin razonable está entre 2031 y 2038 **[inferencia del grupo]**.
3. **El riesgo principal es regulatorio, no técnico.** Lo incierto no es si se llega sino si la FCC concede otro alivio. La gestión debería concentrarse en un pedido fundado en un plan de recuperación creíble (≈ 08/2031) **[propuesta de gestión]**.
4. **Faltó un criterio verificable de inicio del servicio.** El inicio se corrió unos dos años en cuatro anuncios sin incumplir un plazo formal. El acta reconstruida lo incorpora **[propuesta de gestión]**.
5. **El alcance crece antes de terminar la primera generación.** Recomendamos separar el caso de negocio de la primera generación del de las líneas nuevas **[propuesta de gestión]**.

## 14.2 Limitaciones

- **Costos:** sin presupuesto ni costos unitarios públicos, no calculamos el CPI, el índice de riesgo ni el apalancamiento.
- **Satélites operativos:** usamos lanzados como aproximación, así que los resultados son optimistas.
- **Fuentes de la empresa:** la mayoría de los datos de Amazon son declaraciones propias.
- **Supuestos de las simulaciones:** el "≈ 0%" del Monte Carlo y el "≈ 0,07%" del PERT dependen de rangos que elegimos nosotros.
- **Datos no verificados:** el protoflight de 2023, el aviso de cumplimiento del 14/08/2026, las licencias por país, la cantidad de estaciones terrestres y el estado de NBN Co.
- **Fecha de corte:** 16/11/2026, un día después de la falla de LV-01, sin causa raíz publicada.

## 14.3 Qué haríamos con más información

Leeríamos el informe anual (10-K) de Amazon para acotar la inversión real y reconstruir un presupuesto en dólares. Pediríamos a la FCC el aviso de cumplimiento y su respuesta. Y reestimaríamos el ritmo cuando Vulcan vuelva a volar y cuando New Glenn haga su primer vuelo para Leo.

# Anexo A. Fuentes

Las 47 fuentes del registro, consultadas el 15 y el 16/11/2026. Las URL completas están en el registro de fuentes del repositorio (`evidencia/registro-fuentes.md`). Los documentos primarios clave son:

- FCC, orden DA 26-553 (05/06/2026): <https://docs.fcc.gov/public/attachments/DA-26-553A1.txt> (#8)
- FCC, orden DA 24-224 (08/03/2024): <https://docs.fcc.gov/public/attachments/DA-24-224A1.pdf> (#7)
- Amazon, *Mission updates* (lista de misiones, #2) y comunicados en aboutamazon.com

| # | Fuente | Tipo | Publicada |
|---|---|---|---|
| 1 | Amazon — "Amazon Leo successfully launches first heavy-lift mission of 2026 with Arianespace" | Oficial | ≈feb 2026 |
| 2 | Amazon — "Amazon Leo mission updates: Launch dates set for next missions on Vulcan and Ariane 6" | Oficial | actualizada |
| 3 | Amazon — "Amazon Leo to launch 40 satellites on its first Vulcan mission" | Oficial | 09/11/2026 |
| 4 | Amazon — "Amazon makes historic launch investment to advance Project Kuiper" | Oficial | 05/04/2022 |
| 5 | SEC EDGAR — Amazon.com Inc, Form 425, Exhibit 99.1: comunicado conjunto Amazon–Globalstar | Regulatoria (primaria) | 14/04/2026 |
| 6 | FCC — Order and Authorization FCC 20-102, 35 FCC Rcd 8324 (autorización original Project Kuiper) | Regulatoria (primaria) | 30/07/2020 |
| 7 | FCC — Order and Authorization DA 24-224 (modificación) | Regulatoria (primaria, texto original consultado) | 08/03/2024 |
| 8 | FCC — Order DA 26-553 (waiver parcial del hito del 50%) | Regulatoria (primaria, texto original consultado) | 05/06/2026 |
| 9 | SpaceNews — "Amazon Secures Up to 83 Launches from Arianespace, Blue Origin, and United Launc… | Técnica/prensa especializada | 05/04/2022 |
| 10 | SpaceNews — "Amazon adds Falcon 9 to multi-billion-dollar Project Kuiper launch campaign" | Técnica/prensa especializada | 2023 |
| 11 | Spaceflight Now — "ULA suffers first total mission failure with loss of Vulcan rocket carryin… | Técnica/prensa especializada | 15/11/2026 |
| 12 | Spaceflight Now — "United Launch Alliance announces mid-November return to flight for Vulcan… | Técnica/prensa especializada | 28/10/2026 |
| 13 | Via Satellite — "Amazon Rebrands Project Kuiper to Amazon Leo, Shares Terminal Lineup" | Prensa especializada | 13/11/2025 |
| 14 | Aviation Week — "Amazon Rebrands Project Kuiper To 'Amazon Leo'" | Prensa especializada | 13/11/2025 |
| 15 | CNBC — "Amazon has deployed enough satellites to launch Leo service later this year" | Prensa general/negocios | 02/07/2026 |
| 16 | The Register — "Amazon Leo's satellite homework is late, but FCC won't flunk it just yet" | Prensa especializada | 08/06/2026 |
| 17 | DCD — "Amazon Leo reveals plans for installation of more than 300 ground stations" | Prensa especializada | 2026 |
| 18 | DCD — "Amazon files to place ground station in Kenya" | Prensa especializada | ≈jun 2026 |
| 19 | Wikipedia — "Amazon Leo" | Terciaria (índice) | viva |
| 20 | Wikipedia — "List of Amazon Leo launches" | Terciaria (índice) | viva |
| 21 | Amazon — Project Kuiper becomes Amazon Leo | Oficial | 13/11/2025 |
| 22 | Amazon — Globalstar y Apple | Oficial | 14/04/2026 |
| 23 | Amazon — Plan de duplicar la cadencia | Oficial | 23/03/2026 |
| 24 | Amazon — Arianespace, 6 lanzamientos nuevos | Oficial | 10/09/2026 |
| 25 | Amazon — Fábrica de Kirkland ampliada | Oficial | 27/10/2022 |
| 26 | Amazon — Dentro de la fábrica de Kirkland | Oficial | 27/06/2024 |
| 27 | Amazon — Instalación en Florida | Oficial | 24/07/2025 |
| 28 | Amazon — What is Project Kuiper | Oficial | 04/11/2025 |
| 29 | Amazon — Enterprise preview Ultra y Pro | Oficial | 24/11/2025 |
| 30 | Amazon — Primera vista de terminales | Oficial | 14/03/2023 |
| 31 | Amazon — Delta | Oficial | 31/03/2026 |
| 32 | Amazon — Vanu | Oficial | 26/02/2026 |
| 33 | Amazon — Herotel | Oficial | 15/07/2026 |
| 34 | Amazon — Direct-to-device | Oficial | 27/07/2026 |
| 35 | Amazon — Uzbekistán | Oficial | 22/09/2026 |
| 36 | Amazon — JetBlue | Oficial | 04/09/2025 |
| 37 | Amazon — Sudamérica / DIRECTV | Oficial | 12/06/2024 |
| 38 | Amazon — Falcon 9 con SpaceX | Oficial | 01/12/2023 |
| 39 | Amazon — Aprobación FCC 2020 | Oficial | 30/07/2020 |
| 40 | Amazon Australia — NBN Co | Oficial | 05/08/2025 |
| 41 | ULA — Vulcan Leo 1 (página de misión) | Técnica / proveedor | sin fecha |
| 42 | CNBC — Amazon Project Kuiper | Prensa general | 04/04/2019 |
| 43 | CNBC — Globalstar y Leo | Prensa general | 14/04/2026 |
| 44 | Via Satellite — FCC aprueba plan de desechos | Prensa especializada | 09/02/2023 |
| 45 | Vice — SpaceX presiona contra Amazon | Prensa general | 19/12/2019 |
| 46 | Amazon — Adelanto de LE-03 | Oficial | 05/06/2026 |
| 47 | AP vía OPB — Explosión de New Glenn en plataforma | Prensa general (confirmada por varios medios) | 29/05/2026 |

# Anexo B. Misiones de lanzamiento

Fuente: Amazon, *Mission updates* (#2) y comunicados de ULA (#11). El acumulado es un cálculo del grupo.

| N.º | Misión | Fecha | Cohete | Satélites | Resultado | Acumulado |
|---|---|---|---|---|---|---|
| 1 | KA-01 | 28/04/2025 | Atlas V 551 | 27 | Lanzada | 27 |
| 2 | KA-02 | 23/06/2025 | Atlas V 551 | 27 | Lanzada | 54 |
| 3 | KF-01 | 16/07/2025 | Falcon 9 | 24 | Lanzada | 78 |
| 4 | KF-02 | 11/08/2025 | Falcon 9 | 24 | Lanzada | 102 |
| 5 | KA-03 | 25/09/2025 | Atlas V 551 | 27 | Lanzada | 129 |
| 6 | KF-03 | 14/10/2025 | Falcon 9 | 24 | Lanzada | 153 |
| 7 | LA-04 | 16/12/2025 | Atlas V 551 | 27 | Lanzada | 180 |
| 8 | LE-01 | 12/02/2026 | Ariane 64 | 32 | Éxito | 212 |
| 9 | LA-05 | 04/04/2026 | Atlas V 551 | 29 | Lanzada | 241 |
| 10 | LA-06 | 28/04/2026 | Atlas V 551 | 29 | Lanzada | 270 |
| 11 | LE-02 | 30/04/2026 | Ariane 64 | 32 | Lanzada | 302 |
| 12 | LA-07 | 29/05/2026 | Atlas V 551 | 29 | Lanzada | 331 |
| 13 | LE-03 | 17/06/2026 | Ariane 64 | 36 | Desplegados 36 | 367 |
| 14 | LA-08 | 02/07/2026 | Atlas V 551 | 29 | Lanzada | 396 |
| 15 | LV-01 | 15/11/2026 | Vulcan VC6L (ULA) | 40 | Falla: carga perdida | 396 (sin sumar) |

# Anexo C. Cifras maestras

Todas las secciones toman sus números de esta tabla. Fecha de corte: 16/11/2026. La unidad de avance es satélites **lanzados**, como aproximación de operativos.

| Cifra | Valor | Origen |
|---|---|---|
| Satélites autorizados (primera generación) | 3.232 | [dato real] #7, #8 |
| Primer plazo | 1.616 al 30/07/2026 | [dato real] #8 ¶3 |
| Plazo final | 3.232 al 30/07/2029 | [dato real] #8 ¶3 |
| Proyección de Amazon a la FCC | ≈ 700 al 30/07/2026 | [dato real] #8 ¶8 |
| Pérdida de prioridad de espectro | Hasta el 30/03/2028 (30/10/2027 si certifica el 50% construido) | [dato real] #8 ¶15 |
| Fianza | No eximida; monto no público | [dato real] #8 ¶18 |
| Misiones realizadas | 15 (14 con despliegue y LV-01 fallida) | [dato real] #2, #11 |
| Satélites lanzados | 396 | [inferencia del grupo] suma de #2 |
| Satélites perdidos | 40 (LV-01, 15/11/2026) | [dato real] #2, #11 |
| Satélites que faltan | 2.836 | [inferencia del grupo] 3.232 − 396 |
| Avance contra el plazo final | 12,3% | [inferencia del grupo] 396 ÷ 3.232 |
| Cumplimiento del primer plazo | 24,5% (396 de 1.616) | [inferencia del grupo] |
| Horizonte hasta el plazo final | ≈ 32,5 meses | [inferencia del grupo] |
| Ritmo observado | ≈ 21 satélites por mes (≈ 0,8 misiones por mes; ≈ 11 por año desde 28/04/2026) | [inferencia del grupo] |
| Ritmo necesario | ≈ 87 satélites por mes (≈ 35 misiones por año a 30 satélites) | [inferencia del grupo] |
| Plan declarado de Amazon | "20+ misiones" en el año dos | [dato real] #23 |
| Satélites por misión | 24 (Falcon 9), 27–29 (Atlas V), 32–36 (Ariane 64), 40 (Vulcan) | [dato real] #2, #3 |
| Capacidad de fábrica declarada | Hasta 30 por semana | [dato real] #23 |
| Satélites fabricados | 1.000 (inicios de 09/2026) | [dato real] #3 |
| Instalaciones en Florida | Más de USD 140 millones (Kennedy Space Center) y más de USD 200 millones (Cabo Cañaveral) | [dato real] #27, #23 |
| Compromiso de inversión inicial | Más de USD 10.000 millones | [dato real] #39 |
| Lanzamientos contratados | ≈ 108 (24 Ariane 6, 38 Vulcan, 9 Atlas V, 24 New Glenn, 13 Falcon 9) | [inferencia del grupo] |
| Lanzamientos que quedan | ≈ 93 (21 Ariane 6, 10 Falcon 9, 1 Atlas V, 37 Vulcan, 24 New Glenn) | [inferencia del grupo] |
| Dependencia de Vulcan y New Glenn | 61 de 93 (≈ 66%) | [inferencia del grupo] |
| Monte Carlo, satélites al 30/07/2029 | P10 ≈ 1.141, P50 ≈ 1.513, P90 ≈ 2.046; llegar a 3.232: ≈ 0% | [inferencia del grupo] sobre supuestos propios |
| PERT | Fin ≈ 11/2035; probabilidad de llegar a tiempo ≈ 0,07% | [inferencia del grupo] |
| SPI | 0,57 (plan de Amazon), 0,25 (FCC), 0,22 (a la fecha de corte) | [inferencia del grupo] |
| Exposición total al riesgo | 0,82 antes y 0,50 después de responder | [propuesta de gestión] |
| Plan de recuperación | ≈ 08/2031, más 4 meses de reserva (≈ 12/2031) | [propuesta de gestión] |

**Lo que no es público:** inversión total actualizada, costo por satélite y por lanzamiento, monto de la fianza y costo real incurrido. Por eso no se calcula el CPI.

# Anexo D. Código

Los cálculos se pueden reproducir con Python 3, sin dependencias externas. Los scripts están en el repositorio del trabajo:

- `informe/riesgos/analisis_cuantitativo.py`: simulación de Monte Carlo (sección 11.8).
- `informe/estimaciones/pert_despliegue.py`: estimación PERT (sección 9).
- `informe/seguimiento/valor_ganado.py`: valor ganado y serie de satélites (sección 12).
