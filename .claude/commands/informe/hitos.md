---
description: "I-2 · Cronología de hitos públicos y mapa de actores"
---

# Checkpoint I-2 — Hitos públicos y mapa de actores

Requiere **I-1 aprobado**. Si `evidencia/registro-fuentes.md` está vacío o I-1 no está aprobado en `PROGRESO.md`, avisá y pará.

Insumo: `evidencia/registro-fuentes.md`. Todo lo que escribas acá referencia una fila de ese registro por su `#`.

## Producto 1 — `evidencia/hitos.md`

Cronología de hitos **públicos y verificables**:

- Tabla ordenada por fecha: fecha · hito · eslabón (fabricación / lanzamiento / estación terrestre / regulación / comercial / financiamiento) · fuente `#` · etiqueta.
- Cada entrada es `[DATO REAL]`. Si una fecha es aproximada o anunciada pero no confirmada, decilo en la propia fila.
- Separá **hitos cumplidos** de **compromisos e hitos anunciados a futuro** (incluidos los plazos regulatorios): la diferencia entre ambos es material para el análisis de gestión.
- Marcá los **hitos que se corrieron** respecto de lo anunciado originalmente, con las dos fechas. Son la base del análisis de desvíos.

## Producto 2 — `evidencia/actores.md`

- **Mapa de actores**: organización · rol en el proyecto · eslabón · relación contractual conocida · fuente `#`. Incluí cliente/impulsor, fabricantes, proveedores de lanzamiento, operadores de estaciones terrestres, reguladores, socios comerciales y competidores relevantes.
- **Cadena fabricación → lanzamiento → estaciones terrestres → operación**: qué debe estar disponible antes de qué. Describí las dependencias e identificá qué eslabón condiciona el ritmo del despliegue.
- Las dependencias que no estén declaradas en una fuente van como `[INFERENCIA DEL GRUPO]`, con evidencia de base y **supuestos explícitos**.

## Reglas

- Tres etiquetas obligatorias (`CLAUDE.md` §4). Ningún párrafo sustantivo sin etiqueta.
- No mezcles anuncio con hecho consumado. Esa distinción es el corazón de la defensa.
- Cifras con fecha de corte.
- No escribas análisis de gestión ni conclusiones del informe: acá se ordena la evidencia.

## Al terminar

1. Informá: cantidad de hitos por eslabón, qué eslabón aparece como condicionante del ritmo, y las 3 dependencias que el equipo debería poder defender.
2. Actualizá `PROGRESO.md`: I-2 a `🟡 esperando revisión`.
3. **Detenete** y pedí revisión manual antes de I-3.
