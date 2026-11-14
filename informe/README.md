# Informe de investigación

**Esta carpeta la escribe el equipo.** La cátedra no acepta presentar como real un documento creado por una herramienta de IA.

Lo que aporta Claude:

| Subcarpeta | Contenido | Quién lo escribe |
|---|---|---|
| `plantillas/` | Esqueletos de los documentos de gestión a reconstruir: qué va en cada campo, con qué criterio, qué evidencia lo sostiene. | Claude (`/informe:estructura`) |
| `guias/` | Guía metodológica por sección: teoría aplicable, evidencia disponible, decisiones a justificar, preguntas de defensa previsibles. | Claude (`/informe:guia <sección>`) |
| `revisiones/` | Observaciones sobre lo redactado: trazabilidad, coherencia, huecos. No reescritura. | Claude (`/informe:revisar`) |
| raíz de `informe/` | **El informe.** Redacción, documentos de gestión reconstruidos, anexos. | El equipo |

## Reglas de redacción

1. **Trazabilidad en todo párrafo sustantivo:** `[DATO REAL]`, `[INFERENCIA DEL GRUPO]` o `[PROPUESTA DE GESTIÓN]`, con lo que exige cada etiqueta (ver `CLAUDE.md` §4).
2. Todo `[DATO REAL]` referencia una fila de `evidencia/registro-fuentes.md` por su `#`.
3. Toda `[INFERENCIA DEL GRUPO]` explicita sus **supuestos**. Un supuesto no declarado es lo primero que cae en la defensa oral.
4. **Coherencia entre documentos** (paso 4 de la consigna): si el cronograma cambia, cambian los riesgos, los costos y el plan de recursos. Nada aislado.
5. Si un dato falta, queda el marcador `[[PENDIENTE: …]]` en lugar de una estimación silenciosa.

## Sugerencia de nomenclatura

`00-estructura.md`, `01-<sección>.md`, `02-<sección>.md`, … y `anexo-<nombre>.md`. El índice definitivo se fija en el checkpoint I-3.
