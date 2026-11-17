# 10. Costos y presupuesto

> Marco: `catedra/Clase 5 · Gestión de Costos de Proyectos.html` (estimar → presupuestar → controlar; costo ≠ gasto; directos/indirectos; fijos/variables; técnicas; reservas de contingencia y gerencial).

**Advertencia de método.** Amazon no publica su presupuesto ni sus costos unitarios. Esta sección reconstruye **la estructura y el método** de la gestión de costos. Solo se usan montos con fuente; donde no la hay, el campo dice «No público». **No se inventan cifras.**

## 10.1 Montos públicos

| Concepto | Monto | Fecha | Etiqueta / fuente |
|---|---|---|---|
| Compromiso de inversión inicial | > USD 10.000 millones | 30/07/2020 | `[DATO REAL]` #39 |
| Inversión total actualizada | "multibillion-dollar" (sin cifra) | 14/04/2026 | `[DATO REAL]` #5 |
| Instalación de procesamiento en KSC | > USD 140 millones | 24/07/2025 | `[DATO REAL]` #27 |
| Instalaciones en Cabo Cañaveral | > USD 200 millones | 23/03/2026 | `[DATO REAL]` #23 |
| Terminal estándar (costo de fabricación esperado) | < USD 400 por unidad | 14/03/2023 | `[DATO REAL]` #30 |
| Lanzamientos | No público | — | Sin fuente pública |
| Costo por satélite | No público | — | Sin fuente pública |
| Fianza (surety bond) | No pública; no eximida | 05/06/2026 | `[DATO REAL]` #8 ¶18 |
| Compra de Globalstar | USD 90 por acción o 0,3210 acciones de Amazon | 14/04/2026 | `[DATO REAL]` #5. **Fuera del alcance** (sección 7) |

**[INFERENCIA DEL GRUPO]** Las dos inversiones en Florida suman **más de USD 340 millones**, alrededor del 3,4% del compromiso inicial. Supuesto: ambas están dentro del compromiso de 2020 y no son adicionales (no se sabe).

## 10.2 Estructura de costos por elemento de la WBS

`[PROPUESTA DE GESTIÓN]` La clasificación es posible aunque falten montos, y es lo que se defiende.

| Elemento WBS | Directo / indirecto | Fijo / variable | Técnica de estimación propuesta (Clase 5) | Monto |
|---|---|---|---|---|
| 1.1 Gestión del proyecto | Indirecto | Fijo | Analogía con programas similares | No público |
| 1.2 Cumplimiento regulatorio (incluye la fianza) | Directo | Fijo | Dato contractual (la fianza la fija la FCC) | No público |
| 1.3 Satélites: planta | Directo | **Fijo** | Ascendente (por instalación) | No público |
| 1.3 Satélites: unidades | Directo | **Variable** (por satélite) | Paramétrica: costo unitario × 3.232 | No público (costo unitario) |
| 1.4 Procesamiento | Directo | Fijo | Dato público | > USD 340 millones (#27, #23) |
| 1.5 Lanzamientos | Directo | **Variable** (por misión) | Paramétrica: precio por misión × ≈ 108; o tres valores por cohete | No público |
| 1.6 Operación de la constelación | Directo | Fijo + variable | Analogía | No público |
| 1.7 Segmento terrestre | Directo | Variable (por gateway) | Paramétrica: costo por gateway × > 300 (#17) | No público |
| 1.8 Terminales | Directo | Variable | Paramétrica | < USD 400 por unidad (#30) × unidades (no público) |
| 1.9 Servicio y socios | Directo | Variable | Analogía | No público |

**[INFERENCIA DEL GRUPO]** Los costos con mayor peso esperado son **variables por unidad** (satélites y lanzamientos). Por eso perder una misión (T-01) cuesta dos veces: los 40 satélites y el lanzamiento. Y por eso **acelerar la cadencia no abarata**: adelanta costos variables. Los fijos (planta, instalaciones) ya están incurridos.
→ Supuesto: el costo por satélite y por lanzamiento son de un orden de magnitud que domina el total, como ocurre en constelaciones comparables. Es un supuesto, sin cifra.

## 10.3 Presupuesto y reservas

`[PROPUESTA DE GESTIÓN]` Estructura de la Clase 5: costos estimados + reserva de contingencia = **línea base de costos**; + reserva gerencial = **presupuesto total**.

| Componente | Monto | Base |
|---|---|---|
| Costos estimados (10.2) | ≥ USD 10.000 millones (compromiso declarado como piso) | #39 |
| Reserva de contingencia | No calculable sin montos. Se compone de: reposición de 40 satélites (R-01/T-01); fianza (R-04); lanzamientos adicionales de recuperación (R-02, OP-1) | Riesgos §6 |
| = Línea base de costos | No calculable | |
| Reserva gerencial | Porcentaje a fijar por el sponsor | Clase 5 |
| = Presupuesto total | No calculable | |

## 10.4 Control de costos

**[INFERENCIA DEL GRUPO]** Sin costo real (AC), el CPI no es calculable (sección 12). Lo que sí se puede seguir públicamente son señales de costo:
- nuevas inversiones anunciadas (KSC, Cabo Cañaveral);
- contratos adicionales de lanzamiento (Ariane 6 + 6; Falcon 9 + 10);
- eventos que generan costo no planificado (pérdida de LV-01).

Todas apuntan a **costo creciente con avance lento**: es la configuración que la Clase 6 describe con sus "paradojas" de valor ganado (mucho gasto con poco trabajo realizado), aunque aquí solo se puede afirmar de forma cualitativa.

## 10.5 Índice de riesgo y apalancamiento

Riesgos §6 los define como Σ ER ÷ costo total y como (ER antes − ER después) ÷ costo de la alternativa. **Siguen sin poder calcularse**: sin costo total y sin el costo de las respuestas, cualquier cifra sería inventada. Si el equipo decide usar el compromiso de USD 10.000 millones como costo total, hay que convertir las exposiciones a dólares, y eso requiere impactos en USD que tampoco son públicos. Queda como límite declarado.
