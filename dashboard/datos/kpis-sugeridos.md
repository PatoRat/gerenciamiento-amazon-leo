# KPIs sugeridos para el dashboard — SUGERENCIA, no definición

> **Esto es una lista de opciones, no los KPIs del tablero.** Según `CLAUDE.md` §8, los KPIs los elige el equipo. Este archivo existe para acelerar esa decisión: el equipo marca cuáles quiere (columna "¿Va?") y con eso se corre `/dashboard:kpis` (D-1). La Instancia 2 **no está iniciada**.
>
> Criterio de la consigna: el tablero "debe servir para responder preguntas" y no ser "diapositivas disfrazadas". Por eso cada KPI parte de **la pregunta de defensa que contesta**. Todos los valores salen de `informe/cifras-maestras.md` (fecha de corte 16/11/2026).

## Bloque 1 — ¿Dónde está el proyecto? (estado)

| ¿Va? | KPI | Pregunta que responde | Valor al corte | Origen | Visual sugerido |
|---|---|---|---|---|---|
| ☐ | Satélites desplegados contra hito final | ¿Cuánto avanzó el despliegue? | 396 / 3.232 (12,3%) | C-12, C-15 | Barra de progreso con marcas en 1.616 y 3.232 |
| ☐ | Cumplimiento del hito del 50% | ¿Cumplió lo que pedía la FCC para 2026? | 396 / 1.616 (24,5%), vencido el 30/07/2026 | C-16 | Indicador con semáforo rojo |
| ☐ | Misiones realizadas y resultado | ¿Cuántas veces lanzó y con qué éxito? | 15 misiones; 14 con despliegue, 1 fallida | C-11 | Tira de 15 puntos coloreados por cohete |
| ☐ | Estado del servicio comercial | ¿Ya funciona el servicio? | Sin lanzamiento comercial; previews limitadas | hitos §4 | Etiqueta de estado |

## Bloque 2 — ¿Está atrasado? (tiempo y seguimiento)

| ¿Va? | KPI | Pregunta que responde | Valor al corte | Origen | Visual sugerido |
|---|---|---|---|---|---|
| ☐ | Curva S: EV contra la línea base FCC | ¿Cuánto se separó del plan y desde cuándo? | EV 396 contra PV 1.777 | `ev_serie.csv`, guía VG | Línea escalonada (EV) contra línea de referencia (PV) |
| ☐ | SPI (dos líneas base) | ¿Qué tan eficiente es el uso del tiempo? | 0,57 (plan Amazon) · 0,25 (FCC) · 0,22 al corte | C-52, guía VG | Dos números grandes con umbral 1,0 |
| ☐ | Cadencia real contra la necesaria | ¿Puede llegar a 2029 a este ritmo? | 21 contra 87 sat/mes | C-21, C-23 | Barras comparadas |
| ☐ | Fin proyectado | ¿Cuándo terminaría? | ≈ 2031 (plan) · ≈ 2038 (ritmo observado) · hito 2029 | guía VG §4 | Línea de tiempo con tres marcas |
| ☐ | Promesas de inicio del servicio | ¿Amazon cumple sus fechas? | 2024 → 2025 → 2026, sin cumplir | hitos §5 | Línea de tiempo de corrimientos |

## Bloque 3 — ¿Qué puede salir mal? (riesgos)

| ¿Va? | KPI | Pregunta que responde | Valor al corte | Origen | Visual sugerido |
|---|---|---|---|---|---|
| ☐ | Matriz P×I con los 7 riesgos | ¿Cuáles son los riesgos principales y por qué? | 2 rojos (R-04, R-02) | Riesgos §4.5 | Matriz 5×5 de la cátedra |
| ☐ | Exposición antes y después de responder | ¿Sirven las respuestas propuestas? | 0,82 → 0,50 | C-53 | Barras apareadas por riesgo |
| ☐ | Probabilidad de llegar a 3.232 (Monte Carlo) | ¿Es posible cumplir el hito final? | ≈ 0% · P50 ≈ 1.510 | C-50, C-51 | Histograma o P10/P50/P90 contra 3.232 |
| ☐ | Concentración del manifiesto por lanzador | ¿De quién depende? | Vulcan + New Glenn = 66% de lo restante | C-41, C-42 | Barra apilada por proveedor |
| ☐ | Temas abiertos | ¿Qué problema está activo hoy? | T-01 (pérdida de LV-01) | Riesgos §7.1 | Lista corta |

## Bloque 4 — ¿Cómo se organiza? (alcance e infraestructura)

| ¿Va? | KPI | Pregunta que responde | Valor al corte | Origen | Visual sugerido |
|---|---|---|---|---|---|
| ☐ | Cadena fabricación → lanzamiento → operación | ¿Cómo se conectan fabricación, lanzamientos y operación? (orientación de la cátedra) | Kirkland hasta 30/sem; 1.000 fabricados; 396 en órbita; > 300 estaciones | C-30, C-31, C-12, C-34 | Diagrama de flujo con cifras |
| ☐ | Mapa de actores | ¿Quién participa? | Amazon, 4 lanzadores, FCC, socios | `evidencia/actores.md` | Diagrama de red simple |

## Lo que el tablero NO puede mostrar (y debe decirlo)

- CPI y costos reales: no públicos → marcador visible de pendiente, con la explicación.
- Satélites operativos: se muestran lanzados, con la aclaración.

## Sugerencia de tamaño

Para que siga siendo un tablero y no una presentación: **8 a 10 KPIs** en una sola pantalla con desplazamiento corto. Si hay que elegir, los que más preguntas cubren son la curva S, la cadencia real contra la necesaria, la matriz P×I, la concentración por lanzador y la cadena fabricación → lanzamiento → operación.
