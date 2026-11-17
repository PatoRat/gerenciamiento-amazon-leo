# KPIs del dashboard (D-1) — selección provisoria

> **Estado: a confirmar por el equipo.** Los KPIs los define el equipo (`CLAUDE.md` §8). Esta es una **selección provisoria** tomada de `kpis-sugeridos.md` (los marcados como "los que más preguntas cubren", más los de estado y riesgos) para tener un tablero funcionando. Para cambiarla: editar `kpis.json` y correr `python dashboard/build_dashboard.py`.
>
> Fecha de corte: 16/11/2026. Todas las cifras salen de `informe/cifras-maestras.md`.

| # | KPI | Qué responde | Valor | Origen | Meta / umbral |
|---|---|---|---|---|---|
| 1 | Satélites desplegados contra hitos | ¿Cuánto avanzó? ¿Cumplió 2026? | 396 / 3.232 (12,3%); 24,5% del hito de 1.616 | `[INFERENCIA]` C-12, C-15, C-16 | Hito 50% = 1.616 (rojo: no cumplido) |
| 2 | Curva S (EV contra PV FCC, recuperación y ritmo observado) | ¿Cuánto se separó del plan y qué pasa si sigue así? | Serie de 14 despliegues + proyecciones | `[DATO REAL]` #2 + `[PROPUESTA]` 8.6 | PV FCC |
| 3 | SPI (tres líneas base) | ¿Qué tan eficiente es el uso del tiempo? | 0,57 · 0,25 · 0,22 | `[INFERENCIA]` C-52 | 1,0 |
| 4 | Ritmo real contra necesario | ¿Puede llegar? ¿Dónde está el cuello de botella? | 21,3 / 50 / 87,5 / 130 sat/mes | C-21, C-25, C-23, C-30 | 87,5 (necesario) |
| 5 | Fin proyectado | ¿Cuándo termina? | 2029 (hito) · 08/2031 · 11/2035 · 2038 | VG, PERT | 30/07/2029 |
| 6 | Promesas de inicio del servicio | ¿Amazon cumple sus fechas? | 2024 → 2025 → 2026 → sin servicio | `[DATO REAL]` hitos §5 | — |
| 7 | Matriz P×I | ¿Cuáles son los riesgos principales? | 2 rojos (R-04, R-02) | `[PROPUESTA]` Riesgos §4.5 | Cortes 0,20 / 0,10 / 0,05 |
| 8 | Exposición antes / después | ¿Sirven las respuestas? | Σ 0,82 → 0,50 | `[PROPUESTA]` C-53 | — |
| 9 | Monte Carlo al 30/07/2029 | ¿Es posible cumplir el hito? | P10 1.141 · P50 1.513 · P90 2.046 · P ≈ 0% | `[INFERENCIA]` C-50, C-51 | 3.232 |
| 10 | Lanzamientos restantes por proveedor | ¿De quién depende? | Vulcan + New Glenn = 61 de 93 (66%) | `[INFERENCIA]` C-41, C-42 | — |
| 11 | Temas abiertos | ¿Qué problema está activo? | T-01 (LV-01) | Riesgos §7.1 | — |
| 12 | Cadena fabricación → lanzamiento → operación | ¿Cómo se conectan? ¿Dónde se traba? | 30/sem · > 100/mes · 21/mes · 396 · > 300 gateways | Sección 7.4 | — |
| — | Pendientes visibles | Qué no se puede mostrar | CPI, costos, operativos | Cifras maestras §7 | `[[PENDIENTE]]` |

**Descartados de la lista sugerida (por espacio):** mapa de actores (se explica oralmente con la sección 4 del informe) y estado del servicio comercial como KPI separado (está en las promesas).
