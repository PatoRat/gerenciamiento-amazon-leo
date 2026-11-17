# Guía — Seguimiento y Valor Ganado aplicado a Amazon Leo

Guía metodológica (I-4) para redactar la sección de Seguimiento y Valor Ganado. Borrador elaborado con asistencia de IA el 16/11/2026: **las decisiones (línea base, unidad, interpretación) las revisa y defiende el equipo.**

- **Marco:** `catedra/Clase 6 Seguimiento y Valor Ganado · Administración de Proyectos · UCA.html` y `catedra/Valor Agregado.html`. El `Paneo_rapido_Gerenciamiento.pdf` lo marca como **PRIORIDAD** ("la única cuenta posible es con EV, PV y AC: sacar SPI = EV/PV y CPI = EV/AC e interpretarlos").
- **Cálculo reproducible:** `informe/seguimiento/valor_ganado.py`, que genera `ev_serie.csv` (serie para el dashboard).
- **Cifras:** las de `informe/cifras-maestras.md`.

---

## 1. Idea central: medir el avance por el output

La cátedra insiste en medir el avance **por el output (lo producido) y no por el input (lo gastado)** (Clase 6, PPT pág. 21). En Amazon Leo el output es directo y público: **satélites desplegados en órbita**. Por eso se propone hacer el valor ganado **en unidades físicas**.

| Concepto (cátedra) | Aplicación a Amazon Leo | Etiqueta |
|---|---|---|
| BAC (presupuesto al término) | 3.232 satélites (hito final de la FCC) | `[DATO REAL]` #8 ¶3 |
| PV (valor planificado) | Satélites que debían estar desplegados a la fecha, según la línea base | `[DATO REAL]` en los hitos; `[PROPUESTA DE GESTIÓN]` entre hitos |
| EV (valor ganado) | Satélites lanzados acumulados (aproximación de operativos) | `[INFERENCIA DEL GRUPO]` suma de #2 |
| AC (costo real) | **No público** | `[[PENDIENTE]]`: el CPI no se puede calcular con datos reales |

**Control de consistencia de la serie EV:** la suma por misión da 180 satélites al 16/12/2025, y Amazon declaró a la FCC "180 satélites lanzados" en su solicitud del 30/01/2026 (#8 ¶8). Las dos fuentes coinciden.

## 2. Dos líneas base (decisión del equipo)

| Línea base | PV al 30/07/2026 | PV al 30/07/2029 | Qué representa |
|---|---|---|---|
| **A · Regulatoria** | 1.616 | 3.232 | Lo que la FCC exige. Entre hitos se interpola linealmente `[PROPUESTA DE GESTIÓN]`. |
| **B · Plan de Amazon** | ≈ 700 | — | Lo que Amazon mismo dijo que lograría (#8 ¶8). Solo hay un punto. |

> Decisión a tomar: cuál se presenta como línea base principal. Sugerencia: **A como restricción** (lo que el proyecto debe cumplir) y **B como plan propio** (contra lo que Amazon se compromete). La diferencia entre las dos (1.616 contra 700) ya muestra que el plan de Amazon nunca apuntó a cumplir el hito intermedio, y es un buen argumento de defensa.

## 3. Resultados (salida de `valor_ganado.py`)

`[INFERENCIA DEL GRUPO]` sobre las líneas base anteriores. Fórmulas de la cátedra: Vcr = EV − PV; %Vcr = Vcr ÷ PV; SPI = EV ÷ PV.

| Corte | Fecha | PV | EV | Vcr | %Vcr | SPI |
|---|---|---|---|---|---|---|
| Hito 50% · línea base A (FCC) | 30/07/2026 | 1.616 | 396 | −1.220 | −75% | **0,25** |
| Hito 50% · línea base B (plan Amazon) | 30/07/2026 | 700 | 396 | −304 | −43% | **0,57** |
| Corte · línea base A interpolada | 16/11/2026 | 1.777 | 396 | −1.381 | −78% | **0,22** |

**Avance físico al 16/11/2026:** 396 ÷ 3.232 = **12,3%**.

**Lectura:** un SPI menor a 1 indica que el proyecto avanza por debajo de lo planificado (Clase 6, pág. 28). Contra el plan de Amazon el proyecto ejecutó el 57% de lo planificado; contra la exigencia de la FCC, el 25%. Entre el 30/07 y el 16/11/2026 el SPI empeora (0,25 → 0,22) porque no hubo lanzamientos exitosos y el plan siguió avanzando.

## 4. Proyección: ¿cuándo terminaría?

La cátedra responde "¿cuándo terminará mi viaje?" proyectando con el rendimiento real (Clase 6, págs. 24–27 y 33). Con satélites:

| Escenario | Ritmo (satélites/mes) | Meses para los 2.836 restantes | Fin aproximado | Etiqueta |
|---|---|---|---|---|
| Ritmo observado | 21,3 | ≈ 133 | ≈ 2038 | `[INFERENCIA DEL GRUPO]` |
| Plan de Amazon (20 misiones/año × 30) | 50,0 | ≈ 57 | ≈ 2031 | `[INFERENCIA DEL GRUPO]` sobre #23 |
| Ritmo necesario para el hito | 87,5 | ≈ 32 | 30/07/2029 | `[INFERENCIA DEL GRUPO]` |

Coincide con el Monte Carlo de Riesgos (§5): ningún escenario realista llega a 2029. Es el mismo hallazgo visto desde otra herramienta, que es justamente lo que pide el paso 4 de la consigna.

## 5. Lo que no se puede calcular y cómo decirlo

- **CPI = EV ÷ AC** y **Vco = EV − AC**: Amazon no publica el costo incurrido (AC) ni el presupuesto (BAC en USD). **No se inventa.** En el informe se escribe: "el CPI no puede calcularse con datos públicos" y se explica qué haría falta.
- Si el área de Costos arma un presupuesto `[PROPUESTA DE GESTIÓN]` (BAC en USD con supuestos), se puede expresar el EV en dólares (EV$ = BAC$ × avance físico), pero el AC sigue sin existir. **El CPI queda sin calcular igual.**
- **Paradojas de la cátedra** (Clase 6, págs. 24–27): con la información pública, Amazon invierte fuerte (fábrica, KSC por más de USD 140 millones, Cabo Cañaveral por más de USD 200 millones, más de 100 lanzamientos contratados; #27, #23) mientras el EV avanza lento. Es el patrón "gasto alto con poco trabajo realizado". **Solo se puede plantear cualitativamente**, sin números de AC.

## 6. Seguimiento propuesto (qué y cómo seguir)

`[PROPUESTA DE GESTIÓN]`, con los instrumentos de la Clase 6 (págs. 8–17):

| Instrumento de la cátedra | Aplicación |
|---|---|
| Informe de situación (mensual) | EV, PV, SPI y cadencia del mes; causas de desvío (lanzador en tierra, falla). |
| Log de temas pendientes | Temas abiertos: T-01 (pérdida de LV-01, ver Riesgos §7.1). |
| Reuniones de avance con proveedores | ULA, Blue Origin, Arianespace y SpaceX: fechas de retorno y manifiesto. |
| Reunión de finalización por hito | Al 30/10/2027 (certificación, #8 ¶15) y al 30/07/2029. |
| Ante desvíos (pág. 17) | Las opciones de la cátedra ya están en juego: "agregar más recursos" (más lanzadores, OP-1), "extender los plazos" (pedido a la FCC, R-04), "eliminar funciones" (resignar satélites, que Amazon rechazó). |

## 7. Coherencia con otras secciones

| Sección | Qué debe coincidir |
|---|---|
| Riesgos | SPI ≈ 0,57 (§7), ritmo de 21 sat/mes, unidad lanzados ≈ operativos (§4.1). |
| Tiempos | Las fechas de los hitos y la línea base A deben ser los hitos del cronograma maestro. |
| Costos | Si se arma un BAC en USD, el mismo avance físico (12,3%). |
| Dashboard | `ev_serie.csv` para la curva S (EV contra la línea base A). |

## 8. Preguntas probables de defensa

1. ¿Por qué miden el valor ganado en satélites y no en dólares? → Output contra input (Clase 6, pág. 21) y AC no público.
2. ¿Por qué hay dos SPI distintos (0,25 y 0,57)? → Dos líneas base: la exigencia del regulador y el plan propio de Amazon.
3. ¿Cuál es el CPI? → No calculable con datos públicos; explicar por qué y qué haría falta.
4. ¿Cuándo termina el despliegue? → ≈ 2031 con el plan de Amazon y ≈ 2038 con el ritmo observado; coincide con el Monte Carlo.
5. ¿Satélites lanzados son satélites operativos? → No necesariamente: es una aproximación optimista (Riesgos §4.1).
