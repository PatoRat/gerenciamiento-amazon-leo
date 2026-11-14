---
description: "D-2 · Layout y jerarquía del tablero"
---

# Checkpoint D-2 — Wireframe y jerarquía

Requiere **D-1 aprobado** y los KPIs confirmados en `dashboard/datos/kpis.md`.

Criterio que manda: la cátedra pide un **tablero funcional y ejecutivo** que *sirva para responder preguntas*, y aclara que **no debe convertirse en "diapositivas disfrazadas"**. La defensa es oral y sin diapositivas: el tablero es la herramienta de consulta, no el guion.

## Producto — `dashboard/wireframe.md`

1. **Pregunta por bloque**: para cada bloque del tablero, qué pregunta previsible de la defensa responde. **Un bloque que no responde ninguna pregunta no va.**
2. **Jerarquía de lectura**: qué se ve primero (estado general del proyecto), qué en segundo nivel (por eslabón: fabricación, lanzamientos, estaciones terrestres, operación), qué queda como detalle de consulta.
3. **Esquema del layout** en texto/ASCII: zonas, qué va en cada una y por qué ahí.
4. **Tipo de visualización por KPI**, con justificación (evolución → línea; comparación entre categorías → barras; hito y cumplimiento → marcador contra umbral; estado único → tile numérico). Señalá qué KPIs **no** conviene graficar.
5. **Lectura del estado**: cómo se distingue a simple vista lo cumplido de lo comprometido a futuro, y lo que es `[DATO REAL]` de lo reconstruido por el equipo. Esto último es requisito de trazabilidad, no decoración.
6. **Qué NO entra** y por qué: lo que corresponde al informe y no al tablero.
7. **Comportamiento en pantalla y en PDF**: qué debe quedar visible sin scroll en una notebook, y cómo se pagina en la impresión.

Antes de definir tipos de gráfico, cargá la skill **`dataviz`**.

## Reglas

- Texto y esquemas: **no escribas el HTML todavía**, eso es D-3.
- No propongas KPIs nuevos ni inventes valores.
- Si los KPIs confirmados no alcanzan para responder las preguntas previsibles de la defensa, decilo: es un hallazgo para el equipo, no un hueco a tapar.

## Al terminar

1. Informá: bloques propuestos con su pregunta asociada, y qué preguntas de la defensa quedan **sin** cobertura.
2. Actualizá `PROGRESO.md`: D-2 a `🟡 esperando revisión`.
3. **Detenete.** El equipo aprueba el layout antes de que se escriba el HTML.
