# Estado del trabajo — Amazon Leo

Punto de entrada de cada sesión. Las dos instancias son corridas separadas y **cada checkpoint cierra con revisión manual** de un miembro del equipo. Desde el 16/11/2026, **cada cambio va en su propia rama** y se revisa por Pull Request (ver "Ramas y cambios").

Estados: `⬜ pendiente` · `🔄 en curso` · `🟡 esperando revisión` · `✅ aprobado`

**Checkpoint actual:** I-1 e I-2 🟡 esperando revisión manual. La sección de Riesgos está redactada por adelantado (antes de I-3). Siguiente: aprobar I-1/I-2, mergear las ramas `fix/*` en orden y revisar I-3.

---

## Instancia 1 — Informe de investigación

| # | Checkpoint | Comando | Estado | Fecha | Revisó | Archivos generados |
|---|---|---|---|---|---|---|
| I-1 | Mapeo y evaluación de fuentes | `/informe:fuentes` | 🟡 | 15/11/2026 · verificado 16/11/2026 | — | `evidencia/registro-fuentes.md` (20 fuentes), `evidencia/verificacion-i1-2026-11-16.md` (confirma #7, #8 y #11 contra el primario; corrige #5) |
| I-2 | Hitos públicos y mapa de actores | `/informe:hitos` | 🟡 borrador | 16/11/2026 | — | `evidencia/hitos.md`, `evidencia/actores.md` (proponen fuentes #21 a #47) |
| I-3 | Estructura del informe y plantillas | `/informe:estructura` | ⬜ | — | — | — |
| I-4 | Guías metodológicas por sección | `/informe:guia <sección>` | 🔄 parcial | 16/11/2026 | — | `informe/guias/riesgos.md` |
| I-5 | Revisión de trazabilidad y coherencia | `/informe:revisar` | ⬜ | — | — | — |

### Secciones del informe

| Sección | Estado | Archivos | Notas |
|---|---|---|---|
| Gestión de Riesgos | 🟡 redactada, con correcciones en ramas `fix/*` | `informe/riesgos/gestion-de-riesgos-amazon-leo.md` (+ `.docx`), `analisis_cuantitativo.py` | Adelantada a I-3. Redactada con asistencia de IA y revisada por un integrante. |
| Resto (ubicación, caso de negocio, acta, alcance, tiempos, estimaciones, costos, seguimiento/VG, anexos) | ⬜ | — | Se ordena en I-3. |

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

---

## Bitácora

| Fecha | Checkpoint | Qué pasó / qué decidió el equipo |
|---|---|---|
| 14/11/2026 | — | Inicialización del proyecto: `CLAUDE.md`, estructura de carpetas, registro de fuentes y comandos. |
| 15/11/2026 | I-1 | Primer barrido de fuentes (web). 20 fuentes catalogadas y evaluadas, 6 contradicciones y 7 vacíos registrados. Varias cifras dependen de documentos primarios FCC/SEC aún no leídos (marcados ⚠). Hallazgo fresco: la 1ª misión Vulcan dedicada falló el 15/11/2026 (40 satélites perdidos). |
| 16/11/2026 | I-1 / I-2 / Riesgos | PR #1 (`borrador-riesgos-i2`): verificación de I-1 contra FCC y SEC, borradores de hitos y actores, sección de Riesgos completa con Monte Carlo. |
| 16/11/2026 | Revisión general | Revisión del trabajo contra la consigna y los temas de la cátedra. Se detectaron 6 problemas urgentes (uso de IA, R-01 materializado, R-04 inconsistente con el Monte Carlo, cifras de contratos, lanzados vs operativos, fecha de corte) y faltantes del informe (caso de negocio, acta, EDT, cronograma, estimaciones, costos, valor ganado), del dashboard y de la defensa. |
| 16/11/2026 | Decisión | **La cátedra habilitó el uso de IA para la redacción** (confirmado por el equipo). Se actualiza `CLAUDE.md` §3. Se adopta "una rama por cambio" con PR como revisión. |

---

## Decisiones tomadas por el equipo

- **Marco teórico:** el de los apuntes de la cátedra → se cargan en `catedra/`. No asumir PMBOK/ISO por defecto.
- **Dashboard:** un único HTML local autónomo (funciona sin internet) con botón para generar PDF.
- **Uso de IA (16/11/2026):** habilitado por la cátedra para la redacción. Claude puede redactar borradores; el equipo revisa, aprueba y defiende las decisiones. Cada sección lleva declaración de uso de IA. No se inventan datos.
- **Flujo de trabajo (16/11/2026):** una rama por cambio, apiladas, integradas por PR en orden.
- **Los KPIs los elige el equipo.**

## Pendientes del equipo

- [x] Cargar el material de la cátedra en `catedra/` (14/11/2026).
- [x] Confirmar con la cátedra el uso de IA (confirmado 16/11/2026).
- [ ] Revisar y aprobar I-1 e I-2 (incluye aprobar las fuentes #21 a #47).
- [ ] Revisar y mergear las ramas de "Ramas y cambios" en orden.
- [ ] Dos PDF de la cátedra no tienen capa de texto: `Ejercicio Calidad …pdf` y `Laboratorio de Gestión de las Comunicaciones …pdf`. Hacen falta solo si el informe cubre calidad o comunicaciones.
- [ ] Definir los KPIs del dashboard (antes de D-1).
- [ ] Confirmar fecha de entrega y de defensa (no figuran en la consigna).
