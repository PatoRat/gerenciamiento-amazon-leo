# Estructura del informe — Amazon Leo (I-3)

Índice del informe de investigación. **Estado: 🟡 todas las secciones tienen borrador** (16/11/2026); el estado por sección está en `PROGRESO.md`. Elaborado con asistencia de IA el 16/11/2026 a partir de la consigna (`Trabajo_Integrador_Direccion_Proyectos_2026.html`) y del material de `catedra/`.

**Lógica del índice:** sigue los cinco pasos de la consigna (ubicar → evidencia → reconstruir → conectar → defender) y, dentro de "reconstruir", el orden de la cátedra: selección (caso de negocio) → integración (acta) → alcance → tiempos → estimaciones → costos → riesgos → seguimiento y valor ganado (Paneo rápido, temas 2 a 10).

**Unidad de medida, fecha de corte y números:** todas las secciones usan `informe/cifras-maestras.md`, fecha de corte 16/11/2026 (a confirmar) y satélites lanzados ≈ operativos.

Extensión total orientativa: **35 a 50 páginas** más anexos.

---

## Índice

| N.° | Sección | Objetivo (una línea) | `[DATO REAL]` | `[INFERENCIA DEL GRUPO]` | `[PROPUESTA DE GESTIÓN]` | Evidencia principal | Documento / plantilla | Extensión | Estado |
|---|---|---|---|---|---|---|---|---|---|
| 0 | Resumen ejecutivo | Las 5 conclusiones que el equipo defiende | Cifras clave | Hallazgos | Recomendaciones | Cifras maestras | — | 1 pág. | ⬜ (al final) |
| 1 | Introducción y método | Qué se investigó, cómo y con qué reglas (trazabilidad, uso de IA, fecha de corte) | — | — | Criterios del equipo | Consigna; registro §taxonomía | — | 1–2 págs. | ⬜ |
| 2 | Ubicación del proyecto | Qué problema u oportunidad aborda, quién lo impulsa y en qué estado está (paso 1) | Historia 2019–2026, rebrand, estado al corte | Lectura del estado | — | #13, #21, #28, #39, #42, #2, hitos §1–4 | — | 3–4 págs. | ⬜ |
| 3 | Evidencia y fuentes | Qué se buscó, qué se encontró, qué no es público (paso 2) | Registro, contradicciones | Evaluación de confiabilidad | — | `evidencia/registro-fuentes.md` | Anexo A | 2 págs. + anexo | 🟡 registro listo |
| 4 | Actores e interesados | Quién participa y con qué rol e influencia | Actores con rol | Influencia / interés | Gestión de interesados | `evidencia/actores.md` | Anexo C | 2–3 págs. | 🟡 evidencia lista |
| 5 | Caso de negocio | Por qué Amazon hace Leo y contra qué alternativas | Inversiones declaradas, acuerdos, competencia | Problema, alineación estratégica | Análisis de alternativas; costo-beneficio cualitativo | #4, #5, #22, #23, #27, #31, #36, #45 | `plantillas/caso-de-negocio.md` | 3–4 págs. | ⬜ |
| 6 | Acta de constitución | Reconstruir el documento que habría autorizado el proyecto | Hitos FCC, sponsor visible | Objetivo SMART, supuestos | Acta completa | #8, #21, actores §1 | `plantillas/acta-constitucion.md` | 2–3 págs. | ⬜ |
| 7 | Alcance y WBS | Qué entra y qué no; cómo se conectan fabricación, lanzamientos y operación | Infraestructura, terminales, contratos | Cuello de botella | Declaración del alcance + WBS | hitos §3–4, actores §2–3 | `plantillas/declaracion-alcance-wbs.md`, guía `alcance-wbs.md` | 4–5 págs. | 🟡 guía lista |
| 8 | Tiempos: cronograma maestro | Hitos, dependencias y camino fabricación → lanzamiento → servicio | Fechas de misiones y de la FCC | Corrimientos, ritmo | Cronograma maestro (milestones + inch-pebbles) | hitos §1–2, §5 | `plantillas/cronograma-maestro.md` | 4–5 págs. | ⬜ |
| 9 | Estimaciones | Cuánto dura y con qué incertidumbre | Capacidades y cadencias declaradas | Ritmos observados | Estimación PERT/tres valores de la cadencia | #23, #25–27, cifras C-20 a C-26 | `plantillas/estimaciones.md` | 2–3 págs. | ⬜ |
| 10 | Costos y presupuesto | Estructura de costos y presupuesto reconstruido con supuestos | Inversiones públicas (KSC, Cabo Cañaveral, Globalstar) | Órdenes de magnitud | Presupuesto con reservas | #5, #22, #23, #27; cifras §7 | `plantillas/presupuesto-costos.md` | 3–4 págs. | ⬜ |
| 11 | Riesgos | Registro, análisis, respuestas y seguimiento | Fallas, órdenes FCC | Exposiciones, Monte Carlo | Respuestas y reservas | Riesgos (anexo B del informe) | `plantillas/registro-riesgos.md` | 6–8 págs. | ✅ redactada (correcciones en ramas 2–5) |
| 12 | Seguimiento y valor ganado | ¿Está atrasado, cuánto y cuándo termina? | Serie de misiones | SPI, proyecciones | Instrumentos de seguimiento | guía `seguimiento-valor-ganado.md`, `valor_ganado.py` | `plantillas/informe-situacion.md` | 3–4 págs. | 🟡 guía y cálculo listos |
| 13 | Integración y coherencia | Cómo se conectan las secciones (paso 4) | — | Cadena de causas | Mapa de coherencia | Esta estructura §"Mapa" | — | 1–2 págs. | ⬜ |
| 14 | Conclusiones y limitaciones | Qué se puede afirmar, qué no y por qué | — | Conclusiones | Recomendaciones | Todo | — | 2 págs. | ⬜ |
| — | Declaración de uso de IA | Qué hizo la herramienta y qué decidió el equipo | — | — | — | CLAUDE.md §3 | — | ½ pág. | ⬜ |

### Anexos

| Anexo | Contenido | Fuente en el repo | Estado |
|---|---|---|---|
| A | Registro de fuentes completo (#1 a #47, contradicciones, vacíos) | `evidencia/registro-fuentes.md` | 🟡 |
| B | Cronología de hitos y misiones | `evidencia/hitos.md` | 🟡 |
| C | Mapa de actores | `evidencia/actores.md` | 🟡 |
| D | Cifras maestras | `informe/cifras-maestras.md` | 🟡 |
| E | Código del Monte Carlo y del valor ganado | `informe/riesgos/analisis_cuantitativo.py`, `informe/seguimiento/valor_ganado.py` | 🟡 |
| F | Verificación contra fuentes primarias (FCC, SEC) | `evidencia/verificacion-i1-2026-11-16.md` | 🟡 |

### Fuera del índice (decisión del equipo)

- **Calidad y Comunicaciones:** la cátedra tiene material (dos PDF sin capa de texto). Si el equipo quiere incluirlos, hace falta transcribirlos. Sugerencia: una subsección de "plan de comunicaciones con interesados" dentro de la sección 4 alcanza para la defensa.

---

## Mapa de coherencia (paso 4: "Conectar")

Lo que debe coincidir entre secciones. Si una cambia, cambian las que tienen ✔ en su fila.

| Si cambia… | Acta | Alcance | Tiempos | Estim. | Costos | Riesgos | VG | Dashboard |
|---|---|---|---|---|---|---|---|---|
| Objetivo y alcance (Gen1 = 3.232; exclusiones) | ✔ | ✔ | ✔ | | ✔ | ✔ | ✔ (BAC) | ✔ |
| Hitos FCC (30/07/2026, 30/10/2027, 30/07/2029) | ✔ | | ✔ | | | ✔ (R-04, R-05) | ✔ (PV) | ✔ |
| Satélites en órbita al corte (396) | | | ✔ | ✔ | | ✔ | ✔ (EV) | ✔ |
| Cadencia (observada 21 sat/mes; necesaria 87) | | | ✔ | ✔ | | ✔ (§5) | ✔ (proyección) | ✔ |
| Contratos de lanzamiento (108; 66% Vulcan + New Glenn) | | ✔ (1.5) | ✔ | | ✔ | ✔ (R-02) | | ✔ |
| Reservas de tiempo (≈ 4 meses por R-02) | | | ✔ | | | ✔ | | |
| Reservas de costo / gerencial | | | | | ✔ | ✔ | | |
| Criterio de inicio del servicio | ✔ | ✔ (1.9.2) | ✔ | | | ✔ (R-03) | | ✔ |
| Unidad de avance (lanzados ≈ operativos) | | | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |

**Cadena causal que el informe entero debería contar** `[INFERENCIA DEL GRUPO]`: el lanzamiento es el cuello de botella (Alcance) → la cadencia real es un cuarto de la necesaria (Tiempos/Estimaciones) → el SPI es de 0,22 a 0,57 (VG) → no llegar a 3.232 en 2029 es casi seguro (Monte Carlo) → el riesgo principal pasa a ser regulatorio (R-04) → la respuesta es un pedido de alivio con evidencia y más capacidad de lanzamiento (OP-1), lo que tiene costo (Costos) y se justifica por el caso de negocio.

---

## Secciones con evidencia flaca (necesitan más I-1)

| Sección | Qué falta | Dónde buscar |
|---|---|---|
| 10 Costos | Inversión total; costo por satélite y por lanzamiento; monto de la fianza | 10-K / 10-Q de Amazon (SEC); contratos públicos de los lanzadores; prensa financiera con cita |
| 5 Caso de negocio | Proyecciones de ingresos y suscriptores; competencia (Starlink) con datos | Declaraciones a inversores de Amazon; FCC (competencia); prensa especializada |
| 7 Alcance (1.7) | Lista de gateways y su estado | Expedientes de licencias por país; FCC (earth stations) |
| 8 Tiempos | Fechas de misiones futuras de Atlas V, Falcon 9, New Glenn; retorno de Vulcan | #2 (página viva); ULA; Blue Origin |
| 4 Actores | Proveedores de componentes del satélite | No hay fuente primaria; dejar como límite |
