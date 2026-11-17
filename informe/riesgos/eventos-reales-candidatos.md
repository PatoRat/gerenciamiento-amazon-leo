# Eventos y condiciones reales candidatos a riesgo — Amazon Leo

**Esto NO es el registro de riesgos.** Son hechos con fuente que podrías usar como punto de partida. No asigno probabilidad, impacto, estrategia ni propietario: eso es tuyo.
Fecha de corte: 16/11/2026. Las referencias `#n` apuntan al registro de fuentes (#1 a #20) o a las fuentes nuevas propuestas en `I-2-borrador/hitos.md` (#21 a #46, pendientes de aprobación del equipo).
Cada fila separa el **hecho** (`[DATO REAL]`) de la **lectura** posible (`[INFERENCIA DEL GRUPO]`, con supuestos).

Categorías según la RBS de la cátedra.

---

## A. Riesgos externos (regulación)

| # | Hecho `[DATO REAL]` | Fuente | Lectura posible / pregunta para vos |
|---|---|---|---|
| E1 | La FCC exigía 1.616 satélites operativos al 30/07/2026 y 3.232 al 30/07/2029. Concedió un waiver parcial el 05/06/2026, no una prórroga. | #8 ¶3, ¶11 | ¿Qué riesgo había antes del waiver? ¿Se materializó? |
| E2 | Los satélites no desplegados al 30/07/2026 pierden la prioridad de espectro hasta el 30/03/2028 (o 30/10/2027 si Amazon certifica que construyó el 50% y contrató lanzamientos). | #8 ¶15, ¶22–23 | Riesgo con disparador explícito: la certificación de 15 meses. |
| E3 | Si falla el hito de 2029, la autorización se reduce al número de satélites operativos a esa fecha. | #8 ¶12 | Consecuencia sobre el alcance. |
| E4 | La FCC no eximió la fianza: si no se alcanzaba el 50%, Amazon la pierde. | #8 ¶18 | Impacto directo en costos. El monto de la fianza **no se encontró**. |
| E5 | SpaceX tenía pendiente una solicitud de revisión de la orden de desechos orbitales de 2023 y se opuso a Amazon en 2019. | #7, #45 | Riesgo regulatorio o de competencia; la fuente de 2019 es secundaria. |
| E6 | La adquisición de Globalstar tiene cierre previsto en 2027, sujeto a aprobaciones regulatorias e hitos de satélites HIBLEO-4. | #22 | Condición externa sobre la línea D2D. |
| E7 | Licencias nacionales por país (Uzbekistán, Sudáfrica, Australia, Kenia): sin verificar. | #18, #33 | `NO VERIFICADO`: marcá como supuesto si lo usás. |

---

## B. Riesgos técnicos y de lanzamiento

| # | Hecho `[DATO REAL]` | Fuente | Lectura posible / pregunta para vos |
|---|---|---|---|
| T1 | El 15/11/2026 el Vulcan falló unos 10 minutos tras el despegue: se perdieron los 40 satélites de la misión LV-01. Causa raíz no publicada. | #2, #11 | **Riesgo materializado.** ¿Cuál era el riesgo del plan original? ¿qué respuesta tenía? |
| T2 | Hubo un hold en T-20 s antes del lanzamiento, sin explicar. | #11 | ¿Señal temprana o ruido? No se sabe si influyó. |
| T3 | Vulcan estuvo ~9 meses en tierra antes de este vuelo por problemas en los boosters sólidos. | #12 | Antecedente: riesgo del proveedor ya visible antes de LV-01. |
| T4 | Una fuente reporta una explosión de New Glenn en plataforma en 05/2026. Amazon tiene 24 lanzamientos New Glenn firmes y ninguno voló. | #11, #23 | Corroborar con otra fuente antes de citar. |
| T5 | Las órdenes de la FCC prohíben desplegar satélites directo a la altitud operativa. | #7 ¶43 | Restricción técnica de la secuencia de lanzamiento y operación. |

---

## C. Riesgos de gestión (proveedores, cronograma, costos)

| # | Hecho `[DATO REAL]` | Fuente | Lectura posible / pregunta para vos |
|---|---|---|---|
| G1 | Amazon proyectó ~700 satélites desplegados al 30/07/2026 y tenía ~396. | #8 ¶8, #2 | `[INFERENCIA]`: desvío del 43% contra su propio plan, si "desplegados" equivale a "en órbita". |
| G2 | El inicio del servicio comercial se corrió: 2024 (dicho en 2023), 2025 (dicho en 2024), 2026 (dicho en 2025). Sigue sin anunciarse al 16/11/2026. | #30, #26, #29, #3 | `[INFERENCIA]`: requiere asumir que las frases se refieren al mismo hito. |
| G3 | Contratos de lanzamiento: Arianespace 24, ULA 38 Vulcan + 9 Atlas V, New Glenn 24, Falcon 9 13. Total ~108. | #24, #3, #4, #23, #38 | `[INFERENCIA]`: Vulcan y New Glenn suman 62 de 108 (57%); concentración de proveedor. |
| G4 | Amazon completó el satélite n.º 1.000 a inicios de 09/2026. Los lanzados eran 396 al 02/07/2026. | #3, #2 | `[INFERENCIA]`: posible stock de satélites fabricados sin lanzar (riesgo de almacenamiento y de costo hundido). Supuestos: los 1.000 incluyen los ya lanzados y no hubo otros lanzamientos exitosos entre julio y septiembre. |
| G5 | La capacidad declarada de fabricación fue 4/día (2022), 5/día (2024) y 30/semana (2026). | #25, #26, #23 | Capacidad ≠ ritmo real. Ritmo de fábrica vs cadencia de lanzamiento. |
| G6 | Inversión: "multibillion-dollar investment" (Amazon); "más de US$10 mil millones" en 2020, a confirmar. Costo por satélite y por lanzamiento: **no público**. | #22, #39 | Costos de respuesta tendrán que ser tuyos, con supuestos. |

---

## D. Riesgos de organización y de negocio

| # | Hecho `[DATO REAL]` | Fuente | Lectura posible / pregunta para vos |
|---|---|---|---|
| O1 | El servicio depende de socios locales y distribuidores (Herotel, UZ-SAT, Vanu, DIRECTV LatAm, NBN Co). | #33, #35, #32, #37, #40 | Dependencia de terceros en la última milla. |
| O2 | Amazon es la única que diseña, fabrica y opera el sistema ("in-house"). | #22 | `[INFERENCIA]`: concentra riesgo técnico en una sola organización. |
| O3 | El tamaño del segmento terrestre (estaciones) no es público. | #17 | `NO VERIFICADO`. |

---

## E. Oportunidades (la cátedra también las pide)

| # | Hecho `[DATO REAL]` | Fuente |
|---|---|---|
| OP1 | Arianespace amplió su contrato de 18 a 24 lanzamientos (10/09/2026). | #24 |
| OP2 | 10 Falcon 9 adicionales contratados a fines de 2025. | #23 |
| OP3 | Acuerdos con aerolíneas: JetBlue (desde 2027) y Delta (desde 2028, 500 aviones). | #36, #31 |
| OP4 | Adquisición de Globalstar y acuerdo con Apple para direct-to-device (desde 2028). | #22 |
| OP5 | Kirkland con capacidad declarada de "as many as 30 satellites per week". | #23 |

---

## Cómo usar esta lista

1. Elegí **cuáles son riesgos del plan** y cuáles son problemas que ya ocurrieron (T1, E1, G1).
2. Para los que ya ocurrieron, preguntate qué riesgo del plan original representaban.
3. Agregá los que **no** están acá: esto es un punto de partida, no la lista completa. Usá el análisis de supuestos de la cátedra.
4. Reescribí cada uno como "causa → evento → consecuencia" en la plantilla.
5. Todo lo que marqué `NO VERIFICADO` o `[INFERENCIA]` necesita que lo confirmes o lo declares como supuesto.
