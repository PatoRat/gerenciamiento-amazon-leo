# Amazon Leo — Trabajo Integrador de Investigación · Dirección de Proyectos 2026

> **Al iniciar cualquier sesión:** leer `PROGRESO.md` para saber en qué checkpoint está el trabajo. No arrancar tareas de investigación o construcción sin que el equipo lo pida explícitamente.

---

## 1. Proyecto y rol del equipo

**Proyecto asignado:** Amazon Leo — constelación satelital.
Despliegue de una constelación de satélites y servicios de conectividad que requiere lanzamientos, fabricación, estaciones terrestres, proveedores, integración y operación a gran escala.

**Mirada del equipo:** planeamiento y gestión / gerenciamiento de proyectos. El trabajo consiste en **investigar el proyecto real, reconstruir cómo podría organizarse su gestión y sostener esas decisiones con evidencia**.

Consigna textual de la cátedra, que ordena todo lo demás:

> «La clave no es "contar de qué se trata el proyecto", sino demostrar que el equipo puede investigarlo, documentarlo, tomar decisiones y defenderlas.»

No se busca una descripción periodística ni una recopilación de noticias.

---

## 2. Qué pide la cátedra

**Dos productos entregables:**

| # | Producto | Qué es |
|---|---|---|
| 1 | **Informe de investigación** | Documento completo, con fuentes, documentación de gestión reconstruida, anexos y trazabilidad clara entre evidencia, inferencias y propuestas. |
| 2 | **Dashboard** | Tablero ejecutivo y funcional para la defensa oral. No reemplaza al informe ni debe convertirse en "diapositivas disfrazadas". Debe servir para **responder preguntas**. |

**Modalidad:** trabajo grupal. **Defensa:** oral, **sin diapositivas**.

**Los cinco pasos del proceso de investigación (según la consigna):**

1. **Ubicar el proyecto** — qué problema u oportunidad aborda, quién lo impulsa, cuál es su estado actual.
2. **Buscar evidencia** — priorizar fuentes oficiales, técnicas, institucionales y publicaciones confiables.
3. **Reconstruir** — completar lo que no sea público mediante inferencias razonables y propuestas justificadas.
4. **Conectar** — evitar documentos aislados: todo lo elaborado debe ser coherente entre sí.
5. **Defender** — poder explicar decisiones, supuestos, fuentes y relaciones entre variables del proyecto.

**Criterio de cierre:** el trabajo está completo cuando existe **coherencia entre lo investigado, lo reconstruido y lo que el equipo pueda defender oralmente**.

**Orientación inicial de la cátedra para este proyecto:** investigar cómo se organiza el despliegue, qué hitos públicos existen, qué infraestructura debe estar disponible y cómo se conectan fabricación, lanzamientos y operación.

---

## 3. Reparto de trabajo humano / IA — REGLA DURA

La consigna establece: **«No se aceptará presentar como real un documento creado por una herramienta de IA.»**

**Actualización 16/11/2026:** la cátedra **habilitó el uso de IA para la redacción** (confirmado por el equipo). Desde esa fecha:

- Claude **puede redactar borradores** de secciones del informe y de los documentos de gestión reconstruidos, a pedido del equipo.
- Todo borrador redactado con IA queda **marcado como borrador** hasta que un integrante lo revise y lo apruebe (vía Pull Request o anotación en `PROGRESO.md`).
- Cada sección del informe lleva una **declaración de uso de IA** (qué hizo la herramienta y qué decidió el equipo).
- Las **decisiones de gestión** (probabilidades, impactos, estrategias, prioridades, KPIs) las toma y defiende el equipo. Claude las propone marcadas como propuesta y explica el criterio.
- Siguen vigentes sin cambios: **no inventar datos**, trazabilidad obligatoria (§4) y marcadores `[[PENDIENTE]]`.

Lo que sigue en esta sección describe el reparto original; donde contradiga esta actualización, manda la actualización.

### Claude SÍ hace

- Buscar, verificar y **evaluar fuentes**; armar catálogos de evidencia.
- Construir **cronologías de hitos públicos** y mapas de actores, siempre con cita y fecha de consulta.
- Explicar y aplicar la **metodología y la teoría de la cátedra** (ver `catedra/`).
- Proponer **estructura, índices y esqueletos** del informe.
- Generar **plantillas vacías o con instrucciones** de los documentos de gestión a reconstruir (qué debe ir en cada campo, no el contenido final).
- **Revisar** lo que redacta el equipo: trazabilidad, coherencia entre documentos, huecos lógicos, supuestos no explicitados.
- Preparar **preguntas probables de defensa** y señalar qué no está respondido.
- **Construir el dashboard**: código, layout y estética.

### Claude NO hace

- **No redacta la prosa del informe** ni los documentos de gestión reconstruidos como si fueran producción del equipo. Ante un pedido de ese tipo: ofrecer plantilla + guía metodológica, y decirlo explícitamente.
- **No inventa** datos, cifras, fechas, nombres, contratos ni KPIs. Tampoco "ejemplos ilustrativos" que puedan confundirse con datos reales.
- **No completa** un dato sin fuente identificable ni etiqueta de trazabilidad.
- **No define** los KPIs ni el contenido del dashboard: eso lo entrega el equipo. Claude puede sugerir opciones **si se lo piden**, marcadas como sugerencia.

### Ante un dato faltante

Dejar un marcador explícito, nunca una estimación silenciosa:

```
[[PENDIENTE: cantidad de satélites operativos a la fecha — buscar en informe trimestral o presentación a inversores]]
```

---

## 4. Regla fundamental de trazabilidad

Cada dato, documento o decisión relevante debe poder identificarse según su origen. **Las tres etiquetas son obligatorias en todos los archivos de `evidencia/` e `informe/`. Ningún párrafo sustantivo queda sin etiqueta.**

| Etiqueta | Qué es | Qué debe acompañarla |
|---|---|---|
| `[DATO REAL]` | Información encontrada en una fuente verificable. | Fuente + URL + fecha de publicación + fecha de consulta. |
| `[INFERENCIA DEL GRUPO]` | Conclusión razonable a partir de la evidencia disponible. | Evidencia de base (referencia al registro de fuentes) + **supuestos explícitos**. |
| `[PROPUESTA DE GESTIÓN]` | Documento, estimación, decisión o respuesta creada por el equipo para reconstruir cómo debería gestionarse el proyecto. | Justificación + criterio o teoría aplicada. |

Formato sugerido en los archivos:

```markdown
**[DATO REAL]** Amazon obtuvo la autorización de la FCC para operar X satélites.
→ Fuente: FCC, *Order and Authorization* DA-XX-XXXX — https://… (publicado dd/mm/aaaa, consultado dd/mm/aaaa)

**[INFERENCIA DEL GRUPO]** Esto implica una ventana de cumplimiento regulatorio que condiciona el cronograma de lanzamientos.
→ Base: fuentes #4 y #7 del registro. Supuestos: (a) no hay prórroga concedida; (b) la cadencia de lanzamientos informada se mantiene.

**[PROPUESTA DE GESTIÓN]** Hito de control trimestral de cumplimiento regulatorio en el cronograma maestro.
→ Justificación: … (según el enfoque de la cátedra para gestión de restricciones externas)
```

Regla de oro: **si no se puede decir de dónde salió, no entra al informe.**

---

## 5. Marco teórico

El marco metodológico es **el de la cátedra**, no un estándar genérico.

- Antes de aplicar cualquier teoría, **leer el material disponible en `catedra/`**.
- Si `catedra/` está vacío o no cubre el tema que se necesita: **preguntar al equipo** en lugar de asumir PMBOK, ISO 21500/21502, PRINCE2 u otro marco.
- Si se usa una referencia externa como complemento, decirlo explícitamente y marcarla como externa al material de la cátedra.
- Al citar, referenciar **archivo + clase/unidad** (ej.: `catedra/Clase 3 Gestión de los Tiempos · UCA.html`), y usar la **denominación de la cátedra** para cada documento, no la del estándar internacional.

### Inventario de `catedra/` (cargado 14/11/2026)

| Tema | Archivo |
|---|---|
| Encuadre de la materia · gerenciamiento y evaluación | `Clase 1 Gerenciamiento_Evaluacion_Proyectos_UCA_2026.html`, `Clase 1 Evaluación de Proyectos.html`, `Paneo_rapido_Gerenciamiento.pdf` |
| Alcance | `Clase 2 Alcance.html`, `Ejemplo Proceso de Alcance.html` |
| Tiempos / cronograma | `Clase 3 Gestión de los Tiempos · UCA.html` |
| Estimaciones | `Clase 4 Estimaciones 1ra. Parte …html`, `Clase 4 Estimaciones · Segunda Parte …html` |
| Costos | `Clase 5 · Gestión de Costos de Proyectos.html` |
| Riesgos | `Clase 5 · Gestión de Riesgos …html` |
| Seguimiento y valor ganado | `Clase 6 Seguimiento y Valor Ganado …html`, `Valor Agregado.html`, `Desafío Valor Ganado_Ratcliffe.pdf` |
| Calidad | `Ejercicio Calidad. Ratcliffe, Arrizurieta, Sabor, D'Imperio.pdf` |
| Comunicaciones | `Laboratorio de Gestión de las Comunicaciones. Ratcliffe …pdf` |
| Acta del proyecto (plantillas y casos) | `Proyectos_02 Ejercicio 02 Acta del Proyecto_0100.pdf`, `Caso_DOWN_Proyecto_SAFIRO_Acta_Interactiva_con_descarga.html` |
| Caso de negocio | `PMOInformatica Plantilla Caso de Negocio.pdf` |
| Prácticas | `Práctica.pdf` |

**Cómo leer este material:**

- **HTML**: son páginas con el contenido en el cuerpo; extraer el texto quitando `<script>` y `<style>` (todo el texto es recuperable). Varias tienen imágenes embebidas en base64 que no se pueden ver sin extraerlas: si el contenido clave está en una imagen, pedírselo al equipo.
- **PDF**: usar `pdftotext` (disponible en el entorno). `pdftoppm` **no** está instalado, así que las páginas no se pueden renderizar para leerlas como imagen.
- **Sin capa de texto** (no legibles hoy, requieren OCR o transcripción del equipo): `Ejercicio Calidad …pdf` y `Laboratorio de Gestión de las Comunicaciones …pdf`. Si se necesita calidad o comunicaciones, **pedirle al equipo el contenido** en lugar de suponerlo.

---

## 6. Workflow: dos instancias con checkpoints

**Reglas de ejecución, no negociables:**

1. Las dos instancias son **corridas separadas**. La Instancia 2 (dashboard) **no arranca** sin pedido explícito del equipo, aunque la Instancia 1 esté terminada.
2. Al terminar cada checkpoint: **detenerse, informar qué se produjo y esperar revisión manual de un miembro del equipo.** No encadenar checkpoints en una misma corrida.
3. Al cerrar un checkpoint, **actualizar `PROGRESO.md`** (estado, fecha, archivos generados).
4. Si el equipo pide avanzar varios pasos de una vez: hacer solo el primero y recordar la regla.
5. **Una rama por cambio.** Cada cambio va en su propia rama (`fix/NN-…` para correcciones, `feat/NN-…` para agregados), apilada sobre la anterior, y se integra a `main` por Pull Request, en orden. El PR es la instancia de revisión manual. Cada rama registra lo que hizo en la sección "Ramas y cambios" de `PROGRESO.md`.

### Instancia 1 — Informe

| Checkpoint | Comando | Qué produce |
|---|---|---|
| **I-1** Mapeo de fuentes | `/informe:fuentes` | `evidencia/registro-fuentes.md` |
| **I-2** Hitos y actores | `/informe:hitos` | `evidencia/hitos.md`, `evidencia/actores.md` |
| **I-3** Estructura y plantillas | `/informe:estructura` | `informe/00-estructura.md`, `informe/plantillas/*.md` |
| **I-4** Guía metodológica por sección | `/informe:guia <sección>` | `informe/guias/<sección>.md` |
| **I-5** Revisión de lo redactado | `/informe:revisar` | observaciones + `informe/revisiones/*.md` |

→ **Revisión manual final del informe antes de cerrar la Instancia 1.**

### Instancia 2 — Dashboard

| Checkpoint | Comando | Qué produce |
|---|---|---|
| **D-1** KPIs y modelo de datos | `/dashboard:kpis` | `dashboard/datos/kpis.md`, `dashboard/datos/kpis.json` |
| **D-2** Wireframe y jerarquía | `/dashboard:wireframe` | `dashboard/wireframe.md` |
| **D-3** Construcción del tablero | `/dashboard:build` | `dashboard/amazon-leo-dashboard.html` |
| **D-4** Guion de defensa | `/dashboard:defensa` | `dashboard/guion-defensa.md` |

→ **Revisión manual final del dashboard antes de cerrar la Instancia 2.**

---

## 7. Estructura del repositorio

```
.
├── CLAUDE.md                  ← este archivo
├── PROGRESO.md                ← estado de los checkpoints (leer al iniciar sesión)
├── Trabajo_Integrador_Direccion_Proyectos_2026.html   ← consigna original de la cátedra
├── catedra/                   ← apuntes, PPTs, normas y material de la materia
├── evidencia/                 ← fuentes, hitos, actores (insumos verificables)
│   └── registro-fuentes.md
├── informe/                   ← acá redacta el equipo
│   ├── plantillas/            ← esqueletos de documentos de gestión (Claude)
│   ├── guias/                 ← guías metodológicas por sección (Claude)
│   └── revisiones/            ← observaciones de revisión (Claude)
└── dashboard/
    ├── datos/                 ← KPIs y valores que entrega el equipo
    └── amazon-leo-dashboard.html
```

### Convenciones

- **Idioma:** español rioplatense (es-AR). Registro técnico-profesional.
- **Archivos:** `kebab-case.md`, sin tildes ni espacios en los nombres.
- **Citas:** siempre URL + fecha de publicación + **fecha de consulta**.
- **Unidades y monedas:** explícitas (USD, EUR, km, kg, Gbps, satélites/lanzamiento). Nunca "millones" sin moneda.
- **Fechas:** formato `dd/mm/aaaa`; en los nombres de archivo, `aaaa-mm-dd`.
- **Nombres propios:** respetar la denominación de la fuente (Amazon Leo / Project Kuiper según corresponda y según la fecha) y aclarar el cambio de marca cuando sea relevante.

---

## 8. Dashboard — especificación técnica

- **Un único archivo HTML autónomo**: `dashboard/amazon-leo-dashboard.html`.
- **Sin dependencias de red.** CSS y JS **inline**; sin CDNs, sin Google Fonts, sin fetch externo. Debe abrirse y funcionar completo en una notebook sin internet en el aula.
- **Botón "Descargar PDF"**: `window.print()` + hoja `@media print` (colores legibles, sin cortes de bloques, el botón oculto en la impresión, orientación y escala pensadas para el PDF).
- **Datos embebidos** en el propio HTML, tomados de `dashboard/datos/`.
- **Contenido y KPIs: los define el equipo.** Claude no inventa valores ni usa datos de relleno; si falta un número, el tablero muestra un marcador visible de pendiente.
- **Funcional, no decorativo:** cada bloque existe para responder una pregunta previsible de la defensa. No es una presentación.
- Antes de escribir cualquier gráfico, cargar la skill **`dataviz`**.

---

## 9. Comandos disponibles

| Comando | Para qué |
|---|---|
| `/estado` | Dónde está el trabajo y cuál es el paso siguiente. |
| `/informe:fuentes` | I-1 · catálogo de fuentes evaluadas. |
| `/informe:hitos` | I-2 · cronología de hitos públicos y mapa de actores. |
| `/informe:estructura` | I-3 · índice del informe y plantillas de documentos de gestión. |
| `/informe:guia <sección>` | I-4 · guía metodológica de una sección. |
| `/informe:revisar` | I-5 · revisión de trazabilidad y coherencia de lo redactado. |
| `/dashboard:kpis` | D-1 · estructurar los KPIs que entrega el equipo. |
| `/dashboard:wireframe` | D-2 · layout y jerarquía del tablero. |
| `/dashboard:build` | D-3 · construir el HTML autónomo con botón PDF. |
| `/dashboard:defensa` | D-4 · preguntas probables y cobertura del tablero. |

---

## 10. Cierre de turno

Todo turno que haya modificado archivos o corrido comandos termina con un resumen breve:

- **Archivos cambiados**: ruta + qué cambió y por qué.
- **Comandos corridos**: cada uno con su resultado.
- **Pendiente / necesita al equipo**: pasos salteados, fallas, decisiones que debe tomar una persona.

Y, si se cerró un checkpoint: indicar que corresponde **revisión manual** antes de seguir.
