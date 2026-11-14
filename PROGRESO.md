# Estado del trabajo — Amazon Leo

Punto de entrada de cada sesión. Las dos instancias son corridas separadas y **cada checkpoint cierra con revisión manual** de un miembro del equipo.

Estados: `⬜ pendiente` · `🔄 en curso` · `🟡 esperando revisión` · `✅ aprobado`

**Checkpoint actual: I-1 — Mapeo de fuentes** (siguiente comando: `/informe:fuentes`)

---

## Instancia 1 — Informe de investigación

| # | Checkpoint | Comando | Estado | Fecha | Revisó | Archivos generados |
|---|---|---|---|---|---|---|
| I-1 | Mapeo y evaluación de fuentes | `/informe:fuentes` | ⬜ | — | — | — |
| I-2 | Hitos públicos y mapa de actores | `/informe:hitos` | ⬜ | — | — | — |
| I-3 | Estructura del informe y plantillas | `/informe:estructura` | ⬜ | — | — | — |
| I-4 | Guías metodológicas por sección | `/informe:guia <sección>` | ⬜ | — | — | — |
| I-5 | Revisión de trazabilidad y coherencia | `/informe:revisar` | ⬜ | — | — | — |

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

## Bitácora

| Fecha | Checkpoint | Qué pasó / qué decidió el equipo |
|---|---|---|
| 14/11/2026 | — | Inicialización del proyecto: `CLAUDE.md`, estructura de carpetas, registro de fuentes y comandos. |

---

## Decisiones tomadas por el equipo

- **Marco teórico:** el de los apuntes de la cátedra → se cargan en `catedra/`. No asumir PMBOK/ISO por defecto.
- **Dashboard:** un único HTML local autónomo (funciona sin internet) con botón para generar PDF.
- **Reparto de trabajo:** el equipo redacta el informe; Claude aporta fuentes, metodología, plantillas, revisión y el código del dashboard. Los KPIs los elige el equipo.

## Pendientes del equipo

- [x] Cargar el material de la cátedra en `catedra/` (cargado el 14/11/2026: clases 1 a 6 — alcance, tiempos, estimaciones, costos, riesgos, seguimiento y valor ganado — más prácticas, acta del proyecto y plantilla de caso de negocio).
- [ ] Dos PDF de la cátedra no tienen capa de texto y hoy no se pueden leer: `Ejercicio Calidad …pdf` y `Laboratorio de Gestión de las Comunicaciones …pdf`. Hacen falta solo si el informe cubre calidad o comunicaciones.
- [ ] Definir los KPIs del dashboard (antes de D-1).
- [ ] Confirmar fecha de entrega y de defensa (no figuran en la consigna).
