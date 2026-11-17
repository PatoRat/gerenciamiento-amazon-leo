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
| 3 | Amazon — "Amazon Leo to launch 40 satellites on its first Vulcan mission" | Oficial | https://www.aboutamazon.com/news/amazon-leo/amazon-leo-vulcan-satellites-launch | 09/11/2026 (act. 14/11/2026) | 16/11/2026 | Alta (pero desactualizada) | 40 satélites en la 1ª misión Vulcan dedicada; 1.000ª unidad completada a inicios de septiembre. **Al 16/11/2026 no refleja la falla de LV-01**: para el resultado citar #2. | [DATO REAL] |
| 4 | Amazon — "Amazon makes historic launch investment to advance Project Kuiper" | Oficial | https://www.aboutamazon.com/news/innovation-at-amazon/amazon-makes-historic-launch-investment-to-advance-project-kuiper | 05/04/2022 | 15/11/2026 | Alta | Compra de lanzamientos 2022: 38 Vulcan + 18 Ariane 6 + 12 New Glenn (+15 opcionales) = hasta 83. | [DATO REAL] |
| 5 | SEC EDGAR — Amazon.com Inc, Form 425, Exhibit 99.1: comunicado conjunto Amazon–Globalstar | Regulatoria (primaria) | https://www.sec.gov/Archives/edgar/data/1018724/000110465926042891/tm2611746d2_ex99-1.htm | 14/04/2026 | 16/11/2026 | Alta | **No es un informe financiero.** Anuncia la adquisición de Globalstar ($90/acción o 0,3210 acciones de Amazon; cierre previsto 2027) y el acuerdo con Apple; constelación inicial "more than 3,000 satellites"; D2D desde 2028. Inversión en Leo solo como "multibillion-dollar", sin cifra. | [DATO REAL] |

### B. Regulatorias e institucionales

| # | Fuente (organización, título) | Tipo | URL | Publicado | Consultado | Confiabilidad | Qué dato aporta | Etiqueta |
|---|---|---|---|---|---|---|---|---|
| 6 | FCC — Order and Authorization FCC 20-102, 35 FCC Rcd 8324 (autorización original Project Kuiper) | Regulatoria (primaria) | https://www.fcc.gov/document/fcc-authorizes-kuiper-satellite-constellation (403 a la lectura automática; reproducción parcial en TelecomTV) | 30/07/2020 (adoptada 29/07/2020) | 16/11/2026 | Alta | 3.236 satélites en 98 planos (590, 610 y 630 km); servicio desde los primeros 578. ⚠ Original sin leer: abrir el PDF desde un navegador. Hitos 2026/2029 confirmados indirectamente por #7 y #8. | [DATO REAL] |
| 7 | FCC — Order and Authorization DA 24-224 (modificación) | Regulatoria (primaria, leída) | https://docs.fcc.gov/public/attachments/DA-24-224A1.pdf | 08/03/2024 | 16/11/2026 | Alta | Reduce la constelación de 3.236 a 3.232 (¶1) y redistribuye órbitas: 782 a 590 km/33°, 2 a 590 km/30°, 1.292 a 610 km/42°, 1.156 a 630 km/51,9° (¶4). Prohíbe desplegar directo a altitud operativa (¶43). Hitos en ¶52(b) (dice "July 20, 2029", ver contradicciones). Aviso de cumplimiento antes del 14/08/2026 (¶53). | [DATO REAL] |
| 8 | FCC — Order DA 26-553 (waiver parcial del hito del 50%) | Regulatoria (primaria, leída) | https://docs.fcc.gov/public/attachments/DA-26-553A1.txt | 05/06/2026 | 16/11/2026 | Alta | Hitos: 1.616 al 30/07/2026 y 3.232 al 30/07/2029 (¶3). Waiver **parcial**, no prórroga (¶11, ¶19). Pérdida de prioridad de espectro Ka/Ku (2020) y banda V (2021) hasta el 30/03/2028, o 30/10/2027 si certifica el 50% construido (¶15). Si falla 2029, la autorización se reduce a los operativos (¶12). **La fianza no se exime** (¶18). Amazon declaró 180 lanzados y proyectó ~700 al 30/07/2026 (¶8). | [DATO REAL] |

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
| Resultado de la 1ª misión Vulcan dedicada | #2/#3 (Amazon, previo) vs #11 (Spaceflight Now, 15/11/2026) | Las notas oficiales previas anunciaban la misión Vulcan con 40 satélites como próximo hito; el 15/11/2026 la misión **falló** (anomalía en Centaur, 40 satélites perdidos, primera falla total de ULA/Vulcan). | **Resuelto 16/11/2026:** Amazon confirma la falla en #2. Se cita #2 para el resultado. En Riesgos se registra como tema T-01 (riesgo R-01 materializado). |
| Satélites autorizados por la FCC | Prensa: 3.236 (grant 2020, #6) vs 3.232 (orden DA 24-224, 2024, #7) vs outliers 3.276 | La cifra autorizada se habría reducido de 3.236 a 3.232 en 2024. Un medio menor habla de 3.276 (probable error). | **Resuelto 16/11/2026:** #7 leído en el primario. Vigente: 3.232. Evolución 3.236 (2020) → 3.232 (2024). |
| Fecha del hito intermedio / deadline | #16/#8 (hito 50% = 1.616 sat. al 30/07/2026, incumplido; deadline final 30/07/2029) vs un agregador (1.618 sat. al 30/07/2027) | La mayoría: hito del 50% vencido en jul/2026 y deadline 2029 intacto. El agregador da otra fecha, se descarta por inconsistente. | **Resuelto 16/11/2026:** #8 leído. Hito oficial: 1.616 al 30/07/2026 y 3.232 al 30/07/2029. El agregador queda descartado. |
| Fecha del rebrand a "Amazon Leo" | #13/#14 (13/11/2025) vs Wikipedia #19 (12/11/2025) | Difieren en un día. | Usar 13/11/2025 (dos fuentes especializadas coinciden); nota al pie sobre la discrepancia. |
| Ritmo de producción de satélites | Amazon vía #2/#3 ("5 por día" / "1.000ª unidad") vs prensa ("27 por semana") | Capacidad declarada vs ritmo efectivo citado. No son lo mismo (capacidad ≠ ritmo real). | Distinguir **capacidad instalada** de **ritmo efectivo**; citar cada cifra con su fuente y fecha de corte. |
| Fecha de la 1.000ª unidad | #3 (Amazon: "inicios de septiembre") vs prensa (8 o 22 de octubre 2026) | Las notas difieren entre septiembre y octubre. | Confirmar en la página oficial #2/#3 con captura fechada. |
| Fecha final del hito 2029 | #7 DA 24-224 ¶52(b) ("July 20, 2029") vs #8 DA 26-553 ¶3 (30/07/2029) | Difieren en 10 días. | Usar **30/07/2029** (orden posterior y coincidente con el resto); nota al pie. Probable error de redacción en DA 24-224. |
| Lanzamientos New Glenn contratados | #4 (05/04/2022: 12 firmes + 15 opcionales) vs #23 (23/03/2026: 24 firmes, "opciones convertidas") | Son conteos de fechas distintas, no una contradicción. | Usar **24 (al 23/03/2026)** como vigente. El "12" es el dato de 2022. Ver "Cifras de contratos con fecha de corte". |

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
| Fecha del próximo retorno al vuelo de Vulcan tras la falla del 15/11 | #11, #12 | Aún no anunciada al 16/11/2026. Seguir. |
| Aviso de cumplimiento del hito del 30/07/2026 (debido antes del 14/08/2026, #7 ¶53) y respuesta de la FCC | Búsqueda web 16/11/2026 | No encontrado. Buscar en ICFS (expediente SAT-MOD-20260129-00065). |
| Original de FCC 20-102 | fcc.gov (403) | Abrir el PDF desde un navegador o desde fcc.report. |

---

## Cifras de contratos de lanzamiento con fecha de corte

Las cifras de contratos cambiaron con el tiempo. **Siempre se citan con su fecha.** La columna "Vigente" es la que usa todo el informe.

| Proveedor (cohete) | 05/04/2022 (#4) | Posteriores | **Vigente (al 16/11/2026)** | Fuente vigente |
|---|---|---|---|---|
| ULA (Atlas V) | 9 (contrato previo a 2022) | — | 9 (8 volados para Leo) | #4, #2 |
| ULA (Vulcan) | 38 | — | 38 (1 volado y fallido: LV-01) | #3, #2 |
| Arianespace (Ariane 6) | 18 | 24 (10/09/2026) | 24 (3 volados) | #24 |
| Blue Origin (New Glenn) | 12 + 15 opcionales | 24 firmes, "opciones convertidas" (23/03/2026) | 24 (0 volados) | #23 |
| SpaceX (Falcon 9) | — | 3 (01/12/2023) + 10 "a fines de 2025" | 13 (3 volados) | #38, #23 |
| **Total** | hasta 83 | "up to 92" (10/2022, #25); "more than 100" (2026, #23) | **≈ 108** `[INFERENCIA DEL GRUPO]` (suma) | `evidencia/hitos.md` §5, inferencia 3 |

---

## E. Fuentes incorporadas en I-2 (#21 a #47)

Propuestas en `evidencia/hitos.md` §8 e incorporadas al registro el 16/11/2026 (rama `fix/04-cifras-contratos-y-fuentes`). **Quedan aprobadas cuando el equipo mergee el PR.** Todas consultadas el 16/11/2026. Las rutas de Amazon son relativas a `https://www.aboutamazon.com`.

| # | Fuente | Ruta / URL | Publicada | Tipo | Confiabilidad |
|---|---|---|---|---|---|
| 21 | Amazon — Project Kuiper becomes Amazon Leo | /news/amazon-leo/project-kuiper-becomes-amazon-leo | 13/11/2025 | Oficial | Alta |
| 22 | Amazon — Globalstar y Apple | /news/company-news/amazon-globalstar-apple | 14/04/2026 | Oficial | Alta |
| 23 | Amazon — Plan de duplicar la cadencia | /news/amazon-leo/amazon-leo-plans-double-launch-rate-20-missions | 23/03/2026 | Oficial | Alta |
| 24 | Amazon — Arianespace, 6 lanzamientos nuevos | /news/amazon-leo/amazon-leo-arianespace-new-launches | 10/09/2026 | Oficial | Alta |
| 25 | Amazon — Fábrica de Kirkland ampliada | /news/innovation-at-amazon/amazon-expands-satellite-manufacturing-at-newly-acquired-project-kuiper-facility | 27/10/2022 | Oficial | Alta |
| 26 | Amazon — Dentro de la fábrica de Kirkland | /news/innovation-at-amazon/inside-project-kuiper-satellite-facility-kirkland | 27/06/2024 | Oficial | Alta |
| 27 | Amazon — Instalación en Florida | /news/innovation-at-amazon/project-kuiper-florida-satellite-facility | 24/07/2025 | Oficial | Alta |
| 28 | Amazon — What is Project Kuiper | /news/innovation-at-amazon/what-is-amazon-project-kuiper | 04/11/2025 (act. 13/11/2025) | Oficial | Alta |
| 29 | Amazon — Enterprise preview Ultra y Pro | /news/amazon-leo/amazon-leo-satellite-internet-ultra-pro | 24/11/2025 | Oficial | Alta |
| 30 | Amazon — Primera vista de terminales | /news/innovation-at-amazon/heres-your-first-look-at-project-kuipers-low-cost-customer-terminals | 14/03/2023 | Oficial | Alta |
| 31 | Amazon — Delta | /news/amazon-leo/amazon-leo-delta-in-flight-wifi-2028 | 31/03/2026 | Oficial | Alta |
| 32 | Amazon — Vanu | /news/amazon-leo/amazon-leo-vanu-satellite-internet-connectivity-africa | 26/02/2026 | Oficial | Alta |
| 33 | Amazon — Herotel | /news/amazon-leo/amazon-leo-south-africa-herotel-evry | 15/07/2026 | Oficial | Alta |
| 34 | Amazon — Direct-to-device | /news/amazon-leo/amazon-leo-direct-to-device-satellite-service-explained | 27/07/2026 | Oficial | Alta |
| 35 | Amazon — Uzbekistán | /news/amazon-leo/amazon-leo-uzbekistan | 22/09/2026 | Oficial | Alta |
| 36 | Amazon — JetBlue | /news/innovation-at-amazon/jetblue-amazon-project-kuiper-in-flight-wifi-partnership | 04/09/2025 | Oficial | Alta |
| 37 | Amazon — Sudamérica / DIRECTV | /news/innovation-at-amazon/amazon-project-kuiper-in-south-america | 12/06/2024 | Oficial | Alta |
| 38 | Amazon — Falcon 9 con SpaceX | /news/innovation-at-amazon/amazon-project-kuiper-spacex-launch | 01/12/2023 | Oficial | Alta |
| 39 | Amazon — Aprobación FCC 2020 | /news/company-news/amazon-receives-fcc-approval-for-project-kuiper-satellite-constellation | 30/07/2020 | Oficial | Alta |
| 40 | Amazon Australia — NBN Co | https://www.aboutamazon.com.au/news/innovation/project-kuiper-partners-with-nbn-co-to-bring-low-earth-orbit-satellite-broadband-to-rural-australia | 05/08/2025 | Oficial | Alta |
| 41 | ULA — Vulcan Leo 1 (página de misión) | https://www.ulalaunch.com/missions/next-launch/vulcan-leo-1 | sin fecha (previa al lanzamiento) | Técnica / proveedor | Alta |
| 42 | CNBC — Amazon Project Kuiper | https://www.cnbc.com/2019/04/04/amazon-project-kuiper-broadband-internet-small-satellite-network.html | 04/04/2019 | Prensa general | Media |
| 43 | CNBC — Globalstar y Leo | https://www.cnbc.com/2026/04/14/amazon-globalstar-satellite-leo-internet.html | 14/04/2026 | Prensa general | Media |
| 44 | Via Satellite — FCC aprueba plan de desechos | https://www.satellitetoday.com/government-military/2023/02/09/fcc-approves-amazon-kuiper-orbital-debris-plan-clearing-way-for-deployment/ | 09/02/2023 | Prensa especializada | Media-Alta |
| 45 | Vice — SpaceX presiona contra Amazon | https://www.vice.com/en/article/spacex-is-lobbying-against-amazons-internet-beaming-satellites/ | 19/12/2019 | Prensa general | Media |
| 46 | Amazon — Adelanto de LE-03 | /news/amazon-leo/amazon-leo-rocket-satellite-update | 05/06/2026 | Oficial | Alta |
| 47 | AP vía OPB — Explosión de New Glenn en plataforma | https://www.opb.org/article/2026/05/29/blue-origin-rocket-explodes-on-the-launch-pad-during-an-engine-firing-test/ | 29/05/2026 | Prensa general (confirmada por varios medios) | Media-Alta |
