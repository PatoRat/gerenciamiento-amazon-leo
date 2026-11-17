# Cifras maestras — Amazon Leo

**Fuente única de los números que usa todo el trabajo.** Riesgos, Tiempos, Estimaciones, Costos, Seguimiento y Valor Ganado y el dashboard toman sus cifras **de esta tabla**. Si un número cambia, se cambia acá primero y después en cada sección que lo use (columna "Lo usa").

Es la herramienta para cumplir el paso 4 de la consigna (**Conectar**: "evitar documentos aislados") y para la defensa: cualquier número que se diga en voz alta tiene que coincidir con el informe y con el tablero.

- **Fecha de corte:** 16/11/2026 (propuesta pendiente de aprobación; ver `PROGRESO.md`, "Decisiones pendientes").
- **Unidad de avance:** satélites **lanzados** como aproximación de **operativos** (Amazon no publica operativos; la FCC mide operativos). Todos los resultados derivados son optimistas.
- Las referencias `#n` son filas de `evidencia/registro-fuentes.md`.
- Estado: borrador elaborado con asistencia de IA a partir de la evidencia del repo; **requiere revisión del equipo**.

---

## 1. Regulación (FCC)

| ID | Cifra | Valor | Etiqueta | Fuente / cálculo | Lo usa |
|---|---|---|---|---|---|
| C-01 | Satélites autorizados (Gen1) | 3.232 | `[DATO REAL]` | #7 ¶1; #8 ¶3 | Riesgos, Alcance, VG, dashboard |
| C-02 | Hito intermedio (50%) | 1.616 al 30/07/2026 | `[DATO REAL]` | #8 ¶3 | Riesgos, Tiempos, VG |
| C-03 | Hito final (100%) | 3.232 al 30/07/2029 | `[DATO REAL]` | #8 ¶3 (DA 24-224 dice 20/07, ver contradicciones) | Todo |
| C-04 | Proyección de Amazon a la FCC | ≈ 700 desplegados al 30/07/2026 | `[DATO REAL]` | #8 ¶8 (solicitud del 30/01/2026) | VG (línea base), Riesgos |
| C-05 | Pérdida de prioridad de espectro | hasta 30/03/2028 (30/10/2027 si certifica 50% construido) | `[DATO REAL]` | #8 ¶15 | Riesgos R-05, Tiempos |
| C-06 | Fianza (surety bond) | no eximida; monto no público | `[DATO REAL]` / monto no público | #8 ¶18 | Costos, Riesgos R-04 |

## 2. Despliegue (al 16/11/2026)

| ID | Cifra | Valor | Etiqueta | Fuente / cálculo | Lo usa |
|---|---|---|---|---|---|
| C-10 | Primera misión de producción | KA-01, 28/04/2025 | `[DATO REAL]` | #2 | Tiempos, VG |
| C-11 | Misiones realizadas | 15 (14 con despliegue + LV-01 fallida) | `[DATO REAL]` | #2, #11 | Tiempos, Riesgos |
| C-12 | Satélites lanzados y desplegados | 396 | `[INFERENCIA DEL GRUPO]` | Suma por misión de #2; coincide con "nearly 400" de Amazon | Todo |
| C-13 | Satélites perdidos | 40 (LV-01, 15/11/2026) | `[DATO REAL]` | #2, #11 | Riesgos T-01 |
| C-14 | Satélites que faltan para el hito final | 2.836 | `[INFERENCIA DEL GRUPO]` | C-01 − C-12 | Riesgos, Tiempos, VG |
| C-15 | Avance físico contra el hito final | 12,3% | `[INFERENCIA DEL GRUPO]` | 396 ÷ 3.232 | VG, dashboard |
| C-16 | Cumplimiento del hito del 50% | 24,5% (396 de 1.616) | `[INFERENCIA DEL GRUPO]` | C-12 ÷ C-02 (satélites al 02/07/2026: 396, sin lanzamientos hasta el 15/11) | Riesgos R-05, dashboard |

## 3. Ritmo y horizonte

| ID | Cifra | Valor | Etiqueta | Fuente / cálculo | Lo usa |
|---|---|---|---|---|---|
| C-20 | Horizonte hasta el hito final | ≈ 32,5 meses | `[INFERENCIA DEL GRUPO]` | 16/11/2026 → 30/07/2029 | Riesgos, Tiempos |
| C-21 | Ritmo observado (satélites) | ≈ 21 por mes | `[INFERENCIA DEL GRUPO]` | 396 en ≈ 18,6 meses (28/04/2025 → 15/11/2026) | Riesgos, Tiempos, dashboard |
| C-22 | Ritmo observado (misiones) | ≈ 0,8 por mes global; ≈ 11 por año desde 28/04/2026 | `[INFERENCIA DEL GRUPO]` | 15 misiones en 18,6 meses; 6 en 6,5 meses | Riesgos §5, Tiempos |
| C-23 | Ritmo necesario (satélites) | ≈ 87 por mes | `[INFERENCIA DEL GRUPO]` | C-14 ÷ C-20 | Riesgos, Tiempos, dashboard |
| C-24 | Ritmo necesario (misiones) | ≈ 35 por año (a 30 satélites por misión) | `[INFERENCIA DEL GRUPO]` | C-23 × 12 ÷ 30 | Riesgos, Tiempos |
| C-25 | Plan declarado de Amazon | "20+ misiones" en el año dos | `[DATO REAL]` | #23 (23/03/2026) | Riesgos, Tiempos |
| C-26 | Satélites por misión | 24 (Falcon 9) · 27–29 (Atlas V) · 32–36 (Ariane 64) · 40 (Vulcan) | `[DATO REAL]` | #2, #3 | Estimaciones, Riesgos §5 |

## 4. Producción e infraestructura

| ID | Cifra | Valor | Etiqueta | Fuente / cálculo | Lo usa |
|---|---|---|---|---|---|
| C-30 | Capacidad declarada de fábrica (Kirkland) | 4/día (2022) → 5/día (2024) → hasta 30/semana (2026) | `[DATO REAL]` | #25, #26, #23 | Alcance, Estimaciones |
| C-31 | Satélites fabricados | 1.000 (inicios de 09/2026) | `[DATO REAL]` | #3 (fecha discutida, ver contradicciones) | Estimaciones |
| C-32 | Instalación de procesamiento en KSC | 100.000 ft²; > USD 140 millones | `[DATO REAL]` | #27 | Costos, Alcance |
| C-33 | Inversión en Cabo Cañaveral (2026) | > USD 200 millones | `[DATO REAL]` | #23 | Costos |
| C-34 | Estaciones terrestres | > 300 planificadas | `[DATO REAL]` (prensa) | #17 | Alcance |
| C-35 | Compromiso de inversión inicial | > USD 10.000 millones ("more than $10 billion") | `[DATO REAL]` | #39 (30/07/2020), verificado el 16/11/2026 | Caso de negocio, Acta, Costos |

## 5. Lanzamientos contratados (vigente al 16/11/2026)

| ID | Cifra | Valor | Etiqueta | Fuente / cálculo | Lo usa |
|---|---|---|---|---|---|
| C-40 | Total contratado | ≈ 108 (24 Ariane 6 + 38 Vulcan + 9 Atlas V + 24 New Glenn + 13 Falcon 9) | `[INFERENCIA DEL GRUPO]` | Tabla "Cifras de contratos con fecha de corte" del registro | Riesgos, Costos, dashboard |
| C-41 | Lanzamientos restantes | ≈ 93 (21 Ariane 6, 10 Falcon 9, 1 Atlas V, 37 Vulcan, 24 New Glenn) | `[INFERENCIA DEL GRUPO]` | C-40 − volados | Riesgos R-02, dashboard |
| C-42 | Dependencia de Vulcan + New Glenn | 61 de 93 = ≈ 66% | `[INFERENCIA DEL GRUPO]` | C-41 | Riesgos R-02, dashboard |

## 6. Resultados de análisis (salen de otras secciones)

| ID | Cifra | Valor | Etiqueta | Origen | Lo usa |
|---|---|---|---|---|---|
| C-50 | Satélites al 30/07/2029 (Monte Carlo) | P10 ≈ 1.140 · P50 ≈ 1.510 · P90 ≈ 2.050 | `[INFERENCIA DEL GRUPO]` sobre supuestos `[PROPUESTA DE GESTIÓN]` | Riesgos §5, `analisis_cuantitativo.py` | Riesgos, Tiempos, dashboard |
| C-51 | Probabilidad de llegar a 3.232 por cadencia | ≈ 0% | ídem | Riesgos §5 | Riesgos R-04, dashboard |
| C-52 | SPI en satélites al 30/07/2026 | ≈ 0,57 (396 ÷ 700) | `[INFERENCIA DEL GRUPO]` | Riesgos §7; ver `informe/guias/seguimiento-valor-ganado.md` | VG, dashboard |
| C-53 | Exposición total al riesgo | 0,82 antes → 0,50 después de responder | `[PROPUESTA DE GESTIÓN]` | Riesgos §6 | Riesgos, dashboard |
| C-54 | Riesgos en rojo | 2 (R-04, R-02) → 1 después de responder | `[PROPUESTA DE GESTIÓN]` | Riesgos §4.5 y §6 | dashboard |

## 7. Lo que no es público (no inventar)

| Dato | Estado | Cómo se trata |
|---|---|---|
| Inversión total **actualizada** de Amazon en Leo (USD) | Compromiso inicial **verificado**: "more than $10 billion" (#39, 30/07/2020; ver C-35). En 2026 solo "multibillion-dollar" (#5). No hay cifra actualizada. | Usar C-35 como piso declarado en 2020; el total actual queda sin dato público |
| Costo por satélite y por lanzamiento | No público | Supuesto explícito del grupo en Costos |
| Monto de la fianza | No público | Se declara como límite |
| Satélites **operativos** | No público | Se usa lanzados (ver unidad de avance) |
| Costo real incurrido (AC) | No público | El CPI no se puede calcular con datos reales |
