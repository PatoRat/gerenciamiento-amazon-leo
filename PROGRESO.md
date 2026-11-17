# Estado del trabajo — Amazon Leo

Punto de entrada de cada sesión. Cada checkpoint cierra con **revisión manual** de un miembro del equipo; desde el 16/11/2026 la revisión se hace por **Pull Request** (ver "Ramas y cambios").

Estados: `⬜ pendiente` · `🔄 en curso` · `🟡 esperando revisión` · `✅ aprobado`

**Estado actual (16/11/2026):** 🟡 **informe completo en borrador y dashboard funcionando, esperando revisión del equipo** en el PR de la rama `entrega/informe-y-dashboard`. Siguiente: cada integrante revisa sus secciones (ver "Reparto"), el equipo confirma los KPIs y las decisiones pendientes, y se mergea a `main`.

**Cómo ver todo rápido:**
- Informe completo: `informe/Informe_Amazon_Leo.docx` (o `.md`). Se regenera con `python informe/compilar_informe.py`.
- Dashboard: abrir `dashboard/amazon-leo-dashboard.html` con doble clic (funciona sin internet). Se regenera con `python dashboard/build_dashboard.py`.

---

## Instancia 1 — Informe de investigación

| # | Checkpoint | Estado | Fecha | Revisó | Archivos |
|---|---|---|---|---|---|
| I-1 | Mapeo y evaluación de fuentes | 🟡 | 15–16/11/2026 | — | `evidencia/registro-fuentes.md` (47 fuentes), `evidencia/verificacion-i1-2026-11-16.md` |
| I-2 | Hitos públicos y mapa de actores | 🟡 | 16/11/2026 | — | `evidencia/hitos.md`, `evidencia/actores.md` |
| I-3 | Estructura del informe y plantillas | 🟡 | 16/11/2026 | — | `informe/00-estructura.md`, `informe/plantillas/*.md` (8) |
| I-4 | Guías metodológicas | 🟡 | 16/11/2026 | — | `informe/guias/riesgos.md`, `seguimiento-valor-ganado.md`, `alcance-wbs.md` |
| — | **Redacción de secciones** (borradores con IA, habilitada por la cátedra) | 🟡 | 16/11/2026 | — | `informe/00-resumen-ejecutivo.md` a `informe/14-conclusiones-y-limitaciones.md` |
| I-5 | Revisión de trazabilidad y coherencia | 🔄 autocontrol hecho (§13.3 del informe); falta la revisión del equipo | 16/11/2026 | — | `informe/13-integracion-y-coherencia.md` |

### Secciones del informe

| N.° | Sección | Archivo | Estado | Revisa |
|---|---|---|---|---|
| 0 | Resumen ejecutivo | `00-resumen-ejecutivo.md` | 🟡 borrador | Todos |
| 1 | Introducción, método y declaración de IA | `01-introduccion-y-metodo.md` | 🟡 borrador | Todos |
| 2 | Ubicación del proyecto | `02-ubicacion-del-proyecto.md` | 🟡 borrador | A |
| 3 | Evidencia y fuentes | `03-evidencia-y-fuentes.md` | 🟡 borrador | A |
| 4 | Actores e interesados (+ plan de comunicaciones) | `04-actores-e-interesados.md` | 🟡 borrador | A |
| 5 | Caso de negocio | `05-caso-de-negocio.md` | 🟡 borrador | A |
| 6 | Acta de constitución (reconstruida al 30/07/2020) | `06-acta-de-constitucion.md` | 🟡 borrador | A |
| 7 | Alcance y WBS | `07-alcance-y-wbs.md` | 🟡 borrador | B |
| 8 | Cronograma maestro | `08-cronograma-maestro.md` | 🟡 borrador | B |
| 9 | Estimaciones (PERT) | `09-estimaciones.md` + `estimaciones/pert_despliegue.py` | 🟡 borrador | B |
| 10 | Costos y presupuesto | `10-costos-y-presupuesto.md` | 🟡 borrador | C |
| 11 | Riesgos | `riesgos/gestion-de-riesgos-amazon-leo.md` (+ `.docx`) | 🟡 corregida (ramas 2–5) | D |
| 12 | Seguimiento y valor ganado | `12-seguimiento-y-valor-ganado.md` + `seguimiento/valor_ganado.py` | 🟡 borrador | C |
| 13 | Integración y coherencia | `13-integracion-y-coherencia.md` | 🟡 borrador | D |
| 14 | Conclusiones y limitaciones | `14-conclusiones-y-limitaciones.md` | 🟡 borrador | Todos |
| Anexos | A fuentes · B hitos · C actores · D cifras maestras · E código · F verificación | `evidencia/`, `informe/cifras-maestras.md` | 🟡 | D |

### Propuesta de reparto (A DEFINIR por el equipo; las letras no son personas asignadas)

| Integrante | Revisa y defiende |
|---|---|
| A | 2 Ubicación · 3 Evidencia · 4 Actores · 5 Caso de negocio · 6 Acta |
| B | 7 Alcance y WBS · 8 Cronograma · 9 Estimaciones |
| C | 10 Costos · 12 Valor ganado |
| D (autor/a de Riesgos) | 11 Riesgos · 13 Integración · cifras maestras · anexos |
| Todos | 0 Resumen · 1 Método · 14 Conclusiones · guion de defensa |

**Cierre de la Instancia 1:** ⬜ informe revisado y aprobado por el equipo.

---

## Instancia 2 — Dashboard de defensa

Iniciada el 16/11/2026 por pedido del equipo ("avanzar todo lo posible").

| # | Checkpoint | Estado | Fecha | Archivos |
|---|---|---|---|---|
| D-1 | KPIs y modelo de datos | 🟡 **selección provisoria**, a confirmar | 16/11/2026 | `dashboard/datos/kpis.md`, `kpis.json` (12 KPIs de `kpis-sugeridos.md`) |
| D-2 | Wireframe y jerarquía | 🟡 | 16/11/2026 | `dashboard/wireframe.md` |
| D-3 | Construcción del HTML | 🟡 | 16/11/2026 | `dashboard/amazon-leo-dashboard.html` (generado), `plantilla-dashboard.html`, `build_dashboard.py` |
| D-4 | Guion de defensa | 🟡 | 16/11/2026 | `dashboard/guion-defensa.md` (16 preguntas probables) |

Verificado: un solo archivo de 32 KB sin dependencias de red (el build lo controla), JS sin errores, capturas en claro, oscuro y celular, paleta validada para daltonismo. **Falta que el equipo pruebe el PDF y el tablero en la notebook del aula.**

**Cierre de la Instancia 2:** ⬜ dashboard probado sin internet y PDF verificado por el equipo.

---

## Ramas y cambios

Las 11 ramas apiladas del 16/11/2026 se **unificaron** en `entrega/informe-y-dashboard` para un solo PR a `main`. Se conservan como historia (un commit por cambio).

| Orden | Rama (commit) | Tipo | Qué cambia |
|---|---|---|---|
| 1 | `fix/01-uso-ia-y-progreso` | Corrección | Uso de IA habilitado por la cátedra (CLAUDE.md §3); PROGRESO al día; regla "una rama por cambio". |
| 2 | `fix/02-r01-riesgo-materializado` | Corrección | R-01 ocurrió (LV-01) → **tema T-01** con el formulario de Resolución de Temas (Clase 6); R-01 mide la recurrencia. |
| 3 | `fix/03-r04-reformulacion` | Corrección | R-04 = "la FCC no concede un nuevo alivio"; no llegar por cadencia es condición prevista (Monte Carlo ≈ 0%). |
| 4 | `fix/04-cifras-contratos-y-fuentes` | Corrección | Contratos con fecha de corte (New Glenn = 24, total ≈ 108); fuentes #21–#47 al registro; correcciones de la verificación. |
| 5 | `fix/05-operativos-y-fecha-de-corte` | Corrección | Lanzados ≈ operativos explícito; fecha de corte propuesta; `.docx` de Riesgos regenerado. |
| 6 | `feat/06-cifras-maestras` | Sugerencia | `informe/cifras-maestras.md`: fuente única de números. |
| 7 | `feat/07-promesas-inicio-servicio` | Sugerencia | Línea de tiempo de promesas de inicio del servicio. |
| 8 | `feat/08-valor-ganado-satelites` | Sugerencia | Valor ganado en satélites (guía + script). |
| 9 | `feat/09-kpis-sugeridos-dashboard` | Sugerencia | 16 KPIs sugeridos. |
| 10 | `feat/10-edt-flujo-fisico` | Sugerencia | Guía de Alcance con WBS por flujo físico. |
| 11 | `feat/11-i3-estructura-informe` | Desarrollo | I-3: índice, mapa de coherencia y plantillas. |
| 12 | `entrega/informe-y-dashboard` | Desarrollo | Informe completo (secciones 0–14 + compilador a `.docx`), PERT, dashboard (D-1 a D-4), verificación de la inversión de 2020. |

---

## Bitácora

| Fecha | Checkpoint | Qué pasó / qué decidió el equipo |
|---|---|---|
| 14/11/2026 | — | Inicialización del proyecto: `CLAUDE.md`, estructura de carpetas, registro de fuentes y comandos. |
| 15/11/2026 | I-1 | Primer barrido de fuentes: 20 fuentes, 6 contradicciones, 7 vacíos. La 1ª misión Vulcan dedicada falló el 15/11/2026. |
| 16/11/2026 | I-1 / I-2 / Riesgos | PR #1: verificación de I-1 contra FCC y SEC, borradores de hitos y actores, sección de Riesgos con Monte Carlo. |
| 16/11/2026 | Revisión general | Revisión contra la consigna y la cátedra: 6 problemas urgentes y faltantes del informe, el dashboard y la defensa. |
| 16/11/2026 | Decisión | **La cátedra habilitó el uso de IA para la redacción.** Se adopta "una rama por cambio" con PR. |
| 16/11/2026 | Ramas 1–11 | Correcciones urgentes, sugerencias e I-3 (ver "Ramas y cambios"). |
| 16/11/2026 | Entrega (rama 12) | Pedido del equipo: avanzar todo lo posible y unificar en un PR. Se redactaron las secciones 0–14 (borradores), se agregó la estimación PERT (fin ≈ 11/2035; P ≈ 0,07% de cumplir 2029), se verificó en el primario la inversión de 2020 (> USD 10.000 millones, #39) y se construyó el dashboard con KPIs provisorios y guion de defensa. |

---

## Decisiones tomadas por el equipo

- **Marco teórico:** el de la cátedra (`catedra/`). No asumir PMBOK/ISO por defecto.
- **Dashboard:** un único HTML local autónomo con botón de PDF.
- **Uso de IA (16/11/2026):** habilitado por la cátedra. Claude redacta borradores; el equipo revisa, aprueba y defiende. Declaración en §1.5 del informe. No se inventan datos.
- **Flujo de trabajo (16/11/2026):** un commit/rama por cambio; integración por PR.

## Decisiones pendientes del equipo (revisar en el PR)

- [ ] **Fecha de corte:** propuesta 16/11/2026. Si se mueve (por ejemplo, para incluir LE-04 del 23/11), se actualiza todo junto: cifras maestras → `kpis.json` → scripts → compilar.
- [ ] **KPIs del dashboard:** confirmar o cambiar la selección provisoria de `dashboard/datos/kpis.md`.
- [ ] **Alcance:** confirmar que Gen2, Polar, D2D y Globalstar quedan fuera (§7.1).
- [ ] **Fecha del acta:** se reconstruyó al 30/07/2020 (§6). Confirmar.
- [ ] **Línea base de recuperación** (≈ 08/2031 + 4 meses de reserva, §8.6): confirmar como propuesta del equipo.
- [ ] **Probabilidades e impactos de Riesgos:** cada integrante tiene que poder justificarlos (guion, §3).

## Pendientes del equipo

- [x] Cargar el material de la cátedra (14/11/2026).
- [x] Confirmar con la cátedra el uso de IA (16/11/2026).
- [ ] Revisar el PR por secciones (reparto) y mergear a `main`.
- [ ] Probar el dashboard sin internet en la notebook del aula y generar el PDF.
- [ ] Ensayar la defensa con `dashboard/guion-defensa.md`.
- [ ] Confirmar fecha de entrega y de defensa.
- [ ] Opcional: transcribir los PDF de Calidad y Comunicaciones si se quiere ampliar §4.
