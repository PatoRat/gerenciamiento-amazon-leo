# Sección de Riesgos — borradores para revisión

**Estado: borradores sin revisar por el equipo.** Fueron preparados por un integrante con asistencia de IA (Claude) y revisados punto por punto por esa persona el 16/11/2026. Esta rama es para que el resto del equipo los revise antes de integrarlos a `main`.

## Versión para entregar

- `gestion-de-riesgos-amazon-leo.md` y `Gestion_de_Riesgos_Amazon_Leo.docx`: la sección de Riesgos en una sola versión limpia, lista para integrar al informe (el `.docx` es la misma versión en Word).
- `analisis_cuantitativo.py`: código de la simulación de la sección 5 (`python3 analisis_cuantitativo.py`).
- Los demás archivos de esta carpeta son el material de trabajo del que sale esa versión.

**Antes de entregar** hay que revisar que la declaración de uso de IA de la sección 1 sea cierta (dice que el docente habilitó su uso), integrar la sección al informe con el mismo formato del resto y conciliar las reservas con las áreas de costos y tiempos.

## Dónde está cada cosa

Dentro de los archivos hay referencias a nombres de archivo de la carpeta de trabajo original. En este repo están así:

| Nombre que aparece en el texto | Ubicación en el repo |
|---|---|
| `borrador-parte0.md` | `informe/riesgos/borrador-parte0.md` |
| `registro-riesgos.md` | `informe/riesgos/registro-riesgos.md` |
| `analisis-y-seguimiento.md` | `informe/riesgos/analisis-y-seguimiento.md` |
| `eventos-reales-candidatos.md` | `informe/riesgos/eventos-reales-candidatos.md` |
| `guia-riesgos.md` | `informe/guias/riesgos.md` |
| `plantilla-registro-riesgos.md` | `informe/plantillas/registro-riesgos.md` |
| `I-2-borrador/hitos.md` | `evidencia/hitos.md` |
| `I-2-borrador/actores.md` | `evidencia/actores.md` |
| `verificacion-i1-2026-11-16.md` | `evidencia/verificacion-i1-2026-11-16.md` |

## Qué conviene revisar primero

1. `evidencia/verificacion-i1-2026-11-16.md`: corrige la fila #5 del registro de fuentes (no es un informe financiero) y confirma las cifras de la FCC.
2. Las fuentes nuevas #21 a #46, propuestas al final de `evidencia/hitos.md`: el equipo tiene que aprobarlas antes de pasarlas a `evidencia/registro-fuentes.md`.
3. Las marcas `[[REVISAR]]` y `[[PENDIENTE]]` dentro de cada archivo.

## Lo que no se hizo a propósito

- No se actualizó `PROGRESO.md`: los checkpoints I-1 e I-2 siguen sin revisión manual del equipo.
- No se completaron datos que no son públicos (costo de un satélite, monto de la fianza, costo de las respuestas). Quedan como `[[PENDIENTE]]`.
