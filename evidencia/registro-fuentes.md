# Registro de fuentes — Amazon Leo

Catálogo único de evidencia del trabajo. **Todo `[DATO REAL]` del informe debe referenciar una fila de esta tabla por su `#`.**

Se completa en el checkpoint **I-1** (`/informe:fuentes`) y se amplía en los pasos siguientes.

---

## Taxonomía de fuentes

| Tipo | Qué incluye | Prioridad |
|---|---|---|
| **Oficial de la organización** | Comunicados, blog corporativo, informes anuales y trimestrales, presentaciones a inversores, prensa de la propia empresa. | Alta |
| **Regulatoria / institucional** | Presentaciones y autorizaciones ante organismos (FCC, ITU, ENACOM y equivalentes), licencias, expedientes públicos, organismos espaciales. | Alta |
| **Técnica** | Papers, especificaciones, documentación de proveedores de lanzamiento y fabricación, normas. | Alta |
| **Prensa especializada** | Medios del sector espacial y de telecomunicaciones con cobertura técnica. | Media |
| **Prensa general** | Medios masivos. Sirven para ubicar un hecho, no como única fuente de un dato duro. | Baja |

**Reglas de uso (paso 2 de la consigna: "priorizar fuentes oficiales, técnicas, institucionales y publicaciones confiables"):**

1. Un dato relevante sostenido **solo** por prensa general se marca como tal y se intenta confirmar con una fuente de prioridad alta.
2. Cifras que cambian en el tiempo (satélites lanzados, lanzamientos contratados, cobertura) llevan **fecha de corte** explícita.
3. Si dos fuentes se contradicen, se registran **ambas** y la discrepancia se trata como hallazgo, no se promedia.
4. Guardar la fecha de consulta: las páginas corporativas cambian sin aviso.

---

## Tabla de fuentes

> **Nota sobre este primer barrido (I-1):** catálogo inicial para que el equipo arranque, con fecha de consulta 15/11/2026. Varias cifras provienen de **fuentes secundarias** (prensa) que citan documentos primarios (FCC, SEC, comunicados de Amazon): están marcadas con ⚠ y **deben verificarse contra el documento primario** antes de usarse como `[DATO REAL]` en el informe. Las columnas "Publicado" con `≈` son fechas aproximadas a confirmar.

### A. Oficiales de la organización (Amazon / proveedores)

| # | Fuente (organización, título) | Tipo | URL | Publicado | Consultado | Confiabilidad | Qué dato aporta | Etiqueta |
|---|---|---|---|---|---|---|---|---|
| 1 | Amazon — "Amazon Leo successfully launches first heavy-lift mission of 2026 with Arianespace" | Oficial | https://www.aboutamazon.com/news/amazon-leo/amazon-leo-arianespace-first-mission-satellites | ≈feb 2026 | 15/11/2026 | Alta | Primera misión pesada 2026 con Arianespace (Ariane 6); satélites desplegados por misión. | [DATO REAL] |
| 2 | Amazon — "Amazon Leo mission updates: Launch dates set for next missions on Vulcan and Ariane 6" | Oficial | https://www.aboutamazon.com/news/innovation-at-amazon/project-kuiper-satellite-rocket-launch-progress-updates | actualizada (rolling) | 15/11/2026 | Alta (pero cambia sin aviso) | Calendario oficial de próximas misiones; totales de satélites; hito "1.000ª unidad". Página viva: guardar captura con fecha. | [DATO REAL] |
| 3 | Amazon — "Amazon Leo to launch 40 satellites on its first Vulcan mission" | Oficial | https://www.aboutamazon.com/news/amazon-leo/amazon-leo-vulcan-satellites-launch | ≈nov 2026 | 15/11/2026 | Alta | 40 satélites en la 1ª misión Vulcan dedicada; 1.000ª unidad completada a inicios de septiembre (según esta nota). | [DATO REAL] |
| 4 | Amazon — "Amazon makes historic launch investment to advance Project Kuiper" | Oficial | https://www.aboutamazon.com/news/innovation-at-amazon/amazon-makes-historic-launch-investment-to-advance-project-kuiper | 05/04/2022 | 15/11/2026 | Alta | Compra de lanzamientos 2022: 38 Vulcan + 18 Ariane 6 + 12 New Glenn (+15 opcionales) = hasta 83. | [DATO REAL] |
| 5 | SEC EDGAR — Amazon.com Inc, Form 425 FY2026 | Regulatoria/financiera (primaria) | https://www.sec.gov/Archives/edgar/data/1018724/000110465926042891/tm2611746d2_ex99-1.htm | FY2026 | 15/11/2026 | Alta | Documento financiero oficial de Amazon; verificar qué dice sobre Leo/inversión. ⚠ sin leer en detalle aún. | [DATO REAL] |

### B. Regulatorias e institucionales

| # | Fuente (organización, título) | Tipo | URL | Publicado | Consultado | Confiabilidad | Qué dato aporta | Etiqueta |
|---|---|---|---|---|---|---|---|---|
| 6 | FCC — Orden/autorización original Project Kuiper (3.236 satélites) | Regulatoria (primaria) | [[PENDIENTE: localizar en fcc.gov/ECFS, expediente Kuiper]] | 2020 | 15/11/2026 | Alta | Autorización original de 3.236 satélites. ⚠ cifra vía prensa; falta el doc FCC. | [DATO REAL] |
| 7 | FCC — Orden DA 24-224 (reducción a 3.232 satélites) | Regulatoria (primaria) | [[PENDIENTE: localizar DA 24-224 en fcc.gov]] | 08/03/2024 | 15/11/2026 | Alta | Reduce la constelación autorizada a 3.232. ⚠ vía prensa, confirmar. | [DATO REAL] |
| 8 | FCC — Orden DA 26-553 (waiver del hito del 50%) | Regulatoria (primaria) | [[PENDIENTE: localizar DA 26-553 en fcc.gov]] | 05/06/2026 | 15/11/2026 | Alta | Waiver limitado del hito de desplegar 50% al 30/07/2026; penalidad de prioridad de espectro Ka/Ku; deadline final 30/07/2029 sin cambios. ⚠ vía prensa, confirmar número de orden y términos. | [DATO REAL] |

### C. Técnicas y de proveedores de lanzamiento

| # | Fuente (organización, título) | Tipo | URL | Publicado | Consultado | Confiabilidad | Qué dato aporta | Etiqueta |
|---|---|---|---|---|---|---|---|---|
| 9 | SpaceNews — "Amazon Secures Up to 83 Launches from Arianespace, Blue Origin, and United Launch Alliance for Project Kuiper" | Técnica/prensa especializada | https://spacenews.com/amazon-secures-up-to-83-launches-from-arianespace-blue-origin-and-united-launch-alliance-for-project-kuiper/ | 05/04/2022 | 15/11/2026 | Alta | Detalle de los contratos de lanzamiento 2022. | [DATO REAL] |
| 10 | SpaceNews — "Amazon adds Falcon 9 to multi-billion-dollar Project Kuiper launch campaign" | Técnica/prensa especializada | https://spacenews.com/amazon-adds-falcon-9-to-multi-billion-dollar-project-kuiper-launch-campaign/ | 2023 | 15/11/2026 | Alta | Incorporación de SpaceX Falcon 9 (3 misiones) al plan de lanzamiento. | [DATO REAL] |
| 11 | Spaceflight Now — "ULA suffers first total mission failure with loss of Vulcan rocket carrying 40 Amazon Leo satellites" | Técnica/prensa especializada | https://spaceflightnow.com/2026/11/15/ula-suffers-first-total-mission-failure-with-loss-of-vulcan-rocket-carrying-40-amazon-leo-satellites/ | 15/11/2026 | 15/11/2026 | Alta | Falla total de la 1ª misión Vulcan dedicada a Leo el 15/11/2026: anomalía en etapa Centaur ~10 min tras despegue; 40 satélites perdidos. | [DATO REAL] |
| 12 | Spaceflight Now — "United Launch Alliance announces mid-November return to flight for Vulcan rocket" | Técnica/prensa especializada | https://spaceflightnow.com/2026/10/28/united-launch-alliance-announces-mid-november-return-to-flight-for-vulcan-rocket/ | 28/10/2026 | 15/11/2026 | Alta | Vulcan estuvo ~9 meses en tierra por problemas en los boosters sólidos; contexto del retorno al vuelo. | [DATO REAL] |

### D. Prensa especializada y general (para ubicar hechos / confirmar)

| # | Fuente (organización, título) | Tipo | URL | Publicado | Consultado | Confiabilidad | Qué dato aporta | Etiqueta |
|---|---|---|---|---|---|---|---|---|
| 13 | Via Satellite — "Amazon Rebrands Project Kuiper to Amazon Leo, Shares Terminal Lineup" | Prensa especializada | https://www.satellitetoday.com/connectivity/2025/11/13/amazon-rebrands-project-kuiper-to-amazon-leo-shares-terminal-lineup/ | 13/11/2025 | 15/11/2026 | Media-Alta | Fecha del rebrand Project Kuiper → Amazon Leo (13/11/2025); línea de terminales. | [DATO REAL] |
| 14 | Aviation Week — "Amazon Rebrands Project Kuiper To 'Amazon Leo'" | Prensa especializada | https://aviationweek.com/space/satellites/amazon-rebrands-project-kuiper-amazon-leo | 13/11/2025 | 15/11/2026 | Media-Alta | Confirma rebrand; declaraciones de Rajeev Badyal (VP Amazon Leo). | [DATO REAL] |
| 15 | CNBC — "Amazon has deployed enough satellites to launch Leo service later this year" | Prensa general/negocios | https://www.cnbc.com/2026/07/02/amazon-has-deployed-enough-satellites-to-launch-leo-service-this-year.html | 02/07/2026 | 15/11/2026 | Media | Amazon declara tener satélites suficientes para servicio inicial en 2026; conteo ~390+. | base de [INFERENCIA DEL GRUPO] |
| 16 | The Register — "Amazon Leo's satellite homework is late, but FCC won't flunk it just yet" | Prensa especializada | https://www.theregister.com/networks/2026/06/08/amazon-leos-satellite-homework-is-late-but-fcc-wont-flunk-it-just-yet/ | 08/06/2026 | 15/11/2026 | Media-Alta | Explica el waiver FCC y el hito incumplido de 1.616 satélites. Útil como mapa, confirmar cifras con #8. | base de [INFERENCIA DEL GRUPO] |
| 17 | DCD — "Amazon Leo reveals plans for installation of more than 300 ground stations" | Prensa especializada | https://www.datacenterdynamics.com/en/news/amazon-leo-reveals-plans-for-installation-of-more-than-300-ground-stations/ | 2026 | 15/11/2026 | Media | Plan de +300 estaciones terrestres; arquitectura gateway + Point of Presence (POP) + fibra/AWS. | [DATO REAL] |
| 18 | DCD — "Amazon files to place ground station in Kenya" | Prensa especializada | https://www.datacenterdynamics.com/en/news/amazon-files-to-place-ground-station-in-kenya-report/ | ≈jun 2026 | 15/11/2026 | Media | Solicitud de licencia de gateway internacional (15 años) en Kenia; 1ª estación en África. ⚠ "report", confirmar. | base de [INFERENCIA DEL GRUPO] |
| 19 | Wikipedia — "Amazon Leo" | Terciaria (índice) | https://en.wikipedia.org/wiki/Amazon_Leo | viva | 15/11/2026 | Baja como fuente / Alta como índice | Punto de partida y lista de referencias primarias. **No citar como fuente directa**: seguir sus referencias. | — (navegación) |
| 20 | Wikipedia — "List of Amazon Leo launches" | Terciaria (índice) | https://en.wikipedia.org/wiki/List_of_Amazon_Leo_launches | viva | 15/11/2026 | Baja como fuente / Alta como índice | Cronología de lanzamientos con fechas y cohetes; usar para ubicar y luego verificar cada misión. | — (navegación) |

> Confiabilidad: `Alta` / `Media` / `Baja`, con criterio explícito. ⚠ = dato vía fuente secundaria, verificar contra el primario.
> Agregadores no incluidos en la tabla por baja confiabilidad (orbitalradar.com, 5gstore, martianalpha, trioflatmount, insidedeeptech, shuttlepresskit): sirven para orientarse, **no para citar**. Todo dato que aparezca solo ahí va a "Datos buscados y no encontrados" hasta confirmarlo.

---

## Contradicciones y vacíos detectados

| Tema | Fuentes en conflicto | Qué dice cada una | Cómo lo resolvió el equipo |
|---|---|---|---|
| Resultado de la 1ª misión Vulcan dedicada | #2/#3 (Amazon, previo) vs #11 (Spaceflight Now, 15/11/2026) | Las notas oficiales previas anunciaban la misión Vulcan con 40 satélites como próximo hito; el 15/11/2026 la misión **falló** (anomalía en Centaur, 40 satélites perdidos, primera falla total de ULA/Vulcan). | [[PENDIENTE equipo: decisión de gestión — es un evento de riesgo materializado. No presentar la misión como exitosa.]] |
| Satélites autorizados por la FCC | Prensa: 3.236 (grant 2020, #6) vs 3.232 (orden DA 24-224, 2024, #7) vs outliers 3.276 | La cifra autorizada se habría reducido de 3.236 a 3.232 en 2024. Un medio menor habla de 3.276 (probable error). | Usar 3.232 como vigente **solo tras confirmar #7 en fcc.gov**; registrar la evolución 3.236→3.232. |
| Fecha del hito intermedio / deadline | #16/#8 (hito 50% = 1.616 sat. al 30/07/2026, incumplido; deadline final 30/07/2029) vs un agregador (1.618 sat. al 30/07/2027) | La mayoría: hito del 50% vencido en jul/2026 y deadline 2029 intacto. El agregador da otra fecha, se descarta por inconsistente. | Tomar la versión mayoritaria; **confirmar números y fechas exactas en la orden FCC #8**. |
| Fecha del rebrand a "Amazon Leo" | #13/#14 (13/11/2025) vs Wikipedia #19 (12/11/2025) | Difieren en un día. | Usar 13/11/2025 (dos fuentes especializadas coinciden); nota al pie sobre la discrepancia. |
| Ritmo de producción de satélites | Amazon vía #2/#3 ("5 por día" / "1.000ª unidad") vs prensa ("27 por semana") | Capacidad declarada vs ritmo efectivo citado. No son lo mismo (capacidad ≠ ritmo real). | Distinguir **capacidad instalada** de **ritmo efectivo**; citar cada cifra con su fuente y fecha de corte. |
| Fecha de la 1.000ª unidad | #3 (Amazon: "inicios de septiembre") vs prensa (8 o 22 de octubre 2026) | Las notas difieren entre septiembre y octubre. | Confirmar en la página oficial #2/#3 con captura fechada. |

---

## Datos buscados y no encontrados

Lo que **no** es público importa tanto como lo que sí: define qué se reconstruye como `[INFERENCIA DEL GRUPO]` o `[PROPUESTA DE GESTIÓN]`.

| Dato buscado | Dónde se buscó | Conclusión |
|---|---|---|
| Inversión total comprometida por Amazon en Leo/Kuiper (USD) | Búsqueda web general; notas de rebrand e inversión | No surgió una cifra oficial consolidada. Buscar en reportes financieros de Amazon (10-K/10-Q, #5 SEC) o declaraciones a inversores. |
| Órdenes FCC primarias (texto completo de DA 26-553, DA 24-224 y grant 2020) | Búsqueda web | Solo vía prensa hasta ahora. **Falta leer los documentos en fcc.gov/ECFS.** Condiciona #6, #7, #8. |
| Costo unitario por satélite y costo por lanzamiento | Búsqueda web | No público. Deberá reconstruirse como [INFERENCIA DEL GRUPO] o [PROPUESTA DE GESTIÓN] con supuestos. |
| Cronograma maestro interno / EDT del programa | Búsqueda web | No público (esperable en un proyecto privado). Es el núcleo a **reconstruir** por el equipo. |
| Ubicaciones y estado concretos de las +300 estaciones terrestres | #17, #18 | Solo cifra agregada y casos sueltos (Kenia, Australia, Alemania). Falta un listado verificable. |
| Totales de lanzamientos contratados **vigentes** (post-SpaceX y renegociaciones) | #4, #9, #10 | Las fuentes dan cifras distintas (hasta 83 en 2022; recuentos posteriores difieren en Atlas V, Ariane 6, New Glenn). Confirmar el estado actual con Amazon/proveedores antes de usar un total. |
| Fecha del próximo retorno al vuelo de Vulcan tras la falla del 15/11 | #11, #12 | Aún no anunciada al 15/11/2026. Seguir. |
