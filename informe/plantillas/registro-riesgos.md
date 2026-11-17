# Plantilla: Registro de Riesgos — Amazon Leo

**Plantilla vacía.** Está para que la completes vos; no trae contenido del informe.
Método y nombres de la cátedra: `Clase 10 · Gestión de Riesgos` y `Proyectos_10 Riesgos_0100` (`PDFs Teoria/`). La guía paso a paso está en `guia-riesgos.md`.

Regla de trazabilidad (obligatoria en `informe/`): cada fila lleva una etiqueta.
- `[DATO REAL]`: solo para lo que describe un hecho con fuente (por ejemplo el evento que ya ocurrió).
- `[INFERENCIA DEL GRUPO]`: conclusión razonable a partir de evidencia, con supuestos escritos.
- `[PROPUESTA DE GESTIÓN]`: la probabilidad, el impacto, la estrategia, el propietario, el disparador y la reserva **son siempre propuesta tuya**, aunque el riesgo parta de un hecho real. Cada una necesita una justificación.

---

## Parte 0 — Planificación de la gestión (se completa una sola vez)

| Campo | Qué va | Tu respuesta |
|---|---|---|
| Objetivos que se protegen | Cuáles de costo, plazo, alcance y calidad pesan más en Amazon Leo y por qué. | `[[COMPLETAR]]` |
| Apetito al riesgo | ¿Aversión, búsqueda o indiferencia? Justificalo con evidencia de cómo actúa Amazon. | `[[COMPLETAR]]` |
| Tolerancia y umbrales | Variación aceptable por objetivo (ej.: "hasta x% de desvío en plazo") y qué dispara una respuesta. | `[[COMPLETAR]]` |
| Categorías (RBS) | Técnicos, gestión del proyecto, organización, externos. Podés abrir subcategorías propias. | `[[COMPLETAR]]` |
| Escalas | Usar las de la cátedra (ver guía) o declarar cuáles cambiás y por qué. | `[[COMPLETAR]]` |
| Etiqueta de esta parte | | `[PROPUESTA DE GESTIÓN]` |

---

## Parte 1 — Registro de riesgos (una fila por riesgo)

Copiá la fila tantas veces como riesgos tengas. Cada riesgo se escribe como **causa → evento incierto → consecuencia**, sin ambigüedad.

| Campo | Qué va |
|---|---|
| **ID** | R-01, R-02… |
| **Categoría (RBS)** | Técnico / Gestión / Organización / Externo |
| **Tipo** | Amenaza u oportunidad |
| **Descripción** | "Debido a `[causa]`, puede ocurrir `[evento]`, lo que provocaría `[consecuencia]`." |
| **Etiqueta y base** | `[DATO REAL]` + fuente `#n` / `[INFERENCIA]` + supuestos |
| **Objetivo afectado** | Costo, plazo, alcance o calidad |
| **Probabilidad (P)** | Un valor entre 0 y 1, o la categoría de la escala |
| **Impacto (C)** | Valor de la escala (0,05 / 0,10 / 0,20 / 0,40 / 0,80) |
| **Exposición (ER)** | P × C |
| **Color de la matriz** | Rojo / amarillo / verde / azul, según tu mapa |
| **Estrategia** | Evitar / Transferir / Mitigar / Aceptar (pasiva o activa) |
| **Respuesta** | Qué se hace, en concreto |
| **Propietario** | Un rol de la organización (puede salir de `actores.md`) |
| **Disparador / señal temprana** | Qué dato indica que el riesgo se acerca |
| **Plan de contingencia** | Solo si aceptás activamente: acciones, responsables, recursos |
| **Costo de la respuesta** | En USD, con su base |
| **ER después de responder** | P y C reestimados |
| **Apalancamiento** | (ER antes − ER después) / costo de la respuesta |
| **Reserva** | Contingencia (riesgo conocido) o gerencial (desconocido), con monto |
| **Riesgo residual / secundario** | Qué queda y qué riesgo nuevo genera la respuesta |
| **Justificación** | Por qué esos valores y esa estrategia (criterio de la cátedra) |

---

## Parte 2 — Análisis (se completa después de la Parte 1)

| Salida | Qué va |
|---|---|
| Lista de riesgos por prioridad | Ordenada por ER. |
| Matriz de probabilidad e impacto | Con los colores y qué apetito refleja. |
| Riesgos con respuesta urgente | Los rojos. |
| Lista de seguimiento de baja prioridad | Los de baja severidad que igual se vigilan. |
| Concentración por categoría | Dónde se agrupan los riesgos (insumo para decidir). |
| Reservas totales | Suma de contingencia y reserva gerencial, y cómo entran al presupuesto (con el área de costos). |
| Índice de riesgo | Suma de ER ÷ costo total del proyecto (necesita el presupuesto del equipo). |

---

## Parte 3 — Seguimiento (qué se vigila durante el proyecto)

| Campo | Qué va |
|---|---|
| Disparadores a vigilar | Cuáles, con qué frecuencia y quién informa. |
| Reevaluación | Cada cuánto se recalcula la ER. |
| Riesgos nuevos | Cómo se incorporan. |
| Riesgos cerrados | Criterio para darlos por cerrados. |
| Eficacia | Ahorro logrado vs costo de gestión (ROI de gestión de riesgos). |

---

## Conexiones que tenés que cuidar con las otras áreas

- **Costos:** las reservas forman parte del presupuesto.
- **Tiempos:** una reserva de tiempo entra en el cronograma. Además el fast tracking y el crashing aumentan el riesgo.
- **Alcance:** un riesgo que cambia el alcance debe reflejarse en la EDT.
- **Seguimiento y valor ganado:** los disparadores se vigilan en la ejecución.
- Los números de ER, reservas e índice de riesgo **tienen que coincidir** con lo que escriban esas áreas.
