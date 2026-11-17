# Estado del trabajo — Amazon Leo

Punto de entrada de cada sesión. Las dos instancias son corridas separadas y **cada checkpoint cierra con revisión manual** de un miembro del equipo. Desde el 16/11/2026, **cada cambio va en su propia rama** y se revisa por Pull Request (ver "Ramas y cambios").

Estados: `⬜ pendiente` · `🔄 en curso` · `🟡 esperando revisión` · `✅ aprobado`

**Checkpoint actual:** **I-3 🟡 esperando aprobación del índice** (rama 11). I-1 e I-2 también esperan revisión. Siguiente: revisar y mergear las ramas 1 a 11 en orden, aprobar el índice de `informe/00-estructura.md` y repartir la redacción de las secciones (ver "Reparto sugerido").

---

## Instancia 1 — Informe de investigación

| # | Checkpoint | Comando | Estado | Fecha | Revisó | Archivos generados |
|---|---|---|---|---|---|---|
| I-1 | Mapeo y evaluación de fuentes | `/informe:fuentes` | 🟡 | 15/11/2026 · verificado 16/11/2026 | — | `evidencia/registro-fuentes.md` (20 fuentes), `evidencia/verificacion-i1-2026-11-16.md` (confirma #7, #8 y #11 contra el primario; corrige #5) |
| I-2 | Hitos públicos y mapa de actores | `/informe:hitos` | 🟡 borrador | 16/11/2026 | — | `evidencia/hitos.md`, `evidencia/actores.md` (proponen fuentes #21 a #47) |
| I-3 | Estructura del informe y plantillas | `/informe:estructura` | 🟡 | 16/11/2026 | — | `informe/00-estructura.md` (15 secciones + 6 anexos, mapa de coherencia, evidencia flaca); `informe/plantillas/`: `acta-constitucion.md`, `caso-de-negocio.md`, `declaracion-alcance-wbs.md`, `cronograma-maestro.md`, `estimaciones.md`, `presupuesto-costos.md`, `informe-situacion.md` (+ `registro-riesgos.md` previa) |
| I-4 | Guías metodológicas por sección | `/informe:guia <sección>` | 🔄 parcial | 16/11/2026 | — | `informe/guias/riesgos.md`, `informe/guias/seguimiento-valor-ganado.md`, `informe/guias/alcance-wbs.md` |
| I-5 | Revisión de trazabilidad y coherencia | `/informe:revisar` | ⬜ | — | — | — |

### Secciones del informe

| Sección | Estado | Archivos | Notas |
|---|---|---|---|
| Gestión de Riesgos | 🟡 redactada, con correcciones en ramas `fix/*` | `informe/riesgos/gestion-de-riesgos-amazon-leo.md` (+ `.docx`), `analisis_cuantitativo.py` | Adelantada a I-3. Redactada con asistencia de IA y revisada por un integrante. |
| Seguimiento y Valor Ganado | 🟡 guía y cálculo listos | `informe/guias/seguimiento-valor-ganado.md`, `informe/seguimiento/valor_ganado.py` | Falta redactar la sección. |
| Alcance y WBS | 🟡 guía con WBS propuesta | `informe/guias/alcance-wbs.md` | Falta decidir el alcance y redactar. |
| Cifras maestras (anexo D) | 🟡 | `informe/cifras-maestras.md` | Fuente única de números. |
| Resto (resumen, método, ubicación, caso de negocio, acta, tiempos, estimaciones, costos, integración, conclusiones) | ⬜ | plantillas en `informe/plantillas/` | Índice en `informe/00-estructura.md`. |

### Reparto sugerido (4 integrantes)

| Integrante | Secciones (ver `00-estructura.md`) |
|---|---|
| A | 2 Ubicación · 5 Caso de negocio · 6 Acta |
| B | 7 Alcance y WBS · 8 Tiempos · 9 Estimaciones |
| C | 10 Costos · 12 Seguimiento y Valor Ganado |
| D (autor/a de Riesgos) | 11 Riesgos (revisar ramas 2–5) · 13 Integración · cifras maestras y coherencia |
| Todos | 0 Resumen · 1 Método · 14 Conclusiones · declaración de IA |

**Cierre de la Instancia 1:** ⬜ informe revisado y aprobado por el equipo.

---

## Instancia 2 — Dashboard de defensa

> No arranca sin pedido explícito del equipo, aunque la Instancia 1 esté cerrada.

| # | Checkpoint | Comando | Estado | Fecha | Revisó | Archivos generados |
|---|---|---|---|---|---|---|
| D-1 | KPIs y modelo de datos | `/dashboard:kpis` | ⬜ | — | — | — |
| D-2 | Wireframe y jerarquía | `/dashboard:wireframe` | ⬜ | — | — | — |
| D-3 | Construcción del HTML | `/dashboard:build` | ⬜ | — | — | — |
| D-4 | Guion de defensa | `/dashboard:defensa` | ⬜ | — | — | — |

**Cierre de la Instancia 2:** ⬜ dashboard probado sin internet y PDF verificado.

---

## Ramas y cambios

Cada rama sale de la anterior (están **apiladas**), así que se mergean a `main` **en este orden**. Cada fila la agrega la propia rama.

| Orden | Rama | Tipo | Qué cambia | Estado |
|---|---|---|---|---|
| 1 | `fix/01-uso-ia-y-progreso` | Corrección urgente | Registra que la cátedra habilitó el uso de IA (CLAUDE.md §3, declaración de la sección de Riesgos, LEEME); actualiza este archivo al estado real; agrega la regla "una rama por cambio". | 🟡 PR pendiente |
| 2 | `fix/02-r01-riesgo-materializado` | Corrección urgente | R-01 ocurrió el 15/11/2026 (LV-01): se registra como **tema T-01** con el formulario de Resolución de Temas de la Clase 6 (nueva sección 7.1); R-01 pasa a medir la recurrencia y se justifica por qué queda en azul (el daño grave, cohete en tierra, está en R-02). Los valores P/I del equipo no se cambiaron. | 🟡 PR pendiente |
| 3 | `fix/03-r04-reformulacion` | Corrección urgente | R-04 tenía P = 0,70 de "no cumplir el hito de 2029", pero el Monte Carlo da ≈ 100%. Se reformula: no llegar por cadencia es **condición prevista**; el riesgo es que **la FCC no conceda un nuevo alivio** (P = 0,70 = ≈ 30% de alivio). Respuesta principal: pedido de extensión con evidencia. Se ajustan resumen, sección 3, sección 5, supuestos y criterio de cierre. ER sin cambios (0,28 → 0,20). | 🟡 PR pendiente |
| 4 | `fix/04-cifras-contratos-y-fuentes` | Corrección urgente | Registro de fuentes: aplica las correcciones de la verificación (#3, #5 no es un informe financiero, #6, #7, #8 con párrafos de la FCC), cierra 3 contradicciones resueltas y agrega 2 (fecha 20 vs 30/07/2029; New Glenn 12 vs 24), suma 2 vacíos, incorpora las fuentes **#21 a #47** (sección E) y agrega la tabla **"Cifras de contratos con fecha de corte"** (vigente: 108 lanzamientos; New Glenn = 24). Corrige el "12 New Glenn" de la verificación. | 🟡 PR pendiente |
| 5 | `fix/05-operativos-y-fecha-de-corte` | Corrección urgente | Riesgos §4.1 y §5: explicita que se usan satélites **lanzados** como aproximación de **operativos** (la FCC mide operativos) y que por eso los resultados son optimistas; agrega el supuesto a la tabla de §7. Propone una **fecha de corte única** (16/11/2026) en "Decisiones pendientes". Regenera el `.docx` de Riesgos con las ramas 1 a 5. | 🟡 PR pendiente |
| 6 | `feat/06-cifras-maestras` | Sugerencia (valor) | Nuevo `informe/cifras-maestras.md`: **fuente única de números** (C-01 a C-54) con etiqueta, fuente o cálculo y qué sección lo usa. Es el hilo conductor entre Riesgos, Tiempos, Costos, VG y el dashboard. Incluye la lista de datos no públicos que no se deben inventar. | 🟡 PR pendiente |
| 7 | `feat/07-promesas-inicio-servicio` | Sugerencia (valor) | `evidencia/hitos.md` §5: **línea de tiempo de las promesas de inicio del servicio** (2023 → 2026, ≈ 2 años de corrimiento) con previews parciales y una inferencia que conecta con R-03 (definir un criterio verificable de inicio). Lista para el informe y el dashboard. | 🟡 PR pendiente |
| 8 | `feat/08-valor-ganado-satelites` | Sugerencia (valor) | Guía `informe/guias/seguimiento-valor-ganado.md` + script `informe/seguimiento/valor_ganado.py` (genera `ev_serie.csv`). Valor ganado **en satélites** (BAC 3.232): SPI 0,25 (línea base FCC), 0,57 (plan de Amazon), 0,22 al corte; proyección de fin ≈ 2031 (plan) / ≈ 2038 (ritmo observado). CPI no calculable (AC no público). Valida la serie EV contra la declaración de Amazon a la FCC (180 al 30/01/2026). | 🟡 PR pendiente |
| 9 | `feat/09-kpis-sugeridos-dashboard` | Sugerencia (valor) | `dashboard/datos/kpis-sugeridos.md`: 16 KPIs **sugeridos** en 4 bloques (estado, atraso, riesgos, organización), cada uno con la pregunta de defensa que responde, valor al corte y visual. **No es D-1**: el equipo marca cuáles van y después se corre `/dashboard:kpis`. | 🟡 PR pendiente |
| 10 | `feat/10-edt-flujo-fisico` | Sugerencia (valor) | Guía `informe/guias/alcance-wbs.md` (Clase 2): decisión de alcance (Gen1 dentro; Gen2, Polar, D2D y Globalstar fuera, por rolling wave), **WBS propuesta en 3 niveles por flujo físico** (fabricar → procesar → lanzar → órbita → tierra → terminales → servicio) con evidencia por elemento, diccionario a completar, cuello de botella en lanzamientos y mapa riesgo ↔ elemento. Se usa "WBS", la denominación de la cátedra. | 🟡 PR pendiente |
| 11 | `feat/11-i3-estructura-informe` | Desarrollo (checkpoint I-3) | `informe/00-estructura.md`: índice de 15 secciones y 6 anexos (qué es dato, inferencia y propuesta en cada una; evidencia; plantilla; extensión; estado), **mapa de coherencia** y secciones con evidencia flaca. 7 plantillas nuevas con los campos de la cátedra (acta SAFIRO, caso de negocio PMOInformatica, alcance/WBS, cronograma con milestones e inch-pebbles, estimaciones PERT, costos con reservas, informe de situación/VG), todas **vacías** con "Cómo completarlo". | 🟡 PR pendiente · **requiere aprobar el índice** |

---

## Bitácora

| Fecha | Checkpoint | Qué pasó / qué decidió el equipo |
|---|---|---|
| 14/11/2026 | — | Inicialización del proyecto: `CLAUDE.md`, estructura de carpetas, registro de fuentes y comandos. |
| 15/11/2026 | I-1 | Primer barrido de fuentes (web). 20 fuentes catalogadas y evaluadas, 6 contradicciones y 7 vacíos registrados. Varias cifras dependen de documentos primarios FCC/SEC aún no leídos (marcados ⚠). Hallazgo fresco: la 1ª misión Vulcan dedicada falló el 15/11/2026 (40 satélites perdidos). |
| 16/11/2026 | I-1 / I-2 / Riesgos | PR #1 (`borrador-riesgos-i2`): verificación de I-1 contra FCC y SEC, borradores de hitos y actores, sección de Riesgos completa con Monte Carlo. |
| 16/11/2026 | Revisión general | Revisión del trabajo contra la consigna y los temas de la cátedra. Se detectaron 6 problemas urgentes (uso de IA, R-01 materializado, R-04 inconsistente con el Monte Carlo, cifras de contratos, lanzados vs operativos, fecha de corte) y faltantes del informe (caso de negocio, acta, EDT, cronograma, estimaciones, costos, valor ganado), del dashboard y de la defensa. |
| 16/11/2026 | Decisión | **La cátedra habilitó el uso de IA para la redacción** (confirmado por el equipo). Se actualiza `CLAUDE.md` §3. Se adopta "una rama por cambio" con PR como revisión. |
| 16/11/2026 | Correcciones (ramas 1–5) | Uso de IA registrado; R-01 materializado → tema T-01; R-04 reformulado sobre la decisión de la FCC; cifras de contratos unificadas (New Glenn = 24) y fuentes #21–#47 incorporadas; lanzados ≈ operativos explícito; fecha de corte propuesta; `.docx` de Riesgos regenerado. |
| 16/11/2026 | Sugerencias (ramas 6–10) | Cifras maestras; línea de tiempo de promesas de servicio; valor ganado en satélites (SPI 0,22–0,57; fin ≈ 2031–2038); KPIs sugeridos para el dashboard; guía de Alcance con WBS por flujo físico. |
| 16/11/2026 | I-3 (rama 11) | Índice del informe, mapa de coherencia y 7 plantillas. **Detenido para aprobación del índice** (regla de checkpoints). |

---

## Decisiones tomadas por el equipo

- **Marco teórico:** el de los apuntes de la cátedra → se cargan en `catedra/`. No asumir PMBOK/ISO por defecto.
- **Dashboard:** un único HTML local autónomo (funciona sin internet) con botón para generar PDF.
- **Uso de IA (16/11/2026):** habilitado por la cátedra para la redacción. Claude puede redactar borradores; el equipo revisa, aprueba y defiende las decisiones. Cada sección lleva declaración de uso de IA. No se inventan datos.
- **Flujo de trabajo (16/11/2026):** una rama por cambio, apiladas, integradas por PR en orden.
- **Los KPIs los elige el equipo.**

## Decisiones pendientes del equipo

- **Fecha de corte única del informe y del dashboard.** Propuesta: **16/11/2026** (la que ya usan las fuentes, hitos, actores y Riesgos). Todo hecho posterior (por ejemplo LE-04, Ariane 64 con 36 satélites, prevista para no antes del 23/11/2026) **no se mezcla**: o se deja afuera, o se mueve la fecha de corte de **todo** el trabajo y se actualizan juntas las cifras afectadas (satélites en órbita, cadencia, Monte Carlo, SPI). Sugerencia: congelar la fecha de corte una semana antes de la entrega y hacer una sola actualización.
- **Unidad de avance:** satélites lanzados como aproximación de operativos (Amazon no publica operativos). Ya está explicitado en Riesgos §4.1; debe usarse igual en Tiempos, Costos y Valor Ganado.

## Pendientes del equipo

- [x] Cargar el material de la cátedra en `catedra/` (14/11/2026).
- [x] Confirmar con la cátedra el uso de IA (confirmado 16/11/2026).
- [ ] Revisar y aprobar I-1 e I-2 (incluye aprobar las fuentes #21 a #47).
- [ ] Revisar y mergear las ramas de "Ramas y cambios" en orden.
- [ ] Dos PDF de la cátedra no tienen capa de texto: `Ejercicio Calidad …pdf` y `Laboratorio de Gestión de las Comunicaciones …pdf`. Hacen falta solo si el informe cubre calidad o comunicaciones.
- [ ] Definir los KPIs del dashboard (antes de D-1).
- [ ] Confirmar fecha de entrega y de defensa (no figuran en la consigna).
