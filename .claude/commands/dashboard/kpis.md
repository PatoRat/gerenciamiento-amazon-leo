---
description: "D-1 · Estructura los KPIs que entrega el equipo en un modelo de datos"
---

# Checkpoint D-1 — KPIs y modelo de datos

**Inicio de la Instancia 2.** Solo se corre con pedido explícito del equipo.

Entrada: lo que el equipo haya dejado en el chat o en `dashboard/datos/`. Si no hay nada, leé `dashboard/datos/README.md`, mostrá qué se necesita por KPI y **pará**: los KPIs los elige el equipo, no Claude.

## Qué hacer

1. **Normalizar** cada KPI que entregó el equipo en la ficha completa: nombre, qué pregunta de la defensa responde, valor, unidad, fecha de corte, origen (`[DATO REAL]` con `#` de fuente / `[INFERENCIA DEL GRUPO]` / `[PROPUESTA DE GESTIÓN]`), meta o umbral, serie temporal si corresponde.
2. **Verificar contra la evidencia**: cruzá cada `[DATO REAL]` con `evidencia/registro-fuentes.md` y `evidencia/hitos.md`. Si un valor no coincide con la fuente o no tiene respaldo, marcalo y preguntá; no lo corrijas por tu cuenta.
3. **Listar lo que falta**: valores sin dato, sin unidad, sin fecha de corte o sin origen. Una pregunta concreta por cada hueco.
4. **Señalar problemas de diseño de indicador**, sin decidir por el equipo: KPIs que no responden ninguna pregunta previsible, dos que miden lo mismo, un indicador sin umbral que no permite leer si algo está bien o mal.
5. Escribir `dashboard/datos/kpis.md` (legible para el equipo) y `dashboard/datos/kpis.json` (consumible por el HTML, con `pendiente: true` en lo que falte).

## Reglas duras

- **No inventes valores**, ni de ejemplo, ni "aproximados", ni de relleno para que el tablero se vea completo. Lo que falta va como pendiente visible.
- No agregues KPIs por iniciativa propia. Si ves un hueco relevante, sugerilo marcado como sugerencia, para que el equipo decida.
- Toda cifra lleva unidad o moneda y fecha de corte.

## Al terminar

1. Informá: KPIs normalizados, datos faltantes (lista de preguntas concretas) y observaciones de diseño.
2. Actualizá `PROGRESO.md`: D-1 a `🟡 esperando revisión`.
3. **Detenete.** El equipo confirma los KPIs y completa los faltantes antes de D-2.
