# Gestión de Riesgos — Amazon Leo

Trabajo Integrador de Investigación · Dirección de Proyectos 2026 · Fecha de corte de las fuentes: 16/11/2026

## Resumen

Esta sección reconstruye cómo podrían gestionarse los riesgos del despliegue de la constelación Amazon Leo, con el método de la cátedra (Clase 10, Gestión de Riesgos). El grupo eligió el **plazo** como objetivo a proteger con prioridad, porque la FCC fijó hitos con fecha cuyo incumplimiento tiene consecuencias concretas sobre el espectro, la fianza y la cantidad de satélites autorizados.

El registro tiene **cuatro riesgos desarrollados**, **tres en lista de seguimiento** y **dos oportunidades**. Uno de ellos ya ocurrió: la pérdida de 40 satélites en la misión Vulcan del 15/11/2026 (R-01), que se gestiona como tema abierto (T-01) mientras R-01 sigue midiendo que se repita. Hay dos riesgos en rojo: que la FCC no conceda un nuevo alivio del hito de 2029 (exposición 0,28) y que un lanzador clave quede en tierra (0,20). Forman una cadena: un lanzador en tierra frena la cadencia, eso retrasa el servicio y agranda la brecha con el hito final, lo que deja a Amazon dependiendo de la decisión del regulador.

El análisis cuantitativo muestra que, con la cadencia observada o con la del propio plan de Amazon, llegar a los 3.232 satélites antes del 30/07/2029 es prácticamente imposible. Por eso no llegar se trata como una condición prevista y no como un riesgo, y el riesgo principal se formula sobre lo que sí es incierto: si la FCC concede un nuevo alivio.

## 1. Alcance, método y trazabilidad

**Alcance.** Se analizan los riesgos del programa de despliegue de la primera generación de la constelación (3.232 satélites autorizados por la FCC), desde la mirada de la gestión de proyectos, con horizonte al 30/07/2029.

**Marco.** Se usa el de la cátedra: Clase 10 (Gestión de Riesgos), `Proyectos_10 Riesgos` y el capítulo 7 del apunte. Sus seis procesos son planificar, identificar, analizar cualitativamente, analizar cuantitativamente, planificar las respuestas y supervisar. Los nombres de los documentos son los de la cátedra (Registro de Riesgos, Exposición al Riesgo, aceptación pasiva o activa, reservas de contingencia y gerenciales).

**Trazabilidad.** Cada dato lleva una etiqueta:
- `[DATO REAL]`: hecho con fuente verificable (se cita con `#n` del anexo A o con documento y párrafo).
- `[INFERENCIA DEL GRUPO]`: conclusión razonable a partir de la evidencia, con supuestos escritos.
- `[PROPUESTA DE GESTIÓN]`: decisión, estimación o valoración creada por el grupo: probabilidades, impactos, estrategias, propietarios, umbrales y reservas.

**Qué no es público.** Amazon no publica su cronograma, su EDT ni su presupuesto, y casi todo lo que informa es declaración de la propia empresa. Por eso la parte reconstruida (probabilidades, impactos, respuestas) es propuesta del grupo y se justifica en cada caso. Los datos que no existen públicamente (costo de un satélite, monto de la fianza, costo de las respuestas) **no se inventaron**: figuran como limitación en la sección 8.

**Declaración de uso de herramientas de IA.** Esta sección se elaboró con asistencia de Claude (Anthropic) para la búsqueda y verificación de fuentes, la estructura y la redacción de borradores. La cátedra habilitó el uso de IA para la redacción (confirmado por el equipo el 16/11/2026). Las decisiones de contenido (objetivo prioritario, orden de objetivos, apetito, umbrales, probabilidades, impactos, estrategias y criterios de cierre) las revisó y aprobó el autor de esta sección. Las fuentes se leyeron con asistencia de IA y se citan para que cualquiera pueda comprobarlas; lo que no pudo verificarse está señalado.

## 2. Planificación de la gestión de riesgos

### 2.1 Objetivo que se protege con prioridad: plazo

**[DATO REAL]** Si Amazon no llega a 1.616 satélites operativos para el 30/07/2026, pierde prioridad de espectro hasta 30/03/2028.
→ Fuente: FCC, Order DA 26-553, ¶15 (publicada el 05/06/2026, consultada el 16/11/2026).

**[DATO REAL]** Si Amazon no llega al 50% de satélites operativos (1.616) para el 30/07/2026, pierde la fianza (surety bond).
→ Fuente: FCC, Order DA 26-553, ¶18.

**[DATO REAL]** Si Amazon no llega a 3.232 satélites operativos para el 30/07/2029, le reducen la autorización a la cantidad de satélites que tenga operativos ese día.
→ Fuente: FCC, Order DA 26-553, ¶12.

**[INFERENCIA DEL GRUPO]** Amazon sigue ampliando compromisos de lanzamiento pese al atraso, porque extendió su acuerdo con Arianespace de 18 a 24 lanzamientos de Ariane 6 (#24, 10/09/2026), sumando capacidad tras haber contratado 10 vuelos adicionales de Falcon 9 a fines de 2025 (según #23, 23/03/2026).
→ Base: #24, #23 y el atraso respecto del hito (DA 26-553 ¶3, ¶8; #2).
→ Supuesto: cada uno de estos lanzamientos implica un desembolso económico para la compañía, aunque los montos exactos de los contratos no sean públicos.
→ Limitación: en la nota de Arianespace (#24), Amazon no vincula oficialmente la ampliación con la necesidad de recuperar el cronograma; según Chris Weber (VP de negocio y producto de Amazon Leo), la decisión responde a la confianza en el desempeño del Ariane 6 y a una estrategia para fortalecer la capacidad de lanzamiento europea.

**[PROPUESTA DE GESTIÓN]** El grupo propone proteger el plazo como objetivo prioritario porque las tres consecuencias de incumplirlo (pérdida de prioridad de espectro, pérdida de la fianza y reducción de la autorización) las fija un regulador, con fechas concretas. Un atraso no solo consume tiempo: reduce el alcance autorizado y expone un costo. Por eso se lo trata como la restricción que arrastra a los demás objetivos.
→ Justificación: DA 26-553 ¶12, ¶15 y ¶18; criterio de la cátedra de gestionar conectados el plazo, el costo y el alcance (apunte, capítulo 7, "La conexión con el resto").

### 2.2 Orden de los objetivos

**[PROPUESTA DE GESTIÓN]** De más a menos protegido:

| Puesto | Objetivo | Apoyo |
|---|---|---|
| 1.º | Plazo | Sección 2.1. |
| 2.º | Alcance | Amazon mantiene la obligación de 3.232 satélites para 2029 aun después del waiver (DA 26-553 ¶11). |
| 3.º | Calidad | Evidencia débil: fabrica "in-house" (#22) y lanzó un lote de 40 satélites en una misma misión (#3), lo que indica aceptación de riesgo técnico más que prioridad de calidad. |
| 4.º | Costo | Es lo que Amazon parece sacrificar primero (inferencia de la sección 2.1). |

La evidencia pública no alcanza para ubicar la calidad con certeza; se deja explícito como limitación.

### 2.3 Apetito al riesgo

**[DATO REAL]** Amazon aceptó incumplir el hito intermedio de la FCC y pidió una extensión de 24 meses o un waiver (DA 26-553 ¶8, ¶11); lanzó 40 satélites en una sola misión, el mayor lote hasta la fecha (#3, #11); fabrica todo en casa (#22); y diversifica lanzadores entre Arianespace, ULA, Blue Origin y SpaceX (#24, #3, #23, #38).

**[INFERENCIA DEL GRUPO]** Amazon muestra una actitud de **búsqueda de riesgo moderada**: acepta concentrar riesgo técnico y de plazo para acelerar el despliegue, pero lo compensa diversificando proveedores.
→ Base: los hechos anteriores. Supuestos: (a) lanzar 40 satélites juntos es una decisión de Amazon y no una restricción del cohete; (b) la diversificación de lanzadores es una cobertura de riesgo y no solo una decisión comercial.
→ Limitación: ninguna fuente pública declara el apetito al riesgo de Amazon; es una lectura de su comportamiento.

### 2.4 Tolerancia y umbrales

**[PROPUESTA DE GESTIÓN]**
- **Escalas:** las de la cátedra (sección 2.6).
- **Tolerancia para el plazo:** más estricta que para costo y calidad, por las consecuencias regulatorias fijas. Un desvío mayor al 10% del cronograma se considera impacto alto (escala de la cátedra: 10–20% = alto).
- **Colores de la matriz** (la cátedra no fija los cortes; los define el grupo): rojo si ER ≥ 0,20; amarillo entre 0,10 y 0,19; verde entre 0,05 y 0,09; azul por debajo de 0,05.
- **Disparadores:** una falla de lanzamiento; que los satélites operativos no alcancen el hito siguiente de la FCC; el vencimiento de la fecha de certificación que acorta la pérdida de espectro a 15 meses (30/10/2027, DA 26-553 ¶15).

### 2.5 Categorías (RBS)

**[PROPUESTA DE GESTIÓN]** Se usan las cuatro categorías de la cátedra, con subcategorías propias del proyecto:

| Categoría (cátedra) | Subcategorías |
|---|---|
| Técnicos | Lanzamiento · Satélite · Terminal y servicio |
| Gestión del proyecto | Proveedores y contratos · Cronograma · Costos y fondos |
| Organización | Dependencia de socios locales · Capacidad de fabricación |
| Externos | Regulación (FCC y otros) · Competencia · Condiciones de lanzamiento |

### 2.6 Escalas

**[PROPUESTA DE GESTIÓN]** Se usan sin cambios las de la cátedra.

| Probabilidad | Valor | | Impacto | Valores de la matriz |
|---|---|---|---|---|
| Muy alta | > 0,81 | | Muy bajo | 0,05 |
| Alta | 0,61 a 0,80 | | Bajo | 0,10 |
| Moderada | 0,41 a 0,60 | | Moderado | 0,20 |
| Baja | 0,21 a 0,40 | | Alto | 0,40 |
| Muy baja | 0,01 a 0,20 | | Muy alto | 0,80 |

Para el impacto en plazo y costo, la cátedra define: bajo < 5%, moderado 5–10%, alto 10–20%, muy alto > 20%. Para alcance: secundario, principal, inaceptable, totalmente inútil.

## 3. Identificación de riesgos

Se partió de un análisis de supuestos del plan de despliegue y de los hechos reales del programa (lanzamientos, contratos, resoluciones de la FCC, acuerdos comerciales). La lista preliminar tenía 12 amenazas y 3 oportunidades; se depuró fusionando las que comparten causa y evento, y se descartó una inferencia débil (satélites fabricados sin lanzar). Quedó:

| ID | Riesgo | Categoría | Tratamiento |
|---|---|---|---|
| R-01 | Pérdida de satélites por falla de un lanzador (recurrencia; **ocurrió el 15/11/2026 → tema T-01**) | Técnico → Lanzamiento | Desarrollado |
| R-02 | Lanzador clave en tierra, con manifiesto concentrado | Gestión → Proveedores | Desarrollado |
| R-03 | Desvío del cronograma de despliegue y del inicio del servicio | Gestión → Cronograma | Desarrollado |
| R-04 | Que la FCC no conceda un nuevo alivio del hito de 2029 (no llegar por cadencia es una condición prevista, sección 5) | Externo → Regulación | Desarrollado |
| R-05 | Pérdida temporal de prioridad de espectro | Externo → Regulación | Seguimiento |
| R-06 | Dependencia de socios locales | Organización | Seguimiento |
| R-07 | Aprobaciones regulatorias externas | Externo → Regulación | Seguimiento |
| OP-1 | Capacidad de lanzamiento ampliada y diversificada | Oportunidad | Desarrollada |
| OP-2 | Demanda comercial (aerolíneas y direct-to-device) | Oportunidad | Solo mencionada |

## 4. Análisis cualitativo

### 4.1 Cuentas de base

**Unidad de medida: satélites lanzados como aproximación de satélites operativos.** La FCC mide los hitos en satélites **"deployed and operating"** (DA 26-553 ¶3) `[DATO REAL]`. Amazon informa satélites **lanzados** ("nearly 400", #2) y no publica cuántos están operativos `[DATO REAL]`. Todas las cuentas de este documento usan lanzados (≈ 396) como aproximación de operativos `[INFERENCIA DEL GRUPO]`.
→ Supuesto: todos los satélites lanzados llegan a su órbita y operan. Consecuencia: como operativos ≤ lanzados, **todos los resultados son optimistas** para Amazon. La brecha real con los hitos es igual o mayor que la calculada, y la conclusión de R-04 se refuerza, no se debilita.

Estas cuentas se usan en varias fichas. Todas son `[INFERENCIA DEL GRUPO]`.

| Cuenta | Resultado | Base y supuestos |
|---|---|---|
| Lanzamientos restantes por proveedor | 21 Ariane 6, 10 Falcon 9, 1 Atlas V, 37 Vulcan, 24 New Glenn: ≈ 93 | Contratados menos volados (#24, #3, #4, #23, #38, #2). Supuestos: los contratos siguen vigentes; los 9 Atlas V incluyen los 8 volados; el manifiesto incluye lanzamientos para ≈ 800 satélites adicionales (#23), no solo para la primera generación. |
| Dependencia de Vulcan y New Glenn | 61 de ≈ 93 = ≈ 66% | Misma base. |
| Satélites que faltan para 2029 | 3.232 − 396 = 2.836 | DA 26-553 ¶3; #2. |
| Ritmo observado | 15 misiones en ≈ 18,6 meses = ≈ 0,8 por mes | #2 (del 28/04/2025 al 15/11/2026). |
| Horizonte hasta el hito final | ≈ 32,5 meses | Del 16/11/2026 al 30/07/2029. |

### 4.2 Riesgos desarrollados

#### R-04 — Que la FCC no conceda un nuevo alivio del hito de 2029

**Por qué se reformuló.** En la primera versión el evento era "no cumplir el hito de 2029" con P = 0,70, pero el análisis cuantitativo (sección 5) da una probabilidad de no llegar a 3.232 por cadencia de ≈ 100%. Un evento casi seguro no es un riesgo: es una **condición prevista** que el plan tiene que absorber. La incertidumbre real está en la respuesta del regulador. Por eso el evento ahora es que la FCC **no** conceda una prórroga o un waiver. La probabilidad de 0,70 que eligió el grupo mide eso directamente: ≈ 30% de que haya un nuevo alivio, como en 2026 (DA 26-553).

**[INFERENCIA DEL GRUPO] Condición prevista (no riesgo):** con la cadencia observada o planificada, Amazon llegaría al 30/07/2029 con ≈ 1.140–2.050 satélites (P10–P90, sección 5), lejos de 3.232. Esta brecha se trata como supuesto de planificación del cronograma maestro y del caso de negocio, no como evento incierto.
→ Base: sección 5; DA 26-553 ¶3. Supuestos: los de la sección 5.

| Campo | Contenido |
|---|---|
| Categoría y tipo | Externo → Regulación. Amenaza. Objetivo afectado: alcance (principal) y costo (fianza). |
| Descripción | Debido a que Amazon llegaría al 30/07/2029 con unos 1.500 a 2.000 de los 3.232 satélites (condición prevista), puede ocurrir que la FCC no conceda una nueva prórroga o waiver, lo que reduciría la autorización a los satélites operativos ese día y expondría la pérdida de la fianza. |
| Base | `[DATO REAL]` Hito final de 3.232 satélites al 30/07/2029; si falla, la autorización se reduce al número operativo (DA 26-553 ¶3, ¶12); el incumplimiento de un hito implica pérdida de la fianza (DA 24-224 ¶53; DA 26-553 ¶18). `[DATO REAL]` Amazon planifica "20+ misiones" en el "año dos del despliegue" y dice haber estado en camino a 11 lanzamientos en el primer año (#23); el texto no fecha esos años (se infiere que el año uno empieza con la misión KA-01, el 28/04/2025). `[INFERENCIA DEL GRUPO]` A 20 misiones por año durante 32,5 meses, con ≈ 30 satélites por misión, se agregarían ≈ 1.600–1.700 satélites y se llegaría a ≈ 2.050 (≈ 63% de 3.232). Desde el 28/04/2026 hubo 6 misiones en ≈ 6,5 meses (≈ 11 por año), la mitad de lo planificado (#2). Supuestos: se sostiene el ritmo planificado desde hoy; ≈ 30 satélites por misión (rango 24–40). |
| Probabilidad | **0,70** `[PROPUESTA DE GESTIÓN]`: probabilidad de que la FCC **no** conceda un nuevo alivio. A favor de un alivio (≈ 30%): la FCC ya concedió un waiver parcial en 2026 (DA 26-553 ¶11); Amazon tiene capacidad de fábrica declarada de hasta 30 satélites por semana, limitada por los lanzadores (#23), y más de 100 misiones contratadas (#23), que sirven de evidencia de esfuerzo. En contra (≈ 70%): el waiver de 2026 fue **parcial** y la FCC mantuvo intacto el hito de 2029 y la fianza (DA 26-553 ¶11, ¶18); la brecha a cubrir es grande (hacen falta ≈ 35 misiones por año contra un plan de 20 y un ritmo observado de ≈ 11, #23, #2). Supuesto declarado: no hay un dato que permita estimar la conducta futura de la FCC; el 30% es juicio del grupo basado en el único precedente. |
| Impacto | **0,40 (alto)** `[PROPUESTA DE GESTIÓN]`. Quedar en ≈ 2.050 significaría perder ≈ 1.180 satélites autorizados (≈ 37%). En la escala de alcance, "inaceptable" = 0,40. Amazon dijo que cumpliría el 100% para el 30/07/2029 y pidió un waiver en vez de resignar satélites (DA 26-553 ¶8, ¶11) `[DATO REAL]`; de ahí se infiere que no consideraría aceptable una constelación parcial `[INFERENCIA DEL GRUPO]`, aunque Amazon no lo dice. |
| Exposición | 0,70 × 0,40 = **0,28. Rojo.** |
| Estrategia | **Mitigar** `[PROPUESTA DE GESTIÓN]`. Evitar implicaría resignar alcance, que Amazon dijo no aceptar; transferir no aplica a un hito regulatorio; aceptar no corresponde con una exposición de 0,28 (la cátedra la reserva para cuando responder cuesta más que el daño). |
| Respuesta | (1) Preparar y presentar a tiempo un nuevo pedido de extensión o waiver, con evidencia de avance (respuesta principal: actúa sobre la probabilidad). (2) Acelerar la cadencia todo lo posible: no alcanza para llegar a 3.232, pero achica la brecha y fortalece el pedido. (3) Reportar a la FCC la capacidad construida y los lanzamientos contratados. |
| Propietario | Chief Global Affairs and Legal Officer de Amazon (rol que figura en #33). Propuesta del grupo. |
| Disparador | La cadencia de los últimos 6 meses queda por debajo de la necesaria; nuevo atraso de un lanzador (R-02); la FCC cambia la política de hitos o rechaza un pedido de otro operador. |
| Después de responder | P 0,50 × C 0,40 = **0,20. Sigue en rojo:** un pedido bien fundado puede mejorar las chances, pero la decisión es del regulador y la brecha de cadencia sigue siendo grande. |
| Residual y secundario | Residual: la brecha de cadencia. Secundario: acelerar aumenta el riesgo técnico (R-01) y presiona la fabricación. |
| Costo de la respuesta y reserva | No calculable: el monto de la fianza y el costo de ampliar la cadencia no son públicos. |

#### R-02 — Lanzador clave en tierra, con manifiesto concentrado

| Campo | Contenido |
|---|---|
| Categoría y tipo | Gestión → Proveedores y contratos. Amenaza. Objetivo afectado: plazo. |
| Descripción | Debido a que Vulcan y New Glenn concentran ≈ 66% de los lanzamientos que quedan por hacer, y a que Vulcan acaba de fallar y New Glenn todavía no voló para Leo, puede ocurrir que alguno o ambos queden fuera de servicio por seis meses o más, lo que frenaría la cadencia de despliegue y atrasaría los hitos. |
| Base | `[DATO REAL]` Vulcan estuvo ≈ 9 meses en tierra antes de LV-01 (#12) y falló el 15/11/2026 (#2, #11). `[DATO REAL]` New Glenn explotó en su plataforma de Cabo Cañaveral durante una prueba de encendido el 28/05/2026, con causa no determinada al momento de la nota (#47). `[DATO REAL]` Amazon tiene 38 Vulcan y 24 New Glenn contratados (#3, #23) y dice que ajustó sus metas semanales de producción según la disponibilidad de lanzadores (#23): el lanzamiento es el cuello de botella. El 66% es inferencia (sección 4.1). |
| Probabilidad | **0,50** `[PROPUESTA DE GESTIÓN]`. Hay un precedente de una parada de ≈ 9 meses (#12), la causa de la falla actual no se conoce y New Glenn no tiene vuelos de Leo. |
| Impacto | **0,40 (alto)** `[PROPUESTA DE GESTIÓN]`. Seis meses fuera de servicio de ≈ 66% de la capacidad restante equivalen a ≈ 4 meses de cadencia total (6 × 0,66 ≈ 3,96), es decir ≈ 12% del horizonte de 32,5 meses. La escala de plazo marca 10–20% como alto. Supone que el resto de los lanzadores no puede absorber el atraso. |
| Exposición | 0,50 × 0,40 = **0,20. Rojo** (justo en el corte; con P = 0,40 pasaría a amarillo). |
| Estrategia | **Mitigar** `[PROPUESTA DE GESTIÓN]`: reasignar misiones a los lanzadores disponibles (Ariane 6, Falcon 9) y negociar cupos adicionales (OP-1). |
| Respuesta | (1) Priorizar los lanzamientos de Ariane 6 y Falcon 9 mientras se investiga la falla. (2) Pedir a ULA y a Blue Origin fechas de retorno al vuelo. (3) Evaluar nuevos contratos de capacidad. |
| Propietario | Director/a de sistemas de lanzamiento de Amazon Leo (rol que figura en #3). Propuesta del grupo. |
| Disparador | ULA no informa fecha de retorno al vuelo a los 3 meses de la falla; New Glenn sigue sin volar; un segundo evento en cualquiera de los dos. Al 16/11/2026 ULA no había publicado causa raíz ni fecha de retorno. |
| Después de responder | P 0,50 × C 0,20 = **0,10. Amarillo.** Se supone que Ariane 6 y Falcon 9 absorben parte del atraso (≈ 34% del manifiesto restante no depende de Vulcan ni de New Glenn). |
| Residual y secundario | Residual: sigue habiendo dependencia fuerte de Vulcan y New Glenn. Secundario: concentrar la cadencia en Ariane 6 y Falcon 9 los expone a sus propios incidentes y a cupos limitados. |
| Reserva | Reserva de tiempo del orden de 4 meses en el cronograma maestro, a conciliar con el área de tiempos. Costo: no público. |

#### R-03 — Desvío del cronograma de despliegue y del inicio del servicio

| Campo | Contenido |
|---|---|
| Categoría y tipo | Gestión → Cronograma. Amenaza. Objetivo afectado: plazo. |
| Descripción | Debido a que Amazon lleva un ritmo de ≈ 0,8 misiones por mes, muy inferior al plan, y a que ya perdió 40 satélites, puede ocurrir que el inicio del servicio comercial se postergue otra vez más allá de fin de 2026, lo que retrasaría los ingresos y los acuerdos que dependen del servicio. |
| Base | `[DATO REAL]` ≈ 396 satélites contra ≈ 700 proyectados al 30/07/2026 (DA 26-553 ¶8; #2). `[DATO REAL]` El inicio del servicio se fue corriendo: primeros clientes "later that year" en 2023 (#30), servicio "next year" en 2024 (#26), "broader rollout next year" en 2025 (#29) y "later this year" el 09/11/2026 (#3). `[INFERENCIA DEL GRUPO]` Se supone que las cuatro frases se refieren al mismo hito, el inicio del servicio comercial. |
| Probabilidad | **0,70** `[PROPUESTA DE GESTIÓN]`. Quedan ≈ 6 semanas del año, no hay anuncio de lanzamiento comercial y se acaba de perder una misión de 40 satélites. |
| Impacto | **0,20 (moderado)** `[PROPUESTA DE GESTIÓN]`. Cada postergación previa fue de ≈ 1 año; sobre un horizonte de ≈ 10 años (anuncio en 2019, hito final en 2029) es ≈ 10% del cronograma, en el límite entre moderado y alto. Se elige moderado porque otra postergación podría ser menor a un año. |
| Exposición | 0,70 × 0,20 = **0,14. Amarillo.** |
| Estrategia | **Mitigar** `[PROPUESTA DE GESTIÓN]`: iniciar el servicio por regiones y con clientes empresariales mientras sigue el despliegue (hoy hay un "private preview", #35). |
| Respuesta | (1) Definir un criterio de inicio por región (satélites mínimos y cobertura). (2) Comunicar fechas con margen a los socios. (3) Reportar el avance contra el plan y no contra metas aspiracionales. |
| Propietario | VP de negocio y producto de Amazon Leo (rol que figura en #24). Propuesta del grupo. |
| Disparador | Llegar al 30/11/2026 sin anuncio de servicio; una nueva falla de lanzamiento; cadencia mensual por debajo de lo planificado. |
| Después de responder | P 0,70 × C 0,10 = **0,07. Verde.** El inicio parcial reduce el impacto de una demora total. |
| Residual y secundario | Residual: el servicio inicial tendría cobertura limitada. Secundario: lanzar con poca cobertura puede dañar la reputación del servicio. |

#### R-01 — Pérdida de satélites por falla de un lanzador (recurrencia)

**El evento ya ocurrió una vez.** El 15/11/2026 la misión LV-01 falló y se perdieron 40 satélites (#2, #11). Lo que ocurrió deja de ser un riesgo y pasa a ser un **tema** (problema a resolver), que se gestiona en el registro de Resolución de Temas de la sección 7.1 (tema T-01), según la Clase 6 de la cátedra. Esta ficha mide desde ahora la **recurrencia**: que vuelva a pasar en las misiones siguientes.

**[INFERENCIA DEL GRUPO] Por qué R-01 queda en azul aunque se haya materializado.** La consecuencia grave de la falla no son los 40 satélites, sino que el cohete quede en tierra y frene la cadencia. Ese daño se mide en R-02, que está en rojo. Si se sumara también acá, se contaría dos veces. Lo que mide R-01 es la reposición de los satélites perdidos, y en plazo eso equivale a ≈ 1,3 semanas de fábrica (ver Impacto). La ficha tiene un punto débil, que el grupo debe poder defender: el costo de un satélite no es público. Con un costo unitario alto, el impacto en costo subiría a moderado (0,20), la exposición a 0,06 y R-01 pasaría a verde.
→ Base: #2, #11, #23. Supuesto: la separación entre R-01 (pérdida de carga) y R-02 (cohete en tierra) se mantiene en todo el registro.

| Campo | Contenido |
|---|---|
| Categoría y tipo | Técnico → Lanzamiento. Amenaza. Objetivo afectado: costo (principal) y plazo (secundario; el plazo por paralización del cohete se trata en R-02). |
| Estado | **Materializado una vez (15/11/2026) → tema T-01 abierto.** El riesgo de recurrencia sigue activo. |
| Descripción | Debido a que la causa raíz de la falla del 15/11/2026 no es pública y que Vulcan tiene aún 37 lanzamientos contratados con Amazon, puede ocurrir una nueva falla en otra misión, lo que provocaría la pérdida de los satélites a bordo (unos 40 por misión) y obligaría a reponerlos. |
| Base | `[DATO REAL]` El 15/11/2026 el Vulcan falló unos 10 minutos tras el despegue y se perdieron 40 satélites; causa raíz no publicada (#11, #2). Los 37 restantes son un supuesto: que los 38 Vulcan contratados (#3) siguen vigentes. |
| Probabilidad | **0,30 por misión Vulcan** `[PROPUESTA DE GESTIÓN]`. Se estima P = 0,30 porque la frecuencia observada es 0,20 (1 en 5 vuelos, #11), pero con una muestra tan chica de apenas cinco lanzamientos la tasa empírica es poco confiable, y al no haberse resuelto aún la causa raíz persiste una incertidumbre técnica que aumenta el riesgo de recurrencia hasta que se aplique una corrección. |
| Impacto | **0,10 (bajo)** `[PROPUESTA DE GESTIÓN]`. Plazo: 40 satélites son el 1,2% de los 3.232 y reponerlos equivale a ≈ 1,3 semanas de la capacidad de fabricación declarada de 30 por semana (#23), contra ≈ 140 semanas hasta el hito; es insignificante en la escala de plazo. Costo: el valor de un satélite no es público, por lo que no puede expresarse como porcentaje del costo del proyecto; se supone que cae en la franja baja. Punto débil de la ficha: si se estimara un costo unitario alto, el impacto debería subir. |
| Exposición | 0,30 × 0,10 = **0,03. Azul.** Queda azul porque el mayor daño de plazo, que el cohete quede en tierra, se mide en R-02. |
| Estrategia | **Aceptar (activa)** `[PROPUESTA DE GESTIÓN]`: con exposición muy baja, la cátedra indica aceptar; se elige la forma activa porque el riesgo ya ocurrió una vez y hay disparadores concretos. |
| Respuesta | Plan de contingencia: (1) reponer los 40 satélites desde el stock o la producción de Kirkland; (2) reasignar misiones siguientes a otros lanzadores ya contratados; (3) pedir a ULA el resultado de la investigación y las acciones correctivas. |
| Propietario y disparador | Director/a de sistemas de lanzamiento (rol en #3). Disparadores: una anomalía en un vuelo Vulcan; un hold sin explicar en la cuenta regresiva (como el de T-20 s del 15/11, #11); que ULA no publique la causa raíz antes del siguiente vuelo. |
| Reserva | Contingencia, en unidades: reposición de 40 satélites. Monto en dólares: no público. |
| Residual y secundario | Residual: el cohete queda en tierra (R-02). Secundario: usar stock para reponer reduce la disponibilidad para otras misiones. |

### 4.3 Lista de seguimiento de riesgos de baja prioridad

La cátedra prevé esta lista para los riesgos de severidad baja: se vigilan sin desarrollar una respuesta completa. Si un disparador se activa, el riesgo pasa al registro. Los valores son `[PROPUESTA DE GESTIÓN]` con poca evidencia dura, como indica la última columna.

| ID | Riesgo | P | C | ER | Color | Qué se vigila | Límite de la evidencia |
|---|---|---|---|---|---|---|---|
| R-05 | Pérdida temporal de prioridad de espectro hasta el 30/03/2028 (DA 26-553 ¶15): un sistema con prioridad o una nueva ronda de procesamiento podría limitar su espectro y reducir la capacidad del servicio inicial. | 0,30 | 0,20 | 0,06 | Verde | Que la FCC abra una ronda; pedidos de coordinación; la fecha del 30/10/2027, a la que se acorta la pérdida si Amazon certifica que construyó el 50% y contrató lanzamientos. | La condición está activa `[DATO REAL]`; que el hito no se cumplió es inferencia (≈ 396 satélites al 30/07/2026, sin lanzamientos entre el 02/07 y el 15/11, #2). No hay evidencia de una ronda abierta ni de cuánto espectro está en juego. |
| R-06 | Dependencia de socios locales (Herotel #33, UZ-SAT #35, Vanu #32, DIRECTV y Sky Brasil #37, NBN Co #40): un socio podría no lanzar el servicio en fecha, demorando los ingresos de esa región. | 0,50 | 0,10 | 0,05 | Verde | Que un socio no confirme fecha; que el servicio de Amazon se postergue (R-03). | Al 16/11/2026 no se encontró confirmación de que NBN Co haya lanzado el servicio previsto desde mediados de 2026. El valor está justo en el corte con azul. |
| R-07 | Aprobaciones regulatorias externas: la compra de Globalstar (cierre previsto en 2027, #22) y las licencias por país podrían demorarse y retrasar el servicio direct-to-device desde 2028 o el inicio en algún país. | 0,30 | 0,20 | 0,06 | Verde | Que un regulador pida información adicional; que el cierre de Globalstar se corra. | No hay datos del estado de Globalstar ni de las licencias por país; solo se vio la solicitud de Kenia por prensa (#18). |

### 4.4 Oportunidades

La cátedra reconoce que el riesgo puede ser una oportunidad, pero el material no desarrolla estrategias específicas para oportunidades. Para OP-1 se propone "aprovechar", un criterio externo a la cátedra.

**OP-1 — Capacidad de lanzamiento ampliada y diversificada.** Debido a que Amazon sumó 6 lanzamientos de Ariane 6 y 10 de Falcon 9, puede ocurrir que esa capacidad permita sostener la cadencia aunque Vulcan o New Glenn estén en tierra, lo que reduciría el atraso. `[DATO REAL]` Ariane 6 pasó de 18 a 24 lanzamientos (#24) y entregó 100 satélites en tres misiones en menos de cinco meses (#24); se contrataron 10 Falcon 9 adicionales a fines de 2025 (#23). `[INFERENCIA DEL GRUPO]` ≈ 34% del manifiesto restante no depende de Vulcan ni de New Glenn. `[PROPUESTA DE GESTIÓN]` P 0,70 × beneficio 0,20 = +0,14. Es la respuesta de mitigación de R-02. Propietario: director/a de sistemas de lanzamiento.

**OP-2 — Demanda comercial (solo mencionada).** Hay acuerdos con JetBlue (desde 2027, #36), Delta (desde 2028, 500 aviones, #31) y con Apple y Globalstar para direct-to-device (desde 2028, #22). No se desarrolla porque no hay datos de ingresos y depende de que el servicio inicie (R-03).

### 4.5 Matriz de probabilidad e impacto

Matriz de la cátedra con los cortes de la sección 2.4. [R] rojo, [A] amarillo, [V] verde, [Az] azul. En negrita, dónde cae cada riesgo.

| P \ I | 0,05 | 0,10 | 0,20 | 0,40 | 0,80 |
|---|---|---|---|---|---|
| 0,90 | 0,05 [V] | 0,09 [V] | 0,18 [A] | 0,36 [R] | 0,72 [R] |
| 0,70 | 0,04 [Az] | 0,07 [V] | **R-03** 0,14 [A] | **R-04** 0,28 [R] | 0,56 [R] |
| 0,50 | 0,03 [Az] | **R-06** 0,05 [V] | 0,10 [A] | **R-02** 0,20 [R] | 0,40 [R] |
| 0,30 | 0,02 [Az] | **R-01** 0,03 [Az] | **R-05, R-07** 0,06 [V] | 0,12 [A] | 0,24 [R] |
| 0,10 | 0,01 [Az] | 0,01 [Az] | 0,02 [Az] | 0,04 [Az] | 0,08 [V] |

**Priorización:** 1.º R-04 (0,28, rojo); 2.º R-02 (0,20, rojo); 3.º R-03 (0,14, amarillo); 4.º R-05 y R-07 (0,06, verdes); 6.º R-06 (0,05, verde); 7.º R-01 (0,03, azul). Los dos rojos son los de respuesta urgente.

**[INFERENCIA DEL GRUPO]** El riesgo se concentra en regulación (suma de ER de los riesgos externos: 0,40) y en gestión de proveedores y cronograma (0,34), no en lo técnico (0,03) ni en la organización (0,05). Es coherente con el objetivo elegido. Los tres riesgos más altos forman una cadena: un lanzador en tierra (R-02) frena la cadencia, eso retrasa el servicio (R-03) y, si se prolonga, compromete el hito de 2029 (R-04).
→ Base: sección 4.2. Supuesto: la suma de ER entre riesgos es una referencia relativa, no una medida monetaria, porque el impacto está en una escala y no en dólares.

## 5. Análisis cuantitativo

La cátedra propone la simulación de Monte Carlo para estimar la probabilidad de cumplir un objetivo. Amazon no publica su red de actividades ni sus duraciones, así que no se puede simular el cronograma interno. Con datos públicos sí se puede simular **la cantidad de satélites operativos al 30/07/2029**, que es la medida del hito de R-04. El código está en el anexo B y es reproducible.

**Datos de entrada** `[DATO REAL]`: 396 satélites lanzados antes de LV-01 (#2); hito final de 3.232 (DA 26-553 ¶3); 32,5 meses hasta el 30/07/2029. Se usan lanzados como aproximación de operativos (sección 4.1), así que el resultado es un techo optimista.

**Supuestos** `[PROPUESTA DE GESTIÓN]`:
- Cadencia en misiones por mes, distribución triangular: mínimo 0,5 (lanzadores clave en tierra buena parte del período), moda 0,92 (ritmo observado desde el 28/04/2026, ≈ 11 por año) y máximo 2,0 (el plan de "20+ misiones" y algo más).
- Satélites por misión, triangular: mínimo 24, moda 30, máximo 40 (rango de #2 y #3).
- La cadencia se mantiene constante (no se modela una aceleración gradual).

**Escenarios** `[INFERENCIA DEL GRUPO]` (30 satélites por misión):

| Escenario | Misiones por año | Satélites al 30/07/2029 | % de 3.232 |
|---|---|---|---|
| Ritmo observado | 11 | ≈ 1.290 | 40% |
| Plan de Amazon | 20 | ≈ 2.020 | 63% |
| Ritmo necesario | 35 | ≈ 3.240 | 100% |

Con 40 satélites por misión, el plan de 20 por año llegaría a ≈ 2.560 (79%) y la cadencia necesaria bajaría a ≈ 26 por año, todavía por encima del plan.

**Resultado de la simulación** (100.000 corridas):

| Percentil | Satélites al 30/07/2029 | % de 3.232 |
|---|---|---|
| P10 | ≈ 1.140 | 35% |
| P50 | ≈ 1.510 | 47% |
| P90 | ≈ 2.050 | 63% |
| Probabilidad de llegar a 3.232 | ≈ 0% | |

Con un máximo de cadencia de 3,5 misiones por mes (más del triple del ritmo observado), la probabilidad de llegar sube solo a ≈ 7%.

**[INFERENCIA DEL GRUPO]** Con la cadencia observada o con la del propio plan de Amazon, llegar a 3.232 satélites antes del 30/07/2029 es prácticamente imposible. Llegar exigiría ≈ 35 misiones por año: 3 veces el ritmo observado y casi el doble del plan.
→ Limitaciones: el modelo ignora una posible aceleración gradual; usa un promedio de satélites por misión; no incluye fallas de lanzamiento (que empeorarían el resultado); las distribuciones son supuestos del grupo.

**Consecuencia para R-04:** como la probabilidad de no llegar es ≈ 1, no llegar se trata como condición prevista y R-04 se formula sobre la decisión de la FCC (sección 4.2). Este análisis no calcula reservas de costo porque falta el presupuesto.

## 6. Respuestas, reservas y efecto

| ID | ER antes | ER después | Tratamiento |
|---|---|---|---|
| R-04 | 0,28 | 0,20 | Mitigar |
| R-02 | 0,20 | 0,10 | Mitigar |
| R-03 | 0,14 | 0,07 | Mitigar |
| R-05 | 0,06 | 0,03 | Seguimiento |
| R-06 | 0,05 | 0,03 | Seguimiento |
| R-07 | 0,06 | 0,04 | Seguimiento |
| R-01 | 0,03 | 0,03 | Aceptar (activa) |
| **Suma** | **0,82** | **0,50** | |

**[INFERENCIA DEL GRUPO]** Las respuestas propuestas bajan la exposición total ≈ 39%, pero R-04 sigue en rojo. Los valores "después" son propuestas del grupo, no mediciones.

**Reservas** `[PROPUESTA DE GESTIÓN]`. La cátedra distingue reservas de contingencia (riesgos conocidos, parte de la línea base) y gerenciales (riesgos desconocidos, fuera de la línea base de costos):
- R-01: contingencia en unidades, reposición de 40 satélites.
- R-02: contingencia de tiempo, ≈ 4 meses en el cronograma maestro.
- R-03: contingencia de tiempo, a definir con el área de tiempos.
- R-04: contingencia de costo para la fianza y la ampliación de cadencia; monto no público.
- Reserva gerencial para riesgos desconocidos: porcentaje a definir con el área de costos.

**Doble cuenta.** La reserva de tiempo de R-02 alimenta el atraso de R-03 y de R-04; si se suman sin más, el cronograma queda inflado. Debe acordarse con el área de tiempos antes de fijar números.

**Índice de riesgo y apalancamiento.** La cátedra los define como Σ ER ÷ costo total del proyecto y como (ER antes − ER después) ÷ costo de la alternativa. No se pueden calcular: el impacto está en escala, no en dólares, y no existe un presupuesto público ni el costo de las alternativas.

## 7. Seguimiento y control

### 7.1 Riesgos materializados: registro de Resolución de Temas

Cuando un riesgo ocurre deja de ser incierto: pasa a ser un **tema** (problema) y se gestiona con el formulario de Resolución de Temas y el Log de temas pendientes de la cátedra (`catedra/Clase 6 Seguimiento y Valor Ganado`, PPT págs. 12–13).

**Tema T-01 — Pérdida de la misión LV-01 (Vulcan, 40 satélites)** `[PROPUESTA DE GESTIÓN]` con base `[DATO REAL]`

| Campo (cátedra) | Contenido |
|---|---|
| N.° · Título · Fecha | T-01 · Pérdida de LV-01 · 15/11/2026 |
| Fuente | Riesgo R-01 del registro, materializado. `[DATO REAL]` ULA informó una anomalía ≈ 10 minutos después del despegue y Amazon confirmó que "the payload was lost" (#2, #11). |
| Descripción | Se perdieron 40 satélites en el primer vuelo de Vulcan para Amazon (1 de 38 contratados). Causa raíz no publicada al 16/11/2026 (#11). |
| Evaluación y recomendaciones | `[INFERENCIA DEL GRUPO]` El daño directo (40 satélites, ≈ 1,2% de 3.232) es acotado. El daño indirecto es el cohete en tierra, que activa el disparador de R-02 y agrava R-03 y R-04. Se recomienda ejecutar el plan de contingencia de R-01 y la respuesta de R-02 al mismo tiempo. |
| Impacto | Satélites en órbita sin cambios (≈ 396); se pierde la misión que los llevaba a ≈ 436 (#11). Cadencia: Vulcan sin fecha de retorno (#11). |
| Decisión | `[PROPUESTA DE GESTIÓN]` (1) Reponer los 40 satélites con producción de Kirkland. (2) Reasignar las próximas misiones a Ariane 6 y Falcon 9 (LE-04 sigue programada para no antes del 23/11/2026, #2). (3) Exigir a ULA el informe de causa raíz antes de volver a cargar satélites en Vulcan. (4) Reevaluar R-01, R-02, R-03 y R-04 con cada novedad de ULA (sección 7.2, "Reevaluación"). |
| Aprobó · Responsable · Estado | Responsable propuesto: director/a de sistemas de lanzamiento de Amazon Leo (rol en #3). Estado: **abierto**. Se cierra cuando ULA publique la causa raíz y Vulcan vuelva a volar sin anomalías. |

**Log de temas pendientes** `[PROPUESTA DE GESTIÓN]`

| N.° | Tema | Abierto | Responsable | Próxima acción | Estado |
|---|---|---|---|---|---|
| T-01 | Pérdida de LV-01 | 15/11/2026 | Sistemas de lanzamiento | Causa raíz de ULA; reasignación del manifiesto | Abierto |

### 7.2 Indicadores a vigilar

**Indicadores a vigilar** `[PROPUESTA DE GESTIÓN]`:

| Indicador | Riesgo | Umbral que activa la respuesta | Fuente | Frecuencia |
|---|---|---|---|---|
| Anomalía o hold sin explicar en un vuelo Vulcan | R-01, R-02 | Cualquier anomalía | ULA; Amazon (#2) | Por misión |
| Fecha de retorno al vuelo de Vulcan y de New Glenn | R-02 | Sin fecha a los 3 meses de la falla | ULA; Blue Origin; Amazon | Mensual |
| Cadencia de los últimos 6 meses | R-04 | Menos de ≈ 17 misiones en 6 meses | Lista de misiones (#2) | Mensual |
| Satélites operativos por mes | R-04 | Menos de ≈ 87 por mes | Lista de misiones (#2) | Mensual |
| Anuncio del servicio comercial | R-03 | Sin anuncio al 30/11/2026 | Amazon | Puntual |
| Nueva ronda de la FCC o pedido de coordinación | R-05 | Cualquiera | FCC | Trimestral |
| Certificación del 50% construido | R-05 | Antes del 30/10/2027 | FCC (DA 26-553 ¶15) | Trimestral |
| Fecha confirmada por cada socio | R-06 | Un socio sin fecha | Amazon; socios | Trimestral |
| Avance de la aprobación de Globalstar | R-07 | Cierre corrido más allá de 2027 | Amazon (#22) | Trimestral |

**[INFERENCIA DEL GRUPO]** Para llegar a 3.232 desde 396 faltan 2.836 satélites en ≈ 32,5 meses, es decir ≈ 87 por mes. El ritmo observado es ≈ 21 por mes (396 en ≈ 18,6 meses). Los umbrales de cadencia salen de 35 misiones por año ÷ 2 = ≈ 17 por semestre.
→ Base: DA 26-553 ¶3; #2. Supuesto: el hito final es el 30/07/2029 y el ritmo se mide como promedio lineal.

**Reevaluación** `[PROPUESTA DE GESTIÓN]`: reestimar probabilidad e impacto cada trimestre y después de cada evento (una falla, un anuncio de la FCC, un cambio de calendario), y comparar la exposición nueva con la inicial.

**Supuestos a revisar durante el proyecto:**

| Supuesto | Riesgo que lo usa | Se invalida si |
|---|---|---|
| Los 38 Vulcan y los 24 New Glenn siguen contratados | R-01, R-02 | Amazon cancela o reasigna contratos |
| ≈ 30 satélites por misión | R-04, sección 5 | Cambia el tamaño de los lotes |
| Lanzados ≈ operativos | Todos | Amazon o la FCC publican un conteo de operativos menor |
| Sin aceleración fuerte, la cadencia no alcanza para 3.232 (condición prevista) | R-04, sección 5 | La cadencia de 6 meses supera ≈ 17 misiones |
| ≈ 30% de chances de un nuevo alivio de la FCC | R-04 | La FCC se pronuncia sobre un pedido de Amazon o de otro operador |
| El hito de 2026 no se cumplió | R-05 | Amazon demuestra otro conteo |
| Las frases sobre el inicio del servicio se refieren al mismo hito | R-03 | Amazon define dos hitos distintos |

**Criterios de cierre** `[PROPUESTA DE GESTIÓN]`: R-02 se cierra cuando Vulcan y New Glenn completen dos misiones consecutivas sin anomalías cada uno; R-03 al lanzarse el servicio comercial; R-04 cuando la FCC resuelva un pedido de alivio, cuando Amazon alcance 3.232 satélites operativos o el 30/07/2029, lo que ocurra primero; R-05 el 30/03/2028 (o antes si Amazon alcanza el 50% operativo); los demás si el disparador no se activa durante un año.

**Conexión con seguimiento y valor ganado** `[INFERENCIA DEL GRUPO]`: si el avance se mide en satélites operativos, Amazon proyectó ≈ 700 al 30/07/2026 (DA 26-553 ¶8) y había ≈ 396; el índice de desempeño del cronograma (SPI) sería ≈ 0,57 (396 ÷ 700). Supuestos: los satélites operativos son una medida de avance válida; ≈ 700 fue el plan de Amazon para esa fecha; no hubo lanzamientos entre el 02/07 y el 15/11 (#2).

**Eficacia de la gestión.** El indicador cualitativo disponible es la exposición total antes (0,82) y después de responder (0,50), y la cantidad de rojos (2 antes, 1 después). El ROI de la gestión de riesgos requiere montos en dólares y no puede calcularse.

## 8. Limitaciones y datos pendientes

**Datos no públicos.** Costo de un satélite, monto de la fianza, costo de cada respuesta y reserva gerencial. No se completaron con cifras inventadas; estimarlos requiere supuestos escritos del grupo. Sin ellos no se pueden calcular el índice de riesgo, el apalancamiento ni el ROI.

**Lo que no pudo verificarse** (búsqueda del 16/11/2026): si la FCC ejecutó la pérdida de la fianza; si NBN Co lanzó su servicio; la causa raíz de la falla de Vulcan y su fecha de retorno al vuelo; el estado de las licencias por país y de la compra de Globalstar.

**Dependencias con otras áreas del informe.**
- Presupuesto (costos): para calcular el índice de riesgo, el apalancamiento y las reservas en dólares.
- Cronograma (tiempos): para fijar las reservas de tiempo sin doble cuenta.
- Unidad y valores de avance (seguimiento y valor ganado): para usar los mismos satélites y el mismo índice.
- EDT (alcance): para reflejar lo que cambia el alcance en R-04.

**Naturaleza de las fuentes.** La mayor parte proviene de comunicados de Amazon, es decir de declaraciones de la propia empresa; las resoluciones de la FCC son documentos primarios leídos en su texto. El original de la orden FCC 20-102 (2020) no pudo leerse y se usó una reproducción parcial para los datos de esa fecha.

## Apéndice R-A. Fuentes citadas

Todas consultadas el 16/11/2026. Las rutas de Amazon son relativas a `https://www.aboutamazon.com`.

| # | Fuente | Ruta o URL | Publicada | Tipo |
|---|---|---|---|---|
| DA 26-553 | FCC, Order sobre el waiver del hito | https://docs.fcc.gov/public/attachments/DA-26-553A1.txt | 05/06/2026 | Primaria (leída) |
| DA 24-224 | FCC, Order and Authorization | https://docs.fcc.gov/public/attachments/DA-24-224A1.pdf | 08/03/2024 | Primaria (leída) |
| 2 | Amazon, Mission updates | /news/innovation-at-amazon/project-kuiper-satellite-rocket-launch-progress-updates | actualizada 15/11/2026 | Primaria |
| 3 | Amazon, primera misión Vulcan | /news/amazon-leo/amazon-leo-vulcan-satellites-launch | 09/11/2026 | Primaria |
| 4 | Amazon, inversión en lanzamientos | /news/innovation-at-amazon/amazon-makes-historic-launch-investment-to-advance-project-kuiper | 05/04/2022 | Primaria |
| 11 | Spaceflight Now, falla del Vulcan | https://spaceflightnow.com/2026/11/15/ula-suffers-first-total-mission-failure-with-loss-of-vulcan-rocket-carrying-40-amazon-leo-satellites/ | 15/11/2026 | Prensa especializada |
| 12 | Spaceflight Now, retorno al vuelo de Vulcan | https://spaceflightnow.com/2026/10/28/united-launch-alliance-announces-mid-november-return-to-flight-for-vulcan-rocket/ | 28/10/2026 | Prensa especializada |
| 18 | DCD, estación terrena en Kenia | https://www.datacenterdynamics.com/en/news/amazon-files-to-place-ground-station-in-kenya-report/ | 2026 | Prensa especializada |
| 22 | Amazon, Globalstar y Apple | /news/company-news/amazon-globalstar-apple | 14/04/2026 | Primaria |
| 23 | Amazon, plan de duplicar la cadencia | /news/amazon-leo/amazon-leo-plans-double-launch-rate-20-missions | 23/03/2026 | Primaria |
| 24 | Amazon, Arianespace, 6 lanzamientos nuevos | /news/amazon-leo/amazon-leo-arianespace-new-launches | 10/09/2026 | Primaria |
| 26 | Amazon, dentro de la fábrica de Kirkland | /news/innovation-at-amazon/inside-project-kuiper-satellite-facility-kirkland | 27/06/2024 | Primaria |
| 29 | Amazon, enterprise preview | /news/amazon-leo/amazon-leo-satellite-internet-ultra-pro | 24/11/2025 | Primaria |
| 30 | Amazon, primera vista de terminales | /news/innovation-at-amazon/heres-your-first-look-at-project-kuipers-low-cost-customer-terminals | 14/03/2023 | Primaria |
| 31 | Amazon, Delta | /news/amazon-leo/amazon-leo-delta-in-flight-wifi-2028 | 31/03/2026 | Primaria |
| 32 | Amazon, Vanu | /news/amazon-leo/amazon-leo-vanu-satellite-internet-connectivity-africa | 26/02/2026 | Primaria |
| 33 | Amazon, Herotel | /news/amazon-leo/amazon-leo-south-africa-herotel-evry | 15/07/2026 | Primaria |
| 35 | Amazon, Uzbekistán | /news/amazon-leo/amazon-leo-uzbekistan | 22/09/2026 | Primaria |
| 36 | Amazon, JetBlue | /news/innovation-at-amazon/jetblue-amazon-project-kuiper-in-flight-wifi-partnership | 04/09/2025 | Primaria |
| 37 | Amazon, Sudamérica y DIRECTV | /news/innovation-at-amazon/amazon-project-kuiper-in-south-america | 12/06/2024 | Primaria |
| 38 | Amazon, Falcon 9 con SpaceX | /news/innovation-at-amazon/amazon-project-kuiper-spacex-launch | 01/12/2023 | Primaria |
| 40 | Amazon Australia, NBN Co | https://www.aboutamazon.com.au/news/innovation/project-kuiper-partners-with-nbn-co-to-bring-low-earth-orbit-satellite-broadband-to-rural-australia | 05/08/2025 | Primaria |
| 47 | AP vía OPB, explosión de New Glenn en plataforma | https://www.opb.org/article/2026/05/29/blue-origin-rocket-explodes-on-the-launch-pad-during-an-engine-firing-test/ | 29/05/2026 | Prensa (confirmada por varios medios) |

## Apéndice R-B. Código del análisis cuantitativo

El archivo `analisis_cuantitativo.py` (Python 3, sin dependencias externas) reproduce los resultados de la sección 5 con `python3 analisis_cuantitativo.py`. Usa una semilla fija, por lo que el resultado es repetible. Todos los supuestos están en las constantes del encabezado del archivo.
