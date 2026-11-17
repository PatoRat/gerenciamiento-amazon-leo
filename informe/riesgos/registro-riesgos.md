# Registro de Riesgos — Amazon Leo (Parte 1)

**Estado: revisado por el autor el 16/11/2026.** Fecha de corte y consulta: 16/11/2026.
Método y criterios de la Parte 0: `borrador-parte0.md` (aprobada por el autor).
**(autor)** = decidido y escrito por vos. **(borrador IA)** = redactado por Claude y aprobado o ajustado por vos en la revisión. `[[PENDIENTE]]` = dato que no es público o que falta decidir.
Declaración de uso de IA: ver `borrador-parte0.md`.

Escalas y umbrales aplicados: probabilidad e impacto de la cátedra; colores según ER: rojo ≥ 0,20 · amarillo 0,10–0,19 · verde 0,05–0,09 · azul < 0,05.

**Estructura final del registro:**
- **4 riesgos desarrollados:** R-04, R-02, R-03 y R-01.
- **3 riesgos en la lista de seguimiento de baja prioridad:** R-05, R-06 y R-07 (la cátedra prevé esta lista para los de severidad baja: se vigilan sin desarrollar una respuesta completa).
- **1 oportunidad desarrollada** (OP-1) y **1 solo mencionada** (OP-2).

---

## Condensación de la lista (borrador IA)

La lista preliminar tenía 12 amenazas y 3 oportunidades. Se condensó fusionando los que comparten causa y evento:

| Nueva ID | Qué incluye | Fusiona |
|---|---|---|
| R-01 | Pérdida de satélites por falla de un lanzador | R-01 original |
| R-02 | Lanzador clave en tierra, con manifiesto concentrado | R-02 + R-04 originales |
| R-03 | Desvío del cronograma de despliegue y de inicio del servicio | R-05 + R-09 originales |
| R-04 | No cumplir el hito FCC de 2029 | R-06 + R-07 originales |
| R-05 | Pérdida temporal de prioridad de espectro | R-08 original |
| R-06 | Dependencia de socios locales | R-10 original |
| R-07 | Aprobaciones regulatorias externas | R-11 + R-12 originales |
| OP-1 | Capacidad de lanzamiento ampliada y diversificada | OP-1 original |
| OP-2 | Demanda comercial (aerolíneas y direct-to-device) | OP-2 + OP-3 originales |

Se descartó el **R-03 original** (satélites fabricados sin lanzar): era una inferencia débil sin verificar. Queda mencionada como recurso en R-01.

**Cuentas que se usan en varias fichas** (todas `[INFERENCIA DEL GRUPO]`, con sus supuestos):
- **Lanzamientos restantes:** 24 Ariane 6 − 3 volados = 21; 13 Falcon 9 − 3 = 10; 9 Atlas V − 8 = 1; 38 Vulcan − 1 = 37; 24 New Glenn − 0 = 24. Total ≈ 93. Vulcan y New Glenn suman 61, o sea **≈ 66%** de lo que queda.
  → Base: #24, #3, #4, #23, #38, #2. Supuestos: los contratos siguen vigentes; los 9 Atlas V ya contratados incluyen los 8 volados (el protoflight de 2023 no está verificado); el manifiesto total incluye lanzamientos para satélites adicionales (≈ 800+, según #23), no solo para la primera generación, cuyo "bloque inicial" es de 80 lanzamientos.
- **Satélites que faltan para 2029:** 3.232 − 396 = 2.836.
  → Base: DA 26-553 ¶3; #2.
- **Ritmo observado:** 15 misiones entre el 28/04/2025 y el 15/11/2026 (≈ 18,6 meses) = **≈ 0,8 misiones por mes**.
  → Base: #2.
- **Horizonte hasta el hito final:** del 16/11/2026 al 30/07/2029 hay ≈ **32,5 meses**.

---

## R-04 — No cumplir el hito FCC de 2029

**Estado: revisado y cerrado por el autor el 16/11/2026.** Siguen pendientes los datos de costo que no son públicos (monto de la fianza, costo de ampliar la cadencia). El riesgo queda en rojo tras responder (ER residual 0,20), y así debe explicarse en la defensa.

| Campo | Contenido |
|---|---|
| **Categoría (RBS)** | Externo → Regulación (con efecto en Gestión → Cronograma) |
| **Tipo** | Amenaza |
| **Descripción** (aprobada por el autor) | Debido a que a ≈ 20 misiones por año Amazon desplegaría unos 2.000 de los 3.232 satélites antes del 30/07/2029, puede ocurrir que no alcance el hito final, lo que reduciría la autorización a los satélites operativos ese día y expondría la pérdida de la fianza. |
| **Etiqueta y base** | `[DATO REAL]`: hito final de 3.232 satélites al 30/07/2029; si falla, la autorización se reduce al número operativo (DA 26-553 ¶3, ¶12); el incumplimiento de un hito implica pérdida de la fianza (DA 24-224 ¶53, DA 26-553 ¶18). `[DATO REAL]`: Amazon planifica "20+ misiones" en el "año dos del despliegue" y dice haber estado en camino a 11 lanzamientos en el primer año (#23, 23/03/2026); el texto no fecha esos años (inferimos que el año uno empieza con KA-01, el 28/04/2025). `[INFERENCIA DEL GRUPO]`: con 20 misiones por año durante 32,5 meses ≈ 54 misiones × ≈ 30 satélites ≈ 1.600–1.700 satélites nuevos, más 396 actuales = ≈ 2.050 (≈ 63% de 3.232). Además, desde el 28/04/2026 hubo 6 misiones en ≈ 6,5 meses (≈ 11 por año), la mitad de lo planificado (#2). Supuestos: (a) se sostiene el ritmo planificado de 20 por año desde hoy, algo optimista dado R-02 y el ritmo observado; (b) ≈ 30 satélites por misión (rango 24–40, #2, #3); (c) la FCC no concede otro waiver. Para llegar a 3.232 hace falta ≈ 35 misiones por año. |
| **Objetivo afectado** | Alcance (principal) y costo (fianza). |
| **Probabilidad (P)** | **0,70** (valor aprobado por el autor). Para llegar a 3.232 satélites hacen falta ≈ 35 misiones por año; el plan de Amazon es de más de 20 en el año dos (brecha de ≈ 15) y el ritmo observado desde el 28/04/2026 es de ≈ 11 por año (brecha de ≈ 24) (#23, #2). No se sube a 0,90 porque quedan ≈ 32,5 meses para acelerar y Amazon declara capacidad de fábrica de hasta 30 satélites por semana, aunque dice que la limita según la disponibilidad de lanzadores (#23); y porque la FCC concedió un waiver parcial en 2026, aunque eso no garantiza que lo repita (DA 26-553 ¶11). (Redacción: borrador IA.) **Análisis cuantitativo (Parte 2, sección 2.9):** con la cadencia observada y con la del plan, la probabilidad de llegar a 3.232 antes del 30/07/2029 es ≈ 0%; por eso la incertidumbre de P no está en la cadencia sino en si la FCC concede otro alivio. Como P(no cumplir) ≈ 1, P ≈ P(sin nuevo alivio), y 0,70 equivale a suponer ≈ 30% de probabilidad de otro alivio `[PROPUESTA DE GESTIÓN]`; no hay dato que lo respalde. |
| **Impacto (C)** | **0,40** (valor aprobado por el autor). Quedar en ≈ 2.050 significaría perder ≈ 1.180 satélites autorizados (≈ 37%). En la escala de alcance de la cátedra, "inaceptable" = 0,40. Razón del autor: Amazon mantuvo el 100%. Precisión (borrador IA): Amazon dijo que cumpliría el 100% de los satélites para el 30/07/2029 y pidió un waiver en vez de resignar satélites autorizados (DA 26-553 ¶8, ¶11) `[DATO REAL]`. De ahí se infiere que no consideraría aceptable una constelación parcial `[INFERENCIA DEL GRUPO]`; no hay una declaración de Amazon que lo diga. |
| **ER y color** | 0,70 × 0,40 = **0,28 → Rojo.** |
| **Estrategia** | **Mitigar** (aprobada por el autor). Subir la cadencia (más lanzadores, más misiones por año) y preparar un pedido de waiver o prórroga, como Amazon hizo en 2026 (DA 26-553 ¶8). Se descartan evitar (implica resignar alcance, que Amazon dijo no aceptar), transferir (un hito regulatorio no se transfiere) y aceptar (con ER 0,28 la cátedra no la recomienda). |
| **Respuesta** | (Aprobadas por el autor) (1) Llevar la cadencia a ≥ 35 misiones por año. (2) Presentar a tiempo un nuevo pedido de extensión con evidencia de avance. (3) Reportar a la FCC la capacidad construida y los lanzamientos contratados. |
| **Propietario** | Chief Global Affairs and Legal Officer de Amazon (rol en #33). Propuesta del grupo, aprobada por el autor. |
| **Disparador** | La cadencia de los últimos 6 meses queda por debajo de la necesaria; nuevo atraso de un lanzador (R-02); la FCC cambia la política de hitos. |
| **Costo de la respuesta / reserva** | `[[PENDIENTE: monto de la fianza y costo de ampliar la cadencia; no públicos]]`. |
| **ER después de responder** (propuesta) | P 0,50 × C 0,40 = **0,20 → Rojo.** Sigue en rojo: la brecha de cadencia es grande y la mitigación no la cierra sola. |
| **Residual / secundario** | Residual: la brecha de cadencia. Secundario: acelerar (más misiones por año) aumenta el riesgo técnico (R-01) y presiona la fabricación. |
| **Apalancamiento** | No calculable: falta el costo. |

---

## R-02 — Lanzador clave en tierra, con manifiesto concentrado

**Estado: aprobado por el autor en la revisión del 16/11/2026.** Su exposición (0,20) está justo en el corte del rojo: si se baja P a 0,40 pasa a amarillo. Hay que poder defender P = 0,50.

| Campo | Contenido |
|---|---|
| **Categoría (RBS)** | Gestión → Proveedores y contratos (con efecto en Técnico → Lanzamiento) |
| **Tipo** | Amenaza |
| **Descripción** | Debido a que Vulcan y New Glenn concentran ≈ 66% de los lanzamientos que quedan por hacer, y a que Vulcan acaba de fallar y New Glenn todavía no voló para Leo, puede ocurrir que alguno o ambos queden fuera de servicio por seis meses o más, lo que frenaría la cadencia de despliegue y atrasaría los hitos. |
| **Etiqueta y base** | Riesgo `[PROPUESTA DE GESTIÓN]` apoyado en `[DATO REAL]`: Vulcan estuvo ~9 meses en tierra antes de LV-01 (#12) y falló el 15/11/2026 (#2, #11); New Glenn explotó en su plataforma de Cabo Cañaveral durante una prueba de encendido el 28/05/2026, con causa no determinada al momento de la nota (AP vía OPB, #47; confirmado por varios medios el 16/11/2026); Amazon tiene 38 Vulcan y 24 New Glenn contratados (#3, #23). El 66% es `[INFERENCIA DEL GRUPO]` (ver arriba). Además, `[DATO REAL]`: Amazon dice que ajustó sus metas semanales de producción para reflejar la disponibilidad de lanzadores (#23), es decir, el lanzamiento es el cuello de botella. |
| **Objetivo afectado** | Plazo. |
| **Probabilidad (P)** | **0,50.** Hay precedente de una parada de ~9 meses (#12), la causa de la falla actual no se conoce y New Glenn no tiene vuelos de Leo. |
| **Impacto (C)** | **0,40 (alto).** Seis meses fuera de servicio de ≈ 66% de la capacidad restante equivalen a ≈ 4 meses de cadencia total (6 × 0,66 ≈ 3,96), es decir ≈ 12% del horizonte de 32,5 meses hasta el hito final. La escala de plazo de la cátedra marca 10–20% como alto. Supone que el resto de los lanzadores no puede absorber el atraso. |
| **ER y color** | 0,50 × 0,40 = **0,20 → Rojo** (justo en el corte). |
| **Estrategia** | **Mitigar.** Reasignar misiones a los lanzadores disponibles (Ariane 6, Falcon 9) y negociar cupos adicionales; es lo que hace OP-1. |
| **Respuesta** | (1) Priorizar los lanzamientos de Ariane 6 y Falcon 9 mientras se investiga la falla. (2) Pedir a ULA y a Blue Origin fechas de retorno al vuelo. (3) Evaluar nuevos contratos de capacidad. |
| **Propietario** | Director/a de sistemas de lanzamiento de Amazon Leo (rol en #3). Propuesta del grupo, aprobada por el autor. |
| **Disparador** | ULA no informa fecha de retorno al vuelo a los 3 meses de la falla (umbral aprobado por el autor); New Glenn sigue sin volar; un segundo evento en cualquiera de los dos. |
| **Costo de la respuesta / reserva** | `[[PENDIENTE: no público]]`. Reserva de tiempo propuesta: del orden de 4 meses en el cronograma maestro (coordinar con el área de tiempos). |
| **ER después de responder** (propuesta) | P 0,50 × C 0,20 = **0,10 → Amarillo.** Se supone que Ariane 6 y Falcon 9 absorben parte del atraso (≈ 34% del manifiesto restante no depende de Vulcan ni de New Glenn). |
| **Residual / secundario** | Residual: sigue habiendo dependencia fuerte de Vulcan y New Glenn. Secundario: concentrar la cadencia en Ariane 6 y Falcon 9 los expone a sus propios incidentes y a cupos limitados. |
| **Apalancamiento** | No calculable: falta el costo de la respuesta. |

---

## R-03 — Desvío del cronograma de despliegue y de inicio del servicio

**Estado: aprobado por el autor en la revisión del 16/11/2026.**

| Campo | Contenido |
|---|---|
| **Categoría (RBS)** | Gestión → Cronograma |
| **Tipo** | Amenaza |
| **Descripción** | Debido a que Amazon lleva un ritmo de ≈ 0,8 misiones por mes, muy inferior al plan, y a que ya perdió 40 satélites, puede ocurrir que el inicio del servicio comercial se postergue otra vez más allá de fin de 2026, lo que retrasaría los ingresos y los acuerdos que dependen del servicio. |
| **Etiqueta y base** | Apoyado en `[DATO REAL]`: ~396 satélites contra ~700 proyectados al 30/07/2026 (DA 26-553 ¶8; #2); el inicio del servicio se fue corriendo (2024, 2025, 2026) y Amazon dice "later this year" el 09/11/2026 (#30, #26, #29, #3). Que las cuatro frases se refieran al mismo hito es `[INFERENCIA DEL GRUPO]` (supuesto). |
| **Objetivo afectado** | Plazo. |
| **Probabilidad (P)** | **0,70.** Quedan ≈ 6 semanas del año, no hay anuncio de lanzamiento comercial y se acaba de perder una misión de 40 satélites. |
| **Impacto (C)** | **0,20 (moderado).** Cada postergación previa fue de ≈ 1 año. Sobre un horizonte de ≈ 10 años (anuncio en 2019, hito final en 2029), 1 año es ≈ 10% del cronograma, en el límite entre moderado (5–10%) y alto (10–20%). Se elige moderado porque otra postergación podría ser menor a un año. |
| **ER y color** | 0,70 × 0,20 = **0,14 → Amarillo.** |
| **Estrategia** | **Mitigar.** Iniciar el servicio por regiones y con clientes empresariales mientras sigue el despliegue (hoy hay un "private preview", #35). |
| **Respuesta** | (1) Definir un criterio de inicio por región (satélites mínimos y cobertura). (2) Comunicar fechas con margen a los socios. (3) Reportar el avance contra el plan, no contra metas aspiracionales. |
| **Propietario** | VP de negocio y producto de Amazon Leo (rol en #24). Propuesta del grupo, aprobada por el autor. |
| **Disparador** | Llegar al 30/11/2026 sin anuncio de servicio; una nueva falla de lanzamiento; la cadencia mensual queda por debajo de lo planificado. |
| **Costo de la respuesta / reserva** | `[[PENDIENTE]]`. Reserva de tiempo propuesta: a coordinar con el área de tiempos. |
| **ER después de responder** (propuesta) | P 0,70 × C 0,10 = **0,07 → Verde.** El inicio parcial reduce el impacto de una demora total. |
| **Residual / secundario** | Residual: el servicio inicial tendría cobertura limitada. Secundario: lanzar con poca cobertura puede dañar la reputación del servicio. |

---

## R-01 — Pérdida de satélites por falla de un lanzador

**Estado: aprobado por el autor con una advertencia:** el impacto de 0,10 es el punto débil. Su costo unitario no es público; si en la defensa se discute, se sube C y se justifica con una estimación del costo de un satélite. Queda azul porque su daño de plazo se mide en R-02.

| Campo | Contenido |
|---|---|
| **Categoría (RBS)** | Técnico → Lanzamiento |
| **Tipo** | Amenaza |
| **Descripción** (borrador IA) | Debido a que la causa raíz de la falla del 15/11/2026 no es pública y que Vulcan tiene aún 37 lanzamientos contratados con Amazon, puede ocurrir una nueva falla en otra misión, lo que provocaría la pérdida de los satélites a bordo (unos 40 por misión) y obligaría a reponerlos. |
| **Etiqueta y base** | Riesgo `[PROPUESTA DE GESTIÓN]` apoyado en un `[DATO REAL]`: el 15/11/2026 el Vulcan falló unos 10 minutos tras el despegue y se perdieron 40 satélites; causa raíz no publicada (Spaceflight Now, #11; Amazon, #2). Los 37 restantes son un supuesto: que los 38 Vulcan contratados (#3) siguen vigentes. Al 16/11/2026, revisando varios medios, ULA no había publicado la causa raíz ni una fecha de retorno al vuelo. |
| **Objetivo afectado** | Costo (principal) y plazo (secundario). El plazo por paralización del cohete se trata en R-02. |
| **Probabilidad (P)** (autor) | **0,30 por misión Vulcan.** |
| **Justificación de P** (autor) | Se estima P = 0,30 porque la frecuencia observada es 0,20 (1 en 5 vuelos, #11), pero con una muestra tan chica de apenas cinco lanzamientos la tasa empírica es poco confiable, y al no haberse resuelto aún la causa raíz del incidente persiste una incertidumbre técnica que aumenta el riesgo de recurrencia hasta que se aplique una corrección. |
| **Impacto (C)** (borrador IA) | **0,10 (bajo).** |
| **Justificación de C** (borrador IA) | *Plazo:* 40 satélites son el 1,2% de los 3.232 de la constelación final (40 ÷ 3.232). Reponerlos equivale a ~1,3 semanas de la capacidad de fabricación declarada de 30 por semana (#23), contra un horizonte de ~140 semanas hasta el hito de 30/07/2029 (DA 26-553 ¶3). Es insignificante para la escala de plazo. *Costo:* el valor de cada satélite no es público `[[PENDIENTE: costo unitario]]`, así que no se puede expresar como % del costo del proyecto; se supone que cae en la franja "baja" (< 5%). *Límite:* esta ficha excluye a propósito el efecto de que el cohete quede en tierra, que es el mayor daño de plazo y se evalúa en R-02. |
| **Exposición (ER)** | 0,30 × 0,10 = **0,03** |
| **Color** | **Azul** (< 0,05). |
| **Estrategia** (borrador IA) | **Aceptar (activa).** La cátedra la indica cuando responder cuesta más que el daño, y hay un plan con disparadores, acciones y recursos. |
| **Respuesta** (borrador IA) | Plan de contingencia: si ocurre una falla, (1) reponer los 40 satélites desde el stock o la producción de Kirkland, (2) reasignar las misiones siguientes a otros lanzadores ya contratados (Ariane 6, Falcon 9, Atlas V), (3) pedir a ULA el resultado de la investigación y las acciones correctivas. |
| **Propietario** | Director/a de sistemas de lanzamiento de Amazon Leo (rol que aparece en #3). Propuesta del grupo, aprobada por el autor. |
| **Disparador / señal temprana** (borrador IA) | Un reporte de anomalía en un vuelo Vulcan; un hold sin explicar en la cuenta regresiva (como el de T-20 s del 15/11, #11); que ULA no publique la causa raíz antes del siguiente vuelo programado. |
| **Plan de contingencia** | Ver "Respuesta". Recursos: stock de satélites fabricados (inferencia sin verificar: 1.000 fabricados contra ≈ 396 lanzados, #3, #2) y capacidad declarada de Kirkland. |
| **Costo de la respuesta** | `[[PENDIENTE: no público; estimar con supuestos]]` |
| **ER después de responder** | `[[PENDIENTE]]`. La contingencia no reduce P ni C en sí misma; solo acorta la recuperación. |
| **Apalancamiento** | No calculable: falta el costo de las alternativas. Alternativas a comparar: (A) mitigar dividiendo la carga en lotes más chicos por misión, (B) transferir con seguro o cláusula de relanzamiento, (C) aceptar activamente con reserva de satélites. Dato de contexto: Vulcan llevaba 40 satélites, el lote más grande hasta la fecha (#3); Ariane 6 lleva 32–36 y Atlas V 27–29 (#2). `[[PENDIENTE]]` Si Amazon tiene seguro o relanzamiento contratado no se sabe. |
| **Reserva** | De contingencia (riesgo conocido), en **unidades**: reposición de 40 satélites. Monto en USD: `[[PENDIENTE]]`. |
| **Riesgo residual** | El cohete queda en tierra: se trata en R-02. |
| **Riesgo secundario** | Usar stock para reponer reduce la disponibilidad de satélites para otras misiones y puede generar un cuello de botella de fabricación. |
| **Justificación de la respuesta** (borrador IA) | Criterio de la cátedra: con ER azul (muy bajo) corresponde aceptar; la aceptación activa es preferible a la pasiva porque el riesgo ya se materializó una vez y hay disparadores concretos que vigilar (Clase 10: "Aceptación activa" y "Plan de contingencia"). |

---

## Lista de seguimiento de riesgos de baja prioridad

La cátedra prevé esta lista para los riesgos de severidad baja: se vigilan durante el proyecto sin desarrollar una respuesta completa (diapositivas de análisis cualitativo, `Proyectos_10 Riesgos_0100`). Si un disparador se activa, el riesgo se sube al registro y se desarrolla su respuesta. Los valores de P y C son propuestas con poca evidencia dura; la columna "Límite" lo dice.

| ID | Riesgo | Descripción (borrador IA) | P | C | ER | Color | Qué se vigila (disparador) | Límite de la evidencia |
|---|---|---|---|---|---|---|---|---|
| **R-05** | Pérdida temporal de prioridad de espectro | Debido a que Amazon no alcanzó 1.616 satélites operativos el 30/07/2026, sus satélites no desplegados pierden prioridad de espectro hasta el 30/03/2028 (DA 26-553 ¶15); puede ocurrir que en esa ventana un sistema con prioridad o una nueva ronda de procesamiento limite su espectro, lo que reduciría la capacidad o la calidad del servicio inicial. | 0,30 | 0,20 | 0,06 | Verde | La FCC abre una ronda de procesamiento; un operador pide límites de coordinación; se acerca el 30/10/2027 (fecha a la que se acorta la pérdida si Amazon certifica que construyó el 50% y contrató lanzamientos, DA 26-553 ¶15). | `[DATO REAL]` la condición está activa. Que el hito no se cumplió es `[INFERENCIA]` (≈ 396 satélites al 30/07/2026, sin lanzamientos entre el 02/07 y el 15/11 según #2). No hay evidencia de una ronda abierta ni de cuánto espectro está en juego. |
| **R-06** | Dependencia de socios locales | Debido a que el servicio llega al cliente a través de socios y distribuidores locales (Herotel #33, UZ-SAT #35, Vanu #32, DIRECTV LatAm y Sky Brasil #37, NBN Co #40), puede ocurrir que uno no pueda o no quiera lanzar el servicio en la fecha prevista, lo que demoraría los ingresos de esa región. | 0,50 | 0,10 | 0,05 | Verde | Un socio no confirma fecha; el servicio de Amazon se posterga (R-03). | Búsqueda del 16/11/2026: no se encontró confirmación de que NBN Co haya lanzado el servicio previsto "desde mediados de 2026"; una nota dice que el despliegue de Amazon sigue atrasado. El valor está justo en el corte con azul. |
| **R-07** | Aprobaciones regulatorias externas | Debido a que la compra de Globalstar (cierre previsto en 2027, #22) y las licencias por país requieren aprobaciones de reguladores, puede ocurrir que alguna se demore o se niegue, lo que retrasaría el servicio direct-to-device desde 2028 o el inicio del servicio en algún país. | 0,30 | 0,20 | 0,06 | Verde | Un regulador pide información adicional; la fecha de cierre de Globalstar se corre. | Sin datos del estado de Globalstar ni de las licencias por país (`NO VERIFICADO`); solo se vio la solicitud de Kenia por prensa (#18). |

Propietarios propuestos si se activan: R-05 Chief Global Affairs and Legal Officer (#33); R-06 Global head of business de Amazon Leo (#35); R-07 VP de política pública (#27). Son roles propuestos por el grupo, no datos de Amazon.

---

## Oportunidades

La cátedra reconoce que el riesgo "puede ser una oportunidad", pero el material leído **no desarrolla estrategias específicas para oportunidades** (solo las cuatro para amenazas). Para OP-1 se propone "aprovechar", un criterio **externo a la cátedra**. El beneficio se mide con la misma escala y la ER queda en positivo.

### OP-1 — Capacidad de lanzamiento ampliada y diversificada

**Estado: aprobada por el autor en la revisión del 16/11/2026.**

| Campo | Contenido |
|---|---|
| **Descripción** | Debido a que Amazon sumó 6 lanzamientos Ariane 6 y 10 Falcon 9, puede ocurrir que esa capacidad adicional permita sostener la cadencia aunque Vulcan o New Glenn estén en tierra, lo que reduciría el atraso del cronograma. |
| **Base** | `[DATO REAL]`: Ariane 6 de 18 a 24 (#24, 10/09/2026); 10 Falcon 9 adicionales "a fines del año pasado", según una nota de 23/03/2026 (#23); Ariane 6 entregó 100 satélites en tres misiones en menos de cinco meses (#24). `[INFERENCIA DEL GRUPO]`: ≈ 34% del manifiesto restante no depende de Vulcan ni de New Glenn. |
| **P / beneficio** | P **0,70** (contratos firmados y Ariane 6 ya con vuelos) × beneficio **0,20** = **+0,14**. |
| **Estrategia / respuesta** | **Aprovechar** (criterio externo a la cátedra): priorizar la cadencia de Ariane 6 y Falcon 9 y asegurar cupos. |
| **Propietario / disparador** | Director/a de sistemas de lanzamiento (#3). Disparador: una parada de Vulcan o New Glenn. |
| **Relación** | Es la respuesta de mitigación de R-02. |

### OP-2 — Demanda comercial (solo mencionada)

Se menciona pero **no se desarrolla**: no hay datos de ingresos y depende de que el servicio inicie (R-03). `[DATO REAL]`: acuerdos con JetBlue (desde 2027, #36), Delta (desde 2028, 500 aviones, #31) y Apple y Globalstar para direct-to-device desde 2028 (#22). Si el equipo la quiere desarrollar, necesita una estimación de ingresos con supuestos.

---

## Resumen de exposición (antes de responder)

| Orden | ID | Riesgo | P | C | ER | Color | Tratamiento |
|---|---|---|---|---|---|---|---|
| 1 | R-04 | Hito FCC de 2029 | 0,70 | 0,40 | 0,28 | Rojo | Desarrollado |
| 2 | R-02 | Lanzador clave en tierra | 0,50 | 0,40 | 0,20 | Rojo | Desarrollado |
| 3 | R-03 | Desvío de cronograma y servicio | 0,70 | 0,20 | 0,14 | Amarillo | Desarrollado |
| 4 | R-05 | Prioridad de espectro | 0,30 | 0,20 | 0,06 | Verde | Seguimiento |
| 4 | R-07 | Aprobaciones regulatorias | 0,30 | 0,20 | 0,06 | Verde | Seguimiento |
| 6 | R-06 | Socios locales | 0,50 | 0,10 | 0,05 | Verde | Seguimiento |
| 7 | R-01 | Falla de un lanzador | 0,30 | 0,10 | 0,03 | Azul | Desarrollado |
| — | OP-1 | Capacidad de lanzamiento | 0,70 | +0,20 | +0,14 | Oportunidad | Desarrollada |
| — | OP-2 | Demanda comercial | — | — | — | Oportunidad | Solo mencionada |

**Lectura:** los dos rojos (R-04 y R-02) concentran el riesgo en el **plazo**, que es el objetivo que se eligió proteger. R-01 queda azul porque su daño de plazo se mide en R-02. R-02, R-03 y R-04 forman una cadena: un lanzador en tierra frena la cadencia, eso retrasa el servicio y, si se prolonga, compromete el hito de 2029.

**Coherencia a cuidar con otras áreas:** las reservas de tiempo de R-02, R-03 y R-04 deben coincidir con el cronograma del área de tiempos; las de costo (fianza, respuestas) con el presupuesto del área de costos. Todos los `[[PENDIENTE]]` de costo son datos no públicos que habrá que estimar con supuestos escritos.
