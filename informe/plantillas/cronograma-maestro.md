# Plantilla — Cronograma maestro

**Etiqueta del documento:** `[PROPUESTA DE GESTIÓN]` sobre hitos `[DATO REAL]`.
**Marco:** `catedra/Clase 3 Gestión de los Tiempos · UCA.html`. Procesos: definir actividades → secuenciar → estimar recursos → estimar duración → desarrollar y controlar. "Su principal salida es el cronograma aprobado, que constituye la línea base del tiempo." Herramientas de la clase: **milestones**, **inch-pebbles**, relaciones y dependencias, Gantt, redes, acortamiento y nivelación.

---

## 1. Milestones (hitos)

| ID | Hito | Fecha | Tipo (regulatorio / técnico / comercial) | Etiqueta | Fuente | Estado al corte |
|---|---|---|---|---|---|---|
| | | | | | | |

> Cómo completarlo: los hitos públicos están en `evidencia/hitos.md` §1–3 y en `cifras-maestras.md` §1. Incluir los regulatorios (30/07/2026, 14/08/2026, 30/10/2027, 30/03/2028, 30/07/2029) y el de inicio de servicio (con el criterio que proponga el equipo).

## 2. Inch-pebbles (avance intermedio)

> Cómo completarlo: la Clase 3 dice que los inch-pebbles "dividen el avance en puntos intermedios más pequeños" y achican el área de desvío. Propuesta natural: **cada misión es un inch-pebble** (satélites desplegados por misión), y el acumulado por trimestre es el control contra el hito. Base: `informe/seguimiento/ev_serie.csv`.

| Trimestre | Misiones planificadas | Satélites planificados (acumulado) | Real | Desvío |
|---|---|---|---|---|
| | | | | |

## 3. Actividades y dependencias por elemento de la WBS

| Actividad | Elemento WBS | Predecesora | Tipo de relación | Duración (con método) | Recursos |
|---|---|---|---|---|---|
| | | | | | |

> Cómo completarlo: secuencia fabricación (1.3) → procesamiento (1.4) → lanzamiento (1.5) → elevación y puesta en servicio (1.6), en paralelo con el segmento terrestre (1.7). Las duraciones salen de `plantillas/estimaciones.md`; si son reconstrucción, declarar el supuesto.

## 4. Gantt de alto nivel

> Cómo completarlo: por campaña de lanzamiento (Atlas V, Vulcan, Ariane 6, New Glenn, Falcon 9), 2025–2029. Puede ser tabla o imagen. Marcar lo real (2025–2026) y lo planificado.

## 5. Cuando el plazo limita el plan (acortamiento y nivelación)

> Cómo completarlo: la Clase 3 trata qué hacer cuando el plazo o los recursos limitan el plan, incluida la "zona inalcanzable". Aplicación directa: el hito de 2029 exige ≈ 35 misiones por año (C-24) y el plan es de 20 (C-25). Analizar **acortamiento** (más lanzadores, OP-1), **nivelación** (la fábrica se ajusta a los lanzadores, #23) y explicar por qué 2029 parece estar en la "zona inalcanzable" (Monte Carlo, C-50).

## 6. Reservas de tiempo

> Cómo completarlo: incorporar la reserva de ≈ 4 meses de R-02 **sin doble cuenta** con R-03 y R-04 (Riesgos §6).

**Coherencia:** WBS, estimaciones, riesgos (R-02, R-03, R-04, reservas), VG (PV = línea base), dashboard (curva S).
