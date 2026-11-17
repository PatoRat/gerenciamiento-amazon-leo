# Wireframe y jerarquía del dashboard (D-2)

Principio: **cada bloque responde una pregunta previsible de la defensa** (consigna: "debe servir para responder preguntas"; no son diapositivas). El orden sigue el razonamiento de la defensa: estado → atraso → riesgos → organización.

```
┌──────────────────────────────────────────────────────────────────────┐
│ Amazon Leo — Tablero ejecutivo   corte 16/11/2026   [Tema] [PDF]    │
│ nav: Estado · Atraso · Riesgos · Organización                        │
├──────────────────────────────────────────────────────────────────────┤
│ ⚠ Borrador: KPIs provisorios · cifras de cifras-maestras.md           │
├── 1 · ¿DÓNDE ESTÁ? ──────────────────────────────────────────────────┤
│ [396 desplegados] [24,5% del hito 50% ⛔] [15 misiones] [1.000 fabr.] │
│ ████░░░░░░░░░░░░|hito 50%░░░░░░░░░░░░░░░░░░░░░░░░░|hito final       │
├── 2 · ¿ESTÁ ATRASADO? ¿CUÁNDO TERMINA? ──────────────────────────────┤
│ Curva S (ancho completo): EV real · PV FCC · plan 2026 · recuperación │
│ ┌ SPI x3 ───────┐ ┌ Ritmo real/necesario ┐ ┌ Fin proyectado ┐        │
│ └───────────────┘ └──────────────────────┘ └─────────────────┘        │
│ ┌ Promesas de servicio ┐                                              │
├── 3 · ¿QUÉ PUEDE SALIR MAL? ─────────────────────────────────────────┤
│ ┌ Matriz P×I ┐ ┌ Exposición antes/después ┐ ┌ Monte Carlo ┐           │
│ ┌ Manifiesto por proveedor ┐ ┌ Temas abiertos (T-01) ┐                │
├── 4 · ¿CÓMO SE CONECTA? ─────────────────────────────────────────────┤
│ Fabricación → Procesamiento → [LANZAMIENTO] → Órbita → Tierra         │
│ Lo que el tablero no muestra: [[PENDIENTE]] CPI, costos, operativos   │
└──────────────────────────────────────────────────────────────────────┘
```

**Decisiones de diseño**
- Un solo eje en cada gráfico (sin ejes dobles). La curva S usa una sola escala en satélites.
- Color por función: azul = real; naranja = exigencia de la FCC; verde = propuesta; rojo = fallas e incumplimientos (siempre con texto o ícono, nunca solo color).
- Paleta categórica validada para daltonismo en modo claro y oscuro (skill `dataviz`); los colores con bajo contraste llevan etiquetas visibles y "Ver tabla".
- Cada gráfico tiene tooltip al pasar el mouse y una tabla desplegable con los datos.
- Impresión: A4 apaisado, sin botones ni tablas desplegables, siempre en tema claro.
- Sin internet: todo inline; los datos se embeben desde `datos/kpis.json` con `build_dashboard.py`.
