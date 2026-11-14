---
description: "D-3 · Construye el dashboard HTML autónomo con botón PDF"
---

# Checkpoint D-3 — Construcción del tablero

Requiere **D-2 aprobado**. Insumos: `dashboard/wireframe.md`, `dashboard/datos/kpis.json`.

**Antes de escribir una línea de gráfico, cargá la skill `dataviz`.**

## Especificación técnica

- **Un único archivo**: `dashboard/amazon-leo-dashboard.html`.
- **Autónomo, sin red.** CSS y JS **inline**. Sin CDNs, sin Google Fonts, sin `fetch`, sin imágenes remotas. Debe abrirse con doble clic en una notebook sin internet y funcionar completo. Tipografías: stack del sistema. Gráficos: **SVG escrito a mano**, no librerías externas.
- **Datos embebidos** en el propio HTML (objeto JS al inicio del `<script>`, tomado de `kpis.json`), para que el archivo sea portable por sí solo.
- **Botón "Descargar PDF"**: `window.print()`, y hoja `@media print` que —
  - oculte el botón y cualquier control de interfaz;
  - fuerce colores legibles en papel (`print-color-adjust: exact` donde haga falta);
  - evite cortes dentro de un bloque (`break-inside: avoid`);
  - defina orientación y escala razonables (`@page`).
- **Responsive** hasta ancho de notebook; que no requiera scroll horizontal.
- **Trazabilidad visible**: cada KPI muestra su fecha de corte y una marca de origen (`[DATO REAL]` / reconstruido por el equipo). El pie del tablero remite al informe y al registro de fuentes.
- **Pendientes visibles**: todo KPI con `pendiente: true` se muestra con un marcador claro de dato faltante. **Nunca un número inventado, ni un placeholder que parezca real.**

## Reglas duras

- Los valores salen **exclusivamente** de `dashboard/datos/kpis.json`. Si falta un dato, se muestra como pendiente y se avisa al equipo.
- No agregues KPIs, bloques ni textos de análisis que no estén en el wireframe aprobado.
- Funcional, no decorativo: sin animaciones de relleno, sin bloques que no respondan una pregunta.

## Verificación antes de cerrar

1. Buscá en el archivo `http://`, `https://`, `cdn`, `fetch(` y `<link` externo: no debe haber ninguna dependencia de red.
2. Abrí el HTML en el navegador y confirmá que renderiza completo.
3. Probá el botón PDF y revisá el resultado: botón oculto, nada cortado, colores legibles.
4. Avisá al equipo que conviene probarlo **con el WiFi apagado**, en la notebook que se va a usar en la defensa.

## Al terminar

1. Informá: bloques construidos, KPIs pendientes que quedaron marcados y resultado de la verificación.
2. Actualizá `PROGRESO.md`: D-3 a `🟡 esperando revisión`.
3. **Detenete** y pedí revisión manual antes de D-4.
