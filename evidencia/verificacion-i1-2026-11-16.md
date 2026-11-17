# Verificación del registro de fuentes I-1 — Amazon Leo

Fecha de consulta de todo lo de este documento: **16/11/2026**.
Insumo: `evidencia/registro-fuentes.md` (repo PatoRat/gerenciamiento-amazon-leo, commit 9e5a472).
Alcance: solo se verificaron las filas marcadas ⚠ (#5, #6, #7, #8) y el hallazgo Vulcan (#11). El resto del registro no se tocó.

Este documento es **material de revisión para el equipo**, no texto del informe. Las etiquetas siguen la regla de trazabilidad de la cátedra.

---

## Resumen: qué se confirma, qué se corrige, qué sigue pendiente

| Fila | Qué decía el registro | Resultado |
|---|---|---|
| #11 Vulcan | Falla total el 15/11/2026, 40 satélites perdidos | **Confirmado** por 3 medios (Spaceflight Now leído completo; SpaceNews y Space.com solo titular/extracto). Causa raíz aún desconocida. |
| #8 FCC DA 26-553 | Waiver del hito del 50%, deadline 2029 sin cambios | **Confirmado con el documento primario.** Hay precisiones importantes (ver abajo). |
| #7 FCC DA 24-224 | Reduce a 3.232 satélites | **Confirmado con el documento primario.** Además aporta la distribución por órbita. |
| #6 FCC 2020 | 3.236 satélites | **Parcialmente confirmado.** Se identificó el número oficial (FCC 20-102), pero el original da 403; se leyó una reproducción parcial. |
| #5 SEC "Form 425 FY2026" | "Documento financiero; verificar qué dice sobre Leo/inversión" | **La descripción del registro es incorrecta.** No es un resultado financiero (ver abajo). |

---

## 1. Vulcan, 15/11/2026 (fila #11)

**[DATO REAL]** El 15/11/2026 el cohete Vulcan de ULA, en la misión "Vulcan Leo 1" (LV-01), falló unos 10 minutos después del despegue y se perdieron los 40 satélites Amazon Leo que llevaba. Despegó de SLC-41, Cabo Cañaveral, a las 12:40 EST (17:40 UTC). Era el primer vuelo de Vulcan para Amazon (el primero de 38 contratados) y el regreso al vuelo tras ~9 meses en tierra.
→ Fuente: Spaceflight Now, W. Harwood — https://spaceflightnow.com/2026/11/15/ula-suffers-first-total-mission-failure-with-loss-of-vulcan-rocket-carrying-40-amazon-leo-satellites/ (publicado 15/11/2026, consultado 16/11/2026). Coinciden en el titular SpaceNews (https://spacenews.com/vulcan-launch-of-amazon-leo-satellites-fails/, paywall, solo se vio el titular y el pie) y Space.com (resultado de búsqueda, no leído completo).

**[DATO REAL]** Según Spaceflight Now, la primera etapa (BE-4) quemó más de lo previsto y separó tarde, y el Centaur hizo orientaciones inusuales al inicio de su quemada. Causa raíz: **no publicada**. ULA dijo que trabajará con el cliente y los organismos para hallarla y volver a volar "lo antes posible".
→ Misma fuente.

**[DATO REAL]** Antes de este vuelo había ~396 satélites Leo en órbita (Spaceflight Now: el vuelo habría llevado el total lanzado a 436). Otras fuentes dan 398 (14 misiones).
→ Spaceflight Now (misma URL); 398 según resultados de búsqueda de Space.com/SatNews, no leídos completos.

**[DATO REAL]** La página de Amazon sobre esta misión (https://www.aboutamazon.com/news/amazon-leo/amazon-leo-vulcan-satellites-launch) fue publicada el 09/11/2026 y actualizada el 14/11/2026 solo para ajustar la fecha de lanzamiento. **Al 16/11/2026 no mencionaba la falla.** Eso corrige la fila #3 del registro (decía "≈nov 2026"). En cambio, la página *Mission updates* de Amazon (#2, cabecera "Updated: November 15, 2026") sí la reconoce: "ULA experienced an anomaly with the Vulcan rocket carrying Leo satellites, and the payload was lost". Es decir, **Amazon confirma la falla en una fuente primaria**, aunque no corrigió la otra página.

**Novedades útiles para el informe** (no estaban en el registro):
- Hubo un hold en T-20 s antes del lanzamiento. Su causa no se explicó y no se sabe si influyó.
- Spaceflight Now menciona que Amazon depende además del regreso de **New Glenn** (que tuvo una explosión en plataforma en mayo de 2026). Esto afecta directamente los lanzamientos New Glenn contratados: 12 firmes según la fila #4 (dato de 2022), **24 firmes según el dato vigente** (#23, 23/03/2026). *Corrección del 16/11/2026: el informe usa 24; ver "Cifras de contratos con fecha de corte" en el registro de fuentes.*
- La misma página de Amazon anuncia un lanzamiento Ariane 6 con 36 satélites el 23/11/2026. Verificar que siga vigente.

**Sin verificar:** NASASpaceflight (403), texto completo de SpaceNews (paywall), declaraciones de Amazon y de la Space Force sobre el calendario, impacto sobre el hito FCC.

---

## 2. FCC DA 26-553 — waiver del hito (fila #8)

Documento primario leído completo: https://docs.fcc.gov/public/attachments/DA-26-553A1.txt (consultado 16/11/2026).

**[DATO REAL]** Es una *Order* del Space Bureau, firmada por Jay A. Schwarz, **adoptada y publicada el 05/06/2026**. Expediente ICFS SAT-MOD-20260129-00065 (indicativo S3051). → DA 26-553, encabezado y firma.

**[DATO REAL]** Hitos de Gen1 vigentes: **1.616 satélites desplegados y operativos antes del 30/07/2026** (50%) y **3.232 antes del 30/07/2029** (100%). → ¶3.

**[DATO REAL]** Decisión: *"We grant Amazon Leo's request for waiver, in part"* (¶11). No es una prórroga. La Oficina dice que no necesita conceder ni denegar la prórroga de 24 meses solicitada (¶19). El hito final de 2029 se mantiene (¶11-13). → ¶11-13, 19-24.

**[DATO REAL]** Condición de prioridad de espectro: desde el 30/07/2026, los satélites Gen1 no desplegados pierden temporalmente la prioridad de "earlier-round system" en la ronda Ka/Ku de 2020 y en la ronda de banda V de 2021. La pérdida dura **hasta el 30/03/2028** (20 meses) o hasta alcanzar el 50% operativo, lo que ocurra primero. Se reduce a **15 meses (30/10/2027)** si Amazon certifica que construyó los satélites del 50% y contrató lanzamientos suficientes. → ¶15, 22-23.

**[DATO REAL]** Si falla el hito de 2029, la autorización se reduce al número de satélites operativos a esa fecha. → ¶12.

**[DATO REAL]** **La fianza (surety bond) no se exime.** Si no alcanza el 50% el 30/07/2026 pierde la fianza según 47 CFR 25.165(d). Amazon no la había pedido y la Oficina decidió no concederla de oficio. → ¶18.
*Esto no estaba en el registro y es relevante para costos y riesgos.*

**[DATO REAL]** En la solicitud (30/01/2026) Amazon declaró **180 satélites lanzados** y proyectó **~700 desplegados al 30/07/2026** (~21% del total). → ¶8. La orden no dice cuántos había en órbita al 05/06/2026.

**Correcciones al registro:**
- La contradicción "1.618 sat. al 30/07/2027" de un agregador queda **descartada**: el primario dice **1.616 al 30/07/2026**. Algunos medios escriben 1.618; el número oficial es 1.616.
- El registro dice "penalidad de espectro Ka/Ku". El primario nombra Ka/Ku (ronda 2020) **y banda V (ronda 2021)**.

**[INFERENCIA DEL GRUPO]** La distancia entre lo proyectado (~700) y lo real (~396-398 en noviembre, antes de perder 40) es un dato de gestión central: mide el desvío de cronograma contra el plan que el propio Amazon presentó a la FCC.
→ Base: DA 26-553 ¶8 + Spaceflight Now. Supuestos: (a) la proyección de ~700 corresponde a satélites en órbita y operativos; (b) el conteo de ~396 es el correcto a la fecha.

**Sin verificar:** si Amazon presentó la certificación de 15 meses; qué dijo la FCC tras el 30/07/2026 (la orden es anterior).

---

## 3. FCC DA 24-224 — modificación 2024 (fila #7)

Documento primario leído (PDF descargado y convertido con `pdftotext`): https://docs.fcc.gov/public/attachments/DA-24-224A1.pdf (consultado 16/11/2026).

**[DATO REAL]** *Order and Authorization*, Space Bureau, **adoptada y publicada el 08/03/2024**. Archivos ICFS SAT-MOD-20230228-00043 y SAT-AMD-20230613-00140. La modificación **reduce la constelación de 3.236 a 3.232 satélites** y modifica los parámetros orbitales. → ¶1.

**[DATO REAL]** Distribución propuesta por Kuiper (→ ¶4):

| Altitud | Inclinación | Satélites | Planos |
|---|---|---|---|
| 590 km | 33° | 782 | 782 (1 por plano) |
| 590 km | 30° | 2 | 1 (2 por plano) |
| 610 km | 42° | 1.292 | 1.292 (1 por plano) |
| 630 km | 51,9° | 1.156 | 289 (4 por plano) |
| **Total** | | **3.232** | |

La suma da 3.232 (verificado). Kuiper no pidió cambiar las altitudes ni las frecuencias autorizadas.

**[DATO REAL]** Condición: no puede desplegar ningún satélite directamente a su altitud operativa (¶43). → Es una restricción de gestión de lanzamientos y operaciones.

**[DATO REAL]** El ¶52(b) restablece los hitos: 50% antes del 30/07/2026 y el resto antes del **"July 20, 2029"**. DA 26-553 y los demás documentos dicen **30/07/2029**.

**Discrepancia a anotar:** la fecha "20 de julio" del texto de DA 24-224 parece un error de redacción de la FCC. El hito vigente según DA 26-553 es el 30/07/2029. El equipo debe usar 30/07/2029 y dejar una nota al pie.

**[DATO REAL]** El ¶53 fija que antes del 14/08/2026 Kuiper debía demostrar el cumplimiento del hito o avisar por escrito que no se cumplió. → Pendiente: buscar si Amazon presentó ese aviso.

**Sin verificar:** la cita "39 FCC Rcd 2180" que aparece en búsquedas no está en el texto leído; confirmar antes de usarla.

---

## 4. FCC 2020, autorización original (fila #6)

**[DATO REAL]** El número oficial es **FCC 20-102**, *Order and Authorization*, citada como **35 FCC Rcd 8324**. Adoptada el 29/07/2020, publicada el 30/07/2020. Archivo SAT-LOA-20190704-00057, indicativo S3051. Hay una *Erratum* publicada.
→ Cita 35 FCC Rcd 8324 confirmada en el texto de DA 24-224 (nota 4). El número FCC 20-102 y la fe de erratas figuran en la página de documento de la FCC (https://www.fcc.gov/document/fcc-authorizes-kuiper-satellite-constellation), que dio 403 al leerla; se obtuvo por resultados de búsqueda.

**[DATO REAL]** 3.236 satélites en 98 planos orbitales, a 590, 610 y 630 km; cinco fases; el servicio comienza al lanzar los primeros 578 satélites.
→ Reproducción parcial de TelecomTV (https://www.telecomtv.com/content/industry-announcements/fcc-authorizes-kuiper-satellite-constellation-full-fcc-document-39345), que se corta antes de la sección de hitos. **No es el original.**

**Sin verificar en el original:** los hitos de 2020 (50% al 30/07/2026 y 100% al 30/07/2029). Quedan confirmados *indirectamente* porque DA 24-224 ¶52(b) y DA 26-553 ¶3 los restablecen con esos números. Para citar el original, abrir el PDF en fcc.gov desde un navegador (o desde fcc.report, que también lo aloja).

---

## 5. SEC "Form 425 FY2026" (fila #5)

Documento leído: https://www.sec.gov/Archives/edgar/data/1018724/000110465926042891/tm2611746d2_ex99-1.htm (consultado 16/11/2026).

**La fila #5 del registro está mal descripta.** No es un documento financiero anual ni trimestral.

**[DATO REAL]** Es el *Exhibit 99.1*, un comunicado de prensa del **14/04/2026**, de Amazon.com, Inc. y Globalstar, Inc., que anuncia (a) un **acuerdo definitivo por el que Amazon adquirirá Globalstar** y (b) un acuerdo con **Apple** para que Amazon Leo dé servicio satelital a iPhone y Apple Watch.

**[DATO REAL]** Lo que dice sobre Leo:
- Constelación inicial de **"more than 3,000 satellites"**, "designed, built, and operated in-house".
- Menciona la inversión solo como *"multibillion-dollar investment"*: **no da ninguna cifra en USD**.
- Un sistema direct-to-device propio de nueva generación **a partir de 2028**.
- Cierre de la adquisición previsto para **2027**, sujeto a aprobaciones regulatorias y a hitos de satélites de reemplazo de Globalstar.
- No habla de lanzamientos ni del número de satélites lanzados.
- Las únicas cifras en USD son de la compra de Globalstar ($90 por acción en efectivo, o 0,3210 acciones de Amazon; ajuste a la baja de hasta $110 millones por hitos).

**[INFERENCIA DEL GRUPO]** Esto agrega un actor y una línea de negocio que el registro no tenía: la adquisición de Globalstar y la alianza con Apple amplían el alcance de Leo hacia direct-to-device. Es material para el mapa de actores (I-2).
→ Base: fila #5. Supuesto: el acuerdo sigue vigente a la fecha, sin verificar.

**Consecuencia:** la inversión total de Amazon en Leo sigue **sin fuente oficial**. Esta fila no la resuelve. Hay que buscar el 10-K / 10-Q, que es otro documento.

---

## 6. Cambios propuestos al registro (para que el equipo apruebe)

| Qué | Cambio |
|---|---|
| #3 | "Publicado" → 09/11/2026 (actualizada 14/11/2026). Agregar nota: no refleja la falla. |
| #5 | Reescribir la descripción: comunicado del 14/04/2026 sobre Globalstar/Apple, no resultados financieros. Quitar "FY2026" y "verificar qué dice sobre inversión". |
| #6 | Completar con FCC 20-102, 35 FCC Rcd 8324, 30/07/2020. Marcar que falta leer el original. |
| #7 | Completar con la distribución por órbita y ¶ citados. Anotar la discrepancia "July 20, 2029". |
| #8 | Agregar el detalle de la fianza, la banda V, las fechas 30/03/2028 y 30/10/2027, y los ~700 proyectados. |
| Contradicciones | Cerrar "1.618 al 30/07/2027" (queda 1.616 al 30/07/2026). Cerrar "3.236 → 3.232" (confirmado). Agregar la discrepancia 20 vs 30 de julio de 2029. |
| Vacíos | "Inversión total": sigue abierto. "Retorno al vuelo de Vulcan": sigue abierto. Agregar: aviso de cumplimiento del hito (14/08/2026) y respuesta de la FCC. |

## 7. Pendientes que necesitan a una persona

- Abrir desde un navegador el PDF original de FCC 20-102 (fcc.gov dio 403 a la lectura automática).
- Decidir qué hacer con el evento Vulcan en el análisis de riesgos. El registro ya lo marca como `[[PENDIENTE equipo]]`.
- Buscar el aviso del 14/08/2026 a la FCC y qué ocurrió con el hito del 30/07/2026.
- Buscar la inversión total en el 10-K / 10-Q de Amazon.
