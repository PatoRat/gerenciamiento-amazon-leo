# Hitos públicos de Amazon Leo

Fecha de corte y de consulta: **16/11/2026**.
Las referencias `#n` apuntan a `evidencia/registro-fuentes.md` (Anexo A). La sección 8 detalla las fuentes #21 a #47, ya incorporadas a ese registro.
Convención: toda fila de las secciones 1 a 4 es `[DATO REAL]` y trae su fuente. Las secciones 5 y 6 contienen `[INFERENCIA DEL GRUPO]` con supuestos explícitos. La sección 7 lista lo que **no se pudo verificar**.
"Primaria" = Amazon, FCC, ULA. "Secundaria" = medios. Casi todo lo de Amazon es declaración de la propia empresa: describe lo que Amazon dice, no necesariamente lo que ocurrió.

---

## 1. Lanzamientos (todas las misiones listadas por Amazon)

Fuente de toda la tabla: Amazon, *Mission updates* (#2). La página trae dos fechas de actualización contradictorias ("15/11/2026" arriba, "28/10/2026" al pie). Las horas UTC marcadas "calc." las convirtió el equipo de investigación desde la hora local que da Amazon, salvo LE-01 y LE-03. El acumulado **no es un dato publicado**: lo calculó sumando los satélites por misión (sin el protoflight) y coincide con las expresiones "200+", "more than 330" y "nearly 400" de Amazon.

| N.º | Misión | Fecha UTC | Cohete | Sitio | Satélites | Resultado | Acumulado (calc.) | Fuentes |
|---|---|---|---|---|---|---|---|---|
| 1 | KA-01 | 28/04/2025 | Atlas V 551 | SLC-41, Cabo Cañaveral | 27 | Lanzada | 27 | #2 |
| 2 | KA-02 | 23/06/2025 | Atlas V 551 | SLC-41 | 27 | Lanzada | 54 | #2 |
| 3 | KF-01 | 16/07/2025 | Falcon 9 | SLC-40 | 24 | Lanzada | 78 | #2 |
| 4 | KF-02 | 11/08/2025 | Falcon 9 | SLC-40 | 24 | Lanzada | 102 | #2 |
| 5 | KA-03 | 25/09/2025 | Atlas V 551 | SLC-41 | 27 | Lanzada | 129 | #2 |
| 6 | KF-03 | 14/10/2025 | Falcon 9 | SLC-40 | 24 | Lanzada | 153 | #2 |
| 7 | LA-04 | 16/12/2025 | Atlas V 551 | SLC-41 | 27 | Lanzada | 180 | #2 |
| 8 | LE-01 | 12/02/2026 | Ariane 64 | Kourou | 32 | Éxito | 212 | #1 |
| 9 | LA-05 | 04/04/2026 | Atlas V 551 | SLC-41 | 29 | Lanzada | 241 | #2 |
| 10 | LA-06 | 28/04/2026 | Atlas V 551 | SLC-41 | 29 | Lanzada | 270 | #2 |
| 11 | LE-02 | 30/04/2026 | Ariane 64 | Kourou | 32 | Lanzada | 302 | #2 |
| 12 | LA-07 | 29/05/2026 | Atlas V 551 | SLC-41 | 29 | Lanzada | 331 | #2, #46 |
| 13 | LE-03 | 17/06/2026 | Ariane 64 | Kourou | 36 | Desplegados 36 | 367 | #2, #24 |
| 14 | LA-08 | 02/07/2026 | Atlas V 551 | SLC-41 | 29 | Lanzada | 396 | #2 |
| 15 | LV-01 | 15/11/2026 | Vulcan VC6L (ULA) | SLC-41 | 40 | **Falla: carga perdida** | 396 (sin sumar) | #2, #11 |

- **[DATO REAL]** Amazon cuenta "14 missions" y "nearly 400 satellites" antes de LV-01 (#2, #24).
- **[DATO REAL]** Falla de LV-01: ULA informó una anomalía unos 10 minutos después del despegue. Causa raíz no publicada (#11; verificación en `verificacion-i1-2026-11-16.md`). Amazon la reconoce en su página *Mission updates* (#2): "ULA experienced an anomaly with the Vulcan rocket carrying Leo satellites, and the payload was lost".
- **[DATO REAL]** La página de Amazon sobre LV-01 (#3) **no refleja la falla**: sigue describiendo la misión como futura (última actualización 14/11/2026). Amazon mantiene dos páginas que se contradicen. Citar #2 para el resultado.
- **[DATO REAL]** Próxima misión publicada: **LE-04**, Ariane 64, 36 satélites, **no antes del 23/11/2026**, Kourou (#2). Amazon dice que la ventana exacta se informará más cerca de la fecha.
- **[DATO REAL]** LV-02: Amazon decía que se esperaba "within weeks" de un LV-01 nominal (#3). Esa expectativa ya no aplica tal cual, pero Amazon no publicó una nueva fecha.

**Protoflight (KuiperSat-1 y -2, Atlas V, 06/10/2023):** solo aparece en la tabla de Wikipedia. **NO VERIFICADO** en fuente primaria (ninguna página de Amazon consultada lo menciona; Amazon numera desde KA-01 como misión n.º 1).

### Lanzamientos contratados (lo que dice Amazon hoy)

| Proveedor | Cantidad | Fuente |
|---|---|---|
| Arianespace (Ariane 6) | 24 (ampliado desde 18 el 10/09/2026) | #24 |
| ULA (Vulcan) | 38 | #3 |
| ULA (Atlas V) | 9 (contrato previo a 2022) | #4 (05/04/2022) |
| Blue Origin (New Glenn) | 24 firmes ("opciones convertidas") | #23 (23/03/2026) |
| SpaceX (Falcon 9) | 3 (01/12/2023) + 10 más "a fines de 2025" | #38, #23 |
| Total declarado | "more than 100" misiones | #23, #2 |

---

## 2. Hitos regulatorios

| Fecha | Hito | Fuente | Tipo |
|---|---|---|---|
| 04/04/2019 | Se conoce el proyecto por presentaciones federales: 3.236 satélites. | #42 | Secundaria |
| 30/07/2020 | FCC autoriza la constelación (3.236 satélites, banda Ka). Amazon lo comunicó el mismo día. Orden FCC 20-102, 35 FCC Rcd 8324. | #39; #6 | Primaria (Amazon); no se consultó el original de la FCC |
| 09/02/2023 | FCC aprueba el plan actualizado de desechos orbitales (con reportes semestrales). | #44 | Secundaria |
| 08/03/2024 | FCC reduce la constelación a 3.232 satélites y redistribuye órbitas. | #7 | Primaria (FCC, texto original consultado) |
| 30/01/2026 | Amazon pide extender el hito del 50% (24 meses, hasta 30/07/2028) o un waiver. Dijo tener 180 satélites lanzados y proyectó ~700 al 30/07/2026. | #8 ¶8 | Primaria (FCC, texto original consultado) |
| 05/06/2026 | FCC concede un waiver parcial del hito de 1.616 satélites al 30/07/2026; pérdida temporal de prioridad de espectro; hito de 3.232 al 30/07/2029 intacto; la fianza no se exime. | #8 | Primaria (FCC, texto original consultado) |
| 27/07/2026 | Amazon presenta a la FCC el sistema direct-to-device: hasta 5.105 satélites, despliegue desde 2028. Número de expediente **NO VERIFICADO**. | #34 | Primaria (Amazon) |

---

## 3. Hitos de infraestructura, producción y negocio

| Fecha | Hito | Fuente | Tipo |
|---|---|---|---|
| 2020 | Sede de I+D en Redmond, WA (instalación de 219.000 ft² anunciada en 2020). Producción en Kirkland. | #25 | Primaria |
| 27/10/2022 | Fábrica de Kirkland: 172.000 ft²; capacidad "hasta cuatro satélites por día". Amazon habla de "up to 92" lanzamientos pesados. | #25 | Primaria |
| 14/03/2023 | Primera vista de tres terminales (Nano, Pro, Ultra). | #30 | Primaria |
| 01/12/2023 | Contrato con SpaceX: 3 lanzamientos Falcon 9. | #38 | Primaria |
| 04/2024 | Apertura de la fábrica de Kirkland ("opened in April"); pico de "up to five satellites per day". | #26 (27/06/2024) | Primaria |
| 12/06/2024 | Acuerdo de distribución con DIRECTV Latin America y Sky Brasil (Argentina, Brasil, Chile, Colombia, Ecuador, Perú, Uruguay). | #37 | Primaria |
| 24/07/2025 | Instalación de procesamiento en Kennedy Space Center: 100.000 ft²; inversión total "more than $140 million"; capacidad de "more than 100 satellites per month" y tres campañas simultáneas. | #27 | Primaria |
| 04/09/2025 | Acuerdo con JetBlue (Wi-Fi a bordo desde 2027 en aviones seleccionados). | #36 | Primaria |
| 13/11/2025 | **Rebrand de Project Kuiper a Amazon Leo.** Artículo de Rajeev Badyal, "Vice President of Amazon Leo". Cita como socios a JetBlue, L3Harris, DIRECTV LatAm, Sky Brasil y NBN Co. | #21; #13, #14 | Primaria |
| 24/11/2025 | *Enterprise preview*: unidades Leo Pro y Leo Ultra a empresas seleccionadas. Amazon anticipa un "broader rollout next year". | #29 | Primaria |
| 26/02/2026 | Acuerdo con Vanu (África). | #32 | Primaria |
| 23/03/2026 | Plan de duplicar la cadencia: más de 200 satélites desplegados; Kirkland con capacidad de "as many as 30 satellites per week"; "$200+ million" en Cabo Cañaveral (VIF-A, plataforma móvil, segundo barco); "approval to deploy a second-generation system". | #23 | Primaria |
| 31/03/2026 | Acuerdo con Delta Air Lines: servicio desde 2028 en 500 aviones. | #31 | Primaria |
| 14/04/2026 | **Acuerdo para adquirir Globalstar** ($90 por acción en efectivo o 0,3210 acciones de Amazon; cierre previsto en 2027) y acuerdo con Apple para funciones satelitales de iPhone y Apple Watch. Sistema D2D propio "beginning in 2028". Valor total de la operación: ~US$11,57 mil millones según CNBC (Amazon no da el total). | #22 (Amazon), #5 (SEC), #43 (CNBC) | Primaria y secundaria |
| 15/07/2026 | Acuerdo con Herotel (Sudáfrica), servicio "evry"; comercial en 2027. | #33 | Primaria |
| 10/09/2026 | Arianespace: de 18 a 24 lanzamientos contratados. | #24 | Primaria |
| Inicios de 09/2026 | Amazon completa su satélite número 1.000. | #3 | Primaria |
| 22/09/2026 | Acuerdo con Uztelecom / UZ-SAT (Uzbekistán); servicio en "private preview". | #35 | Primaria |

---

## 4. Estado del servicio y terminales

- **[DATO REAL]** Al 16/11/2026 Amazon **no anunció lanzamiento comercial**. Las páginas de septiembre y noviembre de 2026 hablan de "initial service rollout later this year", con clientes empresariales en "private preview" (#35, #24, #3).
- **[DATO REAL]** Terminales (cifras de Amazon, no precios de venta): Nano hasta 100 Mbps; Pro hasta 400 Mbps; Ultra hasta 1 Gbps de bajada y 400 Mbps de subida (#30, #29). Costo de fabricación de terminal estándar esperado "<US$400" (2023, #30). **Precios de venta: NO VERIFICADO.**
- **[DATO REAL]** Capacidad de fabricación declarada de Kirkland por fecha: 4 satélites/día (2022, #25); hasta 5/día (2024, #26); hasta 30/semana (2026, #23). Satélite n.º 1.000 completado a inicios de 09/2026 (#3).

---

## 5. Inferencias del grupo

**[INFERENCIA DEL GRUPO] 1. El inicio del servicio se corrió año tras año.**
Lo que Amazon dijo en cada momento sobre el inicio del servicio a clientes:
- 14/03/2023: primeros clientes "later that year", es decir 2024 (#30).
- 27/06/2024: servicio "next year", es decir 2025 (#26).
- 24/11/2025: "broader rollout next year", es decir 2026 (#29).
- 09/11/2026: "initial service rollout later this year" (#3).
→ Base: #26, #29, #30, #3. Supuestos: (a) las cuatro frases se refieren al mismo hito, el inicio del servicio comercial a clientes; (b) no hay una definición pública de qué cuenta como "inicio".

**Línea de tiempo de las promesas de inicio del servicio** (agregada el 16/11/2026, para el informe y el dashboard)

| Fecha de la declaración | Qué dijo Amazon (textual) | Año de inicio implícito | Corrimiento contra la primera promesa | Etiqueta | Fuente |
|---|---|---|---|---|---|
| 14/03/2023 | primeros clientes "later that year" | 2024 (lectura del grupo) | — (línea base) | `[DATO REAL]` + año `[INFERENCIA DEL GRUPO]` | #30 |
| 27/06/2024 | servicio "next year" | 2025 | +1 año | `[DATO REAL]` + año `[INFERENCIA DEL GRUPO]` | #26 |
| 24/11/2025 | *Enterprise preview* de Leo Pro y Ultra; "broader rollout next year" | 2026 | +2 años | `[DATO REAL]` + año `[INFERENCIA DEL GRUPO]` | #29 |
| 22/09/2026 | Uzbekistán: servicio en "private preview" | — (acceso limitado, no comercial) | — | `[DATO REAL]` | #35 |
| 09/11/2026 | "initial service rollout later this year" | 2026 (quedan ≈ 6 semanas) | +2 años, sin cumplir | `[DATO REAL]` | #3 |
| **16/11/2026 (corte)** | **Sin anuncio de servicio comercial** | — | — | `[DATO REAL]` | #35, #24, #3 |

**[INFERENCIA DEL GRUPO]** Cada promesa corrió el inicio ≈ 1 año, y entre la primera y la última hay ≈ 2 años de corrimiento. Mientras tanto, Amazon fue abriendo accesos parciales (enterprise preview en 2025, private preview en 2026), que funcionan como hitos intermedios no declarados como "inicio". Para la gestión, la lección es definir **un criterio verificable de inicio de servicio** (cobertura mínima, satélites mínimos, clientes pagos) en el acta y en el cronograma. Es la respuesta propuesta para R-03 en Riesgos.
→ Base: tabla anterior; Riesgos R-03. Supuestos: los del bloque anterior; la "private preview" no cuenta como inicio comercial.

**[INFERENCIA DEL GRUPO] 2. Brecha entre el plan presentado a la FCC y lo logrado.**
Amazon proyectó ~700 satélites desplegados al 30/07/2026 (#8 ¶8). Antes de LV-01 había ~396 en órbita, el 24% del hito de 1.616. Con LV-01 exitoso habría llegado a ~436.
→ Base: #8, #2, #11. Supuestos: (a) "desplegados" es comparable con "lanzados y en órbita"; (b) el conteo de ~396 es el correcto.

**[INFERENCIA DEL GRUPO] 3. La cartera de lanzamientos es coherente con "más de 100".**
Suma de lo contratado según Amazon: 24 Ariane 6 + 38 Vulcan + 9 Atlas V + 24 New Glenn + 13 Falcon 9 = 108.
→ Base: #24, #3, #4, #23, #38. Supuestos: (a) los 9 Atlas V incluyen los 8 ya volados más 1 (el protoflight de 2023, no verificado); (b) los 13 Falcon 9 son 3 + 10 adicionales y no se solapan; (c) no hay otros contratos.

**[INFERENCIA DEL GRUPO] 4. Los "4.500 satélites adicionales" que menciona CNBC probablemente son Gen2 y Polar.**
DA 26-553 ¶3 menciona Gen2 (3.212 satélites) y Polar (1.292). La suma es 4.504.
→ Base: #8 ¶3, #43. Supuesto: la mención de CNBC se refiere a esos mismos sistemas. No se consultó la orden que los autoriza.

**[INFERENCIA DEL GRUPO] 5. La falla de LV-01 y la caída de New Glenn concentran el riesgo en dos proveedores.**
Vulcan (38 contratados) y New Glenn (24) suman 62 de ~108 lanzamientos, el 57%, y ambos tienen eventos de falla en 2026 (LV-01 el 15/11; explosión de New Glenn en su plataforma durante una prueba de encendido el 28/05/2026, #47).
→ Base: sección 1, #11. Supuestos: (a) los números de contratos son vigentes.

---

## 6. Discrepancias detectadas

| Tema | Fuente A | Fuente B | Resolución |
|---|---|---|---|
| Fecha del rebrand | Amazon: 13/11/2025 (#21) | Wikipedia: 12/11/2025 | Usar 13/11/2025 (primaria). Cierra la contradicción del registro. |
| Cargo de Rajeev Badyal | Amazon: "Vice President of Amazon Leo" (#21) | Wikipedia: "president" | Usar "Vice President". |
| Fecha límite final FCC | DA 26-553: 30/07/2029 (#8) | DA 24-224 ¶52(b) y Via Satellite (#44): "July 20, 2029" | Usar 30/07/2029; nota al pie. |
| Total de lanzamientos | 83 (04/2022, #4); "up to 92" (10/2022, #25); 77 cohetes pesados (12/2023); "initial block of 80" y "más de 100" (2026, #23) | — | Siempre citar con fecha: son conteos de momentos distintos. |
| Capacidad de producción | 4/día (2022), 5/día (2024), 30/semana (2026) | Prensa: 27/semana | Citar cada cifra con su fecha. 30/semana (Amazon) es capacidad, no ritmo efectivo. |
| Fecha de actualización de #2 | Cabecera: 15/11/2026 | Pie: 28/10/2026 | Guardar captura fechada de la página. |
| Pesos y medidas de terminales | Amazon (#30): Nano 1 lb, Ultra 19x30 in | Wikipedia: otras cifras | Usar Amazon. |

---

## 7. NO VERIFICADO (pendientes)

- Protoflight de 06/10/2023 (solo Wikipedia).
- Contenido del original FCC 20-102 (ver `verificacion-i1-2026-11-16.md`); vuelto a confirmar de forma indirecta por #7 y #8.
- ~~Compromiso de inversión de "más de US$10 mil millones" (2020)~~ **VERIFICADO el 16/11/2026** en #39: "Amazon will invest more than $10 billion in Project Kuiper" (Dave Limp, Senior Vice President de Amazon); propósito: "reliable, affordable broadband service to unserved and underserved communities around the world". También #28 (04/11/2025, act. 13/11/2025): "fast, reliable internet to customers and communities beyond the reach of existing networks"; constelación inicial de "more than 3,000 satellites".
- Aprobación FCC de 4.500 satélites adicionales (CNBC lo menciona sin detalle) y expediente del D2D.
- Aviso a la FCC del 14/08/2026 y qué pasó con el hito del 30/07/2026.
- Estado del S-4 y de las aprobaciones regulatorias de Globalstar.
- Cantidad y ubicación de las estaciones terrestres (el registro #17 habla de más de 300; Amazon solo dice "a global network of ground gateway antennas").
- Precios de venta de terminales.
- Cambios de liderazgo: no se encontró ningún anuncio.
- Número de misiones futuras con fecha de Atlas V, Falcon 9 y New Glenn.
- Hora real de LV-01 (17:11 vs 17:40 UTC según la fuente).
- Fuentes inaccesibles: SpaceNews (429/paywall), Ars Technica, GeekWire, The Verge, NASASpaceflight (403), fcc.gov (403), leo.amazon.com (403).

---

## 8. Fuentes incorporadas al registro

> Estas fuentes están incorporadas a `evidencia/registro-fuentes.md` (sección E). La referencia oficial es el registro.

Todas consultadas el 16/11/2026. Las URL de Amazon son `https://www.aboutamazon.com/...`.

| # | Fuente | Ruta / URL | Publicada | Tipo |
|---|---|---|---|---|
| 21 | Amazon — Project Kuiper becomes Amazon Leo | /news/amazon-leo/project-kuiper-becomes-amazon-leo | 13/11/2025 | Primaria |
| 22 | Amazon — Globalstar y Apple | /news/company-news/amazon-globalstar-apple | 14/04/2026 | Primaria |
| 23 | Amazon — Plan de duplicar la cadencia | /news/amazon-leo/amazon-leo-plans-double-launch-rate-20-missions | 23/03/2026 | Primaria |
| 24 | Amazon — Arianespace, 6 lanzamientos nuevos | /news/amazon-leo/amazon-leo-arianespace-new-launches | 10/09/2026 | Primaria |
| 25 | Amazon — Fábrica de Kirkland ampliada | /news/innovation-at-amazon/amazon-expands-satellite-manufacturing-at-newly-acquired-project-kuiper-facility | 27/10/2022 | Primaria |
| 26 | Amazon — Dentro de la fábrica de Kirkland | /news/innovation-at-amazon/inside-project-kuiper-satellite-facility-kirkland | 27/06/2024 | Primaria |
| 27 | Amazon — Instalación en Florida | /news/innovation-at-amazon/project-kuiper-florida-satellite-facility | 24/07/2025 | Primaria |
| 28 | Amazon — What is Project Kuiper | /news/innovation-at-amazon/what-is-amazon-project-kuiper | 04/11/2025 (act. 13/11/2025) | Primaria |
| 29 | Amazon — Enterprise preview Ultra y Pro | /news/amazon-leo/amazon-leo-satellite-internet-ultra-pro | 24/11/2025 | Primaria |
| 30 | Amazon — Primera vista de terminales | /news/innovation-at-amazon/heres-your-first-look-at-project-kuipers-low-cost-customer-terminals | 14/03/2023 | Primaria |
| 31 | Amazon — Delta | /news/amazon-leo/amazon-leo-delta-in-flight-wifi-2028 | 31/03/2026 | Primaria |
| 32 | Amazon — Vanu | /news/amazon-leo/amazon-leo-vanu-satellite-internet-connectivity-africa | 26/02/2026 | Primaria |
| 33 | Amazon — Herotel | /news/amazon-leo/amazon-leo-south-africa-herotel-evry | 15/07/2026 | Primaria |
| 34 | Amazon — Direct-to-device | /news/amazon-leo/amazon-leo-direct-to-device-satellite-service-explained | 27/07/2026 | Primaria |
| 35 | Amazon — Uzbekistán | /news/amazon-leo/amazon-leo-uzbekistan | 22/09/2026 | Primaria |
| 36 | Amazon — JetBlue | /news/innovation-at-amazon/jetblue-amazon-project-kuiper-in-flight-wifi-partnership | 04/09/2025 | Primaria |
| 37 | Amazon — Sudamérica / DIRECTV | /news/innovation-at-amazon/amazon-project-kuiper-in-south-america | 12/06/2024 | Primaria |
| 38 | Amazon — Falcon 9 con SpaceX | /news/innovation-at-amazon/amazon-project-kuiper-spacex-launch | 01/12/2023 | Primaria |
| 39 | Amazon — Aprobación FCC 2020 | /news/company-news/amazon-receives-fcc-approval-for-project-kuiper-satellite-constellation | 30/07/2020 | Primaria |
| 40 | Amazon Australia — NBN Co | https://www.aboutamazon.com.au/news/innovation/project-kuiper-partners-with-nbn-co-to-bring-low-earth-orbit-satellite-broadband-to-rural-australia | 05/08/2025 | Primaria |
| 41 | ULA — Vulcan Leo 1 (página de misión) | https://www.ulalaunch.com/missions/next-launch/vulcan-leo-1 | sin fecha (previa al lanzamiento) | Primaria |
| 42 | CNBC — Amazon Project Kuiper | https://www.cnbc.com/2019/04/04/amazon-project-kuiper-broadband-internet-small-satellite-network.html | 04/04/2019 | Secundaria |
| 43 | CNBC — Globalstar y Leo | https://www.cnbc.com/2026/04/14/amazon-globalstar-satellite-leo-internet.html | 14/04/2026 | Secundaria |
| 44 | Via Satellite — FCC aprueba plan de desechos | https://www.satellitetoday.com/government-military/2023/02/09/fcc-approves-amazon-kuiper-orbital-debris-plan-clearing-way-for-deployment/ | 09/02/2023 | Secundaria |
| 45 | Vice — SpaceX presiona contra Amazon | https://www.vice.com/en/article/spacex-is-lobbying-against-amazons-internet-beaming-satellites/ | 19/12/2019 | Secundaria |
| 46 | Amazon — Adelanto de LE-03 | /news/amazon-leo/amazon-leo-rocket-satellite-update | 05/06/2026 | Primaria |
| 47 | AP vía OPB — Explosión de New Glenn en plataforma | https://www.opb.org/article/2026/05/29/blue-origin-rocket-explodes-on-the-launch-pad-during-an-engine-firing-test/ | 29/05/2026 | Secundaria (confirmada por varios medios) |
