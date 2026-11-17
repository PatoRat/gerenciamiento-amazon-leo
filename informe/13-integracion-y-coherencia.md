# 13. Integración y coherencia

> **Borrador** redactado con asistencia de IA el 16/11/2026. Requiere revisión del equipo. Responde al paso 4 de la consigna ("Conectar: evitar documentos aislados") y a la Integración del Paneo, tema 3 ("que alcance, tiempo, costo y riesgos no se manejen por separado").

## 13.1 La cadena que conecta todo el informe

**[INFERENCIA DEL GRUPO]**

1. **Alcance (7):** la WBS muestra una cadena fabricación → procesamiento → **lanzamiento** → operación, con el cuello de botella en el lanzamiento.
2. **Tiempos y estimaciones (8, 9):** el ritmo real (≈ 21 satélites por mes) es un cuarto del necesario (≈ 87). El hito de 2029 está en la "zona inalcanzable": PERT da ≈ 0,07% y fin ≈ 11/2035.
3. **Valor ganado (12):** SPI 0,22 a 0,57 según la línea base; fin entre 2031 y 2038.
4. **Riesgos (11):** como no llegar es casi seguro (Monte Carlo ≈ 0%), el riesgo principal pasa a ser **regulatorio** (R-04: que la FCC no conceda un nuevo alivio), alimentado por R-02 (lanzadores en tierra), que el 15/11/2026 se activó con T-01.
5. **Respuesta integrada:** línea base de recuperación (≈ 08/2031, sección 8.6) + pedido de alivio con evidencia (R-04) + más capacidad de lanzamiento (OP-1).
6. **Costos (10):** esa respuesta adelanta costos variables (lanzamientos, satélites) y suma la fianza en riesgo. La reserva de contingencia debe cubrirlos.
7. **Caso de negocio y acta (5, 6):** el caso sigue siendo deseable, pero hay que **reevaluarlo** (5.7) y el acta necesitaba un criterio de inicio de servicio verificable que nunca fue público.

## 13.2 Mismas cifras en todas las secciones

| Cifra (Anexo D) | Secciones que la usan | Valor |
|---|---|---|
| C-01 / C-03 BAC e hito final | 5, 6, 7, 8, 11, 12 | 3.232 al 30/07/2029 |
| C-12 Satélites desplegados | 2, 8, 9, 11, 12 | 396 |
| C-21 / C-23 Ritmo observado / necesario | 7, 8, 9, 11, 12 | 21 / 87 por mes |
| C-40 / C-42 Contratos / dependencia | 7, 8, 10, 11 | ≈ 108 / 66% |
| C-35 Compromiso de inversión | 5, 6, 10 | > USD 10.000 millones |
| C-50 Monte Carlo | 9, 11 | P50 ≈ 1.513 |
| C-52 SPI | 11, 12 | 0,57 (plan) |

## 13.3 Control de coherencia hecho

| Verificación | Resultado |
|---|---|
| Serie EV contra la declaración de Amazon a la FCC | 180 = 180 ✔ |
| Monte Carlo, PERT y VG apuntan a la misma conclusión | ✔ (2029 inalcanzable; fin entre 2031 y 2038) |
| Reserva de tiempo de R-02 contada una sola vez | ✔ (sección 8.7) |
| Contratos con la misma cifra en todas las secciones | ✔ (New Glenn = 24; total ≈ 108) |
| Unidad de avance única (lanzados ≈ operativos) | ✔ (declarada en 1.4 y en Riesgos §4.1) |
| Alcance coherente con el BAC y el horizonte de Riesgos | ✔ (Gen1, 3.232, 30/07/2029) |
| Criterio de inicio del servicio | Propuesto en el acta (6) → usado en la WBS (1.9.2), el cronograma (M-10) y R-03 ✔ |

## 13.4 Elaboración progresiva

La cátedra señala que "para relacionar temas, la llave es la **elaboración progresiva**" (Paneo). En este proyecto se ve en tres planos: el alcance (Gen1 detallado; Gen2 y D2D en rolling wave), las estimaciones (ventanas de reestimación en 9.4) y el caso de negocio (que debe actualizarse con el atraso, 5.7).
