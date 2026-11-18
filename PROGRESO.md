# Estado del trabajo — Amazon Leo

Punto de entrada de cada sesión. Cada checkpoint cierra con **revisión manual** de un miembro del equipo. Desde el 16/11/2026 los cambios se integran por **Pull Request**; el 17/11/2026 la limpieza de entrega se subió directo a `main` (ver "Ramas y cambios").

Estados: `⬜ pendiente` · `🔄 en curso` · `🟡 integrado, sin revisión de pares` · `✅ aprobado`

**Estado actual (17/11/2026):** 🟡 **informe completo y dashboard integrados en `main`, todavía sin revisión de pares.** El PR #2 se mergeó el 17/11/2026 sin reviews registradas. Después se limpió la entrega: sin carteles de "Borrador" ni marcas internas `[[PENDIENTE]]` (ahora "No público" / "No calculable"), anexos sin notas de revisión, sin la sección 1.5, frases de fuentes reescritas como "texto original consultado", Word regenerado con pandoc y desbordes del tablero corregidos. **Falta:** que cada integrante revise sus secciones sobre `main`, confirmar los KPIs y las decisiones pendientes, probar el tablero y su PDF en la notebook del aula, y confirmar fecha y medio de entrega.

**Cómo ver todo rápido:**
- Informe completo: `informe/Informe_Amazon_Leo.docx` (o `.md`). Se regenera con `python informe/compilar_informe.py` (el `.docx` necesita `pandoc` instalado).
- Dashboard: abrir `dashboard/amazon-leo-dashboard.html` con doble clic (funciona sin internet). Se regenera con `python dashboard/build_dashboard.py`.

---

## Instancia 1 — Informe de investigación

| # | Checkpoint | Estado | Fecha | Revisó | Archivos |
|---|---|---|---|---|---|
| I-1 | Mapeo y evaluación de fuentes | 🟡 | 15–16/11/2026 | — | `evidencia/registro-fuentes.md` (47 fuentes), `evidencia/verificacion-i1-2026-11-16.md` |
| I-2 | Hitos públicos y mapa de actores | 🟡 | 16/11/2026 | — | `evidencia/hitos.md`, `evidencia/actores.md` |
| I-3 | Estructura del informe y plantillas | 🟡 | 16/11/2026 | — | `informe/00-estructura.md`, `informe/plantillas/*.md` (8) |
| I-4 | Guías metodológicas | 🟡 | 16/11/2026 | — | `informe/guias/riesgos.md`, `seguimiento-valor-ganado.md`, `alcance-wbs.md` |
| — | **Redacción de secciones** (redactadas con IA, habilitada por la cátedra) | 🟡 | 16/11/2026 | — | `informe/00-resumen-ejecutivo.md` a `informe/14-conclusiones-y-limitaciones.md` |
| I-5 | Revisión de trazabilidad y coherencia | 🔄 autocontrol hecho (§13.3 del informe); falta la revisión del equipo | 16/11/2026 | — | `informe/13-integracion-y-coherencia.md` |

### Secciones del informe

| N.° | Sección | Archivo | Estado | Revisa |
|---|---|---|---|---|
| 0 | Resumen ejecutivo | `00-resumen-ejecutivo.md` | 🟡 sin revisar | Todos |
| 1 | Introducción y método | `01-introduccion-y-metodo.md` | 🟡 sin revisar | Todos |
| 2 | Ubicación del proyecto | `02-ubicacion-del-proyecto.md` | 🟡 sin revisar | A |
| 3 | Evidencia y fuentes | `03-evidencia-y-fuentes.md` | 🟡 sin revisar | A |
| 4 | Actores e interesados (+ plan de comunicaciones) | `04-actores-e-interesados.md` | 🟡 sin revisar | A |
| 5 | Caso de negocio | `05-caso-de-negocio.md` | 🟡 sin revisar | A |
| 6 | Acta de constitución (reconstruida al 30/07/2020) | `06-acta-de-constitucion.md` | 🟡 sin revisar | A |
| 7 | Alcance y WBS | `07-alcance-y-wbs.md` | 🟡 sin revisar | B |
| 8 | Cronograma maestro | `08-cronograma-maestro.md` | 🟡 sin revisar | B |
| 9 | Estimaciones (PERT) | `09-estimaciones.md` + `estimaciones/pert_despliegue.py` | 🟡 sin revisar | B |
| 10 | Costos y presupuesto | `10-costos-y-presupuesto.md` | 🟡 sin revisar | C |
| 11 | Riesgos | `riesgos/gestion-de-riesgos-amazon-leo.md` (+ `.docx`) | 🟡 sin revisar (apéndices R-A y R-B) | D |
| 12 | Seguimiento y valor ganado | `12-seguimiento-y-valor-ganado.md` + `seguimiento/valor_ganado.py` | 🟡 sin revisar | C |
| 13 | Integración y coherencia | `13-integracion-y-coherencia.md` | 🟡 sin revisar | D |
| 14 | Conclusiones y limitaciones | `14-conclusiones-y-limitaciones.md` | 🟡 sin revisar | Todos |
| Anexos | A fuentes · B hitos · C actores · D cifras maestras · E código · F verificación | `evidencia/`, `informe/cifras-maestras.md` | 🟡 | D |

### Propuesta de reparto (A DEFINIR por el equipo; las letras no son personas asignadas)

| Integrante | Revisa y defiende |
|---|---|
| A | 2 Ubicación · 3 Evidencia · 4 Actores · 5 Caso de negocio · 6 Acta |
| B | 7 Alcance y WBS · 8 Cronograma · 9 Estimaciones |
| C | 10 Costos · 12 Valor ganado |
| D (autor/a de Riesgos) | 11 Riesgos · 13 Integración · cifras maestras · anexos |
| Todos | 0 Resumen · 1 Método · 14 Conclusiones · guion de defensa |

### Reparto de la defensa (propuesta del grupo, 17/11/2026)

Orden de exposición. Los números de pregunta son los de `dashboard/guion-defensa.md` §2. Las personas de cada bloque no están asignadas en este documento.

| Bloque | Pregunta que defiende | Secciones (3 cada uno) | Preguntas del guion | Exposición |
|---|---|---|---|---|
| 1 | ¿Qué es y por qué se hace? (abre la defensa) | 2 Ubicación · 3 Fuentes · 5 Caso de negocio | 1, 2, 3, 16 | ≈ 5 min |
| 2 | ¿Quién lo hace y cómo se organiza? | 4 Actores · 6 Acta · 7 Alcance y WBS | 4, 11, 12, 15 | ≈ 5 min |
| 3 | ¿Está atrasado? ¿Cuándo termina? | 8 Cronograma · 9 Estimaciones · 12 Valor ganado | 5, 7, 10, 14 | ≈ 5 min |
| 4 | ¿Qué puede salir mal y qué haríamos? (cierra la defensa) | 10 Costos · 11 Riesgos · 13 Integración | 6, 8, 9, 13 | ≈ 5 min |
| Todos | Resumen, método y conclusiones | 0 · 1 · 14 | — | — |

> `dashboard/guion-defensa.md` §4 todavía tiene la propuesta anterior (A a D con otras preguntas). Hay que alinearlo con este reparto.

**Cierre de la Instancia 1:** ⬜ informe revisado y aprobado por el equipo.

---

## Instancia 2 — Tablero ejecutivo

Iniciada el 16/11/2026 por pedido del equipo ("avanzar todo lo posible").

| # | Checkpoint | Estado | Fecha | Archivos |
|---|---|---|---|---|
| D-1 | KPIs y modelo de datos | 🟡 **selección provisoria**, a confirmar | 16/11/2026 | `dashboard/datos/kpis.md`, `kpis.json` (12 KPIs de `kpis-sugeridos.md`) |
| D-2 | Wireframe y jerarquía | 🟡 | 16/11/2026 | `dashboard/wireframe.md` |
| D-3 | Construcción del HTML | 🟡 sin cartel de borrador; desbordes corregidos | 17/11/2026 | `dashboard/amazon-leo-dashboard.html` (generado), `plantilla-dashboard.html`, `build_dashboard.py` |
| D-4 | Guion de defensa | 🟡 | 16/11/2026 | `dashboard/guion-defensa.md` (16 preguntas probables) |

Verificado: un solo archivo de 32 KB sin dependencias de red (el build lo controla), JS sin errores, capturas en claro, oscuro y celular, paleta validada para daltonismo. El 17/11/2026 se quitó el cartel "Borrador" y se corrigieron dos desbordes (leyenda de lanzamientos restantes y eje del gráfico "Fin proyectado"); se revisó la vista de impresión (6 páginas) con Chrome sin interfaz. **Falta que el equipo pruebe el PDF y el tablero en la notebook del aula, sin internet.**

**Cierre de la Instancia 2:** ⬜ dashboard probado sin internet y PDF verificado por el equipo.

---

## Ramas y cambios

Las 11 ramas apiladas del 16/11/2026 se **unificaron** en `entrega/informe-y-dashboard` para un solo PR a `main`. Se conservan como historia (un commit por cambio). El PR #1 (borradores de Riesgos, I-1 e I-2) se mergeó el 17/11/2026 y el PR #2 el mismo día, sin reviews registradas. Después se subieron directo a `main`, por pedido de un integrante: la limpieza de carteles y marcas internas, el `.docx` regenerado con pandoc, el cambio del tablero y esta actualización (ver `git log`).

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
| 17/11/2026 | PR #1 y PR #2 | Se mergean a `main` los PR #1 y #2, sin reviews registradas. |
| 17/11/2026 | Limpieza de entrega | Directo a `main`: se quitan los carteles de borrador y las marcas `[[PENDIENTE]]` del informe, se renombran los anexos de Riesgos a Apéndice R-A y R-B y se regenera el `.docx`. |
| 17/11/2026 | Dashboard | Se quita el cartel "Borrador", se corrigen dos desbordes de texto y se renombra el tablero a "Tablero ejecutivo" (sin referencias a la defensa). |
| 17/11/2026 | Informe y anexos | Directo a `main`, por pedido de un integrante: anexos sin notas de revisión, se quita la sección 1.5 y las menciones a herramientas de IA (también en Riesgos), y "leída" / "se leyeron" pasan a "texto original consultado" para no atribuir lecturas a un lector no identificado. Se regenera el `.docx`. |
| 17/11/2026 | Versión resumida | Se agrega `informe/resumido/` con una versión del informe de ≈ 10.000 palabras (≈ 27 páginas según un PDF de prueba; en Word hay que contarlas), para revisión del equipo. No reemplaza al informe completo, que no se tocó. Incluye `ajustar_word.py` para reproducir el formato del Word. |
| 17/11/2026 | Tablero y cifras | En el tablero se actualizan las referencias al informe (ahora con la numeración del resumido y, entre paréntesis, la del completo) y se aclara que el ≈ 0% del Monte Carlo depende de los supuestos (≈ 7% con más ritmo). El resumido pasa a mostrar los mismos valores del Monte Carlo que el tablero (P10 ≈ 1.141, P50 ≈ 1.513, P90 ≈ 2.046). |
| 17/11/2026 | Tablero: costos | Se agrega la tarjeta "Costos: lo que sí se sabe" en el bloque Organización, con lo público de la sección 10 (los datos están en `kpis.json`, clave `costos`). |
| 17/11/2026 | Reparto de la defensa | El grupo propone 4 bloques de ≈ 5 min (ver "Reparto de la defensa"). Quedan sin asignar las personas. |

---

## Decisiones tomadas por el equipo

- **Marco teórico:** el de la cátedra (`catedra/`). No asumir PMBOK/ISO por defecto.
- **Dashboard:** un único HTML local autónomo con botón de PDF.
- **Uso de IA (16/11/2026):** habilitado por la cátedra. Claude redacta borradores; el equipo revisa, aprueba y defiende. El 17/11/2026, por pedido de un integrante, se quitaron del informe y de los anexos la sección 1.5 y las demás menciones a herramientas de IA. Las decisiones de contenido las aprueba y defiende el equipo. No se inventan datos.
- **Flujo de trabajo (16/11/2026):** un commit/rama por cambio; integración por PR.

## Decisiones pendientes del equipo

- [ ] **Fecha de corte:** propuesta 16/11/2026. Si se mueve (por ejemplo, para incluir LE-04 del 23/11), se actualiza todo junto: cifras maestras → `kpis.json` → scripts → compilar.
- [ ] **KPIs del dashboard:** confirmar o cambiar la selección provisoria de `dashboard/datos/kpis.md`.
- [ ] **Alcance:** confirmar que Gen2, Polar, D2D y Globalstar quedan fuera (§7.1).
- [ ] **Fecha del acta:** se reconstruyó al 30/07/2020 (§6). Confirmar.
- [ ] **Línea base de recuperación** (≈ 08/2031 + 4 meses de reserva, §8.6): confirmar como propuesta del equipo.
- [ ] **Probabilidades e impactos de Riesgos:** cada integrante tiene que poder justificarlos (guion, §3).

## Pendientes del equipo

- [x] Cargar el material de la cátedra (14/11/2026).
- [x] Confirmar con la cátedra el uso de IA (16/11/2026).
- [x] Mergear a `main` el PR #1 y el PR #2 (17/11/2026).
- [ ] Revisión por secciones sobre `main` (no hubo revisión de pares antes del merge).
- [ ] Asignar personas a los 4 bloques de la defensa y alinear `dashboard/guion-defensa.md` §4.
- [ ] Abrir `informe/Informe_Amazon_Leo.docx` y revisar tablas y saltos de página.
- [ ] Si el repo se va a mostrar: revisar las menciones a IA que quedan en archivos de trabajo (`CLAUDE.md`, `.claude/`, borradores de `informe/riesgos/`, READMEs) y en el historial de commits.
- [ ] Probar el dashboard sin internet en la notebook del aula y generar el PDF.
- [ ] Ensayar la defensa con `dashboard/guion-defensa.md`.
- [ ] Confirmar fecha de entrega y de defensa.
- [ ] Opcional: transcribir los PDF de Calidad y Comunicaciones si se quiere ampliar §4.
