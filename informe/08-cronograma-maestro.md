# 8. Tiempos: cronograma maestro

> Marco: `catedra/Clase 3 Gestión de los Tiempos · UCA.html` (milestones, inch-pebbles, dependencias, Gantt, acortamiento, nivelación y "zona inalcanzable"). Serie de misiones: `informe/seguimiento/ev_serie.csv`.

## 8.1 Milestones

| ID | Hito | Fecha | Tipo | Estado al 16/11/2026 | Etiqueta / fuente |
|---|---|---|---|---|---|
| M-01 | Autorización FCC (3.236 satélites) | 30/07/2020 | Regulatorio | Cumplido | `[DATO REAL]` #6, #39 |
| M-02 | Fábrica de Kirkland operativa | 04/2024 | Técnico | Cumplido | `[DATO REAL]` #26 |
| M-03 | Modificación FCC (3.232 satélites) | 08/03/2024 | Regulatorio | Cumplido | `[DATO REAL]` #7 |
| M-04 | Primera misión de producción (KA-01) | 28/04/2025 | Técnico | Cumplido | `[DATO REAL]` #2 |
| M-05 | Instalación de KSC operativa | 24/07/2025 | Técnico | Cumplido | `[DATO REAL]` #27 |
| M-06 | Preview empresarial | 24/11/2025 | Comercial | Cumplido | `[DATO REAL]` #29 |
| M-07 | Hito FCC del 50% (1.616 operativos) | 30/07/2026 | Regulatorio | **No cumplido** (396) | `[DATO REAL]` #8 / estado `[INFERENCIA]` |
| M-08 | Aviso de cumplimiento a la FCC | 14/08/2026 | Regulatorio | No encontrado | `[DATO REAL]` #7 ¶53 |
| M-09 | Primer vuelo de Vulcan para Leo | 15/11/2026 | Técnico | **Fallido** (tema T-01) | `[DATO REAL]` #2, #11 |
| M-10 | Inicio de servicio comercial | "later this year" (2026) | Comercial | Pendiente; sin criterio público | `[DATO REAL]` #3 / criterio `[PROPUESTA]` |
| M-11 | Certificación del 50% construido (acorta la pérdida de espectro) | 30/10/2027 | Regulatorio | Futuro | `[DATO REAL]` #8 ¶15 |
| M-12 | Fin de la pérdida de prioridad de espectro | 30/03/2028 | Regulatorio | Futuro | `[DATO REAL]` #8 ¶15 |
| M-13 | Hito FCC final (3.232 operativos) | 30/07/2029 | Regulatorio | En riesgo (R-04) | `[DATO REAL]` #8 ¶3 |

## 8.2 Inch-pebbles: cada misión es un punto de control

`[PROPUESTA DE GESTIÓN]` La Clase 3 dice que los inch-pebbles "dividen el avance en puntos intermedios más pequeños" y achican el área de desvío. En este proyecto la unidad natural es **la misión**: se sabe el día, el cohete y los satélites desplegados (#2). El control se hace por trimestre contra lo necesario.

| Trimestre | Misiones reales | Satélites desplegados | Acumulado | Fuente |
|---|---|---|---|---|
| 2T 2025 | 2 | 54 | 54 | #2 |
| 3T 2025 | 3 | 75 | 129 | #2 |
| 4T 2025 | 2 | 51 | 180 | #2 |
| 1T 2026 | 1 | 32 | 212 | #2 |
| 2T 2026 | 5 | 155 | 367 | #2 |
| 3T 2026 | 1 | 29 | 396 | #2 |
| 4T 2026 (al 16/11) | 1 (fallida) | 0 | 396 | #2, #11 |

**Umbral por trimestre** `[INFERENCIA DEL GRUPO]`: para llegar a 3.232 el 30/07/2029 hacen falta ≈ **262 satélites por trimestre** (87 por mes, C-23). El mejor trimestre real fue el 2T 2026, con 155.

## 8.3 Dependencias y secuencia

`[PROPUESTA DE GESTIÓN]` sobre la WBS (sección 7):

| Actividad | WBS | Predecesora | Relación | Comentario |
|---|---|---|---|---|
| Fabricar lote | 1.3.3 | Planta operativa (1.3.2) | Fin–inicio | Capacidad hasta 30/semana (#23) |
| Procesar e integrar carga | 1.4.3 | Fabricar lote; instalación KSC (1.4.1) | Fin–inicio | Hasta tres campañas simultáneas (#27) |
| Lanzar misión | 1.5.x | Procesar carga; cohete disponible (proveedor) | Fin–inicio | **Recurso externo**: depende del proveedor |
| Elevar y poner en servicio | 1.6.1 | Lanzar misión | Fin–inicio | No se despliega directo a la órbita operativa (#7 ¶43) |
| Desplegar gateways | 1.7.1 | Licencias por país (1.2.4) | Fin–inicio | En paralelo con 1.3–1.6 |
| Iniciar servicio por región | 1.9.2 | Satélites operativos (1.6) + gateways (1.7) + terminales (1.8) | Fin–inicio | Criterio del acta |

## 8.4 Gantt de alto nivel por campaña

`[DATO REAL]` hasta el 16/11/2026 (#2); después, `[PROPUESTA DE GESTIÓN]` sobre los contratos vigentes (Anexo A).

| Campaña | 2025 | 2026 | 2027 | 2028 | 2029 | Restantes |
|---|---|---|---|---|---|---|
| Atlas V (9) | ■■■■ (4) | ■■■■ (4) | ■ | | | 1 |
| Falcon 9 (13) | ■■■ (3) | | ▒▒▒▒ | ▒▒▒▒ | ▒▒ | 10 |
| Ariane 6 (24) | | ■■■ (3) | ▒▒▒▒▒ | ▒▒▒▒▒ | ▒▒▒▒▒ | 21 |
| Vulcan (38) | | ✕ LV-01 | ▒▒▒ (retorno sin fecha) | ▒▒▒▒▒▒ | ▒▒▒▒▒▒ | 37 |
| New Glenn (24) | | | ▒▒ (primer vuelo sin fecha) | ▒▒▒▒▒ | ▒▒▒▒▒ | 24 |

■ real · ✕ fallida · ▒ planificado (propuesta, sin fechas públicas).

## 8.5 Cuando el plazo limita el plan: acortamiento, nivelación y zona inalcanzable

**[INFERENCIA DEL GRUPO]** La Clase 3 explica que, si el plazo es fijo, se puede **acortar** (más recursos en paralelo) o **nivelar** (ajustar al recurso escaso), y que existe una **zona inalcanzable** donde ningún acortamiento razonable cumple la fecha. Aplicado a Amazon Leo:

- **Acortamiento:** agregar lanzadores (Ariane 6 de 18 a 24 y 10 Falcon 9 adicionales, #24, #23) es exactamente eso. OP-1 en Riesgos.
- **Nivelación:** Amazon nivela la fábrica según los lanzadores disponibles (#23). La fábrica no es el recurso escaso.
- **Zona inalcanzable:** hacen falta ≈ 35 misiones por año (C-24). El plan de Amazon es de 20 (C-25), el ritmo observado de ≈ 11, y el Monte Carlo (Riesgos §5) y PERT (sección 9) dan ≈ 0% de terminar a tiempo. **El hito de 2029 está en la zona inalcanzable con los recursos contratados.**
→ Supuestos: los del Monte Carlo y la estimación PERT.

## 8.6 Línea base propuesta y línea base de recuperación

`[PROPUESTA DE GESTIÓN]`

| Línea base | Qué es | Fin | Uso |
|---|---|---|---|
| **A · Regulatoria** | Hitos FCC: 1.616 al 30/07/2026; 3.232 al 30/07/2029 | 30/07/2029 | Restricción; PV de Valor Ganado |
| **R · Recuperación** (propuesta) | Plan de Amazon sostenido: 20 misiones por año × 30 satélites = 50 por mes desde el corte | ≈ 08/2031 (`valor_ganado.py`) | Base del **pedido de alivio a la FCC** (respuesta principal de R-04) y del cronograma interno |

La línea base R no cumple 2029, pero es el compromiso más exigente que tiene respaldo (el plan declarado de Amazon, #23). Presentarla con evidencia de avance es lo que mejora las chances de un nuevo alivio.

## 8.7 Reservas de tiempo

`[PROPUESTA DE GESTIÓN]` La reserva de ≈ 4 meses por R-02 (lanzador en tierra) se incorpora **una sola vez** a la línea base R: ≈ 08/2031 + 4 meses ≈ **12/2031**. No se suma de nuevo por R-03 ni por R-04, porque es el mismo atraso visto desde otro riesgo (Riesgos §6, "doble cuenta").
