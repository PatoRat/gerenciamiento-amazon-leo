# 12. Seguimiento y valor ganado

> Marco: `catedra/Clase 6 Seguimiento y Valor Ganado · Administración de Proyectos · UCA.html` y `catedra/Valor Agregado.html`. Cálculo: `informe/seguimiento/valor_ganado.py`. Desarrollo metodológico: `informe/guias/seguimiento-valor-ganado.md`.

## 12.1 Medir por el output

La cátedra pide medir el avance **por el output, no por el input** (Clase 6, pág. 21). En Amazon Leo el output es público y verificable: **satélites desplegados**. Por eso el valor ganado se calcula en unidades físicas `[PROPUESTA DE GESTIÓN]`:

| Concepto | Valor | Etiqueta |
|---|---|---|
| BAC | 3.232 satélites | `[DATO REAL]` #8 ¶3 |
| PV | Línea base A (FCC): 1.616 al 30/07/2026 y 3.232 al 30/07/2029, interpolada linealmente entre hitos. Línea base B (plan de Amazon): ≈ 700 al 30/07/2026 | `[DATO REAL]` en los hitos (#8 ¶3, ¶8); interpolación `[PROPUESTA]` |
| EV | Satélites lanzados acumulados | `[INFERENCIA DEL GRUPO]` (suma de #2) |
| AC | No público | — |

**Control de consistencia:** la serie EV suma 180 satélites al 16/12/2025, y Amazon declaró ante la FCC "180 satélites lanzados" el 30/01/2026 (#8 ¶8).

## 12.2 Resultados

`[INFERENCIA DEL GRUPO]` · Vcr = EV − PV · %Vcr = Vcr ÷ PV · SPI = EV ÷ PV

| Corte | Fecha | PV | EV | Vcr | %Vcr | SPI |
|---|---|---|---|---|---|---|
| Hito 50% · línea base A (FCC) | 30/07/2026 | 1.616 | 396 | −1.220 | −75% | **0,25** |
| Hito 50% · línea base B (plan Amazon) | 30/07/2026 | 700 | 396 | −304 | −43% | **0,57** |
| Corte · línea base A interpolada | 16/11/2026 | 1.777 | 396 | −1.381 | −78% | **0,22** |

**Lectura.** Un SPI menor a 1 indica que el proyecto avanza por debajo de lo planificado (Clase 6, pág. 28). Contra su propio plan, Amazon ejecutó el 57%; contra la exigencia del regulador, el 25%. Entre julio y noviembre de 2026 el SPI empeora (0,25 → 0,22) porque no hubo despliegues exitosos mientras el plan seguía avanzando.

**[INFERENCIA DEL GRUPO]** Que el plan de Amazon (~700) estuviera tan por debajo del hito de la FCC (1.616) muestra que **la empresa nunca planificó cumplir el hito intermedio**: pidió el waiver con un plan que ya lo daba por perdido (#8 ¶8).

## 12.3 Proyección: ¿cuándo termina?

| Escenario | Ritmo | Fin | Etiqueta |
|---|---|---|---|
| Ritmo observado (satélites) | 21,3 por mes | ≈ 2038 | `[INFERENCIA DEL GRUPO]` |
| Plan de Amazon (20 misiones/año × 30) | 50 por mes | ≈ 08/2031 | `[INFERENCIA DEL GRUPO]` sobre #23 |
| PERT (sección 9) | — | te ≈ 11/2035 (σ ≈ 24 meses) | `[PROPUESTA DE GESTIÓN]` |
| Necesario para el hito | 87,5 por mes | 30/07/2029 | `[INFERENCIA DEL GRUPO]` |

## 12.4 Costo: lo que no se puede calcular

El **CPI = EV ÷ AC** y la **Vco = EV − AC** requieren el costo real, que no es público. Se deja explícito y no se estima. Lo que sí se puede afirmar de forma cualitativa es la paradoja de "mucho gasto, poco avance": inversiones en instalaciones (> USD 340 millones, #27, #23) y más de 100 lanzamientos contratados con un avance físico del 12,3% (sección 10.4).

## 12.5 Sistema de seguimiento propuesto

`[PROPUESTA DE GESTIÓN]` con los instrumentos de la Clase 6:

| Instrumento | Contenido | Frecuencia |
|---|---|---|
| Informe de situación | EV, PV, SPI, cadencia del mes, causas de desvío, estimado para terminar | Mensual |
| Log de temas pendientes | T-01 (pérdida de LV-01) y los que se abran | Continuo |
| Resolución de temas | Formulario por tema (Riesgos §7.1) | Por evento |
| Reunión de avance con proveedores | Manifiesto y retorno al vuelo | Mensual y por misión |
| Reunión de finalización | Por hito (30/10/2027; 30/07/2029) | Por hito |

**Ante desvíos (Clase 6, pág. 17):** Amazon ya está aplicando "agregar más recursos" (más lanzadores) y "extender los plazos" (pedido a la FCC); "eliminar funciones" (resignar satélites) lo rechazó (#8 ¶8, ¶11). La propuesta del grupo combina las dos primeras con la **línea base de recuperación** (sección 8.6).
