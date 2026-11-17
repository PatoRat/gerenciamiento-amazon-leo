# Índice-guía del informe — Amazon Leo

Qué trata cada parte del informe, para ubicarse rápido (en la defensa o al revisar). El orden es el del documento compilado `Informe_Amazon_Leo.docx` / `.md`. Estado al 17/11/2026: todas las secciones 🟡 integradas, sin revisión de pares.

## Cuerpo del informe

| N.° | Sección | Archivo | De qué habla | Revisa (propuesta) |
|---|---|---|---|---|
| 0 | **Resumen ejecutivo** | `00-resumen-ejecutivo.md` | Síntesis de todo: qué es Amazon Leo, estado, hallazgos y conclusiones clave en una página. | Todos |
| 1 | **Introducción y método** | `01-introduccion-y-metodo.md` | Qué se investigó, cómo (los 5 pasos), reglas de trazabilidad, convenciones y limitaciones generales. | Todos |
| 2 | **Ubicación del proyecto** | `02-ubicacion-del-proyecto.md` | Qué problema/oportunidad aborda, quién lo impulsa, cómo llegó hasta acá y estado al 16/11/2026. | A |
| 3 | **Evidencia y fuentes** | `03-evidencia-y-fuentes.md` | Qué fuentes se usaron, cómo se evaluaron y qué no es público (y cómo se trató). | A |
| 4 | **Actores e interesados** | `04-actores-e-interesados.md` | Mapa de actores, matriz poder/interés y plan de comunicaciones básico (propuesta de gestión). | A |
| 5 | **Caso de negocio** | `05-caso-de-negocio.md` | Problema, visión, alineación estratégica, costo-beneficio, alternativas y actualización 2026. Reconstruido. | A |
| 6 | **Acta de constitución** | `06-acta-de-constitucion.md` | Acta reconstruida al 30/07/2020 + revisión con el checklist de la cátedra. | A |
| 7 | **Alcance y WBS** | `07-alcance-y-wbs.md` | Declaración de alcance, WBS (niveles 1–3), diccionario de paquetes críticos y cómo se conectan fabricación, lanzamientos y operación. | B |
| 8 | **Cronograma maestro** | `08-cronograma-maestro.md` | Milestones, inch-pebbles (cada misión = control), dependencias, Gantt por campaña, acortamiento/nivelación, línea base y de recuperación, reservas. | B |
| 9 | **Estimaciones (PERT)** | `09-estimaciones.md` + `estimaciones/pert_despliegue.py` | Método, estimación PERT de la duración restante, coherencia entre herramientas, ventana y sesgos. | B |
| 10 | **Costos y presupuesto** | `10-costos-y-presupuesto.md` | Montos públicos, estructura de costos por WBS, presupuesto y reservas, control de costos, índice de riesgo. | C |
| 11 | **Riesgos** | `riesgos/gestion-de-riesgos-amazon-leo.md` (resumen en `11-riesgos.md`) | Identificación, análisis cualitativo y cuantitativo (Monte Carlo), respuestas/reservas, seguimiento. R-01 materializado → tema T-01. | D |
| 12 | **Seguimiento y valor ganado** | `12-seguimiento-y-valor-ganado.md` + `seguimiento/valor_ganado.py` | Medición por output, resultados, proyección de fin, lo no calculable en costo y sistema de seguimiento propuesto. | C |
| 13 | **Integración y coherencia** | `13-integracion-y-coherencia.md` | La cadena que conecta todo, verificación de cifras únicas en todas las secciones, control de coherencia y elaboración progresiva. | D |
| 14 | **Conclusiones y limitaciones** | `14-conclusiones-y-limitaciones.md` | Conclusiones, limitaciones y qué haría el equipo con más información. | Todos |

## Anexos

| Anexo | De qué habla | Archivo |
|---|---|---|
| A | Fuentes (registro evaluado, 47) | `evidencia/registro-fuentes.md` |
| B | Hitos públicos | `evidencia/hitos.md` |
| C | Actores | `evidencia/actores.md` |
| D | Cifras maestras (fuente única de números) | `informe/cifras-maestras.md` |
| E | Código (PERT, valor ganado, Monte Carlo) | `estimaciones/`, `seguimiento/`, Apéndice R-B |
| F | Verificación | `evidencia/verificacion-i1-2026-11-16.md` |

## Cómo se agrupa para la defensa (4 bloques, ver `PROGRESO.md`)

- **Bloque 1 — ¿Qué es y por qué?** → 2 Ubicación · 3 Fuentes · 5 Caso de negocio
- **Bloque 2 — ¿Quién y cómo se organiza?** → 4 Actores · 6 Acta · 7 Alcance y WBS
- **Bloque 3 — ¿Atrasado? ¿Cuándo termina?** → 8 Cronograma · 9 Estimaciones · 12 Valor ganado
- **Bloque 4 — ¿Qué puede salir mal?** → 10 Costos · 11 Riesgos · 13 Integración
- **Todos** → 0 Resumen · 1 Método · 14 Conclusiones

## Material de apoyo (no va en el informe)

- `informe/plantillas/` — esqueletos de los documentos de gestión.
- `informe/guias/` — guía metodológica de Alcance/WBS, Riesgos y Valor ganado.
- `dashboard/` — tablero ejecutivo (`amazon-leo-dashboard.html`) y guion de defensa.
