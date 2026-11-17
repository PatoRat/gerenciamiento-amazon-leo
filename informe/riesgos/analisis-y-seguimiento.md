# Partes 2 y 3 — Análisis y seguimiento de riesgos (Amazon Leo)

**Estado: revisado y aprobado por el autor el 16/11/2026**, salvo los pendientes que dependen de otras áreas. Fecha de corte y consulta: 16/11/2026.
Todo lo de la Parte 2 sale de los valores ya aprobados en `registro-riesgos.md`; no agrega juicios nuevos salvo donde se indica. En la Parte 3, las **frecuencias y umbrales son propuestas** `[PROPUESTA DE GESTIÓN]` (borrador IA) que tenés que revisar.
`[[PENDIENTE]]` = dato que falta o depende de otra área. Declaración de uso de IA: ver `borrador-parte0.md`.

---

# Parte 2 — Análisis

## 2.1 Lista de riesgos por prioridad (antes de responder)

| Orden | ID | Riesgo | P | C | ER | Color |
|---|---|---|---|---|---|---|
| 1 | R-04 | No cumplir el hito FCC de 2029 | 0,70 | 0,40 | 0,28 | Rojo |
| 2 | R-02 | Lanzador clave en tierra | 0,50 | 0,40 | 0,20 | Rojo |
| 3 | R-03 | Desvío de cronograma y servicio | 0,70 | 0,20 | 0,14 | Amarillo |
| 4 | R-05 | Prioridad de espectro | 0,30 | 0,20 | 0,06 | Verde |
| 4 | R-07 | Aprobaciones regulatorias | 0,30 | 0,20 | 0,06 | Verde |
| 6 | R-06 | Socios locales | 0,50 | 0,10 | 0,05 | Verde |
| 7 | R-01 | Falla de un lanzador | 0,30 | 0,10 | 0,03 | Azul |

## 2.2 Matriz de probabilidad e impacto

Matriz de la cátedra (P × I) con los cortes de color aprobados (rojo ≥ 0,20 · amarillo 0,10–0,19 · verde 0,05–0,09 · azul < 0,05). Entre corchetes, el color; en **negrita**, dónde cae cada riesgo.

| P \ I | 0,05 | 0,10 | 0,20 | 0,40 | 0,80 |
|---|---|---|---|---|---|
| **0,90** | 0,05 [V] | 0,09 [V] | 0,18 [A] | 0,36 [R] | 0,72 [R] |
| **0,70** | 0,04 [Az] | 0,07 [V] | **R-03** 0,14 [A] | **R-04** 0,28 [R] | 0,56 [R] |
| **0,50** | 0,03 [Az] | **R-06** 0,05 [V] | 0,10 [A] | **R-02** 0,20 [R] | 0,40 [R] |
| **0,30** | 0,02 [Az] | **R-01** 0,03 [Az] | **R-05, R-07** 0,06 [V] | 0,12 [A] | 0,24 [R] |
| **0,10** | 0,01 [Az] | 0,01 [Az] | 0,02 [Az] | 0,04 [Az] | 0,08 [V] |

[R] = rojo · [A] = amarillo · [V] = verde · [Az] = azul.

**Lo que muestra el mapa:** el riesgo se concentra en la columna de impacto 0,40 (alto) y en las filas de probabilidad 0,50 y 0,70. Los dos rojos están en esa zona. Los demás son bajos: ninguno con impacto 0,80.

**Nota sobre el apetito:** según la cátedra, distintos apetitos producen mapas distintos. Los cortes de color son una propuesta aprobada por vos (apetito "búsqueda moderada"). Con un apetito de aversión, R-03 podría pasar a rojo.

## 2.3 Riesgos con respuesta urgente

Los rojos: **R-04** y **R-02**. Ambos ya tienen estrategia y respuesta definidas (mitigar). R-04 sigue en rojo tras responder.

## 2.4 Lista de seguimiento de riesgos de baja prioridad

**R-05, R-06 y R-07** (verdes, en la lista de seguimiento). **R-01** (azul) se desarrolló porque ya ocurrió una vez y hay un plan de contingencia, pero por su severidad también encaja en esta lista. Decisión del autor: R-01 queda desarrollado.

## 2.5 Concentración por categoría

| Categoría (RBS) | Riesgos | Suma de ER |
|---|---|---|
| Externo | R-04, R-05, R-07 | 0,40 |
| Gestión del proyecto | R-02, R-03 | 0,34 |
| Organización | R-06 | 0,05 |
| Técnico | R-01 | 0,03 |

**[INFERENCIA DEL GRUPO]** El riesgo se concentra en **regulación (externo)** y en **gestión de proveedores y cronograma**, no en lo técnico. Es coherente con el objetivo que se eligió proteger (plazo) y con el hecho de que el mayor daño viene de un lanzador en tierra y de los hitos de la FCC, más que de fallas del satélite.
→ Base: sección 2.1. Supuesto: la suma de ER entre riesgos es una referencia relativa, no una medida monetaria, porque C está en una escala y no en dólares.

## 2.6 Reservas

| Riesgo | Tipo de reserva | Monto |
|---|---|---|
| R-01 | Contingencia | Reposición de 40 satélites (unidades). USD: `[[PENDIENTE]]` |
| R-02 | Contingencia (tiempo) | ≈ 4 meses en el cronograma maestro. Costo: `[[PENDIENTE]]` |
| R-03 | Contingencia (tiempo) | `[[PENDIENTE: coordinar con el área de tiempos]]` |
| R-04 | Contingencia (costo) | Monto de la fianza y costo de ampliar la cadencia: `[[PENDIENTE: no público]]` |
| Riesgos desconocidos | Gerencial | `[[PENDIENTE: porcentaje que decida el equipo, con el área de costos]]` |

**Cuidado con la doble cuenta:** la reserva de tiempo de R-02 (lanzador en tierra) alimenta el atraso de R-03 (servicio) y el de R-04 (hito 2029). Si se suman sin más, el cronograma queda inflado. Hay que acordarlo con el área de tiempos antes de fijar números.
**Reglas de la cátedra:** las reservas de contingencia (riesgos conocidos) forman parte de la línea base; las gerenciales (desconocidos) no forman parte de la línea base de costos, aunque sí del costo total.

## 2.7 Efecto de las respuestas (referencia relativa)

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

**[INFERENCIA DEL GRUPO]** Las respuestas propuestas bajan la exposición total en ≈ 39% ((0,82 − 0,50) ÷ 0,82), pero **R-04 sigue en rojo**.
→ Base: fichas del registro. Supuesto: los valores "después" son propuestas del grupo, no mediciones.

## 2.8 Índice de riesgo y apalancamiento

- **Índice de riesgo** (cátedra): Σ ER ÷ Σ costos del proyecto. **No se puede calcular:** C está expresado en una escala, no en dólares, y no hay un costo total del proyecto público. `[[PENDIENTE: requiere el presupuesto del área de costos y expresar los impactos en USD]]`.
- **Apalancamiento** (cátedra): (ER antes − ER después) ÷ costo de la alternativa. **No se puede calcular:** el costo de cada alternativa no es público. `[[PENDIENTE]]`.
- Si el área de costos entrega un presupuesto, estas dos cuentas se completan en una hora.

## 2.9 Análisis cuantitativo

La cátedra propone la simulación de Monte Carlo para estimar la probabilidad de cumplir un objetivo (Clase 10, "Análisis cuantitativo"). Amazon no publica su red de actividades ni sus duraciones, así que no se puede simular el cronograma interno. Lo que sí se puede simular con datos públicos es **la cantidad de satélites operativos al 30/07/2029**, que es la medida del hito de R-04. El código está en `analisis_cuantitativo.py` y es reproducible.

**Datos de entrada** `[DATO REAL]`: 396 satélites lanzados antes de LV-01 (#2); hito final de 3.232 (DA 26-553 ¶3); 32,5 meses entre el 16/11/2026 y el 30/07/2029.

**Supuestos** `[PROPUESTA DE GESTIÓN]` (el grupo los define; no son datos publicados):
- Cadencia en misiones por mes, distribución triangular: mínimo 0,5 (lanzadores clave en tierra buena parte del período, R-02), moda 0,92 (ritmo observado desde el 28/04/2026, ≈ 11 por año, #2) y máximo 2,0 (el plan de Amazon de "20+ misiones" en el año dos, #23, y algo más).
- Satélites por misión, triangular: mínimo 24, moda 30, máximo 40 (rango de #2 y #3).
- La cadencia se mantiene constante durante todo el período (no se modela una aceleración gradual).

**Escenarios determinísticos** `[INFERENCIA DEL GRUPO]` (30 satélites por misión):

| Escenario | Misiones por año | Misiones hasta el hito | Satélites al 30/07/2029 | % de 3.232 |
|---|---|---|---|---|
| Ritmo observado | 11 | ≈ 30 | ≈ 1.290 | 40% |
| Plan de Amazon | 20 | ≈ 54 | ≈ 2.020 | 63% |
| Ritmo necesario | 35 | ≈ 95 | ≈ 3.240 | 100% |

Con 40 satélites por misión (el lote de Vulcan) la cuenta mejora, pero el plan de 20 por año llegaría solo a ≈ 2.560 (79%); la cadencia necesaria bajaría a ≈ 26 por año, todavía por encima del plan.

**Resultado de la simulación** (100.000 corridas):

| Percentil | Satélites al 30/07/2029 | % de 3.232 |
|---|---|---|
| P10 | ≈ 1.140 | 35% |
| P50 | ≈ 1.510 | 47% |
| P90 | ≈ 2.050 | 63% |
| **Probabilidad de llegar a 3.232** | **≈ 0%** | |

**Sensibilidad al máximo de cadencia:** subiendo el máximo de 2,0 a 3,5 misiones por mes (más del triple del ritmo observado), la probabilidad de llegar recién sube a ≈ 7%.

**[INFERENCIA DEL GRUPO] Lectura:** con la cadencia observada o con la del propio plan de Amazon, **llegar a 3.232 satélites antes del 30/07/2029 es prácticamente imposible**. Llegar exigiría ≈ 35 misiones por año, 3 veces el ritmo observado y casi el doble del plan.
→ Base: los datos de entrada y los supuestos de arriba. Limitaciones: (a) el modelo ignora una posible aceleración gradual de la cadencia; (b) usa un promedio de satélites por misión; (c) no incluye fallas de lanzamiento (que empeorarían el resultado); (d) las distribuciones son supuestos del grupo.

**Consecuencia para R-04:** como la probabilidad de no llegar es ≈ 1, la incertidumbre de R-04 **no está en la cadencia sino en si la FCC concede otro alivio**. P = 0,70 equivale a suponer ≈ 30% de probabilidad de un nuevo waiver o prórroga `[PROPUESTA DE GESTIÓN]`; no hay un dato que lo respalde, solo el antecedente del waiver parcial de 2026 (DA 26-553 ¶11).

**Uso de reservas:** este análisis no calcula reservas de costo porque falta el presupuesto; la reserva de tiempo se vincula con el área de tiempos.

---

# Parte 3 — Seguimiento

## 3.1 Disparadores a vigilar

Frecuencias y umbrales: `[PROPUESTA DE GESTIÓN]` (borrador IA, aprobada por el autor). Cada uno es una decisión del grupo; si el resto del equipo propone otros, hay que coordinarlos.

| Indicador | Riesgo | Cómo se mide | Umbral que activa la respuesta | Fuente de datos | Frecuencia |
|---|---|---|---|---|---|
| Anomalía o hold sin explicar en un vuelo Vulcan | R-01, R-02 | Evento por misión | Cualquier anomalía | ULA; Amazon (#2) | Por misión |
| Fecha de retorno al vuelo de Vulcan y de New Glenn | R-02 | Fecha anunciada | Sin fecha tras 3 meses de la falla | ULA; Blue Origin; Amazon | Mensual |
| Cadencia de los últimos 6 meses | R-04 | Misiones realizadas | Menos de ≈ 17 misiones en 6 meses (35 por año ÷ 2) | Lista de misiones de Amazon (#2) | Mensual |
| Satélites operativos por mes | R-04 | Acumulado ÷ meses | Menos de ≈ 87 por mes | Lista de misiones (#2) | Mensual |
| Anuncio del servicio comercial | R-03 | Fecha de anuncio | Sin anuncio al 30/11/2026 | Amazon | Puntual |
| Nueva ronda de procesamiento de la FCC o pedido de coordinación | R-05 | Evento | Cualquiera | FCC | Trimestral |
| Certificación del 50% construido y lanzamientos contratados | R-05 | Fecha | Antes del 30/10/2027 | FCC (DA 26-553 ¶15) | Trimestral |
| Fecha de lanzamiento confirmada por cada socio | R-06 | Fecha | Un socio sin fecha | Amazon; socios | Trimestral |
| Avance de la aprobación de Globalstar | R-07 | Estado | Cierre corrido más allá de 2027 | Amazon (#22) | Trimestral |

**De dónde salen los números de los dos indicadores de cadencia** (`[INFERENCIA DEL GRUPO]`): para llegar a 3.232 satélites desde 396, faltan 2.836 en ≈ 32,5 meses, o sea ≈ 87 por mes (2.836 ÷ 32,5). El ritmo observado es ≈ 21 por mes (396 ÷ 18,6 meses desde el 28/04/2025). Supuestos: el ritmo de 396 en 18,6 meses se mantiene como referencia; el hito final es el 30/07/2029.
→ Base: DA 26-553 ¶3; #2.

## 3.2 Reevaluación

**[PROPUESTA DE GESTIÓN]** Reestimar P y C **cada trimestre** y **después de cada evento** (una falla, un anuncio de la FCC, un cambio de calendario). Se compara la ER nueva con la inicial. Frecuencia aprobada por el autor.

## 3.3 Riesgos nuevos y supuestos a revisar

La cátedra pide revisar la validez de los supuestos a medida que avanza el proyecto. Los que sostienen este registro:

| Supuesto | Riesgo que lo usa | Se invalida si |
|---|---|---|
| Los 38 Vulcan y los 24 New Glenn siguen contratados | R-01, R-02 | Amazon cancela o reasigna contratos |
| ≈ 30 satélites por misión | R-04 | Cambia el tamaño de los lotes |
| La FCC no concede otro waiver | R-04 | La FCC otorga una prórroga |
| El hito de 2026 no se cumplió | R-05 | Amazon demuestra otro conteo |
| Las frases sobre el inicio del servicio se refieren al mismo hito | R-03 | Amazon define dos hitos distintos |

Para riesgos nuevos: revisar la lista cada trimestre con el método de análisis de supuestos y brainstorming (técnicas de la cátedra).

## 3.4 Criterios de cierre

**[PROPUESTA DE GESTIÓN]** (aprobada por el autor, salvo el último punto)
- **R-05:** se cierra el 30/03/2028 (o antes si Amazon alcanza el 50% operativo).
- **R-04:** se cierra al alcanzar 3.232 satélites operativos o el 30/07/2029.
- **R-02:** se cierra cuando Vulcan y New Glenn completen **dos misiones consecutivas sin anomalías cada uno** (criterio del autor).
- **R-03:** se cierra al lanzarse el servicio comercial.
- Los demás se cierran si el disparador no se activa durante un año `[[REVISAR]]`.

## 3.5 Eficacia de la gestión

- **ROI de la gestión de riesgos** (cátedra: ahorros ÷ costos de gestión): `[[PENDIENTE: requiere montos en USD]]`. Aclaración: la cátedra muestra el caso Proyecto Anguila (138.000 ÷ 61.500 = 2,24); es un ejemplo de la cátedra, no un dato de Amazon.
- **Indicador cualitativo disponible:** ER total antes (0,82) y después de responder (0,50), y la cantidad de rojos (2 antes, 1 después).

## 3.6 Conexión con seguimiento y valor ganado (para coordinar con tus compañeros)

**[INFERENCIA DEL GRUPO]** Si el área de seguimiento mide el avance en satélites operativos, la referencia del plan es: Amazon proyectó ≈ 700 satélites desplegados al 30/07/2026 (DA 26-553 ¶8) y había ≈ 396. Eso daría un índice de desempeño del cronograma (SPI) de ≈ 0,57 (396 ÷ 700).
→ Base: DA 26-553 ¶8; #2. Supuestos: (a) los satélites operativos son una medida de avance válida; (b) la proyección de ≈ 700 fue el plan de Amazon para esa fecha; (c) a esa fecha había ≈ 396 (sin lanzamientos entre el 02/07 y el 15/11, según #2).
`[[PENDIENTE]]` Coordinar con quien tome seguimiento y valor ganado para que usen la misma unidad y los mismos valores.

---

## Pendientes de estas partes

- Presupuesto del área de costos para el índice de riesgo y el apalancamiento.
- Cronograma del área de tiempos para fijar las reservas de tiempo sin doble cuenta.
- Decidir con el equipo frecuencias, umbrales y criterios de cierre de la Parte 3.
- Decisión tomada: R-01 queda desarrollado.
