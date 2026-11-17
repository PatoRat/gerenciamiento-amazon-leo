# Guía metodológica: Riesgos — Amazon Leo

Marco: **el de la cátedra**. Fuentes leídas (en `PDFs Teoria/` y `Resumen/`):
- `Clase 10 · Gestión de Riesgos · Gerenciamiento y Evaluación de Proyectos · UCA.pdf`
- `Proyectos_10 Riesgos_0100.pdf`
- `Apunte_Gerenciamiento_para_leer.pdf` (capítulo 7, Riesgos)
- `Proyectos_Ejercicio 14 Riesgos_Caso DIA_0100.pdf` (práctica de identificación)

Esta guía explica **cómo** hacerlo. Los riesgos, números y respuestas son tuyos.

---

## 1. Qué es un riesgo, con el vocabulario de la cátedra

- Un riesgo es un **evento o condición incierta** que, si ocurre, afecta al menos un objetivo (costo, plazo, alcance o calidad). Tiene causa(s), evento y consecuencia(s).
- **Riesgo vs. problema:** un riesgo es un problema que todavía no ocurrió; un problema es un riesgo que ya se materializó.
- El riesgo **puede ser una oportunidad**, no solo una amenaza.
- **Conocidos vs. desconocidos:** los conocidos se gestionan de forma proactiva; para los desconocidos se prevé reserva.
- **Exposición al Riesgo:** `ER = Probabilidad × Consecuencia`.

> **Aplicación a Amazon Leo:** la falla del Vulcan del 15/11/2026 es un riesgo **materializado**, o sea un problema. Pregunta de diseño: ¿ese riesgo estaba en el registro? ¿con qué respuesta y qué disparador? Es un buen caso para el informe. Ver `eventos-reales-candidatos.md`.

---

## 2. Los seis procesos (en orden, cíclicos)

### Paso 1 — Planificar la gestión de riesgos
Decidí **cómo** vas a gestionar. Definí:
- **Categorías (RBS):** técnicos, gestión del proyecto, organización, externos.
  - Técnicos: requerimientos, complejidad, tecnología, performance, calidad.
  - Gestión: contratistas, recursos, fondos, estimación, planificación, control, comunicaciones.
  - Organización: cliente, prioridades, cultura.
  - Externos: regulaciones, mercado, clima.
- **Apetito al riesgo:** aversión, búsqueda o indiferencia.
- **Tolerancia y umbrales:** variación aceptable por objetivo, con disparadores.

*Cómo justificarlo:* mirá cómo se comporta Amazon (qué decisiones tomó, cuánto invirtió, qué asumió). Eso es una `[INFERENCIA]` sobre su apetito; tu umbral es una `[PROPUESTA]`.

### Paso 2 — Identificar riesgos
Técnicas de la cátedra: check-lists, base de datos de proyectos anteriores, entrevistas, revisiones, brainstorming, formularios, encuestas y **análisis de supuestos**.

Para este trabajo, las más útiles son:
- **Análisis de supuestos:** ¿qué supone el plan de Amazon que podría no cumplirse? (lanzadores disponibles, aprobación regulatoria, ritmo de fábrica).
- **Base de datos de otros proyectos:** el caso del aeropuerto de Denver (práctica 14 de la cátedra) sirve como analogía de un sistema nuevo, complejo y con cronograma ajustado.
- **Lista de eventos reales:** ver `eventos-reales-candidatos.md`.

Cómo se redacta: **"Debido a [causa], puede ocurrir [evento], lo que provocaría [consecuencia]"**. La práctica de la cátedra pide descripciones claras y no ambiguas, y que cada grupo pueda defender por qué algo es un riesgo.

Producto: la **lista depurada** y la lista de respuestas potenciales, dentro del Registro de Riesgos.

### Paso 3 — Análisis cualitativo
Priorizar. Asigná probabilidad (0 a 1) e impacto por objetivo, con las **escalas de la cátedra**.

| Probabilidad | Valor |
|---|---|
| Muy alta | > 0,81 |
| Alta | 0,61 a 0,80 |
| Moderada | 0,41 a 0,60 |
| Baja | 0,21 a 0,40 |
| Muy baja | 0,01 a 0,20 |

| Objetivo | Muy bajo | Bajo | Moderado | Alto | Muy alto |
|---|---|---|---|---|---|
| Costo | Insignificante | < 5% | 5–10% | 10–20% | > 20% |
| Plazo | Insignificante | < 5% | 5–10% | 10–20% | > 20% |
| Alcance | Imperceptible | Secundario | Principal | Inaceptable | Totalmente inútil |
| Calidad | Imperceptible | Funciones exigentes | Importante | Inaceptable | Totalmente inutilizable |

Valores numéricos de impacto de la matriz de la cátedra: **0,05 / 0,10 / 0,20 / 0,40 / 0,80**. Probabilidades de la matriz: **0,10 / 0,30 / 0,50 / 0,70 / 0,90**.

Matriz P × I de la cátedra (la ER sale de multiplicar):

| P \ I | 0,05 | 0,10 | 0,20 | 0,40 | 0,80 |
|---|---|---|---|---|---|
| 0,90 | 0,05 | 0,09 | 0,18 | 0,36 | 0,72 |
| 0,70 | 0,04 | 0,07 | 0,14 | 0,28 | 0,56 |
| 0,50 | 0,03 | 0,05 | 0,10 | 0,20 | 0,40 |
| 0,30 | 0,02 | 0,03 | 0,06 | 0,12 | 0,24 |
| 0,10 | 0,01 | 0,01 | 0,02 | 0,04 | 0,08 |

- La cátedra remarca: **importan más los colores que los números**. Rojo = realmente inaceptable, amarillo = inaceptable, verde = aceptable, azul = muy bajo (puede ser oportunidad). Los umbrales entre colores **dependen del apetito**: definilos vos y justificalos.
- **Ejemplo de la cátedra (Proyecto Anguila):** tecnología nueva con impacto 0,40 y probabilidad 0,70 → ER = 0,28 (alto). Rotación del equipo con impacto 0,40 y probabilidad 0,10 → ER = 0,04 (bajo). Es un ejemplo de la cátedra: **no lo copies como si fuera de Amazon Leo**.

Salida: lista ordenada por prioridad, riesgos agrupados por categoría, lista de respuestas urgentes y lista de seguimiento de baja prioridad.

### Paso 4 — Análisis cuantitativo
Mide numéricamente el efecto sobre plazo y presupuesto. Sirve para dimensionar **reservas**, saber la probabilidad de cumplir plazo o costo e identificar qué riesgos pesan más.

Técnica de la cátedra: **simulación Monte Carlo** (red del proyecto → distribución de duraciones → valores al azar → repetir n veces → plazo con x% de confianza).

*Realidad del trabajo:* Amazon no publica su red ni sus duraciones. Para hacerlo necesitás antes el cronograma que reconstruya el área de tiempos. **Decidí con el equipo si lo hacen**; si no, dejá escrito que el análisis cuantitativo queda fuera y por qué. No inventes distribuciones sin justificarlas: son `[PROPUESTA]` con supuestos.

### Paso 5 — Planificar la respuesta
Cada respuesta es un compromiso entre su **costo** y la consecuencia que evita. Cada riesgo tiene un **propietario**.

| Estrategia | Qué es | Cuándo conviene |
|---|---|---|
| Evitar | Cambiar el plan para eliminar el riesgo. | Riesgos graves y probables, mejor temprano. |
| Transferir | Pasar la consecuencia y la responsabilidad a un tercero (seguro, contrato de precio fijo, tercerizar). No elimina el riesgo y puede crear otros. | Cuando otro lo gestiona mejor. |
| Mitigar | Reducir probabilidad o consecuencia con acciones tempranas. | Cuando prevenir cuesta menos que la consecuencia. |
| Aceptar | Asumir la consecuencia. **Pasiva:** sin plan ni reserva, decisión explícita. **Activa:** con reserva y plan de contingencia (disparadores, acciones, responsables, recursos). | Cuando responder cuesta más que el daño. |

- **Reservas de contingencia:** para riesgos **conocidos**, asociadas a tareas, forman parte de la línea base. **Reservas gerenciales:** para **desconocidos**, asociadas al proyecto, no forman parte de la línea base de costos.
- **Elegir entre alternativas:** `Apalancamiento = (ER antes − ER después) / costo de la alternativa`. Compará al menos dos alternativas por cada riesgo importante.
- **Riesgos residuales** (los que quedan) y **secundarios** (los que crea tu respuesta) también se registran.

> **Aplicación a Amazon Leo:** una respuesta típica a la concentración de lanzadores es contratar proveedores adicionales. Amazon amplió contratos: Arianespace subió de 18 a 24 lanzamientos y se sumaron 10 Falcon 9 (`[DATO REAL]`). Amazon no dice que sea una respuesta a la concentración de proveedores: leerlo así es una `[INFERENCIA]` tuya y necesita su supuesto. Pregunta de diseño: ¿qué riesgo secundario crea? ¿cuánto cuesta? (el costo es `NO VERIFICADO`; vas a tener que estimarlo con supuestos).

### Paso 6 — Supervisar y controlar
Los riesgos cambian. Verificá si las respuestas se implementaron y funcionan, seguí los disparadores y la evolución de la ER, detectá riesgos nuevos, revisá supuestos y cerrá los que ya no apliquen.

Indicadores de la cátedra:
- **Índice de riesgo** = Σ ER ÷ Σ costos del proyecto (hay que incluir todos los riesgos).
- **ROI de la gestión de riesgos** = ahorros ÷ costos de gestión (en Anguila: 138.000 / 61.500 = 2,24).

---

## 3. Cómo conectar con las otras áreas (criterio de coherencia)

- **Costos:** la reserva de contingencia y la gerencial salen de acá y entran en el presupuesto. Sincronizá montos.
- **Tiempos:** una reserva de tiempo se refleja en el cronograma. Cuidado: acelerar (fast tracking, crashing) aumenta el riesgo.
- **Alcance:** si una respuesta cambia entregables, debe reflejarse en la EDT.
- **Estimaciones:** una estimación es una probabilidad, no una certeza.
- **Seguimiento:** los disparadores se miden en la ejecución con indicadores de valor ganado.

---

## 4. Errores frecuentes (para revisar tu trabajo)

- Listar riesgos sin **causa y consecuencia** (son preocupaciones, no riesgos).
- **Confundir riesgo con problema.** Lo que ya pasó es un problema; para el informe, preguntate qué riesgo del plan original se materializó.
- Poner P e I **sin justificación**. Cada número es una propuesta que tenés que poder defender.
- **Miopía selectiva:** registrar solo los riesgos fáciles de controlar.
- Asignar un propietario que no existe en la organización.
- No cerrar el ciclo: sin disparadores ni seguimiento, el registro no sirve.
- Mezclar etiquetas: un hecho es `[DATO REAL]`; tu valoración es `[PROPUESTA]`.

---

## 5. Preguntas probables de defensa

1. ¿Por qué ese riesgo y no otro? ¿Cómo los identificaron?
2. ¿Por qué esa probabilidad y ese impacto? ¿En qué evidencia se basan?
3. ¿Cuánto apetito al riesgo tiene Amazon y cómo lo saben?
4. ¿Qué riesgos ya se materializaron y qué hicieron ustedes con eso?
5. ¿Por qué eligieron esa estrategia en vez de otra? Muestren el apalancamiento.
6. ¿Cuánta reserva propusieron y cómo se vincula con costos y cronograma?
7. ¿Qué riesgo secundario genera su respuesta?
8. ¿Qué disparador les avisa que el riesgo se acerca?
9. ¿Qué parte es dato real y qué parte es propuesta suya?
10. ¿Qué riesgos son desconocidos y cómo los cubren?

---

## 6. Orden de trabajo sugerido

1. Completar la Parte 0 de la plantilla (apetito, umbrales, categorías).
2. Armar la lista preliminar de riesgos desde `eventos-reales-candidatos.md` y el análisis de supuestos. Idealmente 10 a 15, depurada.
3. Puntuar P e I y calcular ER; armar la matriz con colores.
4. Elegir estrategia y alternativas para los rojos y amarillos; calcular apalancamiento.
5. Cuadrar reservas con costos y tiempos.
6. Definir disparadores y seguimiento.
7. Pasarme la sección para revisar trazabilidad y coherencia.
