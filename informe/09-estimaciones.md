# 9. Estimaciones

> Marco: `catedra/Clase 4 Estimaciones 1ra. Parte …html` (métodos, ventana, prejuicios) y `catedra/Clase 4 Estimaciones · Segunda Parte …html` (PERT por tres valores). Cálculo: `informe/estimaciones/pert_despliegue.py`.

## 9.1 Qué se estima y con qué método

| Variable | Método (Clase 4) | Por qué | Base |
|---|---|---|---|
| Satélites por misión | **Análoga** (misiones ya voladas por cohete) | Hay historia real por vehículo | #2, #3: 24 (Falcon 9), 27–29 (Atlas V), 32–36 (Ariane 64), 40 (Vulcan) |
| Cadencia de lanzamiento | **Tres valores (PERT)** | Alta incertidumbre: fallas, retornos al vuelo, cohetes nuevos | #2, #23, R-02 |
| Duración del despliegue restante | **Paramétrica** (satélites que faltan ÷ ritmo) + PERT | Relación cuantitativa directa | C-14 |
| Producción | Dato declarado (no se estima) | No es el cuello de botella | #23 |

## 9.2 Estimación PERT de la duración restante

`[PROPUESTA DE GESTIÓN]` Se estima cuánto tarda desplegar los 2.836 satélites que faltan (C-14), con 30 satélites por misión. Los tres valores son **los mismos del Monte Carlo** de Riesgos (§5), para que ambas herramientas sean coherentes.

| Valor | Cadencia | Justificación | Duración | Fin |
|---|---|---|---|---|
| a · optimista ("sin milagros") | 2,0 misiones/mes (24/año) | Por encima del plan "20+" de Amazon (#23) | 47,3 meses | ≈ 10/2030 |
| m · más probable | 0,92 misiones/mes (≈ 11/año) | Ritmo observado desde el 28/04/2026 (#2) | 102,8 meses | ≈ 06/2035 |
| b · pesimista ("sin catástrofes") | 0,5 misiones/mes (6/año) | Lanzadores clave en tierra buena parte del período (R-02) | 189,1 meses | ≈ 08/2042 |

**Resultado** `[INFERENCIA DEL GRUPO]`:
- te = (a + 4m + b) / 6 = **107,9 meses → ≈ 11/2035**
- σ = (b − a) / 6 = **23,6 meses**
- Meses disponibles hasta el 30/07/2029: 32,4 → z = −3,19 → **P(terminar a tiempo) ≈ 0,07%** (aproximación normal)

## 9.3 Coherencia entre las tres herramientas

| Herramienta | Resultado | Por qué difiere |
|---|---|---|
| Monte Carlo (Riesgos §5) | P50 ≈ 1.513 satélites al 30/07/2029; P(llegar) ≈ 0% | Distribución triangular sobre la **cadencia** |
| PERT (esta sección) | Fin ≈ 11/2035; P ≈ 0,07% | Beta sobre la **duración**. Los pesimistas pesan más, porque la duración es inversa a la cadencia |
| Valor Ganado (sección 12) | Fin ≈ 2031 (plan) · ≈ 2038 (ritmo observado en satélites) | Proyección lineal de un solo escenario |

**[INFERENCIA DEL GRUPO]** Las tres herramientas, con supuestos distintos, llegan a la misma conclusión: **el hito de 2029 no se cumple con la capacidad contratada**. El rango razonable de fin está entre 2031 y 2038.

## 9.4 Ventana de estimación

`[PROPUESTA DE GESTIÓN]` La Clase 4 propone estimar todo a alto nivel y en detalle la etapa siguiente, y **reestimar al cerrar cada etapa**. Ventanas propuestas:
1. **Al retorno al vuelo de Vulcan** (cierre del tema T-01): reestimar m y b.
2. **Al primer vuelo de New Glenn para Leo:** reestimar a.
3. **Cada trimestre** con los inch-pebbles (sección 8.2).

## 9.5 Prejuicios en las estimaciones

**[INFERENCIA DEL GRUPO]** La Clase 4 advierte sobre los prejuicios en las estimaciones. Hay dos visibles en este caso:
- **Optimismo de la fuente:** las cifras de Amazon (capacidad de 30 por semana, "20+ misiones", "~700 al 30/07/2026") son declaraciones propias. La proyección presentada a la FCC (~700) terminó en 396 (C-04, C-12).
- **Anclaje en la capacidad instalada:** confundir capacidad (fábrica, contratos) con ritmo efectivo. El registro de fuentes ya separa "capacidad declarada" de "ritmo real".
Por eso el valor más probable (m) se tomó del **ritmo observado** y no del plan.
