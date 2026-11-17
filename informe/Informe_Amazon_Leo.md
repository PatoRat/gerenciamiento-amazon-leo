# Amazon Leo — Informe de investigación

**Trabajo Integrador de Investigación · Dirección de Proyectos 2026 · Facultad de Ingeniería y Ciencias Agrarias (UCA)**
Fecha de corte de la evidencia: 16/11/2026 · Versión del 17/11/2026

---

# Resumen ejecutivo

Amazon Leo (antes Project Kuiper) es el programa de Amazon para desplegar una constelación de banda ancha en órbita baja. La FCC autorizó 3.232 satélites, con dos hitos: 1.616 operativos al 30/07/2026 y 3.232 al 30/07/2029. Amazon anunció en 2020 una inversión de más de USD 10.000 millones (#39).

**Estado al 16/11/2026.** Hay ≈ 396 satélites desplegados (12,3% del total) en 15 misiones, una de ellas fallida: el 15/11/2026 la misión LV-01 de Vulcan perdió 40 satélites. El hito del 50% no se cumplió y la FCC concedió solo un waiver parcial. El servicio comercial todavía no empezó.

**Qué reconstruyó el equipo.** Caso de negocio, acta de constitución, alcance y WBS, cronograma maestro, estimaciones PERT, estructura de costos, registro de riesgos con Monte Carlo y valor ganado medido en satélites, todo con el marco de la cátedra y con trazabilidad de cada dato.

**Principales conclusiones.**

1. El **cuello de botella es el lanzamiento**: la fábrica produce mucho más de lo que se lanza.
2. **El hito de 2029 no es alcanzable** con la capacidad contratada. El Monte Carlo da ≈ 0%, PERT ≈ 0,07% y el valor ganado un SPI de 0,22 a 0,57. El fin razonable está entre 2031 y 2038.
3. El **riesgo principal es regulatorio**: que la FCC no conceda un nuevo alivio. La respuesta propuesta es una línea base de recuperación (≈ 08/2031) más el pedido de alivio y más capacidad de lanzamiento.
4. Faltó un **criterio verificable de inicio del servicio**: el inicio se corrió unos 2 años sin incumplir un hito formal.
5. El **alcance crece** (Gen2, direct-to-device, Globalstar) antes de terminar Gen1. Conviene separar sus casos de negocio.

**Límite principal.** Amazon no publica costos: no se calcula el CPI ni se inventan montos.

---

# 1. Introducción y método

## 1.1 Qué se investigó

Este informe investiga **Amazon Leo** (hasta el 13/11/2025, *Project Kuiper*), el programa de Amazon para desplegar una constelación de satélites en órbita baja que da conectividad de banda ancha. El objetivo no es describir el proyecto, sino **reconstruir cómo podría organizarse su gestión** y sostener esas decisiones con evidencia, como pide la consigna del Trabajo Integrador.

Siguiendo la orientación de la cátedra para este proyecto, el hilo del informe es **cómo se organiza el despliegue, qué hitos públicos existen, qué infraestructura debe estar disponible y cómo se conectan fabricación, lanzamientos y operación**.

## 1.2 Método

Se siguieron los cinco pasos de la consigna:

| Paso | Qué se hizo | Dónde está |
|---|---|---|
| 1. Ubicar | Historia, impulsores y estado al corte | Sección 2 |
| 2. Buscar evidencia | 47 fuentes evaluadas, con prioridad para las primarias (Amazon, FCC, SEC, ULA); verificación de las órdenes FCC en su texto original | Sección 3, Anexos A y F |
| 3. Reconstruir | Caso de negocio, acta, alcance y WBS, cronograma, estimaciones, costos, riesgos y seguimiento, con el marco de la cátedra | Secciones 5 a 12 |
| 4. Conectar | Cifras maestras únicas y mapa de coherencia entre secciones | Sección 13, Anexo D |
| 5. Defender | Dashboard para la defensa oral y guion de preguntas probables | Dashboard |

**Marco teórico:** el de la cátedra (Clases 1 a 6, Paneo rápido, plantillas de acta y caso de negocio). Se usan sus denominaciones (Acta de Constitución, WBS, Registro de Riesgos, Exposición al Riesgo, Valor Ganado). Cuando se usa un criterio externo, se aclara.

## 1.3 Reglas de trazabilidad

Cada afirmación sustantiva lleva una etiqueta:

- `[DATO REAL]`: información de una fuente verificable. Se cita con `#n` del registro de fuentes (Anexo A), que incluye URL, fecha de publicación y fecha de consulta.
- `[INFERENCIA DEL GRUPO]`: conclusión razonable a partir de la evidencia, con sus **supuestos escritos**.
- `[PROPUESTA DE GESTIÓN]`: documento, estimación o decisión creada por el grupo para reconstruir la gestión, con su justificación.

Lo que no es público **no se inventa**: queda marcado como «No público» o como límite del análisis.

## 1.4 Convenciones

- **Fecha de corte:** 16/11/2026. Hechos posteriores no se incorporan.
- **Unidad de avance:** satélites **lanzados** como aproximación de satélites **operativos**. La FCC mide operativos y Amazon publica lanzados, así que los resultados son optimistas para Amazon.
- **Números:** todos salen de las cifras maestras (Anexo D). Si un número no está ahí, no está en el informe.
- **Monedas y unidades:** explícitas (USD, satélites, misiones/mes).

## 1.5 Declaración de uso de herramientas de IA

La cátedra habilitó el uso de IA para la redacción (confirmado por el equipo el 16/11/2026). Se usó Claude (Anthropic) para buscar y verificar fuentes, ordenar la evidencia, proponer la estructura, programar los cálculos (Monte Carlo y valor ganado), redactar borradores de las secciones y construir el dashboard. Las decisiones de gestión (objetivo prioritario, alcance, línea base, probabilidades e impactos, respuestas, KPIs) las revisó, ajustó y aprobó el equipo, que es quien las defiende. Todas las fuentes se citan para que cualquiera pueda comprobarlas; lo que no se pudo verificar está señalado.

## 1.6 Limitaciones generales

- Amazon es una empresa privada y no publica su cronograma, su WBS ni su presupuesto. Casi toda la información de la empresa es **declaración propia**.
- Algunas fuentes no pudieron leerse por bloqueo o paywall (SpaceNews, fcc.gov en lectura automática, entre otras; ver Anexo A).
- El proyecto está en curso: la falla de la misión LV-01 ocurrió un día antes de la fecha de corte.

---

# 2. Ubicación del proyecto

> Fuentes: Anexo A; cronología completa: Anexo B.

## 2.1 Qué problema u oportunidad aborda

**[DATO REAL]** Amazon presentó el proyecto en 2020 como un servicio de "reliable, affordable broadband service to unserved and underserved communities around the world" y anunció que invertiría "more than $10 billion" (#39, 30/07/2020). En 2025 lo describe como "fast, reliable internet to customers and communities beyond the reach of existing networks" y afirma que "there are billions of people on the planet who lack high-speed internet access" (#28, 04/11/2025).

**[DATO REAL]** El sistema combina tres segmentos: satélites en órbita baja; red terrestre de gateways, antenas de telemetría y fibra dedicada hacia Internet, la nube o redes privadas (#22, #28); y terminales de usuario (Nano hasta 100 Mbps, Pro hasta 400 Mbps, Ultra hasta 1 Gbps, #29, #30).

**[INFERENCIA DEL GRUPO]** La oportunidad tiene dos caras: una social (conectividad donde no llega la red terrestre) y una comercial (aerolíneas, empresas, operadores móviles y servicio *direct-to-device* para teléfonos). Los acuerdos firmados entre 2024 y 2026 se concentran en la segunda (JetBlue, Delta, Apple, DIRECTV, NBN Co, Herotel, Vanu, UZ-SAT; #31, #36, #22, #37, #40, #33, #32, #35).
→ Supuesto: los acuerdos anunciados reflejan las prioridades comerciales del programa.

## 2.2 Quién lo impulsa

**[DATO REAL]** Amazon Leo es un negocio de Amazon dentro de Devices & Services, con I+D en Redmond y producción en Kirkland (Washington) (#28). Lo dirige Rajeev Badyal, "Vice President of Amazon Leo" (#21). En 2020 el anuncio lo hizo Dave Limp, Senior Vice President de Amazon (#39), y en 2026 el acuerdo con Globalstar y Apple lo encabezó Panos Panay, SVP de Devices & Services (#22).

**[DATO REAL]** La FCC es el actor externo que fija las reglas del despliegue: autorizó 3.236 satélites en 2020 (#6), los redujo a 3.232 en 2024 (#7) y en 2026 concedió un waiver parcial del hito intermedio (#8).

**[DATO REAL]** Cuatro proveedores de lanzamiento comparten el manifiesto: ULA (Atlas V y Vulcan), Arianespace (Ariane 6), Blue Origin (New Glenn) y SpaceX (Falcon 9) (Anexo A, "Cifras de contratos"). Blue Origin fue fundada por Jeff Bezos y es una empresa separada de Amazon (#28).

## 2.3 Cómo llegó hasta acá

| Etapa | Período | Qué pasó | Fuente |
|---|---|---|---|
| Anuncio y autorización | 2019–2020 | Se conoce por presentaciones federales (3.236 satélites). La FCC autoriza el 30/07/2020. Compromiso de > USD 10.000 millones. | #42, #6, #39 |
| Preparación industrial | 2022–2024 | Contratos de lanzamiento "más grandes de la historia comercial" (hasta 83, 2022); fábrica de Kirkland (abre en 04/2024); terminales presentados (2023). | #4, #25, #26, #30 |
| Ajuste regulatorio | 2023–2024 | Plan de desechos orbitales aprobado (2023); constelación modificada a 3.232 (2024). | #44, #7 |
| Despliegue inicial | 04/2025 → | Primera misión de producción KA-01 (28/04/2025); 14 misiones con despliegue hasta el 02/07/2026; ≈ 396 satélites. | #2 |
| Rebrand y preview | 11/2025 | Project Kuiper pasa a llamarse Amazon Leo (13/11/2025); preview empresarial (24/11/2025). | #21, #29 |
| Atraso regulatorio | 2026 | Amazon pide prórroga o waiver (30/01/2026); la FCC concede un waiver **parcial** (05/06/2026). El hito de 1.616 satélites al 30/07/2026 no se alcanza. | #8 |
| Expansión del negocio | 2026 | Acuerdo para comprar Globalstar y alianza con Apple (14/04/2026); D2D desde 2028; más lanzamientos (Ariane 6 de 18 a 24). | #22, #5, #34, #24 |
| Falla | 15/11/2026 | La misión LV-01 (Vulcan, 40 satélites) falla ≈ 10 minutos después del despegue. | #2, #11 |

## 2.4 Estado al 16/11/2026

| Indicador | Valor | Etiqueta |
|---|---|---|
| Satélites desplegados | ≈ 396 de 3.232 (12,3%) | `[INFERENCIA DEL GRUPO]` (suma de #2) |
| Hito del 50% (1.616 al 30/07/2026) | No cumplido (24,5%) | `[INFERENCIA DEL GRUPO]` sobre #8 |
| Hito final | 3.232 al 30/07/2029 | `[DATO REAL]` #8 |
| Misiones | 15 (14 con despliegue y 1 fallida) | `[DATO REAL]` #2, #11 |
| Satélites fabricados | 1.000 (inicios de 09/2026) | `[DATO REAL]` #3 |
| Servicio comercial | No lanzado; previews empresariales | `[DATO REAL]` #3, #29, #35 |
| Próxima misión | LE-04 (Ariane 64, 36 satélites), no antes del 23/11/2026 | `[DATO REAL]` #2 |

**[INFERENCIA DEL GRUPO] Lectura del estado.** El proyecto tiene la capacidad industrial instalada (fábrica, procesamiento en Florida, más de 100 lanzamientos contratados) pero **no logra convertirla en satélites en órbita al ritmo que exige el regulador**. El cuello de botella es el lanzamiento, y la falla del 15/11/2026 lo agravó. A la vez, Amazon amplía el alcance del programa (Gen2, D2D, Globalstar) antes de terminar la primera generación.
→ Base: secciones 7, 8 y 12; #23, #3, #2, #8. Supuestos: los del Anexo D.

---

# 3. Evidencia y fuentes

> El registro completo está en el Anexo A (`evidencia/registro-fuentes.md`) y la verificación contra los documentos primarios en el Anexo F.

## 3.1 Qué se usó

**[DATO REAL]** El registro reúne **47 fuentes**, consultadas entre el 15 y el 16/11/2026:

| Tipo | Ejemplos | Uso |
|---|---|---|
| Oficial de Amazon (≈ 30) | Comunicados de aboutamazon.com, página *Mission updates* | Hechos de la empresa (son **declaraciones propias**) |
| Regulatoria primaria | FCC 20-102 (2020), DA 24-224 (2024), DA 26-553 (2026); SEC Form 425 (2026) | Hitos, obligaciones, sanciones |
| Técnica / proveedor | ULA, Spaceflight Now | Lanzamientos y fallas |
| Prensa especializada y general | SpaceNews, Via Satellite, CNBC, DCD, AP | Para ubicar hechos y confirmar; nunca como única fuente de un dato duro |
| Índices (Wikipedia) | Lista de lanzamientos | Solo para navegar; **no se citan** |

## 3.2 Cómo se evaluó

- **Prioridad:** primero las fuentes primarias. Las órdenes DA 24-224 y DA 26-553 de la FCC **se leyeron completas** (Anexo F).
- **Contradicciones:** se registraron como hallazgo y no se promediaron. Ejemplos: fecha final del hito (20 contra 30/07/2029), contratos de New Glenn (12 en 2022 contra 24 en 2026), capacidad de fábrica contra ritmo real.
- **Correcciones:** la fila #5 se había catalogado como informe financiero y resultó ser el comunicado de compra de Globalstar; se corrigió.
- **Fechas de corte:** las cifras que cambian (contratos, satélites) se citan siempre con fecha.

## 3.3 Qué no es público (y cómo se trató)

| Dato | Tratamiento |
|---|---|
| Inversión total actualizada | Se usa el compromiso inicial verificado (> USD 10.000 millones, #39) como piso declarado en 2020 |
| Costo por satélite y por lanzamiento, monto de la fianza | No público; estructura de costos sin montos inventados (sección 10) |
| Cronograma interno, WBS, presupuesto | Se **reconstruyen** como propuesta de gestión (secciones 6 a 10) |
| Satélites operativos | Se usan lanzados como aproximación (sección 1.4) |
| Causa raíz de la falla de LV-01 | No publicada al corte; se registra como tema abierto (sección 11) |

**[INFERENCIA DEL GRUPO]** Lo que no es público define el trabajo: la parte "investigable" (hitos, contratos, regulación) es sólida; la parte económica es débil y obliga a reconstruir con supuestos. Por eso el informe pone el peso en **plazo y alcance**, que son medibles con evidencia, más que en costo.

---

# 4. Actores e interesados

> Detalle con fuentes: Anexo C (`evidencia/actores.md`).

## 4.1 Mapa de actores

| Grupo | Actores | Rol | Fuente |
|---|---|---|---|
| Patrocinio y dirección | Amazon (Devices & Services); VP de Amazon Leo (R. Badyal); SVP de Devices & Services (P. Panay) | Financia, dirige y decide | #21, #22, #28 |
| Equipo del proyecto (roles visibles) | Negocio y producto (C. Weber); sistemas de lanzamiento (M. Wuerl); operaciones de producción (S. Metayer); asuntos legales y regulatorios (D. Zapolsky); política pública (B. Huseman) | Gestionan cada frente | #24, #3, #27, #33 |
| Regulador | FCC (Space Bureau); reguladores nacionales (Kenia y otros) | Autoriza, fija hitos y sanciones | #6, #7, #8, #18 |
| Proveedores de lanzamiento | ULA, Arianespace, Blue Origin, SpaceX | Ejecutan el cuello de botella | Anexo A, "Cifras de contratos" |
| Proveedores industriales | Beyond Gravity (dispensadores) | Integración de carga | #4 |
| Infraestructura pública | NASA, Space Force, Space Florida | Sitios y coordinación de lanzamiento | #27, #23 |
| Clientes y socios | JetBlue, Delta, Apple, DIRECTV LatAm/Sky Brasil, NBN Co, Herotel, Vanu, UZ-SAT; Globalstar (adquisición) | Demanda y distribución | #36, #31, #22, #37, #40, #33, #32, #35, #5 |
| Competidores | SpaceX (Starlink), OneWeb, Telesat | Se opusieron ante la FCC en 2019 | #45 |

**[INFERENCIA DEL GRUPO]** SpaceX es a la vez **competidor y proveedor**: se opuso a Amazon ante la FCC en 2019 (#45) y hoy le vende lanzamientos (#38, #23). Supuesto: no hay acuerdos públicos que reconcilien ambas posiciones.

## 4.2 Poder e interés (propuesta de gestión)

`[PROPUESTA DE GESTIÓN]` Clasificación de los interesados por poder sobre el proyecto e interés en su resultado, para decidir cómo gestionarlos. Criterio externo a la cátedra (matriz poder/interés), usado como complemento.

| | Interés alto | Interés bajo |
|---|---|---|
| **Poder alto** | **Gestionar de cerca:** FCC; ULA y Blue Origin (66% del manifiesto restante); dirección de Amazon | **Mantener satisfechos:** reguladores nacionales; NASA y Space Force |
| **Poder bajo** | **Mantener informados:** socios de distribución (NBN Co, Herotel, DIRECTV); aerolíneas; Apple | **Monitorear:** competidores; prensa |

→ Justificación: el poder sale de la evidencia. La FCC puede reducir la autorización (#8 ¶12) y los lanzadores definen la cadencia (Riesgos, R-02). Los socios dependen del inicio del servicio (R-06).

## 4.3 Plan de comunicaciones básico (propuesta de gestión)

`[PROPUESTA DE GESTIÓN]` Usa los instrumentos de seguimiento de la Clase 6 (informe de situación, reuniones de avance con proveedores y dirección).

| Interesado | Qué necesita saber | Instrumento | Frecuencia | Responsable (rol) |
|---|---|---|---|---|
| FCC | Avance contra hitos; certificación del 50% construido; pedidos de alivio | Reportes formales; aviso de cumplimiento (#7 ¶53) | Por hito y semestral | Legal y regulatorio |
| Lanzadores | Manifiesto, disponibilidad de satélites, fechas de retorno al vuelo | Reunión de avance con proveedores | Mensual y por misión | Sistemas de lanzamiento |
| Dirección de Amazon | EV, SPI, riesgos rojos, temas abiertos | Informe de situación | Mensual | VP de Amazon Leo |
| Socios de distribución | Fecha y criterio de inicio del servicio por región | Comunicación con margen (R-03) | Trimestral | Negocio y producto |
| Equipo interno | Avance, problemas, log de temas | Reunión de equipo (Clase 6: semanal, 30–60 min) | Semanal | Gerente del proyecto |

**[INFERENCIA DEL GRUPO]** La serie de promesas de inicio del servicio que se fueron corriendo (Anexo B, §5) muestra un problema de **gestión de expectativas**: la Clase 2 advierte que "un proyecto puede estar excelentemente administrado y fracasar si no cumple las expectativas iniciales" y señala la "sobreventa de beneficios" como causa de distorsión. Por eso el plan propone comunicar fechas con margen y un criterio de inicio verificable.

---

# 5. Caso de negocio (reconstruido)

> Estructura: `catedra/PMOInformatica Plantilla Caso de Negocio.pdf`. Marco: Paneo, tema 2 (el Business Case juzga si el proyecto es deseable, viable y alcanzable, y se actualiza en todo el ciclo de vida).

**Proyecto:** Despliegue de la constelación Amazon Leo, primera generación (antes Project Kuiper) · **Organización:** Amazon.com, Inc. (Devices & Services) · **Fecha de la reconstrucción:** 16/11/2026 · **Patrocinador:** dirección de Devices & Services (rol) · **Etiqueta del documento:** `[PROPUESTA DE GESTIÓN]` con base `[DATO REAL]`.

## 5.1 Resumen ejecutivo

Amazon busca entrar al mercado de banda ancha satelital en órbita baja para dar conectividad donde no llegan las redes existentes y para abrir líneas de negocio (empresas, aviación, operadores, dispositivos móviles). El proyecto despliega 3.232 satélites, una red terrestre y terminales propios. Se eligió una **integración vertical** (fabricación, terminales y operación propias, #22) con **lanzamiento tercerizado y diversificado** en cuatro proveedores. El caso sigue siendo deseable (los acuerdos comerciales crecen) pero su viabilidad en plazo está comprometida: al ritmo actual, el hito regulatorio de 2029 no se alcanza (sección 11).

## 5.2 Descripción del problema

**[DATO REAL]** Amazon plantea el problema como acceso: "billions of people on the planet who lack high-speed internet access" (#28) y servicio para "unserved and underserved communities around the world" (#39).

**[INFERENCIA DEL GRUPO]** Para Amazon como organización, el problema es también estratégico: sin una red propia, depende de terceros para conectar dispositivos, clientes empresariales y la nube. El proyecto crea un negocio nuevo dentro de Devices & Services (#28) con impacto en procesos (fabricación aeroespacial en serie, operaciones de lanzamiento) que la empresa no tenía.
→ Base: #28, #4 (AWS "will provide networking and infrastructure"), #22. Supuesto: la integración con AWS y dispositivos es parte de la motivación, aunque Amazon no la formula como problema.

## 5.3 Visión general del proyecto

| Objetivo | Métrica | Indicador de éxito | Etiqueta |
|---|---|---|---|
| Cumplir la autorización de la FCC | Satélites desplegados y operativos | 3.232 al 30/07/2029 (#8 ¶3) | `[DATO REAL]` |
| Iniciar el servicio comercial | Criterio de inicio (cobertura, satélites, clientes pagos) | A definir y comunicar con margen | `[PROPUESTA DE GESTIÓN]` |
| Monetizar acuerdos firmados | Socios con servicio activo | Aerolíneas: JetBlue 2027 (#36), Delta 2028 (#31); D2D 2028 (#22) | `[DATO REAL]` (fechas) |
| Ingresos y suscriptores | Clientes; ingresos en USD | No público | — |

**Premisas** `[PROPUESTA DE GESTIÓN]`: los contratos de lanzamiento siguen vigentes; la fábrica alcanza su capacidad declarada; la demanda empresarial y de aviación se sostiene.
**Restricciones** `[DATO REAL]`: hitos de la FCC y pérdida de la fianza si no se cumplen (#8 ¶3, ¶12, ¶18); prohibición de desplegar directamente a la órbita operativa (#7 ¶43); capacidad de lanzamiento de terceros.

## 5.4 Alineación con los objetivos estratégicos

| Plan estratégico | Objetivo estratégico | Relación con el proyecto | Etiqueta |
|---|---|---|---|
| Devices & Services | Conectar dispositivos y clientes | Leo y el acuerdo con Apple llevan conectividad satelital a teléfonos (#22, #34) | `[DATO REAL]` + relación `[INFERENCIA DEL GRUPO]` |
| AWS | Infraestructura de red y nube | En 2022 Amazon dijo que AWS "will provide networking and infrastructure" (#4) | `[DATO REAL]` |
| Mercado empresarial | Servicios a empresas y gobierno | Preview empresarial con Leo Pro y Ultra (#29) | `[DATO REAL]` |

Amazon no publica un plan estratégico de Leo: la alineación es lectura del grupo sobre declaraciones verificables.

## 5.5 Análisis costo-beneficio

**Costos con fuente** `[DATO REAL]`

| Descripción | Costo | Fuente |
|---|---|---|
| Compromiso de inversión inicial | > USD 10.000 millones | #39 (30/07/2020) |
| Instalación de procesamiento en Kennedy Space Center | > USD 140 millones | #27 |
| Instalaciones en Cabo Cañaveral (VIF-A, plataforma, barco) | > USD 200 millones | #23 |
| Lanzamientos (≈ 108 contratados) | No público ("the largest commercial procurement of launch vehicles in history", #28) | — |
| Terminal estándar (costo de fabricación esperado) | < USD 400 por unidad | #30 (2023) |
| Fianza ante la FCC | No pública; no eximida | #8 ¶18 |

**Beneficios** `[INFERENCIA DEL GRUPO]` (cualitativos, sin montos públicos): ingresos por servicio a empresas, aviación (500 aviones de Delta desde 2028, #31), operadores y D2D; sinergias con AWS y dispositivos; posición en un mercado con pocos operadores de órbita baja.

**[INFERENCIA DEL GRUPO]** Sin ingresos ni costo total públicos, el análisis solo puede ser **cualitativo**. Con datos internos, la cátedra indica usar VAN, TIR, payback o costo-beneficio (Paneo, tema 2: solo nombrar). El dato económico más relevante para la gestión es que los costos ya comprometidos (fábrica, instalaciones, lanzamientos) son altos y en gran parte **fijos**, mientras que los beneficios dependen de iniciar el servicio, que se corrió unos 2 años (Anexo B, §5).

## 5.6 Análisis de alternativas

`[PROPUESTA DE GESTIÓN]`, con base en la evidencia citada.

| Alternativa | Razones para no seleccionarla |
|---|---|
| Mantener el statu quo (no entrar) | Dejaría a Amazon dependiendo de terceros para conectividad satelital; los competidores ya se movían (oposición de SpaceX, OneWeb y Telesat ante la FCC en 2019, #45). |
| Comprar capacidad a un operador existente | Menor control y menor margen. Amazon eligió diseñar, fabricar y operar "in-house" (#22). |
| Constelación más chica o por regiones | Reduciría la cobertura global prometida y el alcance autorizado; Amazon rechazó resignar satélites ante la FCC (#8 ¶8, ¶11). |
| Solo direct-to-device | No cubre banda ancha fija ni empresas. Amazon lo suma como línea adicional desde 2028 (#34), no como reemplazo. |
| **Seleccionada:** constelación propia integrada, con lanzamiento diversificado | Control de la cadena y diversificación del riesgo de lanzamiento (OP-1), a costa de un plazo exigente. |

## 5.7 Actualización del caso (2026)

**[INFERENCIA DEL GRUPO]** La cátedra dice que el caso de negocio "no es estático". Al 16/11/2026 conviene reevaluarlo: el hito de 2029 no es alcanzable al ritmo actual (secciones 11 y 12), el inicio del servicio se corrió unos 2 años y el alcance del programa creció (Gen2, D2D, Globalstar). La recomendación es **separar el caso de Gen1** (cumplir la autorización e iniciar servicio) del de las líneas nuevas, para no justificar el atraso de uno con el potencial del otro.

**Aprobaciones:** reconstrucción académica; sin firmas.

---

# 6. Acta de Constitución del Proyecto (reconstruida)

> Campos: laboratorio SAFIRO (`catedra/Caso_DOWN_Proyecto_SAFIRO_…html`) y `catedra/Proyectos_02 …Acta del Proyecto`. Etiqueta del documento: `[PROPUESTA DE GESTIÓN]`.

**Decisión del grupo sobre la fecha del acta:** se reconstruye el acta **al 30/07/2020**, el día en que la FCC autorizó la constelación y Amazon anunció la inversión (#6, #39). Es el momento en que el proyecto queda formalmente habilitado. El nombre de entonces es *Project Kuiper*; desde el 13/11/2025 se llama Amazon Leo (#21).

## 6.1 Análisis previo

| Explícito en la evidencia `[DATO REAL]` | Debe investigarse / validarse | Supuestos `[PROPUESTA DE GESTIÓN]` |
|---|---|---|
| 3.236 satélites autorizados (#6); hitos 50% al 30/07/2026 y 100% al 30/07/2029 (confirmados en #7 y #8); > USD 10.000 millones (#39); propósito declarado (#39) | Presupuesto detallado; organigrama del proyecto en 2020; cronograma interno; costo de lanzamientos | El VP del programa actúa como gerente; los lanzamientos se contratan a terceros; la fabricación es propia |

## 6.2 Acta

| Campo | Contenido | Etiqueta |
|---|---|---|
| Nombre del proyecto | Project Kuiper: despliegue de la constelación de primera generación (desde 13/11/2025: Amazon Leo) | `[DATO REAL]` #39, #21 |
| Organización | Amazon.com, Inc. | `[DATO REAL]` |
| Objetivo del proyecto | Desplegar y poner en operación 3.236 satélites (desde 2024: 3.232) con su red terrestre y terminales, cumpliendo el 50% al 30/07/2026 y el 100% al 30/07/2029, y habilitar el servicio comercial de banda ancha | `[DATO REAL]` (cifras y fechas) / redacción `[PROPUESTA]` |
| Propósito / justificación | "Reliable, affordable broadband service to unserved and underserved communities around the world" (#39); oportunidad de negocio (sección 5) | `[DATO REAL]` + `[INFERENCIA]` |
| Antecedentes | Presentaciones federales de 2019 (#42); oposición de competidores ante la FCC (#45); autorización FCC 20-102 (#6) | `[DATO REAL]` |
| Beneficios esperados | Conectividad en zonas sin cobertura; nuevo negocio de Devices & Services; sinergias con AWS (#4) | `[INFERENCIA DEL GRUPO]` |
| Descripción del producto | Constelación en órbita baja (590, 610 y 630 km), gateways y fibra, terminales de usuario de bajo costo | `[DATO REAL]` #6, #28, #30 |
| Objetivos medibles / criterios de éxito | (1) 1.616 satélites operativos al 30/07/2026; (2) 3.232 al 30/07/2029; (3) inicio de servicio comercial con criterio verificable: cobertura mínima por región, cantidad mínima de satélites operativos y primeros clientes pagos | (1)(2) `[DATO REAL]`; (3) `[PROPUESTA]` |
| Entregables principales | Satélites fabricados; instalaciones de procesamiento; campañas de lanzamiento; constelación operativa; segmento terrestre; terminales; servicio habilitado (WBS, sección 7) | `[PROPUESTA DE GESTIÓN]` |
| Requisitos de alto nivel | Cumplir la autorización y las condiciones de la FCC (desechos orbitales, despliegue no directo a la órbita operativa, #7 ¶43); terminales de bajo costo (< USD 400, #30) | `[DATO REAL]` |
| Equipo del proyecto | Roles: gerente del programa; sistemas de lanzamiento; operaciones de producción; legal y regulatorio; negocio y producto (roles visibles en #3, #24, #27, #33) | `[DATO REAL]` (roles, 2024–2026) / asignación `[PROPUESTA]` |
| Gerente del proyecto | VP a cargo del programa (en 2025: Rajeev Badyal, "Vice President of Amazon Leo", #21) | `[DATO REAL]` (2025) / rol `[PROPUESTA]` |
| Autoridad del gerente | Asignar presupuesto dentro de la línea base; contratar lanzamientos dentro del marco aprobado; priorizar el manifiesto; escalar a la dirección los cambios de alcance y los pedidos a la FCC | `[PROPUESTA DE GESTIÓN]` |
| Stakeholders principales | FCC; proveedores de lanzamiento; dirección de Amazon; AWS; clientes y socios (sección 4) | `[DATO REAL]` |
| Plazo de alto nivel | 30/07/2020 → 30/07/2029 (9 años), con hito intermedio el 30/07/2026 | `[DATO REAL]` |
| Presupuesto de alto nivel | Compromiso > USD 10.000 millones (#39). Detalle no público | `[DATO REAL]` |
| Supuestos | Capacidad de lanzamiento disponible a tiempo; fábrica propia a escala; la FCC mantiene el marco regulatorio | `[PROPUESTA DE GESTIÓN]` |
| Restricciones | Hitos FCC con sanción (reducción de la autorización y pérdida de la fianza); dependencia de lanzadores de terceros; coordinación de espectro | `[DATO REAL]` #8 |
| Riesgos iniciales (vistos en 2020) | Disponibilidad y confiabilidad de lanzadores nuevos (Vulcan, New Glenn, Ariane 6); atraso regulatorio; oposición de competidores; escalado de la fabricación | `[INFERENCIA DEL GRUPO]` (se materializaron en 2025–2026: sección 11) |
| Criterios de aprobación / aceptación | Satélites "deployed and operating" según la FCC (#8 ¶3); criterio de inicio de servicio aprobado por el sponsor | `[DATO REAL]` / `[PROPUESTA]` |
| Sponsor / patrocinador | Dirección senior de Amazon (en 2020 anunció el proyecto Dave Limp, Senior Vice President, #39) | `[DATO REAL]` (2020) / rol `[PROPUESTA]` |
| Aprobado por · Fecha | Reconstrucción académica · 30/07/2020 (fecha del acta reconstruida) | — |

## 6.3 Revisión con el checklist de la cátedra

- [x] Explica por qué (propósito, antecedentes, beneficios).
- [x] Define qué se autoriza (objetivo, producto, entregables).
- [x] Distingue hechos de supuestos (columna de etiquetas).
- [x] Identifica responsables (sponsor, gerente, roles).
- [x] Incluye límites (plazo, presupuesto, restricciones, riesgos).
- [x] No se transforma en el plan (la WBS, el cronograma y los costos van en las secciones 7 a 10).

**[INFERENCIA DEL GRUPO] Lo que el acta reconstruida deja ver.** El criterio de éxito (3) no existía de forma pública. Eso explica que el inicio del servicio pudiera correrse cuatro veces sin un hito formal incumplido (Anexo B, §5). Con este campo, la R-03 del registro de riesgos tendría un disparador verificable.

---

# 7. Alcance y WBS

> Marco: `catedra/Clase 2 Alcance.html`. Desarrollo metodológico y evidencia por elemento: `informe/guias/alcance-wbs.md`.

## 7.1 Declaración del alcance

`[PROPUESTA DE GESTIÓN]` con base `[DATO REAL]`.

| Campo (Clase 2) | Contenido |
|---|---|
| Descripción del producto | Sistema de banda ancha satelital en órbita baja: constelación de primera generación (3.232 satélites, #7), red terrestre (gateways, POP y fibra, #17, #28) y terminales Nano, Pro y Ultra (#29, #30). |
| Alcance del producto | Servicio de conectividad de hasta 100 Mbps (Nano), 400 Mbps (Pro) y 1 Gbps de bajada (Ultra) (#29, #30), con cobertura según los satélites operativos. |
| Alcance del proyecto | Fabricar, procesar, lanzar y poner en operación los 3.232 satélites; desplegar el segmento terrestre; producir terminales; habilitar el servicio comercial; cumplir las obligaciones de la FCC. |
| Entregables | Los del nivel 2 de la WBS (7.2). |
| Criterios de aceptación | Satélites "deployed and operating" (#8 ¶3); 3.232 al 30/07/2029; servicio comercial según el criterio del acta (sección 6). |
| Exclusiones | Gen2 (3.212 satélites) y sistema Polar (1.292) (#8 ¶3); direct-to-device (hasta 5.105 satélites desde 2028, #34); integración de Globalstar (#22); operación comercial posterior al inicio del servicio. |
| Supuestos | Contratos de lanzamiento vigentes; capacidad de fábrica declarada alcanzable; lanzados ≈ operativos. |
| Restricciones | Hitos y sanciones de la FCC (#8 ¶3, ¶12, ¶18); no desplegar directamente a la órbita operativa (#7 ¶43); plan de desechos con reportes semestrales (#44). |

**Justificación de las exclusiones.** Amazon Leo es un **programa** y el despliegue de Gen1 es el **proyecto** con línea base pública (Paneo, tema 2: programa contra proyecto). Las líneas nuevas se tratan con **elaboración progresiva (rolling wave)** (Clase 2): se detallarán cuando haya información. Así el alcance es SMART y coherente con el horizonte de Riesgos (30/07/2029) y con el BAC de Valor Ganado (3.232).

## 7.2 WBS (niveles 1 a 3)

`[PROPUESTA DE GESTIÓN]` orientada a entregables y ordenada por el **flujo físico** del despliegue.

```
1. Despliegue de Amazon Leo Gen1 (3.232 satélites)
├── 1.1 Gestión del proyecto
│   ├── 1.1.1 Acta y caso de negocio
│   ├── 1.1.2 Plan para la dirección (alcance, tiempos, costos, riesgos)
│   └── 1.1.3 Seguimiento y control (informes de situación, VG, log de temas)
├── 1.2 Cumplimiento regulatorio
│   ├── 1.2.1 Autorización y modificaciones FCC
│   ├── 1.2.2 Gestión de hitos (aviso, waiver, certificación del 50% construido)
│   ├── 1.2.3 Plan de desechos orbitales y reportes semestrales
│   └── 1.2.4 Licencias por país
├── 1.3 Satélites
│   ├── 1.3.1 Diseño y prototipos
│   ├── 1.3.2 Planta de Kirkland
│   └── 1.3.3 Lotes fabricados y aceptados
├── 1.4 Procesamiento e integración
│   ├── 1.4.1 Instalación de Kennedy Space Center
│   ├── 1.4.2 Instalaciones de Cabo Cañaveral
│   └── 1.4.3 Integración de dispensadores y carga por misión
├── 1.5 Lanzamientos
│   ├── 1.5.1 Campaña Atlas V      ├── 1.5.4 Campaña New Glenn
│   ├── 1.5.2 Campaña Vulcan       └── 1.5.5 Campaña Falcon 9
│   └── 1.5.3 Campaña Ariane 6
├── 1.6 Constelación en órbita
│   ├── 1.6.1 Elevación a órbita operativa y puesta en servicio por lote
│   └── 1.6.2 Centro de operaciones
├── 1.7 Segmento terrestre
│   ├── 1.7.1 Gateways
│   ├── 1.7.2 Points of Presence e integración con AWS
│   └── 1.7.3 Fibra / backhaul
├── 1.8 Terminales de usuario (Nano, Pro, Ultra)
└── 1.9 Servicio habilitado
    ├── 1.9.1 Preview empresarial
    ├── 1.9.2 Inicio de servicio comercial (criterio del acta)
    └── 1.9.3 Socios de distribución
```

La evidencia de cada elemento está en la guía (§3). Lo que no tiene fuente (1.3.1 prototipos, 1.6.2 centro de operaciones) está marcado como reconstrucción.

## 7.3 Diccionario de la WBS (paquetes críticos)

`[PROPUESTA DE GESTIÓN]`

| Paquete | Entregable verificable | Criterio de aceptación | Responsable (rol) | Dependencias | Riesgos | Hito |
|---|---|---|---|---|---|---|
| 1.3.3 Lotes fabricados | Satélites aceptados para vuelo | Pruebas de aceptación aprobadas | Operaciones de producción | 1.3.2 | — | — |
| 1.5.2 Campaña Vulcan | Lote de hasta 40 satélites desplegado por misión (#3) | Separación nominal y contacto con todos los satélites | Sistemas de lanzamiento | 1.3.3, 1.4.3 | R-01, R-02, T-01 | Retorno al vuelo |
| 1.5.4 Campaña New Glenn | Lotes desplegados | Ídem | Sistemas de lanzamiento | 1.3.3, 1.4.3 | R-02 | Primer vuelo para Leo |
| 1.6.1 Puesta en servicio | Satélites en órbita operativa | "Deployed and operating" (#8) | Operaciones | 1.5.x | R-04, R-05 | 30/07/2029 |
| 1.2.2 Gestión de hitos | Certificación del 50% construido | Presentada y aceptada por la FCC | Legal y regulatorio | 1.3.3, 1.5 | R-05, R-04 | 30/10/2027 |
| 1.9.2 Inicio comercial | Servicio a clientes pagos | Criterio del acta cumplido | Negocio y producto | 1.6, 1.7, 1.8 | R-03, R-06 | A fijar |

## 7.4 Cómo se conectan fabricación, lanzamientos y operación

**[INFERENCIA DEL GRUPO]** La WBS es una cadena en serie con un cuello de botella claro: **el lanzamiento (1.5)**.

| Eslabón | Capacidad o ritmo | Fuente |
|---|---|---|
| Fabricación (1.3) | Capacidad declarada de hasta 30 satélites por semana (≈ 130 por mes); 1.000 fabricados a inicios de 09/2026 | #23, #3 |
| Procesamiento (1.4) | KSC: "more than 100 satellites per month" y tres campañas simultáneas | #27 |
| Lanzamiento (1.5) | ≈ 21 satélites por mes desplegados (promedio 04/2025–11/2026) | Anexo D, C-21 |
| Operación (1.6) | Requiere ≈ 87 por mes para llegar al hito | Anexo D, C-23 |

Amazon mismo dice que ajusta la producción a la disponibilidad de lanzadores (#23).
→ Supuestos: (a) las capacidades declaradas son alcanzables; (b) lanzados ≈ operativos. La diferencia entre fabricados (1.000) y lanzados (396) **no se presenta como stock confirmado**: puede incluir satélites en pruebas o descartados (Riesgos descartó esa inferencia por débil).

**Conclusión para la gestión** `[PROPUESTA DE GESTIÓN]`: el esfuerzo de control debe ponerse en 1.5 (manifiesto, proveedores, retorno al vuelo), no en la fábrica. Es la base de R-02 y de OP-1 en Riesgos.

---

# 8. Tiempos: cronograma maestro

> Marco: `catedra/Clase 3 Gestión de los Tiempos · UCA.html` (milestones, inch-pebbles, dependencias, Gantt, acortamiento, nivelación y "zona inalcanzable"). Serie de misiones: `informe/seguimiento/ev_serie.csv`.

## 8.1 Milestones

| ID | Hito | Fecha | Tipo | Estado al 16/11/2026 | Etiqueta / fuente |
|---|---|---|---|---|---|
| M-01 | Autorización FCC (3.236 satélites) | 30/07/2020 | Regulatorio | Cumplido | `[DATO REAL]` #6, #39 |
| M-02 | Fábrica de Kirkland operativa | 04/2024 | Técnico | Cumplido | `[DATO REAL]` #26 |
| M-03 | Modificación FCC (3.232 satélites) | 08/03/2024 | Regulatorio | Cumplido | `[DATO REAL]` #7 |
| M-04 | Primera misión de producción (KA-01) | 28/04/2025 | Técnico | Cumplido | `[DATO REAL]` #2 |
| M-05 | Instalación de KSC operativa | 24/07/2025 | Técnico | Cumplido | `[DATO REAL]` #27 |
| M-06 | Preview empresarial | 24/11/2025 | Comercial | Cumplido | `[DATO REAL]` #29 |
| M-07 | Hito FCC del 50% (1.616 operativos) | 30/07/2026 | Regulatorio | **No cumplido** (396) | `[DATO REAL]` #8 / estado `[INFERENCIA]` |
| M-08 | Aviso de cumplimiento a la FCC | 14/08/2026 | Regulatorio | No encontrado | `[DATO REAL]` #7 ¶53 |
| M-09 | Primer vuelo de Vulcan para Leo | 15/11/2026 | Técnico | **Fallido** (tema T-01) | `[DATO REAL]` #2, #11 |
| M-10 | Inicio de servicio comercial | "later this year" (2026) | Comercial | Pendiente; sin criterio público | `[DATO REAL]` #3 / criterio `[PROPUESTA]` |
| M-11 | Certificación del 50% construido (acorta la pérdida de espectro) | 30/10/2027 | Regulatorio | Futuro | `[DATO REAL]` #8 ¶15 |
| M-12 | Fin de la pérdida de prioridad de espectro | 30/03/2028 | Regulatorio | Futuro | `[DATO REAL]` #8 ¶15 |
| M-13 | Hito FCC final (3.232 operativos) | 30/07/2029 | Regulatorio | En riesgo (R-04) | `[DATO REAL]` #8 ¶3 |

## 8.2 Inch-pebbles: cada misión es un punto de control

`[PROPUESTA DE GESTIÓN]` La Clase 3 dice que los inch-pebbles "dividen el avance en puntos intermedios más pequeños" y achican el área de desvío. En este proyecto la unidad natural es **la misión**: se sabe el día, el cohete y los satélites desplegados (#2). El control se hace por trimestre contra lo necesario.

| Trimestre | Misiones reales | Satélites desplegados | Acumulado | Fuente |
|---|---|---|---|---|
| 2T 2025 | 2 | 54 | 54 | #2 |
| 3T 2025 | 3 | 75 | 129 | #2 |
| 4T 2025 | 2 | 51 | 180 | #2 |
| 1T 2026 | 1 | 32 | 212 | #2 |
| 2T 2026 | 5 | 155 | 367 | #2 |
| 3T 2026 | 1 | 29 | 396 | #2 |
| 4T 2026 (al 16/11) | 1 (fallida) | 0 | 396 | #2, #11 |

**Umbral por trimestre** `[INFERENCIA DEL GRUPO]`: para llegar a 3.232 el 30/07/2029 hacen falta ≈ **262 satélites por trimestre** (87 por mes, C-23). El mejor trimestre real fue el 2T 2026, con 155.

## 8.3 Dependencias y secuencia

`[PROPUESTA DE GESTIÓN]` sobre la WBS (sección 7):

| Actividad | WBS | Predecesora | Relación | Comentario |
|---|---|---|---|---|
| Fabricar lote | 1.3.3 | Planta operativa (1.3.2) | Fin–inicio | Capacidad hasta 30/semana (#23) |
| Procesar e integrar carga | 1.4.3 | Fabricar lote; instalación KSC (1.4.1) | Fin–inicio | Hasta tres campañas simultáneas (#27) |
| Lanzar misión | 1.5.x | Procesar carga; cohete disponible (proveedor) | Fin–inicio | **Recurso externo**: depende del proveedor |
| Elevar y poner en servicio | 1.6.1 | Lanzar misión | Fin–inicio | No se despliega directo a la órbita operativa (#7 ¶43) |
| Desplegar gateways | 1.7.1 | Licencias por país (1.2.4) | Fin–inicio | En paralelo con 1.3–1.6 |
| Iniciar servicio por región | 1.9.2 | Satélites operativos (1.6) + gateways (1.7) + terminales (1.8) | Fin–inicio | Criterio del acta |

## 8.4 Gantt de alto nivel por campaña

`[DATO REAL]` hasta el 16/11/2026 (#2); después, `[PROPUESTA DE GESTIÓN]` sobre los contratos vigentes (Anexo A).

| Campaña | 2025 | 2026 | 2027 | 2028 | 2029 | Restantes |
|---|---|---|---|---|---|---|
| Atlas V (9) | ■■■■ (4) | ■■■■ (4) | ■ | | | 1 |
| Falcon 9 (13) | ■■■ (3) | | ▒▒▒▒ | ▒▒▒▒ | ▒▒ | 10 |
| Ariane 6 (24) | | ■■■ (3) | ▒▒▒▒▒ | ▒▒▒▒▒ | ▒▒▒▒▒ | 21 |
| Vulcan (38) | | ✕ LV-01 | ▒▒▒ (retorno sin fecha) | ▒▒▒▒▒▒ | ▒▒▒▒▒▒ | 37 |
| New Glenn (24) | | | ▒▒ (primer vuelo sin fecha) | ▒▒▒▒▒ | ▒▒▒▒▒ | 24 |

■ real · ✕ fallida · ▒ planificado (propuesta, sin fechas públicas).

## 8.5 Cuando el plazo limita el plan: acortamiento, nivelación y zona inalcanzable

**[INFERENCIA DEL GRUPO]** La Clase 3 explica que, si el plazo es fijo, se puede **acortar** (más recursos en paralelo) o **nivelar** (ajustar al recurso escaso), y que existe una **zona inalcanzable** donde ningún acortamiento razonable cumple la fecha. Aplicado a Amazon Leo:

- **Acortamiento:** agregar lanzadores (Ariane 6 de 18 a 24 y 10 Falcon 9 adicionales, #24, #23) es exactamente eso. OP-1 en Riesgos.
- **Nivelación:** Amazon nivela la fábrica según los lanzadores disponibles (#23). La fábrica no es el recurso escaso.
- **Zona inalcanzable:** hacen falta ≈ 35 misiones por año (C-24). El plan de Amazon es de 20 (C-25), el ritmo observado de ≈ 11, y el Monte Carlo (Riesgos §5) y PERT (sección 9) dan ≈ 0% de terminar a tiempo. **El hito de 2029 está en la zona inalcanzable con los recursos contratados.**
→ Supuestos: los del Monte Carlo y la estimación PERT.

## 8.6 Línea base propuesta y línea base de recuperación

`[PROPUESTA DE GESTIÓN]`

| Línea base | Qué es | Fin | Uso |
|---|---|---|---|
| **A · Regulatoria** | Hitos FCC: 1.616 al 30/07/2026; 3.232 al 30/07/2029 | 30/07/2029 | Restricción; PV de Valor Ganado |
| **R · Recuperación** (propuesta) | Plan de Amazon sostenido: 20 misiones por año × 30 satélites = 50 por mes desde el corte | ≈ 08/2031 (`valor_ganado.py`) | Base del **pedido de alivio a la FCC** (respuesta principal de R-04) y del cronograma interno |

La línea base R no cumple 2029, pero es el compromiso más exigente que tiene respaldo (el plan declarado de Amazon, #23). Presentarla con evidencia de avance es lo que mejora las chances de un nuevo alivio.

## 8.7 Reservas de tiempo

`[PROPUESTA DE GESTIÓN]` La reserva de ≈ 4 meses por R-02 (lanzador en tierra) se incorpora **una sola vez** a la línea base R: ≈ 08/2031 + 4 meses ≈ **12/2031**. No se suma de nuevo por R-03 ni por R-04, porque es el mismo atraso visto desde otro riesgo (Riesgos §6, "doble cuenta").

---

# 9. Estimaciones

> Marco: `catedra/Clase 4 Estimaciones 1ra. Parte …html` (métodos, ventana, prejuicios) y `catedra/Clase 4 Estimaciones · Segunda Parte …html` (PERT por tres valores). Cálculo: `informe/estimaciones/pert_despliegue.py`.

## 9.1 Qué se estima y con qué método

| Variable | Método (Clase 4) | Por qué | Base |
|---|---|---|---|
| Satélites por misión | **Análoga** (misiones ya voladas por cohete) | Hay historia real por vehículo | #2, #3: 24 (Falcon 9), 27–29 (Atlas V), 32–36 (Ariane 64), 40 (Vulcan) |
| Cadencia de lanzamiento | **Tres valores (PERT)** | Alta incertidumbre: fallas, retornos al vuelo, cohetes nuevos | #2, #23, R-02 |
| Duración del despliegue restante | **Paramétrica** (satélites que faltan ÷ ritmo) + PERT | Relación cuantitativa directa | C-14 |
| Producción | Dato declarado (no se estima) | No es el cuello de botella | #23 |

## 9.2 Estimación PERT de la duración restante

`[PROPUESTA DE GESTIÓN]` Se estima cuánto tarda desplegar los 2.836 satélites que faltan (C-14), con 30 satélites por misión. Los tres valores son **los mismos del Monte Carlo** de Riesgos (§5), para que ambas herramientas sean coherentes.

| Valor | Cadencia | Justificación | Duración | Fin |
|---|---|---|---|---|
| a · optimista ("sin milagros") | 2,0 misiones/mes (24/año) | Por encima del plan "20+" de Amazon (#23) | 47,3 meses | ≈ 10/2030 |
| m · más probable | 0,92 misiones/mes (≈ 11/año) | Ritmo observado desde el 28/04/2026 (#2) | 102,8 meses | ≈ 06/2035 |
| b · pesimista ("sin catástrofes") | 0,5 misiones/mes (6/año) | Lanzadores clave en tierra buena parte del período (R-02) | 189,1 meses | ≈ 08/2042 |

**Resultado** `[INFERENCIA DEL GRUPO]`:
- te = (a + 4m + b) / 6 = **107,9 meses → ≈ 11/2035**
- σ = (b − a) / 6 = **23,6 meses**
- Meses disponibles hasta el 30/07/2029: 32,4 → z = −3,19 → **P(terminar a tiempo) ≈ 0,07%** (aproximación normal)

## 9.3 Coherencia entre las tres herramientas

| Herramienta | Resultado | Por qué difiere |
|---|---|---|
| Monte Carlo (Riesgos §5) | P50 ≈ 1.513 satélites al 30/07/2029; P(llegar) ≈ 0% | Distribución triangular sobre la **cadencia** |
| PERT (esta sección) | Fin ≈ 11/2035; P ≈ 0,07% | Beta sobre la **duración**. Los pesimistas pesan más, porque la duración es inversa a la cadencia |
| Valor Ganado (sección 12) | Fin ≈ 2031 (plan) · ≈ 2038 (ritmo observado en satélites) | Proyección lineal de un solo escenario |

**[INFERENCIA DEL GRUPO]** Las tres herramientas, con supuestos distintos, llegan a la misma conclusión: **el hito de 2029 no se cumple con la capacidad contratada**. El rango razonable de fin está entre 2031 y 2038.

## 9.4 Ventana de estimación

`[PROPUESTA DE GESTIÓN]` La Clase 4 propone estimar todo a alto nivel y en detalle la etapa siguiente, y **reestimar al cerrar cada etapa**. Ventanas propuestas:
1. **Al retorno al vuelo de Vulcan** (cierre del tema T-01): reestimar m y b.
2. **Al primer vuelo de New Glenn para Leo:** reestimar a.
3. **Cada trimestre** con los inch-pebbles (sección 8.2).

## 9.5 Prejuicios en las estimaciones

**[INFERENCIA DEL GRUPO]** La Clase 4 advierte sobre los prejuicios en las estimaciones. Hay dos visibles en este caso:
- **Optimismo de la fuente:** las cifras de Amazon (capacidad de 30 por semana, "20+ misiones", "~700 al 30/07/2026") son declaraciones propias. La proyección presentada a la FCC (~700) terminó en 396 (C-04, C-12).
- **Anclaje en la capacidad instalada:** confundir capacidad (fábrica, contratos) con ritmo efectivo. El registro de fuentes ya separa "capacidad declarada" de "ritmo real".
Por eso el valor más probable (m) se tomó del **ritmo observado** y no del plan.

---

# 10. Costos y presupuesto

> Marco: `catedra/Clase 5 · Gestión de Costos de Proyectos.html` (estimar → presupuestar → controlar; costo ≠ gasto; directos/indirectos; fijos/variables; técnicas; reservas de contingencia y gerencial).

**Advertencia de método.** Amazon no publica su presupuesto ni sus costos unitarios. Esta sección reconstruye **la estructura y el método** de la gestión de costos. Solo se usan montos con fuente; donde no la hay, el campo dice «No público». **No se inventan cifras.**

## 10.1 Montos públicos

| Concepto | Monto | Fecha | Etiqueta / fuente |
|---|---|---|---|
| Compromiso de inversión inicial | > USD 10.000 millones | 30/07/2020 | `[DATO REAL]` #39 |
| Inversión total actualizada | "multibillion-dollar" (sin cifra) | 14/04/2026 | `[DATO REAL]` #5 |
| Instalación de procesamiento en KSC | > USD 140 millones | 24/07/2025 | `[DATO REAL]` #27 |
| Instalaciones en Cabo Cañaveral | > USD 200 millones | 23/03/2026 | `[DATO REAL]` #23 |
| Terminal estándar (costo de fabricación esperado) | < USD 400 por unidad | 14/03/2023 | `[DATO REAL]` #30 |
| Lanzamientos | No público | — | Sin fuente pública |
| Costo por satélite | No público | — | Sin fuente pública |
| Fianza (surety bond) | No pública; no eximida | 05/06/2026 | `[DATO REAL]` #8 ¶18 |
| Compra de Globalstar | USD 90 por acción o 0,3210 acciones de Amazon | 14/04/2026 | `[DATO REAL]` #5. **Fuera del alcance** (sección 7) |

**[INFERENCIA DEL GRUPO]** Las dos inversiones en Florida suman **más de USD 340 millones**, alrededor del 3,4% del compromiso inicial. Supuesto: ambas están dentro del compromiso de 2020 y no son adicionales (no se sabe).

## 10.2 Estructura de costos por elemento de la WBS

`[PROPUESTA DE GESTIÓN]` La clasificación es posible aunque falten montos, y es lo que se defiende.

| Elemento WBS | Directo / indirecto | Fijo / variable | Técnica de estimación propuesta (Clase 5) | Monto |
|---|---|---|---|---|
| 1.1 Gestión del proyecto | Indirecto | Fijo | Analogía con programas similares | No público |
| 1.2 Cumplimiento regulatorio (incluye la fianza) | Directo | Fijo | Dato contractual (la fianza la fija la FCC) | No público |
| 1.3 Satélites: planta | Directo | **Fijo** | Ascendente (por instalación) | No público |
| 1.3 Satélites: unidades | Directo | **Variable** (por satélite) | Paramétrica: costo unitario × 3.232 | No público (costo unitario) |
| 1.4 Procesamiento | Directo | Fijo | Dato público | > USD 340 millones (#27, #23) |
| 1.5 Lanzamientos | Directo | **Variable** (por misión) | Paramétrica: precio por misión × ≈ 108; o tres valores por cohete | No público |
| 1.6 Operación de la constelación | Directo | Fijo + variable | Analogía | No público |
| 1.7 Segmento terrestre | Directo | Variable (por gateway) | Paramétrica: costo por gateway × > 300 (#17) | No público |
| 1.8 Terminales | Directo | Variable | Paramétrica | < USD 400 por unidad (#30) × unidades (no público) |
| 1.9 Servicio y socios | Directo | Variable | Analogía | No público |

**[INFERENCIA DEL GRUPO]** Los costos con mayor peso esperado son **variables por unidad** (satélites y lanzamientos). Por eso perder una misión (T-01) cuesta dos veces: los 40 satélites y el lanzamiento. Y por eso **acelerar la cadencia no abarata**: adelanta costos variables. Los fijos (planta, instalaciones) ya están incurridos.
→ Supuesto: el costo por satélite y por lanzamiento son de un orden de magnitud que domina el total, como ocurre en constelaciones comparables. Es un supuesto, sin cifra.

## 10.3 Presupuesto y reservas

`[PROPUESTA DE GESTIÓN]` Estructura de la Clase 5: costos estimados + reserva de contingencia = **línea base de costos**; + reserva gerencial = **presupuesto total**.

| Componente | Monto | Base |
|---|---|---|
| Costos estimados (10.2) | ≥ USD 10.000 millones (compromiso declarado como piso) | #39 |
| Reserva de contingencia | No calculable sin montos. Se compone de: reposición de 40 satélites (R-01/T-01); fianza (R-04); lanzamientos adicionales de recuperación (R-02, OP-1) | Riesgos §6 |
| = Línea base de costos | No calculable | |
| Reserva gerencial | Porcentaje a fijar por el sponsor | Clase 5 |
| = Presupuesto total | No calculable | |

## 10.4 Control de costos

**[INFERENCIA DEL GRUPO]** Sin costo real (AC), el CPI no es calculable (sección 12). Lo que sí se puede seguir públicamente son señales de costo:
- nuevas inversiones anunciadas (KSC, Cabo Cañaveral);
- contratos adicionales de lanzamiento (Ariane 6 + 6; Falcon 9 + 10);
- eventos que generan costo no planificado (pérdida de LV-01).

Todas apuntan a **costo creciente con avance lento**: es la configuración que la Clase 6 describe con sus "paradojas" de valor ganado (mucho gasto con poco trabajo realizado), aunque aquí solo se puede afirmar de forma cualitativa.

## 10.5 Índice de riesgo y apalancamiento

Riesgos §6 los define como Σ ER ÷ costo total y como (ER antes − ER después) ÷ costo de la alternativa. **Siguen sin poder calcularse**: sin costo total y sin el costo de las respuestas, cualquier cifra sería inventada. Si el equipo decide usar el compromiso de USD 10.000 millones como costo total, hay que convertir las exposiciones a dólares, y eso requiere impactos en USD que tampoco son públicos. Queda como límite declarado.

---

# 11. Gestión de riesgos

Trabajo Integrador de Investigación · Dirección de Proyectos 2026 · Fecha de corte de las fuentes: 16/11/2026

### Resumen

Esta sección reconstruye cómo podrían gestionarse los riesgos del despliegue de la constelación Amazon Leo, con el método de la cátedra (Clase 10, Gestión de Riesgos). El grupo eligió el **plazo** como objetivo a proteger con prioridad, porque la FCC fijó hitos con fecha cuyo incumplimiento tiene consecuencias concretas sobre el espectro, la fianza y la cantidad de satélites autorizados.

El registro tiene **cuatro riesgos desarrollados**, **tres en lista de seguimiento** y **dos oportunidades**. Uno de ellos ya ocurrió: la pérdida de 40 satélites en la misión Vulcan del 15/11/2026 (R-01), que se gestiona como tema abierto (T-01) mientras R-01 sigue midiendo que se repita. Hay dos riesgos en rojo: que la FCC no conceda un nuevo alivio del hito de 2029 (exposición 0,28) y que un lanzador clave quede en tierra (0,20). Forman una cadena: un lanzador en tierra frena la cadencia, eso retrasa el servicio y agranda la brecha con el hito final, lo que deja a Amazon dependiendo de la decisión del regulador.

El análisis cuantitativo muestra que, con la cadencia observada o con la del propio plan de Amazon, llegar a los 3.232 satélites antes del 30/07/2029 es prácticamente imposible. Por eso no llegar se trata como una condición prevista y no como un riesgo, y el riesgo principal se formula sobre lo que sí es incierto: si la FCC concede un nuevo alivio.

### 1. Alcance, método y trazabilidad

**Alcance.** Se analizan los riesgos del programa de despliegue de la primera generación de la constelación (3.232 satélites autorizados por la FCC), desde la mirada de la gestión de proyectos, con horizonte al 30/07/2029.

**Marco.** Se usa el de la cátedra: Clase 10 (Gestión de Riesgos), `Proyectos_10 Riesgos` y el capítulo 7 del apunte. Sus seis procesos son planificar, identificar, analizar cualitativamente, analizar cuantitativamente, planificar las respuestas y supervisar. Los nombres de los documentos son los de la cátedra (Registro de Riesgos, Exposición al Riesgo, aceptación pasiva o activa, reservas de contingencia y gerenciales).

**Trazabilidad.** Cada dato lleva una etiqueta:
- `[DATO REAL]`: hecho con fuente verificable (se cita con `#n` del anexo A o con documento y párrafo).
- `[INFERENCIA DEL GRUPO]`: conclusión razonable a partir de la evidencia, con supuestos escritos.
- `[PROPUESTA DE GESTIÓN]`: decisión, estimación o valoración creada por el grupo: probabilidades, impactos, estrategias, propietarios, umbrales y reservas.

**Qué no es público.** Amazon no publica su cronograma, su EDT ni su presupuesto, y casi todo lo que informa es declaración de la propia empresa. Por eso la parte reconstruida (probabilidades, impactos, respuestas) es propuesta del grupo y se justifica en cada caso. Los datos que no existen públicamente (costo de un satélite, monto de la fianza, costo de las respuestas) **no se inventaron**: figuran como limitación en la sección 8.

**Declaración de uso de herramientas de IA.** Esta sección se elaboró con asistencia de Claude (Anthropic) para la búsqueda y verificación de fuentes, la estructura y la redacción de borradores. La cátedra habilitó el uso de IA para la redacción (confirmado por el equipo el 16/11/2026). Las decisiones de contenido (objetivo prioritario, orden de objetivos, apetito, umbrales, probabilidades, impactos, estrategias y criterios de cierre) las revisó y aprobó el autor de esta sección. Las fuentes se leyeron con asistencia de IA y se citan para que cualquiera pueda comprobarlas; lo que no pudo verificarse está señalado.

### 2. Planificación de la gestión de riesgos

#### 2.1 Objetivo que se protege con prioridad: plazo

**[DATO REAL]** Si Amazon no llega a 1.616 satélites operativos para el 30/07/2026, pierde prioridad de espectro hasta 30/03/2028.
→ Fuente: FCC, Order DA 26-553, ¶15 (publicada el 05/06/2026, consultada el 16/11/2026).

**[DATO REAL]** Si Amazon no llega al 50% de satélites operativos (1.616) para el 30/07/2026, pierde la fianza (surety bond).
→ Fuente: FCC, Order DA 26-553, ¶18.

**[DATO REAL]** Si Amazon no llega a 3.232 satélites operativos para el 30/07/2029, le reducen la autorización a la cantidad de satélites que tenga operativos ese día.
→ Fuente: FCC, Order DA 26-553, ¶12.

**[INFERENCIA DEL GRUPO]** Amazon sigue ampliando compromisos de lanzamiento pese al atraso, porque extendió su acuerdo con Arianespace de 18 a 24 lanzamientos de Ariane 6 (#24, 10/09/2026), sumando capacidad tras haber contratado 10 vuelos adicionales de Falcon 9 a fines de 2025 (según #23, 23/03/2026).
→ Base: #24, #23 y el atraso respecto del hito (DA 26-553 ¶3, ¶8; #2).
→ Supuesto: cada uno de estos lanzamientos implica un desembolso económico para la compañía, aunque los montos exactos de los contratos no sean públicos.
→ Limitación: en la nota de Arianespace (#24), Amazon no vincula oficialmente la ampliación con la necesidad de recuperar el cronograma; según Chris Weber (VP de negocio y producto de Amazon Leo), la decisión responde a la confianza en el desempeño del Ariane 6 y a una estrategia para fortalecer la capacidad de lanzamiento europea.

**[PROPUESTA DE GESTIÓN]** El grupo propone proteger el plazo como objetivo prioritario porque las tres consecuencias de incumplirlo (pérdida de prioridad de espectro, pérdida de la fianza y reducción de la autorización) las fija un regulador, con fechas concretas. Un atraso no solo consume tiempo: reduce el alcance autorizado y expone un costo. Por eso se lo trata como la restricción que arrastra a los demás objetivos.
→ Justificación: DA 26-553 ¶12, ¶15 y ¶18; criterio de la cátedra de gestionar conectados el plazo, el costo y el alcance (apunte, capítulo 7, "La conexión con el resto").

#### 2.2 Orden de los objetivos

**[PROPUESTA DE GESTIÓN]** De más a menos protegido:

| Puesto | Objetivo | Apoyo |
|---|---|---|
| 1.º | Plazo | Sección 2.1. |
| 2.º | Alcance | Amazon mantiene la obligación de 3.232 satélites para 2029 aun después del waiver (DA 26-553 ¶11). |
| 3.º | Calidad | Evidencia débil: fabrica "in-house" (#22) y lanzó un lote de 40 satélites en una misma misión (#3), lo que indica aceptación de riesgo técnico más que prioridad de calidad. |
| 4.º | Costo | Es lo que Amazon parece sacrificar primero (inferencia de la sección 2.1). |

La evidencia pública no alcanza para ubicar la calidad con certeza; se deja explícito como limitación.

#### 2.3 Apetito al riesgo

**[DATO REAL]** Amazon aceptó incumplir el hito intermedio de la FCC y pidió una extensión de 24 meses o un waiver (DA 26-553 ¶8, ¶11); lanzó 40 satélites en una sola misión, el mayor lote hasta la fecha (#3, #11); fabrica todo en casa (#22); y diversifica lanzadores entre Arianespace, ULA, Blue Origin y SpaceX (#24, #3, #23, #38).

**[INFERENCIA DEL GRUPO]** Amazon muestra una actitud de **búsqueda de riesgo moderada**: acepta concentrar riesgo técnico y de plazo para acelerar el despliegue, pero lo compensa diversificando proveedores.
→ Base: los hechos anteriores. Supuestos: (a) lanzar 40 satélites juntos es una decisión de Amazon y no una restricción del cohete; (b) la diversificación de lanzadores es una cobertura de riesgo y no solo una decisión comercial.
→ Limitación: ninguna fuente pública declara el apetito al riesgo de Amazon; es una lectura de su comportamiento.

#### 2.4 Tolerancia y umbrales

**[PROPUESTA DE GESTIÓN]**
- **Escalas:** las de la cátedra (sección 2.6).
- **Tolerancia para el plazo:** más estricta que para costo y calidad, por las consecuencias regulatorias fijas. Un desvío mayor al 10% del cronograma se considera impacto alto (escala de la cátedra: 10–20% = alto).
- **Colores de la matriz** (la cátedra no fija los cortes; los define el grupo): rojo si ER ≥ 0,20; amarillo entre 0,10 y 0,19; verde entre 0,05 y 0,09; azul por debajo de 0,05.
- **Disparadores:** una falla de lanzamiento; que los satélites operativos no alcancen el hito siguiente de la FCC; el vencimiento de la fecha de certificación que acorta la pérdida de espectro a 15 meses (30/10/2027, DA 26-553 ¶15).

#### 2.5 Categorías (RBS)

**[PROPUESTA DE GESTIÓN]** Se usan las cuatro categorías de la cátedra, con subcategorías propias del proyecto:

| Categoría (cátedra) | Subcategorías |
|---|---|
| Técnicos | Lanzamiento · Satélite · Terminal y servicio |
| Gestión del proyecto | Proveedores y contratos · Cronograma · Costos y fondos |
| Organización | Dependencia de socios locales · Capacidad de fabricación |
| Externos | Regulación (FCC y otros) · Competencia · Condiciones de lanzamiento |

#### 2.6 Escalas

**[PROPUESTA DE GESTIÓN]** Se usan sin cambios las de la cátedra.

| Probabilidad | Valor | | Impacto | Valores de la matriz |
|---|---|---|---|---|
| Muy alta | > 0,81 | | Muy bajo | 0,05 |
| Alta | 0,61 a 0,80 | | Bajo | 0,10 |
| Moderada | 0,41 a 0,60 | | Moderado | 0,20 |
| Baja | 0,21 a 0,40 | | Alto | 0,40 |
| Muy baja | 0,01 a 0,20 | | Muy alto | 0,80 |

Para el impacto en plazo y costo, la cátedra define: bajo < 5%, moderado 5–10%, alto 10–20%, muy alto > 20%. Para alcance: secundario, principal, inaceptable, totalmente inútil.

### 3. Identificación de riesgos

Se partió de un análisis de supuestos del plan de despliegue y de los hechos reales del programa (lanzamientos, contratos, resoluciones de la FCC, acuerdos comerciales). La lista preliminar tenía 12 amenazas y 3 oportunidades; se depuró fusionando las que comparten causa y evento, y se descartó una inferencia débil (satélites fabricados sin lanzar). Quedó:

| ID | Riesgo | Categoría | Tratamiento |
|---|---|---|---|
| R-01 | Pérdida de satélites por falla de un lanzador (recurrencia; **ocurrió el 15/11/2026 → tema T-01**) | Técnico → Lanzamiento | Desarrollado |
| R-02 | Lanzador clave en tierra, con manifiesto concentrado | Gestión → Proveedores | Desarrollado |
| R-03 | Desvío del cronograma de despliegue y del inicio del servicio | Gestión → Cronograma | Desarrollado |
| R-04 | Que la FCC no conceda un nuevo alivio del hito de 2029 (no llegar por cadencia es una condición prevista, sección 5) | Externo → Regulación | Desarrollado |
| R-05 | Pérdida temporal de prioridad de espectro | Externo → Regulación | Seguimiento |
| R-06 | Dependencia de socios locales | Organización | Seguimiento |
| R-07 | Aprobaciones regulatorias externas | Externo → Regulación | Seguimiento |
| OP-1 | Capacidad de lanzamiento ampliada y diversificada | Oportunidad | Desarrollada |
| OP-2 | Demanda comercial (aerolíneas y direct-to-device) | Oportunidad | Solo mencionada |

### 4. Análisis cualitativo

#### 4.1 Cuentas de base

**Unidad de medida: satélites lanzados como aproximación de satélites operativos.** La FCC mide los hitos en satélites **"deployed and operating"** (DA 26-553 ¶3) `[DATO REAL]`. Amazon informa satélites **lanzados** ("nearly 400", #2) y no publica cuántos están operativos `[DATO REAL]`. Todas las cuentas de este documento usan lanzados (≈ 396) como aproximación de operativos `[INFERENCIA DEL GRUPO]`.
→ Supuesto: todos los satélites lanzados llegan a su órbita y operan. Consecuencia: como operativos ≤ lanzados, **todos los resultados son optimistas** para Amazon. La brecha real con los hitos es igual o mayor que la calculada, y la conclusión de R-04 se refuerza, no se debilita.

Estas cuentas se usan en varias fichas. Todas son `[INFERENCIA DEL GRUPO]`.

| Cuenta | Resultado | Base y supuestos |
|---|---|---|
| Lanzamientos restantes por proveedor | 21 Ariane 6, 10 Falcon 9, 1 Atlas V, 37 Vulcan, 24 New Glenn: ≈ 93 | Contratados menos volados (#24, #3, #4, #23, #38, #2). Supuestos: los contratos siguen vigentes; los 9 Atlas V incluyen los 8 volados; el manifiesto incluye lanzamientos para ≈ 800 satélites adicionales (#23), no solo para la primera generación. |
| Dependencia de Vulcan y New Glenn | 61 de ≈ 93 = ≈ 66% | Misma base. |
| Satélites que faltan para 2029 | 3.232 − 396 = 2.836 | DA 26-553 ¶3; #2. |
| Ritmo observado | 15 misiones en ≈ 18,6 meses = ≈ 0,8 por mes | #2 (del 28/04/2025 al 15/11/2026). |
| Horizonte hasta el hito final | ≈ 32,5 meses | Del 16/11/2026 al 30/07/2029. |

#### 4.2 Riesgos desarrollados

##### R-04 — Que la FCC no conceda un nuevo alivio del hito de 2029

**Por qué se reformuló.** En la primera versión el evento era "no cumplir el hito de 2029" con P = 0,70, pero el análisis cuantitativo (sección 5) da una probabilidad de no llegar a 3.232 por cadencia de ≈ 100%. Un evento casi seguro no es un riesgo: es una **condición prevista** que el plan tiene que absorber. La incertidumbre real está en la respuesta del regulador. Por eso el evento ahora es que la FCC **no** conceda una prórroga o un waiver. La probabilidad de 0,70 que eligió el grupo mide eso directamente: ≈ 30% de que haya un nuevo alivio, como en 2026 (DA 26-553).

**[INFERENCIA DEL GRUPO] Condición prevista (no riesgo):** con la cadencia observada o planificada, Amazon llegaría al 30/07/2029 con ≈ 1.140–2.050 satélites (P10–P90, sección 5), lejos de 3.232. Esta brecha se trata como supuesto de planificación del cronograma maestro y del caso de negocio, no como evento incierto.
→ Base: sección 5; DA 26-553 ¶3. Supuestos: los de la sección 5.

| Campo | Contenido |
|---|---|
| Categoría y tipo | Externo → Regulación. Amenaza. Objetivo afectado: alcance (principal) y costo (fianza). |
| Descripción | Debido a que Amazon llegaría al 30/07/2029 con unos 1.500 a 2.000 de los 3.232 satélites (condición prevista), puede ocurrir que la FCC no conceda una nueva prórroga o waiver, lo que reduciría la autorización a los satélites operativos ese día y expondría la pérdida de la fianza. |
| Base | `[DATO REAL]` Hito final de 3.232 satélites al 30/07/2029; si falla, la autorización se reduce al número operativo (DA 26-553 ¶3, ¶12); el incumplimiento de un hito implica pérdida de la fianza (DA 24-224 ¶53; DA 26-553 ¶18). `[DATO REAL]` Amazon planifica "20+ misiones" en el "año dos del despliegue" y dice haber estado en camino a 11 lanzamientos en el primer año (#23); el texto no fecha esos años (se infiere que el año uno empieza con la misión KA-01, el 28/04/2025). `[INFERENCIA DEL GRUPO]` A 20 misiones por año durante 32,5 meses, con ≈ 30 satélites por misión, se agregarían ≈ 1.600–1.700 satélites y se llegaría a ≈ 2.050 (≈ 63% de 3.232). Desde el 28/04/2026 hubo 6 misiones en ≈ 6,5 meses (≈ 11 por año), la mitad de lo planificado (#2). Supuestos: se sostiene el ritmo planificado desde hoy; ≈ 30 satélites por misión (rango 24–40). |
| Probabilidad | **0,70** `[PROPUESTA DE GESTIÓN]`: probabilidad de que la FCC **no** conceda un nuevo alivio. A favor de un alivio (≈ 30%): la FCC ya concedió un waiver parcial en 2026 (DA 26-553 ¶11); Amazon tiene capacidad de fábrica declarada de hasta 30 satélites por semana, limitada por los lanzadores (#23), y más de 100 misiones contratadas (#23), que sirven de evidencia de esfuerzo. En contra (≈ 70%): el waiver de 2026 fue **parcial** y la FCC mantuvo intacto el hito de 2029 y la fianza (DA 26-553 ¶11, ¶18); la brecha a cubrir es grande (hacen falta ≈ 35 misiones por año contra un plan de 20 y un ritmo observado de ≈ 11, #23, #2). Supuesto declarado: no hay un dato que permita estimar la conducta futura de la FCC; el 30% es juicio del grupo basado en el único precedente. |
| Impacto | **0,40 (alto)** `[PROPUESTA DE GESTIÓN]`. Quedar en ≈ 2.050 significaría perder ≈ 1.180 satélites autorizados (≈ 37%). En la escala de alcance, "inaceptable" = 0,40. Amazon dijo que cumpliría el 100% para el 30/07/2029 y pidió un waiver en vez de resignar satélites (DA 26-553 ¶8, ¶11) `[DATO REAL]`; de ahí se infiere que no consideraría aceptable una constelación parcial `[INFERENCIA DEL GRUPO]`, aunque Amazon no lo dice. |
| Exposición | 0,70 × 0,40 = **0,28. Rojo.** |
| Estrategia | **Mitigar** `[PROPUESTA DE GESTIÓN]`. Evitar implicaría resignar alcance, que Amazon dijo no aceptar; transferir no aplica a un hito regulatorio; aceptar no corresponde con una exposición de 0,28 (la cátedra la reserva para cuando responder cuesta más que el daño). |
| Respuesta | (1) Preparar y presentar a tiempo un nuevo pedido de extensión o waiver, con evidencia de avance (respuesta principal: actúa sobre la probabilidad). (2) Acelerar la cadencia todo lo posible: no alcanza para llegar a 3.232, pero achica la brecha y fortalece el pedido. (3) Reportar a la FCC la capacidad construida y los lanzamientos contratados. |
| Propietario | Chief Global Affairs and Legal Officer de Amazon (rol que figura en #33). Propuesta del grupo. |
| Disparador | La cadencia de los últimos 6 meses queda por debajo de la necesaria; nuevo atraso de un lanzador (R-02); la FCC cambia la política de hitos o rechaza un pedido de otro operador. |
| Después de responder | P 0,50 × C 0,40 = **0,20. Sigue en rojo:** un pedido bien fundado puede mejorar las chances, pero la decisión es del regulador y la brecha de cadencia sigue siendo grande. |
| Residual y secundario | Residual: la brecha de cadencia. Secundario: acelerar aumenta el riesgo técnico (R-01) y presiona la fabricación. |
| Costo de la respuesta y reserva | No calculable: el monto de la fianza y el costo de ampliar la cadencia no son públicos. |

##### R-02 — Lanzador clave en tierra, con manifiesto concentrado

| Campo | Contenido |
|---|---|
| Categoría y tipo | Gestión → Proveedores y contratos. Amenaza. Objetivo afectado: plazo. |
| Descripción | Debido a que Vulcan y New Glenn concentran ≈ 66% de los lanzamientos que quedan por hacer, y a que Vulcan acaba de fallar y New Glenn todavía no voló para Leo, puede ocurrir que alguno o ambos queden fuera de servicio por seis meses o más, lo que frenaría la cadencia de despliegue y atrasaría los hitos. |
| Base | `[DATO REAL]` Vulcan estuvo ≈ 9 meses en tierra antes de LV-01 (#12) y falló el 15/11/2026 (#2, #11). `[DATO REAL]` New Glenn explotó en su plataforma de Cabo Cañaveral durante una prueba de encendido el 28/05/2026, con causa no determinada al momento de la nota (#47). `[DATO REAL]` Amazon tiene 38 Vulcan y 24 New Glenn contratados (#3, #23) y dice que ajustó sus metas semanales de producción según la disponibilidad de lanzadores (#23): el lanzamiento es el cuello de botella. El 66% es inferencia (sección 4.1). |
| Probabilidad | **0,50** `[PROPUESTA DE GESTIÓN]`. Hay un precedente de una parada de ≈ 9 meses (#12), la causa de la falla actual no se conoce y New Glenn no tiene vuelos de Leo. |
| Impacto | **0,40 (alto)** `[PROPUESTA DE GESTIÓN]`. Seis meses fuera de servicio de ≈ 66% de la capacidad restante equivalen a ≈ 4 meses de cadencia total (6 × 0,66 ≈ 3,96), es decir ≈ 12% del horizonte de 32,5 meses. La escala de plazo marca 10–20% como alto. Supone que el resto de los lanzadores no puede absorber el atraso. |
| Exposición | 0,50 × 0,40 = **0,20. Rojo** (justo en el corte; con P = 0,40 pasaría a amarillo). |
| Estrategia | **Mitigar** `[PROPUESTA DE GESTIÓN]`: reasignar misiones a los lanzadores disponibles (Ariane 6, Falcon 9) y negociar cupos adicionales (OP-1). |
| Respuesta | (1) Priorizar los lanzamientos de Ariane 6 y Falcon 9 mientras se investiga la falla. (2) Pedir a ULA y a Blue Origin fechas de retorno al vuelo. (3) Evaluar nuevos contratos de capacidad. |
| Propietario | Director/a de sistemas de lanzamiento de Amazon Leo (rol que figura en #3). Propuesta del grupo. |
| Disparador | ULA no informa fecha de retorno al vuelo a los 3 meses de la falla; New Glenn sigue sin volar; un segundo evento en cualquiera de los dos. Al 16/11/2026 ULA no había publicado causa raíz ni fecha de retorno. |
| Después de responder | P 0,50 × C 0,20 = **0,10. Amarillo.** Se supone que Ariane 6 y Falcon 9 absorben parte del atraso (≈ 34% del manifiesto restante no depende de Vulcan ni de New Glenn). |
| Residual y secundario | Residual: sigue habiendo dependencia fuerte de Vulcan y New Glenn. Secundario: concentrar la cadencia en Ariane 6 y Falcon 9 los expone a sus propios incidentes y a cupos limitados. |
| Reserva | Reserva de tiempo del orden de 4 meses en el cronograma maestro, a conciliar con el área de tiempos. Costo: no público. |

##### R-03 — Desvío del cronograma de despliegue y del inicio del servicio

| Campo | Contenido |
|---|---|
| Categoría y tipo | Gestión → Cronograma. Amenaza. Objetivo afectado: plazo. |
| Descripción | Debido a que Amazon lleva un ritmo de ≈ 0,8 misiones por mes, muy inferior al plan, y a que ya perdió 40 satélites, puede ocurrir que el inicio del servicio comercial se postergue otra vez más allá de fin de 2026, lo que retrasaría los ingresos y los acuerdos que dependen del servicio. |
| Base | `[DATO REAL]` ≈ 396 satélites contra ≈ 700 proyectados al 30/07/2026 (DA 26-553 ¶8; #2). `[DATO REAL]` El inicio del servicio se fue corriendo: primeros clientes "later that year" en 2023 (#30), servicio "next year" en 2024 (#26), "broader rollout next year" en 2025 (#29) y "later this year" el 09/11/2026 (#3). `[INFERENCIA DEL GRUPO]` Se supone que las cuatro frases se refieren al mismo hito, el inicio del servicio comercial. |
| Probabilidad | **0,70** `[PROPUESTA DE GESTIÓN]`. Quedan ≈ 6 semanas del año, no hay anuncio de lanzamiento comercial y se acaba de perder una misión de 40 satélites. |
| Impacto | **0,20 (moderado)** `[PROPUESTA DE GESTIÓN]`. Cada postergación previa fue de ≈ 1 año; sobre un horizonte de ≈ 10 años (anuncio en 2019, hito final en 2029) es ≈ 10% del cronograma, en el límite entre moderado y alto. Se elige moderado porque otra postergación podría ser menor a un año. |
| Exposición | 0,70 × 0,20 = **0,14. Amarillo.** |
| Estrategia | **Mitigar** `[PROPUESTA DE GESTIÓN]`: iniciar el servicio por regiones y con clientes empresariales mientras sigue el despliegue (hoy hay un "private preview", #35). |
| Respuesta | (1) Definir un criterio de inicio por región (satélites mínimos y cobertura). (2) Comunicar fechas con margen a los socios. (3) Reportar el avance contra el plan y no contra metas aspiracionales. |
| Propietario | VP de negocio y producto de Amazon Leo (rol que figura en #24). Propuesta del grupo. |
| Disparador | Llegar al 30/11/2026 sin anuncio de servicio; una nueva falla de lanzamiento; cadencia mensual por debajo de lo planificado. |
| Después de responder | P 0,70 × C 0,10 = **0,07. Verde.** El inicio parcial reduce el impacto de una demora total. |
| Residual y secundario | Residual: el servicio inicial tendría cobertura limitada. Secundario: lanzar con poca cobertura puede dañar la reputación del servicio. |

##### R-01 — Pérdida de satélites por falla de un lanzador (recurrencia)

**El evento ya ocurrió una vez.** El 15/11/2026 la misión LV-01 falló y se perdieron 40 satélites (#2, #11). Lo que ocurrió deja de ser un riesgo y pasa a ser un **tema** (problema a resolver), que se gestiona en el registro de Resolución de Temas de la sección 7.1 (tema T-01), según la Clase 6 de la cátedra. Esta ficha mide desde ahora la **recurrencia**: que vuelva a pasar en las misiones siguientes.

**[INFERENCIA DEL GRUPO] Por qué R-01 queda en azul aunque se haya materializado.** La consecuencia grave de la falla no son los 40 satélites, sino que el cohete quede en tierra y frene la cadencia. Ese daño se mide en R-02, que está en rojo. Si se sumara también acá, se contaría dos veces. Lo que mide R-01 es la reposición de los satélites perdidos, y en plazo eso equivale a ≈ 1,3 semanas de fábrica (ver Impacto). La ficha tiene un punto débil, que el grupo debe poder defender: el costo de un satélite no es público. Con un costo unitario alto, el impacto en costo subiría a moderado (0,20), la exposición a 0,06 y R-01 pasaría a verde.
→ Base: #2, #11, #23. Supuesto: la separación entre R-01 (pérdida de carga) y R-02 (cohete en tierra) se mantiene en todo el registro.

| Campo | Contenido |
|---|---|
| Categoría y tipo | Técnico → Lanzamiento. Amenaza. Objetivo afectado: costo (principal) y plazo (secundario; el plazo por paralización del cohete se trata en R-02). |
| Estado | **Materializado una vez (15/11/2026) → tema T-01 abierto.** El riesgo de recurrencia sigue activo. |
| Descripción | Debido a que la causa raíz de la falla del 15/11/2026 no es pública y que Vulcan tiene aún 37 lanzamientos contratados con Amazon, puede ocurrir una nueva falla en otra misión, lo que provocaría la pérdida de los satélites a bordo (unos 40 por misión) y obligaría a reponerlos. |
| Base | `[DATO REAL]` El 15/11/2026 el Vulcan falló unos 10 minutos tras el despegue y se perdieron 40 satélites; causa raíz no publicada (#11, #2). Los 37 restantes son un supuesto: que los 38 Vulcan contratados (#3) siguen vigentes. |
| Probabilidad | **0,30 por misión Vulcan** `[PROPUESTA DE GESTIÓN]`. Se estima P = 0,30 porque la frecuencia observada es 0,20 (1 en 5 vuelos, #11), pero con una muestra tan chica de apenas cinco lanzamientos la tasa empírica es poco confiable, y al no haberse resuelto aún la causa raíz persiste una incertidumbre técnica que aumenta el riesgo de recurrencia hasta que se aplique una corrección. |
| Impacto | **0,10 (bajo)** `[PROPUESTA DE GESTIÓN]`. Plazo: 40 satélites son el 1,2% de los 3.232 y reponerlos equivale a ≈ 1,3 semanas de la capacidad de fabricación declarada de 30 por semana (#23), contra ≈ 140 semanas hasta el hito; es insignificante en la escala de plazo. Costo: el valor de un satélite no es público, por lo que no puede expresarse como porcentaje del costo del proyecto; se supone que cae en la franja baja. Punto débil de la ficha: si se estimara un costo unitario alto, el impacto debería subir. |
| Exposición | 0,30 × 0,10 = **0,03. Azul.** Queda azul porque el mayor daño de plazo, que el cohete quede en tierra, se mide en R-02. |
| Estrategia | **Aceptar (activa)** `[PROPUESTA DE GESTIÓN]`: con exposición muy baja, la cátedra indica aceptar; se elige la forma activa porque el riesgo ya ocurrió una vez y hay disparadores concretos. |
| Respuesta | Plan de contingencia: (1) reponer los 40 satélites desde el stock o la producción de Kirkland; (2) reasignar misiones siguientes a otros lanzadores ya contratados; (3) pedir a ULA el resultado de la investigación y las acciones correctivas. |
| Propietario y disparador | Director/a de sistemas de lanzamiento (rol en #3). Disparadores: una anomalía en un vuelo Vulcan; un hold sin explicar en la cuenta regresiva (como el de T-20 s del 15/11, #11); que ULA no publique la causa raíz antes del siguiente vuelo. |
| Reserva | Contingencia, en unidades: reposición de 40 satélites. Monto en dólares: no público. |
| Residual y secundario | Residual: el cohete queda en tierra (R-02). Secundario: usar stock para reponer reduce la disponibilidad para otras misiones. |

#### 4.3 Lista de seguimiento de riesgos de baja prioridad

La cátedra prevé esta lista para los riesgos de severidad baja: se vigilan sin desarrollar una respuesta completa. Si un disparador se activa, el riesgo pasa al registro. Los valores son `[PROPUESTA DE GESTIÓN]` con poca evidencia dura, como indica la última columna.

| ID | Riesgo | P | C | ER | Color | Qué se vigila | Límite de la evidencia |
|---|---|---|---|---|---|---|---|
| R-05 | Pérdida temporal de prioridad de espectro hasta el 30/03/2028 (DA 26-553 ¶15): un sistema con prioridad o una nueva ronda de procesamiento podría limitar su espectro y reducir la capacidad del servicio inicial. | 0,30 | 0,20 | 0,06 | Verde | Que la FCC abra una ronda; pedidos de coordinación; la fecha del 30/10/2027, a la que se acorta la pérdida si Amazon certifica que construyó el 50% y contrató lanzamientos. | La condición está activa `[DATO REAL]`; que el hito no se cumplió es inferencia (≈ 396 satélites al 30/07/2026, sin lanzamientos entre el 02/07 y el 15/11, #2). No hay evidencia de una ronda abierta ni de cuánto espectro está en juego. |
| R-06 | Dependencia de socios locales (Herotel #33, UZ-SAT #35, Vanu #32, DIRECTV y Sky Brasil #37, NBN Co #40): un socio podría no lanzar el servicio en fecha, demorando los ingresos de esa región. | 0,50 | 0,10 | 0,05 | Verde | Que un socio no confirme fecha; que el servicio de Amazon se postergue (R-03). | Al 16/11/2026 no se encontró confirmación de que NBN Co haya lanzado el servicio previsto desde mediados de 2026. El valor está justo en el corte con azul. |
| R-07 | Aprobaciones regulatorias externas: la compra de Globalstar (cierre previsto en 2027, #22) y las licencias por país podrían demorarse y retrasar el servicio direct-to-device desde 2028 o el inicio en algún país. | 0,30 | 0,20 | 0,06 | Verde | Que un regulador pida información adicional; que el cierre de Globalstar se corra. | No hay datos del estado de Globalstar ni de las licencias por país; solo se vio la solicitud de Kenia por prensa (#18). |

#### 4.4 Oportunidades

La cátedra reconoce que el riesgo puede ser una oportunidad, pero el material no desarrolla estrategias específicas para oportunidades. Para OP-1 se propone "aprovechar", un criterio externo a la cátedra.

**OP-1 — Capacidad de lanzamiento ampliada y diversificada.** Debido a que Amazon sumó 6 lanzamientos de Ariane 6 y 10 de Falcon 9, puede ocurrir que esa capacidad permita sostener la cadencia aunque Vulcan o New Glenn estén en tierra, lo que reduciría el atraso. `[DATO REAL]` Ariane 6 pasó de 18 a 24 lanzamientos (#24) y entregó 100 satélites en tres misiones en menos de cinco meses (#24); se contrataron 10 Falcon 9 adicionales a fines de 2025 (#23). `[INFERENCIA DEL GRUPO]` ≈ 34% del manifiesto restante no depende de Vulcan ni de New Glenn. `[PROPUESTA DE GESTIÓN]` P 0,70 × beneficio 0,20 = +0,14. Es la respuesta de mitigación de R-02. Propietario: director/a de sistemas de lanzamiento.

**OP-2 — Demanda comercial (solo mencionada).** Hay acuerdos con JetBlue (desde 2027, #36), Delta (desde 2028, 500 aviones, #31) y con Apple y Globalstar para direct-to-device (desde 2028, #22). No se desarrolla porque no hay datos de ingresos y depende de que el servicio inicie (R-03).

#### 4.5 Matriz de probabilidad e impacto

Matriz de la cátedra con los cortes de la sección 2.4. [R] rojo, [A] amarillo, [V] verde, [Az] azul. En negrita, dónde cae cada riesgo.

| P \ I | 0,05 | 0,10 | 0,20 | 0,40 | 0,80 |
|---|---|---|---|---|---|
| 0,90 | 0,05 [V] | 0,09 [V] | 0,18 [A] | 0,36 [R] | 0,72 [R] |
| 0,70 | 0,04 [Az] | 0,07 [V] | **R-03** 0,14 [A] | **R-04** 0,28 [R] | 0,56 [R] |
| 0,50 | 0,03 [Az] | **R-06** 0,05 [V] | 0,10 [A] | **R-02** 0,20 [R] | 0,40 [R] |
| 0,30 | 0,02 [Az] | **R-01** 0,03 [Az] | **R-05, R-07** 0,06 [V] | 0,12 [A] | 0,24 [R] |
| 0,10 | 0,01 [Az] | 0,01 [Az] | 0,02 [Az] | 0,04 [Az] | 0,08 [V] |

**Priorización:** 1.º R-04 (0,28, rojo); 2.º R-02 (0,20, rojo); 3.º R-03 (0,14, amarillo); 4.º R-05 y R-07 (0,06, verdes); 6.º R-06 (0,05, verde); 7.º R-01 (0,03, azul). Los dos rojos son los de respuesta urgente.

**[INFERENCIA DEL GRUPO]** El riesgo se concentra en regulación (suma de ER de los riesgos externos: 0,40) y en gestión de proveedores y cronograma (0,34), no en lo técnico (0,03) ni en la organización (0,05). Es coherente con el objetivo elegido. Los tres riesgos más altos forman una cadena: un lanzador en tierra (R-02) frena la cadencia, eso retrasa el servicio (R-03) y, si se prolonga, compromete el hito de 2029 (R-04).
→ Base: sección 4.2. Supuesto: la suma de ER entre riesgos es una referencia relativa, no una medida monetaria, porque el impacto está en una escala y no en dólares.

### 5. Análisis cuantitativo

La cátedra propone la simulación de Monte Carlo para estimar la probabilidad de cumplir un objetivo. Amazon no publica su red de actividades ni sus duraciones, así que no se puede simular el cronograma interno. Con datos públicos sí se puede simular **la cantidad de satélites operativos al 30/07/2029**, que es la medida del hito de R-04. El código está en el anexo B y es reproducible.

**Datos de entrada** `[DATO REAL]`: 396 satélites lanzados antes de LV-01 (#2); hito final de 3.232 (DA 26-553 ¶3); 32,5 meses hasta el 30/07/2029. Se usan lanzados como aproximación de operativos (sección 4.1), así que el resultado es un techo optimista.

**Supuestos** `[PROPUESTA DE GESTIÓN]`:
- Cadencia en misiones por mes, distribución triangular: mínimo 0,5 (lanzadores clave en tierra buena parte del período), moda 0,92 (ritmo observado desde el 28/04/2026, ≈ 11 por año) y máximo 2,0 (el plan de "20+ misiones" y algo más).
- Satélites por misión, triangular: mínimo 24, moda 30, máximo 40 (rango de #2 y #3).
- La cadencia se mantiene constante (no se modela una aceleración gradual).

**Escenarios** `[INFERENCIA DEL GRUPO]` (30 satélites por misión):

| Escenario | Misiones por año | Satélites al 30/07/2029 | % de 3.232 |
|---|---|---|---|
| Ritmo observado | 11 | ≈ 1.290 | 40% |
| Plan de Amazon | 20 | ≈ 2.020 | 63% |
| Ritmo necesario | 35 | ≈ 3.240 | 100% |

Con 40 satélites por misión, el plan de 20 por año llegaría a ≈ 2.560 (79%) y la cadencia necesaria bajaría a ≈ 26 por año, todavía por encima del plan.

**Resultado de la simulación** (100.000 corridas):

| Percentil | Satélites al 30/07/2029 | % de 3.232 |
|---|---|---|
| P10 | ≈ 1.140 | 35% |
| P50 | ≈ 1.510 | 47% |
| P90 | ≈ 2.050 | 63% |
| Probabilidad de llegar a 3.232 | ≈ 0% | |

Con un máximo de cadencia de 3,5 misiones por mes (más del triple del ritmo observado), la probabilidad de llegar sube solo a ≈ 7%.

**[INFERENCIA DEL GRUPO]** Con la cadencia observada o con la del propio plan de Amazon, llegar a 3.232 satélites antes del 30/07/2029 es prácticamente imposible. Llegar exigiría ≈ 35 misiones por año: 3 veces el ritmo observado y casi el doble del plan.
→ Limitaciones: el modelo ignora una posible aceleración gradual; usa un promedio de satélites por misión; no incluye fallas de lanzamiento (que empeorarían el resultado); las distribuciones son supuestos del grupo.

**Consecuencia para R-04:** como la probabilidad de no llegar es ≈ 1, no llegar se trata como condición prevista y R-04 se formula sobre la decisión de la FCC (sección 4.2). Este análisis no calcula reservas de costo porque falta el presupuesto.

### 6. Respuestas, reservas y efecto

| ID | ER antes | ER después | Tratamiento |
|---|---|---|---|
| R-04 | 0,28 | 0,20 | Mitigar |
| R-02 | 0,20 | 0,10 | Mitigar |
| R-03 | 0,14 | 0,07 | Mitigar |
| R-05 | 0,06 | 0,03 | Seguimiento |
| R-06 | 0,05 | 0,03 | Seguimiento |
| R-07 | 0,06 | 0,04 | Seguimiento |
| R-01 | 0,03 | 0,03 | Aceptar (activa) |
| **Suma** | **0,82** | **0,50** | |

**[INFERENCIA DEL GRUPO]** Las respuestas propuestas bajan la exposición total ≈ 39%, pero R-04 sigue en rojo. Los valores "después" son propuestas del grupo, no mediciones.

**Reservas** `[PROPUESTA DE GESTIÓN]`. La cátedra distingue reservas de contingencia (riesgos conocidos, parte de la línea base) y gerenciales (riesgos desconocidos, fuera de la línea base de costos):
- R-01: contingencia en unidades, reposición de 40 satélites.
- R-02: contingencia de tiempo, ≈ 4 meses en el cronograma maestro.
- R-03: contingencia de tiempo, a definir con el área de tiempos.
- R-04: contingencia de costo para la fianza y la ampliación de cadencia; monto no público.
- Reserva gerencial para riesgos desconocidos: porcentaje a definir con el área de costos.

**Doble cuenta.** La reserva de tiempo de R-02 alimenta el atraso de R-03 y de R-04; si se suman sin más, el cronograma queda inflado. Debe acordarse con el área de tiempos antes de fijar números.

**Índice de riesgo y apalancamiento.** La cátedra los define como Σ ER ÷ costo total del proyecto y como (ER antes − ER después) ÷ costo de la alternativa. No se pueden calcular: el impacto está en escala, no en dólares, y no existe un presupuesto público ni el costo de las alternativas.

### 7. Seguimiento y control

#### 7.1 Riesgos materializados: registro de Resolución de Temas

Cuando un riesgo ocurre deja de ser incierto: pasa a ser un **tema** (problema) y se gestiona con el formulario de Resolución de Temas y el Log de temas pendientes de la cátedra (`catedra/Clase 6 Seguimiento y Valor Ganado`, PPT págs. 12–13).

**Tema T-01 — Pérdida de la misión LV-01 (Vulcan, 40 satélites)** `[PROPUESTA DE GESTIÓN]` con base `[DATO REAL]`

| Campo (cátedra) | Contenido |
|---|---|
| N.° · Título · Fecha | T-01 · Pérdida de LV-01 · 15/11/2026 |
| Fuente | Riesgo R-01 del registro, materializado. `[DATO REAL]` ULA informó una anomalía ≈ 10 minutos después del despegue y Amazon confirmó que "the payload was lost" (#2, #11). |
| Descripción | Se perdieron 40 satélites en el primer vuelo de Vulcan para Amazon (1 de 38 contratados). Causa raíz no publicada al 16/11/2026 (#11). |
| Evaluación y recomendaciones | `[INFERENCIA DEL GRUPO]` El daño directo (40 satélites, ≈ 1,2% de 3.232) es acotado. El daño indirecto es el cohete en tierra, que activa el disparador de R-02 y agrava R-03 y R-04. Se recomienda ejecutar el plan de contingencia de R-01 y la respuesta de R-02 al mismo tiempo. |
| Impacto | Satélites en órbita sin cambios (≈ 396); se pierde la misión que los llevaba a ≈ 436 (#11). Cadencia: Vulcan sin fecha de retorno (#11). |
| Decisión | `[PROPUESTA DE GESTIÓN]` (1) Reponer los 40 satélites con producción de Kirkland. (2) Reasignar las próximas misiones a Ariane 6 y Falcon 9 (LE-04 sigue programada para no antes del 23/11/2026, #2). (3) Exigir a ULA el informe de causa raíz antes de volver a cargar satélites en Vulcan. (4) Reevaluar R-01, R-02, R-03 y R-04 con cada novedad de ULA (sección 7.2, "Reevaluación"). |
| Aprobó · Responsable · Estado | Responsable propuesto: director/a de sistemas de lanzamiento de Amazon Leo (rol en #3). Estado: **abierto**. Se cierra cuando ULA publique la causa raíz y Vulcan vuelva a volar sin anomalías. |

**Log de temas pendientes** `[PROPUESTA DE GESTIÓN]`

| N.° | Tema | Abierto | Responsable | Próxima acción | Estado |
|---|---|---|---|---|---|
| T-01 | Pérdida de LV-01 | 15/11/2026 | Sistemas de lanzamiento | Causa raíz de ULA; reasignación del manifiesto | Abierto |

#### 7.2 Indicadores a vigilar

**Indicadores a vigilar** `[PROPUESTA DE GESTIÓN]`:

| Indicador | Riesgo | Umbral que activa la respuesta | Fuente | Frecuencia |
|---|---|---|---|---|
| Anomalía o hold sin explicar en un vuelo Vulcan | R-01, R-02 | Cualquier anomalía | ULA; Amazon (#2) | Por misión |
| Fecha de retorno al vuelo de Vulcan y de New Glenn | R-02 | Sin fecha a los 3 meses de la falla | ULA; Blue Origin; Amazon | Mensual |
| Cadencia de los últimos 6 meses | R-04 | Menos de ≈ 17 misiones en 6 meses | Lista de misiones (#2) | Mensual |
| Satélites operativos por mes | R-04 | Menos de ≈ 87 por mes | Lista de misiones (#2) | Mensual |
| Anuncio del servicio comercial | R-03 | Sin anuncio al 30/11/2026 | Amazon | Puntual |
| Nueva ronda de la FCC o pedido de coordinación | R-05 | Cualquiera | FCC | Trimestral |
| Certificación del 50% construido | R-05 | Antes del 30/10/2027 | FCC (DA 26-553 ¶15) | Trimestral |
| Fecha confirmada por cada socio | R-06 | Un socio sin fecha | Amazon; socios | Trimestral |
| Avance de la aprobación de Globalstar | R-07 | Cierre corrido más allá de 2027 | Amazon (#22) | Trimestral |

**[INFERENCIA DEL GRUPO]** Para llegar a 3.232 desde 396 faltan 2.836 satélites en ≈ 32,5 meses, es decir ≈ 87 por mes. El ritmo observado es ≈ 21 por mes (396 en ≈ 18,6 meses). Los umbrales de cadencia salen de 35 misiones por año ÷ 2 = ≈ 17 por semestre.
→ Base: DA 26-553 ¶3; #2. Supuesto: el hito final es el 30/07/2029 y el ritmo se mide como promedio lineal.

**Reevaluación** `[PROPUESTA DE GESTIÓN]`: reestimar probabilidad e impacto cada trimestre y después de cada evento (una falla, un anuncio de la FCC, un cambio de calendario), y comparar la exposición nueva con la inicial.

**Supuestos a revisar durante el proyecto:**

| Supuesto | Riesgo que lo usa | Se invalida si |
|---|---|---|
| Los 38 Vulcan y los 24 New Glenn siguen contratados | R-01, R-02 | Amazon cancela o reasigna contratos |
| ≈ 30 satélites por misión | R-04, sección 5 | Cambia el tamaño de los lotes |
| Lanzados ≈ operativos | Todos | Amazon o la FCC publican un conteo de operativos menor |
| Sin aceleración fuerte, la cadencia no alcanza para 3.232 (condición prevista) | R-04, sección 5 | La cadencia de 6 meses supera ≈ 17 misiones |
| ≈ 30% de chances de un nuevo alivio de la FCC | R-04 | La FCC se pronuncia sobre un pedido de Amazon o de otro operador |
| El hito de 2026 no se cumplió | R-05 | Amazon demuestra otro conteo |
| Las frases sobre el inicio del servicio se refieren al mismo hito | R-03 | Amazon define dos hitos distintos |

**Criterios de cierre** `[PROPUESTA DE GESTIÓN]`: R-02 se cierra cuando Vulcan y New Glenn completen dos misiones consecutivas sin anomalías cada uno; R-03 al lanzarse el servicio comercial; R-04 cuando la FCC resuelva un pedido de alivio, cuando Amazon alcance 3.232 satélites operativos o el 30/07/2029, lo que ocurra primero; R-05 el 30/03/2028 (o antes si Amazon alcanza el 50% operativo); los demás si el disparador no se activa durante un año.

**Conexión con seguimiento y valor ganado** `[INFERENCIA DEL GRUPO]`: si el avance se mide en satélites operativos, Amazon proyectó ≈ 700 al 30/07/2026 (DA 26-553 ¶8) y había ≈ 396; el índice de desempeño del cronograma (SPI) sería ≈ 0,57 (396 ÷ 700). Supuestos: los satélites operativos son una medida de avance válida; ≈ 700 fue el plan de Amazon para esa fecha; no hubo lanzamientos entre el 02/07 y el 15/11 (#2).

**Eficacia de la gestión.** El indicador cualitativo disponible es la exposición total antes (0,82) y después de responder (0,50), y la cantidad de rojos (2 antes, 1 después). El ROI de la gestión de riesgos requiere montos en dólares y no puede calcularse.

### 8. Limitaciones y datos pendientes

**Datos no públicos.** Costo de un satélite, monto de la fianza, costo de cada respuesta y reserva gerencial. No se completaron con cifras inventadas; estimarlos requiere supuestos escritos del grupo. Sin ellos no se pueden calcular el índice de riesgo, el apalancamiento ni el ROI.

**Lo que no pudo verificarse** (búsqueda del 16/11/2026): si la FCC ejecutó la pérdida de la fianza; si NBN Co lanzó su servicio; la causa raíz de la falla de Vulcan y su fecha de retorno al vuelo; el estado de las licencias por país y de la compra de Globalstar.

**Dependencias con otras áreas del informe.**
- Presupuesto (costos): para calcular el índice de riesgo, el apalancamiento y las reservas en dólares.
- Cronograma (tiempos): para fijar las reservas de tiempo sin doble cuenta.
- Unidad y valores de avance (seguimiento y valor ganado): para usar los mismos satélites y el mismo índice.
- EDT (alcance): para reflejar lo que cambia el alcance en R-04.

**Naturaleza de las fuentes.** La mayor parte proviene de comunicados de Amazon, es decir de declaraciones de la propia empresa; las resoluciones de la FCC son documentos primarios leídos en su texto. El original de la orden FCC 20-102 (2020) no pudo leerse y se usó una reproducción parcial para los datos de esa fecha.

### Apéndice R-A. Fuentes citadas

Todas consultadas el 16/11/2026. Las rutas de Amazon son relativas a `https://www.aboutamazon.com`.

| # | Fuente | Ruta o URL | Publicada | Tipo |
|---|---|---|---|---|
| DA 26-553 | FCC, Order sobre el waiver del hito | https://docs.fcc.gov/public/attachments/DA-26-553A1.txt | 05/06/2026 | Primaria (leída) |
| DA 24-224 | FCC, Order and Authorization | https://docs.fcc.gov/public/attachments/DA-24-224A1.pdf | 08/03/2024 | Primaria (leída) |
| 2 | Amazon, Mission updates | /news/innovation-at-amazon/project-kuiper-satellite-rocket-launch-progress-updates | actualizada 15/11/2026 | Primaria |
| 3 | Amazon, primera misión Vulcan | /news/amazon-leo/amazon-leo-vulcan-satellites-launch | 09/11/2026 | Primaria |
| 4 | Amazon, inversión en lanzamientos | /news/innovation-at-amazon/amazon-makes-historic-launch-investment-to-advance-project-kuiper | 05/04/2022 | Primaria |
| 11 | Spaceflight Now, falla del Vulcan | https://spaceflightnow.com/2026/11/15/ula-suffers-first-total-mission-failure-with-loss-of-vulcan-rocket-carrying-40-amazon-leo-satellites/ | 15/11/2026 | Prensa especializada |
| 12 | Spaceflight Now, retorno al vuelo de Vulcan | https://spaceflightnow.com/2026/10/28/united-launch-alliance-announces-mid-november-return-to-flight-for-vulcan-rocket/ | 28/10/2026 | Prensa especializada |
| 18 | DCD, estación terrena en Kenia | https://www.datacenterdynamics.com/en/news/amazon-files-to-place-ground-station-in-kenya-report/ | 2026 | Prensa especializada |
| 22 | Amazon, Globalstar y Apple | /news/company-news/amazon-globalstar-apple | 14/04/2026 | Primaria |
| 23 | Amazon, plan de duplicar la cadencia | /news/amazon-leo/amazon-leo-plans-double-launch-rate-20-missions | 23/03/2026 | Primaria |
| 24 | Amazon, Arianespace, 6 lanzamientos nuevos | /news/amazon-leo/amazon-leo-arianespace-new-launches | 10/09/2026 | Primaria |
| 26 | Amazon, dentro de la fábrica de Kirkland | /news/innovation-at-amazon/inside-project-kuiper-satellite-facility-kirkland | 27/06/2024 | Primaria |
| 29 | Amazon, enterprise preview | /news/amazon-leo/amazon-leo-satellite-internet-ultra-pro | 24/11/2025 | Primaria |
| 30 | Amazon, primera vista de terminales | /news/innovation-at-amazon/heres-your-first-look-at-project-kuipers-low-cost-customer-terminals | 14/03/2023 | Primaria |
| 31 | Amazon, Delta | /news/amazon-leo/amazon-leo-delta-in-flight-wifi-2028 | 31/03/2026 | Primaria |
| 32 | Amazon, Vanu | /news/amazon-leo/amazon-leo-vanu-satellite-internet-connectivity-africa | 26/02/2026 | Primaria |
| 33 | Amazon, Herotel | /news/amazon-leo/amazon-leo-south-africa-herotel-evry | 15/07/2026 | Primaria |
| 35 | Amazon, Uzbekistán | /news/amazon-leo/amazon-leo-uzbekistan | 22/09/2026 | Primaria |
| 36 | Amazon, JetBlue | /news/innovation-at-amazon/jetblue-amazon-project-kuiper-in-flight-wifi-partnership | 04/09/2025 | Primaria |
| 37 | Amazon, Sudamérica y DIRECTV | /news/innovation-at-amazon/amazon-project-kuiper-in-south-america | 12/06/2024 | Primaria |
| 38 | Amazon, Falcon 9 con SpaceX | /news/innovation-at-amazon/amazon-project-kuiper-spacex-launch | 01/12/2023 | Primaria |
| 40 | Amazon Australia, NBN Co | https://www.aboutamazon.com.au/news/innovation/project-kuiper-partners-with-nbn-co-to-bring-low-earth-orbit-satellite-broadband-to-rural-australia | 05/08/2025 | Primaria |
| 47 | AP vía OPB, explosión de New Glenn en plataforma | https://www.opb.org/article/2026/05/29/blue-origin-rocket-explodes-on-the-launch-pad-during-an-engine-firing-test/ | 29/05/2026 | Prensa (confirmada por varios medios) |

### Apéndice R-B. Código del análisis cuantitativo

El archivo `analisis_cuantitativo.py` (Python 3, sin dependencias externas) reproduce los resultados de la sección 5 con `python3 analisis_cuantitativo.py`. Usa una semilla fija, por lo que el resultado es repetible. Todos los supuestos están en las constantes del encabezado del archivo.

---

# 12. Seguimiento y valor ganado

> Marco: `catedra/Clase 6 Seguimiento y Valor Ganado · Administración de Proyectos · UCA.html` y `catedra/Valor Agregado.html`. Cálculo: `informe/seguimiento/valor_ganado.py`. Desarrollo metodológico: `informe/guias/seguimiento-valor-ganado.md`.

## 12.1 Medir por el output

La cátedra pide medir el avance **por el output, no por el input** (Clase 6, pág. 21). En Amazon Leo el output es público y verificable: **satélites desplegados**. Por eso el valor ganado se calcula en unidades físicas `[PROPUESTA DE GESTIÓN]`:

| Concepto | Valor | Etiqueta |
|---|---|---|
| BAC | 3.232 satélites | `[DATO REAL]` #8 ¶3 |
| PV | Línea base A (FCC): 1.616 al 30/07/2026 y 3.232 al 30/07/2029, interpolada linealmente entre hitos. Línea base B (plan de Amazon): ≈ 700 al 30/07/2026 | `[DATO REAL]` en los hitos (#8 ¶3, ¶8); interpolación `[PROPUESTA]` |
| EV | Satélites lanzados acumulados | `[INFERENCIA DEL GRUPO]` (suma de #2) |
| AC | No público | — |

**Control de consistencia:** la serie EV suma 180 satélites al 16/12/2025, y Amazon declaró ante la FCC "180 satélites lanzados" el 30/01/2026 (#8 ¶8).

## 12.2 Resultados

`[INFERENCIA DEL GRUPO]` · Vcr = EV − PV · %Vcr = Vcr ÷ PV · SPI = EV ÷ PV

| Corte | Fecha | PV | EV | Vcr | %Vcr | SPI |
|---|---|---|---|---|---|---|
| Hito 50% · línea base A (FCC) | 30/07/2026 | 1.616 | 396 | −1.220 | −75% | **0,25** |
| Hito 50% · línea base B (plan Amazon) | 30/07/2026 | 700 | 396 | −304 | −43% | **0,57** |
| Corte · línea base A interpolada | 16/11/2026 | 1.777 | 396 | −1.381 | −78% | **0,22** |

**Lectura.** Un SPI menor a 1 indica que el proyecto avanza por debajo de lo planificado (Clase 6, pág. 28). Contra su propio plan, Amazon ejecutó el 57%; contra la exigencia del regulador, el 25%. Entre julio y noviembre de 2026 el SPI empeora (0,25 → 0,22) porque no hubo despliegues exitosos mientras el plan seguía avanzando.

**[INFERENCIA DEL GRUPO]** Que el plan de Amazon (~700) estuviera tan por debajo del hito de la FCC (1.616) muestra que **la empresa nunca planificó cumplir el hito intermedio**: pidió el waiver con un plan que ya lo daba por perdido (#8 ¶8).

## 12.3 Proyección: ¿cuándo termina?

| Escenario | Ritmo | Fin | Etiqueta |
|---|---|---|---|
| Ritmo observado (satélites) | 21,3 por mes | ≈ 2038 | `[INFERENCIA DEL GRUPO]` |
| Plan de Amazon (20 misiones/año × 30) | 50 por mes | ≈ 08/2031 | `[INFERENCIA DEL GRUPO]` sobre #23 |
| PERT (sección 9) | — | te ≈ 11/2035 (σ ≈ 24 meses) | `[PROPUESTA DE GESTIÓN]` |
| Necesario para el hito | 87,5 por mes | 30/07/2029 | `[INFERENCIA DEL GRUPO]` |

## 12.4 Costo: lo que no se puede calcular

El **CPI = EV ÷ AC** y la **Vco = EV − AC** requieren el costo real, que no es público. Se deja explícito y no se estima. Lo que sí se puede afirmar de forma cualitativa es la paradoja de "mucho gasto, poco avance": inversiones en instalaciones (> USD 340 millones, #27, #23) y más de 100 lanzamientos contratados con un avance físico del 12,3% (sección 10.4).

## 12.5 Sistema de seguimiento propuesto

`[PROPUESTA DE GESTIÓN]` con los instrumentos de la Clase 6:

| Instrumento | Contenido | Frecuencia |
|---|---|---|
| Informe de situación | EV, PV, SPI, cadencia del mes, causas de desvío, estimado para terminar | Mensual |
| Log de temas pendientes | T-01 (pérdida de LV-01) y los que se abran | Continuo |
| Resolución de temas | Formulario por tema (Riesgos §7.1) | Por evento |
| Reunión de avance con proveedores | Manifiesto y retorno al vuelo | Mensual y por misión |
| Reunión de finalización | Por hito (30/10/2027; 30/07/2029) | Por hito |

**Ante desvíos (Clase 6, pág. 17):** Amazon ya está aplicando "agregar más recursos" (más lanzadores) y "extender los plazos" (pedido a la FCC); "eliminar funciones" (resignar satélites) lo rechazó (#8 ¶8, ¶11). La propuesta del grupo combina las dos primeras con la **línea base de recuperación** (sección 8.6).

---

# 13. Integración y coherencia

> Responde al paso 4 de la consigna ("Conectar: evitar documentos aislados") y a la Integración del Paneo, tema 3 ("que alcance, tiempo, costo y riesgos no se manejen por separado").

## 13.1 La cadena que conecta todo el informe

**[INFERENCIA DEL GRUPO]**

1. **Alcance (7):** la WBS muestra una cadena fabricación → procesamiento → **lanzamiento** → operación, con el cuello de botella en el lanzamiento.
2. **Tiempos y estimaciones (8, 9):** el ritmo real (≈ 21 satélites por mes) es un cuarto del necesario (≈ 87). El hito de 2029 está en la "zona inalcanzable": PERT da ≈ 0,07% y fin ≈ 11/2035.
3. **Valor ganado (12):** SPI 0,22 a 0,57 según la línea base; fin entre 2031 y 2038.
4. **Riesgos (11):** como no llegar es casi seguro (Monte Carlo ≈ 0%), el riesgo principal pasa a ser **regulatorio** (R-04: que la FCC no conceda un nuevo alivio), alimentado por R-02 (lanzadores en tierra), que el 15/11/2026 se activó con T-01.
5. **Respuesta integrada:** línea base de recuperación (≈ 08/2031, sección 8.6) + pedido de alivio con evidencia (R-04) + más capacidad de lanzamiento (OP-1).
6. **Costos (10):** esa respuesta adelanta costos variables (lanzamientos, satélites) y suma la fianza en riesgo. La reserva de contingencia debe cubrirlos.
7. **Caso de negocio y acta (5, 6):** el caso sigue siendo deseable, pero hay que **reevaluarlo** (5.7) y el acta necesitaba un criterio de inicio de servicio verificable que nunca fue público.

## 13.2 Mismas cifras en todas las secciones

| Cifra (Anexo D) | Secciones que la usan | Valor |
|---|---|---|
| C-01 / C-03 BAC e hito final | 5, 6, 7, 8, 11, 12 | 3.232 al 30/07/2029 |
| C-12 Satélites desplegados | 2, 8, 9, 11, 12 | 396 |
| C-21 / C-23 Ritmo observado / necesario | 7, 8, 9, 11, 12 | 21 / 87 por mes |
| C-40 / C-42 Contratos / dependencia | 7, 8, 10, 11 | ≈ 108 / 66% |
| C-35 Compromiso de inversión | 5, 6, 10 | > USD 10.000 millones |
| C-50 Monte Carlo | 9, 11 | P50 ≈ 1.513 |
| C-52 SPI | 11, 12 | 0,57 (plan) |

## 13.3 Control de coherencia hecho

| Verificación | Resultado |
|---|---|
| Serie EV contra la declaración de Amazon a la FCC | 180 = 180 ✔ |
| Monte Carlo, PERT y VG apuntan a la misma conclusión | ✔ (2029 inalcanzable; fin entre 2031 y 2038) |
| Reserva de tiempo de R-02 contada una sola vez | ✔ (sección 8.7) |
| Contratos con la misma cifra en todas las secciones | ✔ (New Glenn = 24; total ≈ 108) |
| Unidad de avance única (lanzados ≈ operativos) | ✔ (declarada en 1.4 y en Riesgos §4.1) |
| Alcance coherente con el BAC y el horizonte de Riesgos | ✔ (Gen1, 3.232, 30/07/2029) |
| Criterio de inicio del servicio | Propuesto en el acta (6) → usado en la WBS (1.9.2), el cronograma (M-10) y R-03 ✔ |

## 13.4 Elaboración progresiva

La cátedra señala que "para relacionar temas, la llave es la **elaboración progresiva**" (Paneo). En este proyecto se ve en tres planos: el alcance (Gen1 detallado; Gen2 y D2D en rolling wave), las estimaciones (ventanas de reestimación en 9.4) y el caso de negocio (que debe actualizarse con el atraso, 5.7).

---

# 14. Conclusiones y limitaciones

## 14.1 Conclusiones

1. **El cuello de botella es el lanzamiento, no la fábrica.** Amazon declara capacidad para hasta 30 satélites por semana y llegó a 1.000 fabricados, pero desplegó 396 a un ritmo de ≈ 21 por mes (secciones 7.4 y 8). `[INFERENCIA DEL GRUPO]`
2. **El hito de 2029 no es alcanzable con la capacidad contratada.** Tres herramientas independientes (Monte Carlo, PERT y valor ganado) coinciden: la probabilidad de llegar a 3.232 satélites al 30/07/2029 es prácticamente nula, y el fin razonable está entre 2031 y 2038 (secciones 9 y 12). `[INFERENCIA DEL GRUPO]`
3. **El riesgo principal es regulatorio, no técnico.** Lo incierto no es si se llega, sino si la FCC concede un nuevo alivio. La gestión debería concentrarse en un pedido fundado en una línea base de recuperación creíble (≈ 08/2031) (secciones 8.6 y 11). `[PROPUESTA DE GESTIÓN]`
4. **Faltó un criterio verificable de inicio del servicio.** El inicio se corrió unos 2 años en cuatro anuncios sin incumplir ningún hito formal. El acta reconstruida lo incorpora (secciones 6 y 4.3). `[PROPUESTA DE GESTIÓN]`
5. **El alcance crece antes de terminar la primera generación** (Gen2, D2D, Globalstar). Se recomienda separar el caso de negocio de Gen1 del de las líneas nuevas y tratarlas con elaboración progresiva (secciones 5.7 y 7.1). `[PROPUESTA DE GESTIÓN]`

## 14.2 Limitaciones

- **Costos:** sin presupuesto ni costos unitarios públicos, no se calculan el CPI, el índice de riesgo ni el apalancamiento (secciones 10 y 12.4).
- **Satélites operativos:** se usan lanzados como aproximación, así que los resultados son optimistas (sección 1.4).
- **Fuentes de la empresa:** la mayoría de los datos de Amazon son declaraciones propias.
- **Datos no verificados:** protoflight de 2023, aviso de cumplimiento del 14/08/2026, licencias por país, cantidad de gateways, estado de NBN Co (Anexo B, §7).
- **Fecha de corte:** 16/11/2026, un día después de la falla de LV-01, sin causa raíz publicada.

## 14.3 Qué haría el equipo con más información

- Leer el 10-K de Amazon para acotar la inversión real y reconstruir un BAC en USD.
- Obtener del expediente de la FCC el aviso de cumplimiento y la respuesta del regulador.
- Reestimar la cadencia al retorno al vuelo de Vulcan y al primer vuelo de New Glenn para Leo (ventanas de la sección 9.4).

---

# Anexo A. Registro de fuentes

## Registro de fuentes — Amazon Leo

Catálogo único de evidencia del trabajo. **Todo `[DATO REAL]` del informe debe referenciar una fila de esta tabla por su `#`.**

Se completa en el checkpoint **I-1** (`/informe:fuentes`) y se amplía en los pasos siguientes.

---

### Taxonomía de fuentes

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

### Tabla de fuentes

> **Nota sobre este primer barrido (I-1):** catálogo inicial para que el equipo arranque, con fecha de consulta 15/11/2026. Varias cifras provienen de **fuentes secundarias** (prensa) que citan documentos primarios (FCC, SEC, comunicados de Amazon): están marcadas con ⚠ y **deben verificarse contra el documento primario** antes de usarse como `[DATO REAL]` en el informe. Las columnas "Publicado" con `≈` son fechas aproximadas a confirmar.

#### A. Oficiales de la organización (Amazon / proveedores)

| # | Fuente (organización, título) | Tipo | URL | Publicado | Consultado | Confiabilidad | Qué dato aporta | Etiqueta |
|---|---|---|---|---|---|---|---|---|
| 1 | Amazon — "Amazon Leo successfully launches first heavy-lift mission of 2026 with Arianespace" | Oficial | https://www.aboutamazon.com/news/amazon-leo/amazon-leo-arianespace-first-mission-satellites | ≈feb 2026 | 15/11/2026 | Alta | Primera misión pesada 2026 con Arianespace (Ariane 6); satélites desplegados por misión. | [DATO REAL] |
| 2 | Amazon — "Amazon Leo mission updates: Launch dates set for next missions on Vulcan and Ariane 6" | Oficial | https://www.aboutamazon.com/news/innovation-at-amazon/project-kuiper-satellite-rocket-launch-progress-updates | actualizada (rolling) | 15/11/2026 | Alta (pero cambia sin aviso) | Calendario oficial de próximas misiones; totales de satélites; hito "1.000ª unidad". Página viva: guardar captura con fecha. | [DATO REAL] |
| 3 | Amazon — "Amazon Leo to launch 40 satellites on its first Vulcan mission" | Oficial | https://www.aboutamazon.com/news/amazon-leo/amazon-leo-vulcan-satellites-launch | 09/11/2026 (act. 14/11/2026) | 16/11/2026 | Alta (pero desactualizada) | 40 satélites en la 1ª misión Vulcan dedicada; 1.000ª unidad completada a inicios de septiembre. **Al 16/11/2026 no refleja la falla de LV-01**: para el resultado citar #2. | [DATO REAL] |
| 4 | Amazon — "Amazon makes historic launch investment to advance Project Kuiper" | Oficial | https://www.aboutamazon.com/news/innovation-at-amazon/amazon-makes-historic-launch-investment-to-advance-project-kuiper | 05/04/2022 | 15/11/2026 | Alta | Compra de lanzamientos 2022: 38 Vulcan + 18 Ariane 6 + 12 New Glenn (+15 opcionales) = hasta 83. | [DATO REAL] |
| 5 | SEC EDGAR — Amazon.com Inc, Form 425, Exhibit 99.1: comunicado conjunto Amazon–Globalstar | Regulatoria (primaria) | https://www.sec.gov/Archives/edgar/data/1018724/000110465926042891/tm2611746d2_ex99-1.htm | 14/04/2026 | 16/11/2026 | Alta | **No es un informe financiero.** Anuncia la adquisición de Globalstar ($90/acción o 0,3210 acciones de Amazon; cierre previsto 2027) y el acuerdo con Apple; constelación inicial "more than 3,000 satellites"; D2D desde 2028. Inversión en Leo solo como "multibillion-dollar", sin cifra. | [DATO REAL] |

#### B. Regulatorias e institucionales

| # | Fuente (organización, título) | Tipo | URL | Publicado | Consultado | Confiabilidad | Qué dato aporta | Etiqueta |
|---|---|---|---|---|---|---|---|---|
| 6 | FCC — Order and Authorization FCC 20-102, 35 FCC Rcd 8324 (autorización original Project Kuiper) | Regulatoria (primaria) | https://www.fcc.gov/document/fcc-authorizes-kuiper-satellite-constellation (403 a la lectura automática; reproducción parcial en TelecomTV) | 30/07/2020 (adoptada 29/07/2020) | 16/11/2026 | Alta | 3.236 satélites en 98 planos (590, 610 y 630 km); servicio desde los primeros 578. ⚠ Original sin leer: abrir el PDF desde un navegador. Hitos 2026/2029 confirmados indirectamente por #7 y #8. | [DATO REAL] |
| 7 | FCC — Order and Authorization DA 24-224 (modificación) | Regulatoria (primaria, leída) | https://docs.fcc.gov/public/attachments/DA-24-224A1.pdf | 08/03/2024 | 16/11/2026 | Alta | Reduce la constelación de 3.236 a 3.232 (¶1) y redistribuye órbitas: 782 a 590 km/33°, 2 a 590 km/30°, 1.292 a 610 km/42°, 1.156 a 630 km/51,9° (¶4). Prohíbe desplegar directo a altitud operativa (¶43). Hitos en ¶52(b) (dice "July 20, 2029", ver contradicciones). Aviso de cumplimiento antes del 14/08/2026 (¶53). | [DATO REAL] |
| 8 | FCC — Order DA 26-553 (waiver parcial del hito del 50%) | Regulatoria (primaria, leída) | https://docs.fcc.gov/public/attachments/DA-26-553A1.txt | 05/06/2026 | 16/11/2026 | Alta | Hitos: 1.616 al 30/07/2026 y 3.232 al 30/07/2029 (¶3). Waiver **parcial**, no prórroga (¶11, ¶19). Pérdida de prioridad de espectro Ka/Ku (2020) y banda V (2021) hasta el 30/03/2028, o 30/10/2027 si certifica el 50% construido (¶15). Si falla 2029, la autorización se reduce a los operativos (¶12). **La fianza no se exime** (¶18). Amazon declaró 180 lanzados y proyectó ~700 al 30/07/2026 (¶8). | [DATO REAL] |

#### C. Técnicas y de proveedores de lanzamiento

| # | Fuente (organización, título) | Tipo | URL | Publicado | Consultado | Confiabilidad | Qué dato aporta | Etiqueta |
|---|---|---|---|---|---|---|---|---|
| 9 | SpaceNews — "Amazon Secures Up to 83 Launches from Arianespace, Blue Origin, and United Launch Alliance for Project Kuiper" | Técnica/prensa especializada | https://spacenews.com/amazon-secures-up-to-83-launches-from-arianespace-blue-origin-and-united-launch-alliance-for-project-kuiper/ | 05/04/2022 | 15/11/2026 | Alta | Detalle de los contratos de lanzamiento 2022. | [DATO REAL] |
| 10 | SpaceNews — "Amazon adds Falcon 9 to multi-billion-dollar Project Kuiper launch campaign" | Técnica/prensa especializada | https://spacenews.com/amazon-adds-falcon-9-to-multi-billion-dollar-project-kuiper-launch-campaign/ | 2023 | 15/11/2026 | Alta | Incorporación de SpaceX Falcon 9 (3 misiones) al plan de lanzamiento. | [DATO REAL] |
| 11 | Spaceflight Now — "ULA suffers first total mission failure with loss of Vulcan rocket carrying 40 Amazon Leo satellites" | Técnica/prensa especializada | https://spaceflightnow.com/2026/11/15/ula-suffers-first-total-mission-failure-with-loss-of-vulcan-rocket-carrying-40-amazon-leo-satellites/ | 15/11/2026 | 15/11/2026 | Alta | Falla total de la 1ª misión Vulcan dedicada a Leo el 15/11/2026: anomalía en etapa Centaur ~10 min tras despegue; 40 satélites perdidos. | [DATO REAL] |
| 12 | Spaceflight Now — "United Launch Alliance announces mid-November return to flight for Vulcan rocket" | Técnica/prensa especializada | https://spaceflightnow.com/2026/10/28/united-launch-alliance-announces-mid-november-return-to-flight-for-vulcan-rocket/ | 28/10/2026 | 15/11/2026 | Alta | Vulcan estuvo ~9 meses en tierra por problemas en los boosters sólidos; contexto del retorno al vuelo. | [DATO REAL] |

#### D. Prensa especializada y general (para ubicar hechos / confirmar)

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

### Contradicciones y vacíos detectados

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

### Datos buscados y no encontrados

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

### Cifras de contratos de lanzamiento con fecha de corte

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

### E. Fuentes incorporadas en I-2 (#21 a #47)

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

---

# Anexo B. Cronología de hitos

## Hitos públicos de Amazon Leo (borrador I-2)

**Estado: borrador local, sin revisión del equipo.** Fecha de corte y de consulta: **16/11/2026**.
Las referencias `#n` apuntan a `evidencia/registro-fuentes.md` (#1 a #20 ya existen) o a las **fuentes nuevas propuestas (#21 en adelante)** de la sección 8, que el equipo debe aprobar antes de incorporarlas.
Convención: toda fila de las secciones 1 a 4 es `[DATO REAL]` y trae su fuente. Las secciones 5 y 6 contienen `[INFERENCIA DEL GRUPO]` con supuestos explícitos. La sección 7 lista lo que **no se pudo verificar**.
"Primaria" = Amazon, FCC, ULA. "Secundaria" = medios. Casi todo lo de Amazon es declaración de la propia empresa: describe lo que Amazon dice, no necesariamente lo que ocurrió.

---

### 1. Lanzamientos (todas las misiones listadas por Amazon)

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

**Protoflight (KuiperSat-1 y -2, Atlas V, 06/10/2023):** solo aparece en la tabla de Wikipedia. **NO VERIFICADO** en fuente primaria (ninguna página de Amazon leída lo menciona; Amazon numera desde KA-01 como misión n.º 1).

#### Lanzamientos contratados (lo que dice Amazon hoy)

| Proveedor | Cantidad | Fuente |
|---|---|---|
| Arianespace (Ariane 6) | 24 (ampliado desde 18 el 10/09/2026) | #24 |
| ULA (Vulcan) | 38 | #3 |
| ULA (Atlas V) | 9 (contrato previo a 2022) | #4 (05/04/2022) |
| Blue Origin (New Glenn) | 24 firmes ("opciones convertidas") | #23 (23/03/2026) |
| SpaceX (Falcon 9) | 3 (01/12/2023) + 10 más "a fines de 2025" | #38, #23 |
| Total declarado | "more than 100" misiones | #23, #2 |

---

### 2. Hitos regulatorios

| Fecha | Hito | Fuente | Tipo |
|---|---|---|---|
| 04/04/2019 | Se conoce el proyecto por presentaciones federales: 3.236 satélites. | #42 | Secundaria |
| 30/07/2020 | FCC autoriza la constelación (3.236 satélites, banda Ka). Amazon lo comunicó el mismo día. Orden FCC 20-102, 35 FCC Rcd 8324. | #39; #6 | Primaria (Amazon); original FCC sin leer |
| 09/02/2023 | FCC aprueba el plan actualizado de desechos orbitales (con reportes semestrales). | #44 | Secundaria |
| 08/03/2024 | FCC reduce la constelación a 3.232 satélites y redistribuye órbitas. | #7 | Primaria (FCC, leída) |
| 30/01/2026 | Amazon pide extender el hito del 50% (24 meses, hasta 30/07/2028) o un waiver. Dijo tener 180 satélites lanzados y proyectó ~700 al 30/07/2026. | #8 ¶8 | Primaria (FCC, leída) |
| 05/06/2026 | FCC concede un waiver parcial del hito de 1.616 satélites al 30/07/2026; pérdida temporal de prioridad de espectro; hito de 3.232 al 30/07/2029 intacto; la fianza no se exime. | #8 | Primaria (FCC, leída) |
| 27/07/2026 | Amazon presenta a la FCC el sistema direct-to-device: hasta 5.105 satélites, despliegue desde 2028. Número de expediente **NO VERIFICADO**. | #34 | Primaria (Amazon) |

---

### 3. Hitos de infraestructura, producción y negocio

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

### 4. Estado del servicio y terminales

- **[DATO REAL]** Al 16/11/2026 Amazon **no anunció lanzamiento comercial**. Las páginas de septiembre y noviembre de 2026 hablan de "initial service rollout later this year", con clientes empresariales en "private preview" (#35, #24, #3).
- **[DATO REAL]** Terminales (cifras de Amazon, no precios de venta): Nano hasta 100 Mbps; Pro hasta 400 Mbps; Ultra hasta 1 Gbps de bajada y 400 Mbps de subida (#30, #29). Costo de fabricación de terminal estándar esperado "<US$400" (2023, #30). **Precios de venta: NO VERIFICADO.**
- **[DATO REAL]** Capacidad de fabricación declarada de Kirkland por fecha: 4 satélites/día (2022, #25); hasta 5/día (2024, #26); hasta 30/semana (2026, #23). Satélite n.º 1.000 completado a inicios de 09/2026 (#3).

---

### 5. Inferencias del grupo (para revisar)

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
→ Base: #8 ¶3, #43. Supuesto: la mención de CNBC se refiere a esos mismos sistemas. No se leyó la orden que los autoriza.

**[INFERENCIA DEL GRUPO] 5. La falla de LV-01 y la caída de New Glenn concentran el riesgo en dos proveedores.**
Vulcan (38 contratados) y New Glenn (24) suman 62 de ~108 lanzamientos, el 57%, y ambos tienen eventos de falla en 2026 (LV-01 el 15/11; explosión de New Glenn en su plataforma durante una prueba de encendido el 28/05/2026, #47).
→ Base: sección 1, #11. Supuestos: (a) los números de contratos son vigentes.

---

### 6. Discrepancias detectadas (para el equipo)

| Tema | Fuente A | Fuente B | Resolución propuesta |
|---|---|---|---|
| Fecha del rebrand | Amazon: 13/11/2025 (#21) | Wikipedia: 12/11/2025 | Usar 13/11/2025 (primaria). Cierra la contradicción del registro. |
| Cargo de Rajeev Badyal | Amazon: "Vice President of Amazon Leo" (#21) | Wikipedia: "president" | Usar "Vice President". |
| Fecha límite final FCC | DA 26-553: 30/07/2029 (#8) | DA 24-224 ¶52(b) y Via Satellite (#44): "July 20, 2029" | Usar 30/07/2029; nota al pie. |
| Total de lanzamientos | 83 (04/2022, #4); "up to 92" (10/2022, #25); 77 cohetes pesados (12/2023); "initial block of 80" y "más de 100" (2026, #23) | — | Siempre citar con fecha: son conteos de momentos distintos. |
| Capacidad de producción | 4/día (2022), 5/día (2024), 30/semana (2026) | Prensa: 27/semana | Citar cada cifra con su fecha. 30/semana (Amazon) es capacidad, no ritmo efectivo. |
| Fecha de actualización de #2 | Cabecera: 15/11/2026 | Pie: 28/10/2026 | Guardar captura fechada de la página. |
| Pesos y medidas de terminales | Amazon (#30): Nano 1 lb, Ultra 19x30 in | Wikipedia: otras cifras | Usar Amazon. |

---

### 7. NO VERIFICADO (pendientes)

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

### 8. Fuentes nuevas propuestas para el registro

> **16/11/2026:** estas fuentes se incorporaron a `evidencia/registro-fuentes.md` (sección E). La tabla queda acá como antecedente; la referencia oficial es el registro.

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

---

# Anexo C. Mapa de actores

## Mapa de actores de Amazon Leo (borrador I-2)

**Estado: borrador local, sin revisión del equipo.** Fecha de corte y de consulta: **16/11/2026**.
Las referencias `#n` apuntan a `evidencia/registro-fuentes.md` (#1 a #20) o a las fuentes nuevas propuestas en la sección 8 de `hitos.md` (#21 a #46). "Primaria" = Amazon, FCC, ULA; "Secundaria" = medios.
Convención: toda fila es `[DATO REAL]` salvo que se marque. Las inferencias están en la sección 8 con sus supuestos. Lo que **no se pudo verificar** está en la sección 9 y no debe usarse en el informe.
Casi todo lo de Amazon es declaración de la propia empresa.

---

### 1. Amazon (organización y personas)

| Actor | Rol según la fuente | Fuente | Fecha |
|---|---|---|---|
| Amazon Leo | Negocio de Amazon dentro de Devices & Services. I+D en Redmond, WA; producción en Kirkland, WA. | #28 | 04/11/2025 |
| Rajeev Badyal | "Vice President of Amazon Leo" (firma el anuncio del rebrand). | #21 | 13/11/2025 |
| Chris Weber | "Vice president of Amazon Leo business and product". | #24 | 10/09/2026 |
| Trevor Vieweg | "Global head of business for Amazon Leo". | #35 | 22/09/2026 |
| Melissa Wuerl | Directora de sistemas de lanzamiento de Amazon Leo. | #3 | 09/11/2026 |
| Steve Metayer | VP de operaciones de producción. | #27 | 24/07/2025 |
| Panos Panay | SVP de Devices & Services (acuerdo Globalstar y Apple). | #22 | 14/04/2026 |
| David Zapolsky | Chief Global Affairs and Legal Officer. | #33 | 15/07/2026 |
| Brian Huseman | VP de política pública. | #27 | 24/07/2025 |
| Joe Lathan | Country manager Australia y Nueva Zelanda. | #40 | 05/08/2025 |
| AWS | En 2022 Amazon dijo que AWS "will provide networking and infrastructure". Vínculo específico con AWS Ground Station: **NO VERIFICADO**. | #4 | 05/04/2022 |

- **[DATO REAL]** Amazon afirma que el sistema "is designed, built, and operated in-house at Amazon" (#22, 14/04/2026).
- **[DATO REAL]** No se encontró ningún anuncio de cambio de liderazgo. Esto no prueba que no los haya habido.

---

### 2. Proveedores de lanzamiento

| Actor | Cohete | Contratado según la fuente | Misiones volando para Leo | Fuente |
|---|---|---|---|---|
| United Launch Alliance (ULA) | Atlas V | 9 (deal previo a 2022) | 8 misiones Leo (KA-01 a LA-08) | #4, #2, #41 |
| ULA | Vulcan | 38 | LV-01 (15/11/2026): **falla, 40 satélites perdidos** | #3, #2, #11 |
| Arianespace | Ariane 6 | 24 (de 18, ampliado el 10/09/2026) | LE-01, LE-02, LE-03; próxima LE-04, NET 23/11/2026 | #24, #2 |
| SpaceX | Falcon 9 | 3 (12/2023) + 10 más "a fines de 2025" | KF-01, KF-02, KF-03 | #38, #23, #2 |
| Blue Origin | New Glenn | 24 firmes (opciones convertidas) | Ninguna misión de Leo volada | #23 |

- **[DATO REAL]** Amazon declara "more than 100" misiones en su manifiesto (#23, 23/03/2026).
- **[DATO REAL]** Blue Origin fue fundada por Jeff Bezos y es una empresa separada de Amazon (#28).
- **[DATO REAL]** Mark Peller aparece como presidente y CEO de ULA desde el 17/08/2026 (#41, sitio de prensa de ULA).
- **[DATO REAL]** New Glenn explotó en su plataforma de Cabo Cañaveral durante una prueba de encendido el 28/05/2026 (#47, confirmado por varios medios); Spaceflight Now dice que Amazon depende de su regreso y que ULA no explicó aún la causa de la falla de LV-01 (#11).
- **[DATO REAL]** En 2022 Amazon también había contratado 2 lanzamientos de ABL Space Systems (RS1) para prototipos (#4). Que se hayan realizado: **NO VERIFICADO**.

---

### 3. Fabricación y proveedores

| Actor | Rol | Fuente | Fecha |
|---|---|---|---|
| Amazon (Kirkland, WA) | Fábrica de satélites: 172.000 ft², abierta en 04/2024; capacidad declarada "as many as 30 satellites per week" (2026). Satélite n.º 1.000 completado a inicios de 09/2026. | #25, #26, #23, #3 | 2022–2026 |
| Amazon (Kennedy Space Center, FL) | Instalación de procesamiento: 100.000 ft², inversión "more than $140 million". | #27 | 24/07/2025 |
| Beyond Gravity (Suiza) | Dispensadores de satélites; segunda planta en Linköping, Suecia. | #4 | 05/04/2022 |
| Space Florida, NASA, Space Force | "Long-term partnership" mencionada en el anuncio de Florida. Alcance del vínculo: **NO VERIFICADO**. | #27 | 24/07/2025 |

- **[DATO REAL]** Northrop Grumman, Blue Origin (motores BE-4) y Aerojet Rocketdyne (RL10C) son proveedores de ULA, **no** de Amazon (#41).
- **[DATO REAL]** MDA Space fabrica los satélites de Globalstar, no los de Leo (#22).
- **Proveedores de chips, antenas o componentes del satélite: NO VERIFICADO.** No hay ningún nombre en fuente primaria.

---

### 4. Segmento terrestre e infraestructura

- **[DATO REAL]** Amazon describe gateways, antenas de telemetría y "dedicated fiber" que conectan con Internet, nube o redes privadas (#22, #28). Cantidad y ubicación de gateways: **NO VERIFICADO** (el registro #17 habla de más de 300, pero es prensa).
- **[DATO REAL]** En Cabo Cañaveral, Amazon financió VIF-A, una plataforma móvil y un segundo barco de transporte: más de US$200 millones (#23, 23/03/2026). También hay inversiones en Vandenberg SFB (California) para misiones desde la costa oeste (#23).
- **[DATO REAL]** Socios locales de servicio: Uztelecom / UZ-SAT (Uzbekistán, "authorized distributor", #35); Vanu (África, backhaul celular, #32); Herotel (Sudáfrica, #33).

---

### 5. Clientes y socios comerciales

| Actor | Qué se anunció | Fuente | Fecha |
|---|---|---|---|
| JetBlue | Wi-Fi a bordo desde 2027 en aviones seleccionados. | #36 | 04/09/2025 |
| Delta Air Lines | Servicio desde 2028 en 500 aviones. | #31 | 31/03/2026 |
| DIRECTV Latin America y Sky Brasil | Distribución en Argentina, Brasil, Chile, Colombia, Ecuador, Perú y Uruguay. | #37 | 12/06/2024 |
| NBN Co (Australia) | Más de 300.000 clientes elegibles; lanzamiento "from the middle of 2026". Estado actual: **NO VERIFICADO**. | #40 | 05/08/2025 |
| Herotel (Sudáfrica) | Servicio "evry", comercial en 2027. | #33 | 15/07/2026 |
| Uztelecom / UZ-SAT (Uzbekistán) | Distribuidor autorizado; servicio en "private preview". | #35 | 22/09/2026 |
| Vanu | Acuerdo para backhaul celular rural en África. | #32 | 26/02/2026 |
| L3Harris, Hunt Energy Network, Connected Farms, Crane Worldwide Logistics | Citados como socios o clientes del *enterprise preview* o del rebrand. Detalle de cada relación: **NO VERIFICADO**. | #21, #29 | 11/2025 |
| Apple | Acuerdo para que Leo sirva funciones satelitales de iPhone y Apple Watch (hoy las presta Globalstar). | #22 | 14/04/2026 |
| Globalstar | Adquisición acordada: $90 por acción en efectivo o 0,3210 acciones de Amazon; cierre previsto en 2027, sujeto a aprobaciones regulatorias e hitos de satélites HIBLEO-4; accionistas con ~58% del voto ya aprobaron. | #22, #5 | 14/04/2026 |

- **[DATO REAL]** Socios de la línea direct-to-device citados por Amazon el 27/07/2026: Vodafone, DirecTV, Herotel, NBN Co (#34). Un agente no los encontró en otras fuentes; confirmar a mano antes de usar Vodafone.
- **Verizon, operadores móviles nombrados, clientes gubernamentales: NO VERIFICADO.**

---

### 6. Reguladores e instituciones

| Actor | Rol | Fuente |
|---|---|---|
| FCC (Space Bureau) | Autorizó la constelación (2020), la modificó (2024) y concedió el waiver parcial del hito (2026). Firma de J. A. Schwarz, Chief, Space Bureau. | #6, #7, #8 |
| NASA y Space Force | Coordinación de lanzamientos en Florida y Vandenberg; "partnership" mencionada por Amazon. Detalle: **NO VERIFICADO**. | #27, #23 |
| Ministro de Comunicaciones de Sudáfrica (Solly Malatsi) | Aparece en la foto del anuncio con Herotel. Licencia de ICASA: **NO VERIFICADO**. | #33 |

- **UIT, otros reguladores nacionales (Uzbekistán, Australia, Brasil, Francia, Kenia):** licencias **NO VERIFICADO**. Solo se vio la solicitud de Kenia por prensa (#18).
- **[DATO REAL]** Amazon dice tener "approval to deploy a second-generation system" (#23). La autoridad que lo concedió y los términos: **NO VERIFICADO** (ver `hitos.md`, inferencia 4).

---

### 7. Competidores y terceros con interacción documentada

| Actor | Interacción | Fuente | Tipo |
|---|---|---|---|
| SpaceX | Se opuso en 2019 ante la FCC. Según la nota, se reunió al menos tres veces con el presidente de la FCC y advirtió un "significant detrimental impact". Hoy también es proveedor de lanzamiento de Amazon. | #45 | Secundaria |
| OneWeb, Telesat, Theia Holdings, Iridium | También pidieron denegar la solicitud (2019). | #45 | Secundaria |
| SpaceX (2024) | Tenía una solicitud de revisión pendiente contra la orden de desechos orbitales de 2023. | #7 | Primaria |

- **Eutelsat/OneWeb (2026) e IRIS²:** sin interacción verificada con Amazon Leo.

---

### 8. Inferencias del grupo (para revisar)

**[INFERENCIA DEL GRUPO] 1. SpaceX es a la vez competidor y proveedor.**
SpaceX se opuso a Amazon ante la FCC (2019, #45) y es contratista de lanzamientos de Leo (#38, #23).
→ Base: #45, #38, #23. Supuesto: la oposición de 2019 y los contratos de 2023 en adelante son entre las mismas entidades y no hay acuerdos de por medio que los reconcilien.

**[INFERENCIA DEL GRUPO] 2. Los lanzadores concentran el riesgo externo del programa.**
Los cuatro proveedores de lanzamiento suman ~108 misiones contratadas (ver `hitos.md`, inferencia 3). Dos de ellos tuvieron una falla o un incidente grave en 2026: ULA (LV-01, 15/11) y Blue Origin (explosión de New Glenn en plataforma, 28/05/2026, #47).
→ Base: sección 2 y #11. Supuestos: (a) las cifras de contratos son vigentes.

**[INFERENCIA DEL GRUPO] 3. Amazon integra casi toda la cadena y depende de terceros en lanzamiento y en regulación.**
Fabricación, terminales y operación son internos (#22), pero lanzamiento (proveedores externos) y espectro/licencias (FCC y reguladores locales) no.
→ Base: #22, sección 2, sección 6. Supuesto: la frase "in-house" de Amazon describe fabricación y operación y no excluye subcontratistas de componentes, que no son públicos.

---

### 9. NO VERIFICADO (pendientes)

- Proveedores de chips, antenas y componentes de satélites.
- Vínculo de AWS (Ground Station u otro) con la red terrestre.
- Cantidad y ubicación de las estaciones terrestres.
- Estado actual del acuerdo con NBN Co (lanzamiento "mid-2026").
- Detalle de L3Harris, Hunt Energy, Connected Farms, Crane Worldwide Logistics, Airbus.
- Vodafone y Verizon como socios (solo Vodafone aparece, vía nota D2D de Amazon).
- Licencias de reguladores nacionales y de la UIT.
- Naturaleza del acuerdo con Space Force, NASA y Space Florida.
- Que ABL haya lanzado prototipos de Kuiper.
- Interacción con IRIS² y con Eutelsat/OneWeb en 2026.
- Fuentes no leídas por bloqueo: SpaceNews, Ars Technica, GeekWire, The Verge, NASASpaceflight, fcc.gov, leo.amazon.com. Reuters, Via Satellite (salvo #44), NYT y AP no se consultaron.

---

# Anexo D. Cifras maestras

## Cifras maestras — Amazon Leo

**Fuente única de los números que usa todo el trabajo.** Riesgos, Tiempos, Estimaciones, Costos, Seguimiento y Valor Ganado y el dashboard toman sus cifras **de esta tabla**. Si un número cambia, se cambia acá primero y después en cada sección que lo use (columna "Lo usa").

Es la herramienta para cumplir el paso 4 de la consigna (**Conectar**: "evitar documentos aislados") y para la defensa: cualquier número que se diga en voz alta tiene que coincidir con el informe y con el tablero.

- **Fecha de corte:** 16/11/2026 (propuesta pendiente de aprobación; ver `PROGRESO.md`, "Decisiones pendientes").
- **Unidad de avance:** satélites **lanzados** como aproximación de **operativos** (Amazon no publica operativos; la FCC mide operativos). Todos los resultados derivados son optimistas.
- Las referencias `#n` son filas de `evidencia/registro-fuentes.md`.
- Estado: borrador elaborado con asistencia de IA a partir de la evidencia del repo; **requiere revisión del equipo**.

---

### 1. Regulación (FCC)

| ID | Cifra | Valor | Etiqueta | Fuente / cálculo | Lo usa |
|---|---|---|---|---|---|
| C-01 | Satélites autorizados (Gen1) | 3.232 | `[DATO REAL]` | #7 ¶1; #8 ¶3 | Riesgos, Alcance, VG, dashboard |
| C-02 | Hito intermedio (50%) | 1.616 al 30/07/2026 | `[DATO REAL]` | #8 ¶3 | Riesgos, Tiempos, VG |
| C-03 | Hito final (100%) | 3.232 al 30/07/2029 | `[DATO REAL]` | #8 ¶3 (DA 24-224 dice 20/07, ver contradicciones) | Todo |
| C-04 | Proyección de Amazon a la FCC | ≈ 700 desplegados al 30/07/2026 | `[DATO REAL]` | #8 ¶8 (solicitud del 30/01/2026) | VG (línea base), Riesgos |
| C-05 | Pérdida de prioridad de espectro | hasta 30/03/2028 (30/10/2027 si certifica 50% construido) | `[DATO REAL]` | #8 ¶15 | Riesgos R-05, Tiempos |
| C-06 | Fianza (surety bond) | no eximida; monto no público | `[DATO REAL]` / monto no público | #8 ¶18 | Costos, Riesgos R-04 |

### 2. Despliegue (al 16/11/2026)

| ID | Cifra | Valor | Etiqueta | Fuente / cálculo | Lo usa |
|---|---|---|---|---|---|
| C-10 | Primera misión de producción | KA-01, 28/04/2025 | `[DATO REAL]` | #2 | Tiempos, VG |
| C-11 | Misiones realizadas | 15 (14 con despliegue + LV-01 fallida) | `[DATO REAL]` | #2, #11 | Tiempos, Riesgos |
| C-12 | Satélites lanzados y desplegados | 396 | `[INFERENCIA DEL GRUPO]` | Suma por misión de #2; coincide con "nearly 400" de Amazon | Todo |
| C-13 | Satélites perdidos | 40 (LV-01, 15/11/2026) | `[DATO REAL]` | #2, #11 | Riesgos T-01 |
| C-14 | Satélites que faltan para el hito final | 2.836 | `[INFERENCIA DEL GRUPO]` | C-01 − C-12 | Riesgos, Tiempos, VG |
| C-15 | Avance físico contra el hito final | 12,3% | `[INFERENCIA DEL GRUPO]` | 396 ÷ 3.232 | VG, dashboard |
| C-16 | Cumplimiento del hito del 50% | 24,5% (396 de 1.616) | `[INFERENCIA DEL GRUPO]` | C-12 ÷ C-02 (satélites al 02/07/2026: 396, sin lanzamientos hasta el 15/11) | Riesgos R-05, dashboard |

### 3. Ritmo y horizonte

| ID | Cifra | Valor | Etiqueta | Fuente / cálculo | Lo usa |
|---|---|---|---|---|---|
| C-20 | Horizonte hasta el hito final | ≈ 32,5 meses | `[INFERENCIA DEL GRUPO]` | 16/11/2026 → 30/07/2029 | Riesgos, Tiempos |
| C-21 | Ritmo observado (satélites) | ≈ 21 por mes | `[INFERENCIA DEL GRUPO]` | 396 en ≈ 18,6 meses (28/04/2025 → 15/11/2026) | Riesgos, Tiempos, dashboard |
| C-22 | Ritmo observado (misiones) | ≈ 0,8 por mes global; ≈ 11 por año desde 28/04/2026 | `[INFERENCIA DEL GRUPO]` | 15 misiones en 18,6 meses; 6 en 6,5 meses | Riesgos §5, Tiempos |
| C-23 | Ritmo necesario (satélites) | ≈ 87 por mes | `[INFERENCIA DEL GRUPO]` | C-14 ÷ C-20 | Riesgos, Tiempos, dashboard |
| C-24 | Ritmo necesario (misiones) | ≈ 35 por año (a 30 satélites por misión) | `[INFERENCIA DEL GRUPO]` | C-23 × 12 ÷ 30 | Riesgos, Tiempos |
| C-25 | Plan declarado de Amazon | "20+ misiones" en el año dos | `[DATO REAL]` | #23 (23/03/2026) | Riesgos, Tiempos |
| C-26 | Satélites por misión | 24 (Falcon 9) · 27–29 (Atlas V) · 32–36 (Ariane 64) · 40 (Vulcan) | `[DATO REAL]` | #2, #3 | Estimaciones, Riesgos §5 |

### 4. Producción e infraestructura

| ID | Cifra | Valor | Etiqueta | Fuente / cálculo | Lo usa |
|---|---|---|---|---|---|
| C-30 | Capacidad declarada de fábrica (Kirkland) | 4/día (2022) → 5/día (2024) → hasta 30/semana (2026) | `[DATO REAL]` | #25, #26, #23 | Alcance, Estimaciones |
| C-31 | Satélites fabricados | 1.000 (inicios de 09/2026) | `[DATO REAL]` | #3 (fecha discutida, ver contradicciones) | Estimaciones |
| C-32 | Instalación de procesamiento en KSC | 100.000 ft²; > USD 140 millones | `[DATO REAL]` | #27 | Costos, Alcance |
| C-33 | Inversión en Cabo Cañaveral (2026) | > USD 200 millones | `[DATO REAL]` | #23 | Costos |
| C-34 | Estaciones terrestres | > 300 planificadas | `[DATO REAL]` (prensa) | #17 | Alcance |
| C-35 | Compromiso de inversión inicial | > USD 10.000 millones ("more than $10 billion") | `[DATO REAL]` | #39 (30/07/2020), verificado el 16/11/2026 | Caso de negocio, Acta, Costos |

### 5. Lanzamientos contratados (vigente al 16/11/2026)

| ID | Cifra | Valor | Etiqueta | Fuente / cálculo | Lo usa |
|---|---|---|---|---|---|
| C-40 | Total contratado | ≈ 108 (24 Ariane 6 + 38 Vulcan + 9 Atlas V + 24 New Glenn + 13 Falcon 9) | `[INFERENCIA DEL GRUPO]` | Tabla "Cifras de contratos con fecha de corte" del registro | Riesgos, Costos, dashboard |
| C-41 | Lanzamientos restantes | ≈ 93 (21 Ariane 6, 10 Falcon 9, 1 Atlas V, 37 Vulcan, 24 New Glenn) | `[INFERENCIA DEL GRUPO]` | C-40 − volados | Riesgos R-02, dashboard |
| C-42 | Dependencia de Vulcan + New Glenn | 61 de 93 = ≈ 66% | `[INFERENCIA DEL GRUPO]` | C-41 | Riesgos R-02, dashboard |

### 6. Resultados de análisis (salen de otras secciones)

| ID | Cifra | Valor | Etiqueta | Origen | Lo usa |
|---|---|---|---|---|---|
| C-50 | Satélites al 30/07/2029 (Monte Carlo) | P10 ≈ 1.140 · P50 ≈ 1.510 · P90 ≈ 2.050 | `[INFERENCIA DEL GRUPO]` sobre supuestos `[PROPUESTA DE GESTIÓN]` | Riesgos §5, `analisis_cuantitativo.py` | Riesgos, Tiempos, dashboard |
| C-51 | Probabilidad de llegar a 3.232 por cadencia | ≈ 0% | ídem | Riesgos §5 | Riesgos R-04, dashboard |
| C-52 | SPI en satélites al 30/07/2026 | ≈ 0,57 (396 ÷ 700) | `[INFERENCIA DEL GRUPO]` | Riesgos §7; ver `informe/guias/seguimiento-valor-ganado.md` | VG, dashboard |
| C-53 | Exposición total al riesgo | 0,82 antes → 0,50 después de responder | `[PROPUESTA DE GESTIÓN]` | Riesgos §6 | Riesgos, dashboard |
| C-54 | Riesgos en rojo | 2 (R-04, R-02) → 1 después de responder | `[PROPUESTA DE GESTIÓN]` | Riesgos §4.5 y §6 | dashboard |

### 7. Lo que no es público (no inventar)

| Dato | Estado | Cómo se trata |
|---|---|---|
| Inversión total **actualizada** de Amazon en Leo (USD) | Compromiso inicial **verificado**: "more than $10 billion" (#39, 30/07/2020; ver C-35). En 2026 solo "multibillion-dollar" (#5). No hay cifra actualizada. | Usar C-35 como piso declarado en 2020; el total actual queda sin dato público |
| Costo por satélite y por lanzamiento | No público | Supuesto explícito del grupo en Costos |
| Monto de la fianza | No público | Se declara como límite |
| Satélites **operativos** | No público | Se usa lanzados (ver unidad de avance) |
| Costo real incurrido (AC) | No público | El CPI no se puede calcular con datos reales |

---

# Anexo E. Código

Scripts reproducibles (Python 3, sin dependencias externas):

- `informe/riesgos/analisis_cuantitativo.py`: Monte Carlo (Riesgos §5).
- `informe/estimaciones/pert_despliegue.py`: estimación PERT (sección 9).
- `informe/seguimiento/valor_ganado.py`: valor ganado y serie EV (sección 12).

# Anexo F. Verificación contra fuentes primarias

Ver `evidencia/verificacion-i1-2026-11-16.md`.
