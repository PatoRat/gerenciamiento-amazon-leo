# 5. Caso de negocio (reconstruido)

> **Borrador** redactado con asistencia de IA el 16/11/2026. Requiere revisión del equipo. Estructura: `catedra/PMOInformatica Plantilla Caso de Negocio.pdf`. Marco: Paneo, tema 2 (el Business Case juzga si el proyecto es deseable, viable y alcanzable, y se actualiza en todo el ciclo de vida).

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
| Ingresos y suscriptores | Clientes; ingresos en USD | `[[PENDIENTE: no público]]` | — |

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
| Lanzamientos (≈ 108 contratados) | No público ("the largest commercial procurement of launch vehicles in history", #28) | `[[PENDIENTE]]` |
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
