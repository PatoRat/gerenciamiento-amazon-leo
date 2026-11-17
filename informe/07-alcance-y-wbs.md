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
