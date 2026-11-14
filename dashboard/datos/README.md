# Datos del dashboard

**Los KPIs y sus valores los define y entrega el equipo.** Claude los estructura, construye el tablero y marca lo que falta; no inventa números ni usa datos de relleno.

## Cómo entregar los datos

Cualquiera de estas formas sirve; se normalizan en el checkpoint D-1 (`/dashboard:kpis`):

- Pegar los valores en el chat.
- Dejar un `.md`, `.csv` o `.xlsx` en esta carpeta.
- Completar la plantilla de abajo.

## Qué necesita cada KPI

| Campo | Por qué |
|---|---|
| **Nombre** | Cómo se llama en el tablero. |
| **Qué responde** | La pregunta de la defensa que este indicador contesta. Si no contesta ninguna, no va al tablero. |
| **Valor y unidad** | Con moneda o unidad explícita. |
| **Fecha de corte** | Las cifras del proyecto cambian en el tiempo. |
| **Origen** | `[DATO REAL]` (con `#` del registro de fuentes), `[INFERENCIA DEL GRUPO]` o `[PROPUESTA DE GESTIÓN]`. |
| **Meta o umbral** | Si aplica: contra qué se compara (verde / amarillo / rojo). |
| **Serie temporal** | Si se va a graficar evolución: los puntos de la serie. |

## Plantilla

```markdown
### KPI: <nombre>
- Qué responde: …
- Valor: … <unidad>
- Fecha de corte: dd/mm/aaaa
- Origen: [DATO REAL] fuente #__ / [INFERENCIA DEL GRUPO] / [PROPUESTA DE GESTIÓN]
- Meta o umbral: …
- Serie (opcional): aaaa-mm → valor; aaaa-mm → valor
```

## Archivos de este paso

- `kpis.md` — definición de cada KPI en prosa estructurada (lo legible para el equipo).
- `kpis.json` — los mismos datos en formato consumible por el HTML.
