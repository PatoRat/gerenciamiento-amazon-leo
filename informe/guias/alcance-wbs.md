# Guía — Alcance y WBS de Amazon Leo (flujo físico)

Guía metodológica (I-4) para la sección de Alcance. Borrador elaborado con asistencia de IA el 16/11/2026. La WBS de la sección 3 es una **propuesta de gestión para que el equipo la revise, la ajuste y la defienda**, no un dato.

- **Marco:** `catedra/Clase 2 Alcance.html` y `catedra/Ejemplo Proceso de Alcance.html`. Se usa la denominación de la cátedra: **WBS** (Estructura de Desglose del Trabajo), Declaración del Alcance, Paquetes de Trabajo, Línea Base del Alcance.
- **Por qué importa:** la orientación de la cátedra para este proyecto es "cómo se conectan fabricación, lanzamientos y operación". La WBS es el documento que muestra esa conexión.

---

## 1. Lo que dice la cátedra y cómo aplicarlo

| Concepto (Clase 2) | Aplicación a Amazon Leo |
|---|---|
| "El trabajo que no está en la WBS está fuera del alcance del proyecto." | Hay que decidir explícitamente qué entra: ¿solo Gen1 (3.232)? ¿Gen2, Polar, direct-to-device, Globalstar? |
| WBS orientada a **entregables**, no a actividades | Los elementos son cosas verificables (satélites en órbita, gateways operativos, servicio habilitado), no tareas. |
| WBS + Declaración del Alcance = **Línea Base del Alcance** | La línea base que mide Valor Ganado (3.232 satélites) tiene que salir de acá. |
| Alcance del **producto** contra alcance del **proyecto** | Producto: constelación + red terrestre + terminales + servicio. Proyecto: el trabajo para desplegarlo. |
| Elaboración progresiva / **rolling wave** | Gen1 se detalla hasta paquetes de trabajo; Gen2, D2D y Globalstar quedan en un nivel alto, porque la información pública es mínima. |
| Declaración del Alcance: criterios de aceptación, entregables, exclusiones, supuestos, restricciones | Las restricciones duras son regulatorias (hitos FCC, #8) y técnicas (no desplegar directo a la órbita operativa, #7 ¶43). |

## 2. Decisión de alcance a tomar (equipo)

`[PROPUESTA DE GESTIÓN]` Sugerencia: **el proyecto es el despliegue de Gen1 hasta habilitar el servicio comercial y cumplir el hito de 3.232 satélites.** Quedan **fuera del alcance** (exclusiones), como proyectos o fases del programa:
- Gen2 (3.212 satélites) y sistema Polar (1.292) (#8 ¶3).
- Direct-to-device (hasta 5.105 satélites desde 2028, #34) y la integración de Globalstar (#22).
- Acuerdos comerciales por país (son de la operación, no del despliegue).

→ Justificación: la cátedra distingue proyecto de programa (Paneo, tema 2): Amazon Leo es un **programa** y el despliegue de Gen1 es el **proyecto** que tiene línea base pública (hitos FCC). Así el alcance es medible (SMART, Clase 2) y coherente con Riesgos (horizonte al 30/07/2029) y con Valor Ganado (BAC = 3.232).

## 3. WBS propuesta (niveles 1 a 3)

`[PROPUESTA DE GESTIÓN]` orientada a entregables, ordenada por el **flujo físico**: fabricar → procesar → lanzar → operar en tierra → dar servicio. Cada elemento lleva la evidencia que prueba que el entregable existe en el proyecto real.

```
1. Despliegue de Amazon Leo Gen1 (3.232 satélites)
├── 1.1 Gestión del proyecto
│   ├── 1.1.1 Acta y caso de negocio
│   ├── 1.1.2 Plan para la dirección (alcance, tiempos, costos, riesgos)
│   └── 1.1.3 Seguimiento y control (informes de situación, VG, log de temas)
├── 1.2 Cumplimiento regulatorio
│   ├── 1.2.1 Autorización y modificaciones FCC (FCC 20-102, DA 24-224)
│   ├── 1.2.2 Gestión de hitos (aviso 14/08/2026, waiver DA 26-553, certificación 30/10/2027)
│   ├── 1.2.3 Plan de desechos orbitales y reportes semestrales
│   └── 1.2.4 Licencias por país (gateways y servicio)
├── 1.3 Satélites (fabricación)
│   ├── 1.3.1 Diseño y prototipos (protoflight)
│   ├── 1.3.2 Planta de Kirkland (capacidad hasta 30/semana)
│   └── 1.3.3 Lotes de satélites fabricados y aceptados
├── 1.4 Procesamiento e integración en el sitio de lanzamiento
│   ├── 1.4.1 Instalación de Kennedy Space Center
│   ├── 1.4.2 Instalaciones de Cabo Cañaveral (VIF-A, plataforma móvil, segundo barco)
│   └── 1.4.3 Integración de dispensadores (Beyond Gravity) y carga útil por misión
├── 1.5 Lanzamientos (servicios contratados)
│   ├── 1.5.1 Campaña Atlas V (ULA)
│   ├── 1.5.2 Campaña Vulcan (ULA)
│   ├── 1.5.3 Campaña Ariane 6 (Arianespace)
│   ├── 1.5.4 Campaña New Glenn (Blue Origin)
│   └── 1.5.5 Campaña Falcon 9 (SpaceX)
├── 1.6 Constelación en órbita
│   ├── 1.6.1 Elevación a órbita operativa y puesta en servicio por lote
│   └── 1.6.2 Centro de operaciones de la constelación
├── 1.7 Segmento terrestre
│   ├── 1.7.1 Gateways (más de 300 planificados)
│   ├── 1.7.2 Points of Presence e integración con la red de AWS
│   └── 1.7.3 Red de fibra / backhaul
├── 1.8 Terminales de usuario
│   ├── 1.8.1 Leo Nano (hasta 100 Mbps)
│   ├── 1.8.2 Leo Pro (hasta 400 Mbps)
│   └── 1.8.3 Leo Ultra (hasta 1 Gbps)
└── 1.9 Servicio habilitado
    ├── 1.9.1 Preview empresarial (enterprise / private preview)
    ├── 1.9.2 Inicio de servicio comercial (criterio verificable a definir)
    └── 1.9.3 Socios de distribución (DIRECTV/Sky Brasil, NBN Co, Herotel, Vanu, UZ-SAT, aerolíneas)
```

### Evidencia por elemento

| Elemento | Evidencia | Etiqueta del contenido |
|---|---|---|
| 1.2.1 – 1.2.3 | #6, #7, #8, #44 | `[DATO REAL]` |
| 1.2.4 | #18 (Kenia, prensa) | `[DATO REAL]` parcial; el resto `[[PENDIENTE]]` |
| 1.3.1 | Protoflight 06/10/2023: **NO VERIFICADO** (solo Wikipedia) | `[[PENDIENTE]]` |
| 1.3.2 – 1.3.3 | #25, #26, #23, #3 (1.000 fabricados) | `[DATO REAL]` |
| 1.4.1 – 1.4.2 | #27, #23 | `[DATO REAL]` |
| 1.4.3 | #4 (Beyond Gravity) | `[DATO REAL]` |
| 1.5.x | Registro, "Cifras de contratos con fecha de corte"; #2 | `[DATO REAL]` |
| 1.6.1 | #7 ¶43 (no se despliega directo a la órbita operativa) | `[DATO REAL]` |
| 1.6.2 | Sin fuente pública | `[INFERENCIA DEL GRUPO]`: toda constelación lo requiere |
| 1.7.1 – 1.7.3 | #17 (gateways, POP, fibra/AWS), #4 (AWS) | `[DATO REAL]` (prensa) |
| 1.8.x | #30, #29 | `[DATO REAL]` |
| 1.9.x | #29, #35, #37, #40, #33, #32, #36, #31; promesas en hitos §5 | `[DATO REAL]` |

## 4. Diccionario de la WBS (qué completar por paquete)

Para cada paquete de trabajo del nivel 3, el equipo completa: **entregable verificable** · **criterio de aceptación** · **responsable** (rol de `evidencia/actores.md`) · **dependencias** · **riesgo asociado** (ID de Riesgos) · **hito** (si corresponde).

Ejemplo de formato (**reemplazar**; los contenidos los decide el equipo):

| Campo | <ejemplo de formato — reemplazar> |
|---|---|
| Paquete | 1.5.2 Campaña Vulcan |
| Entregable | Lote de N satélites desplegados por misión |
| Criterio de aceptación | <a definir: separación nominal y contacto con todos los satélites> |
| Responsable | <rol> |
| Dependencias | 1.3.3, 1.4.3 |
| Riesgos | R-01, R-02; tema T-01 |

## 5. Conexión fabricación → lanzamiento → operación (cuello de botella)

`[INFERENCIA DEL GRUPO]` La WBS muestra una cadena en serie donde **el lanzamiento (1.5) es el cuello de botella**: la fábrica tiene capacidad declarada de hasta 30 satélites por semana (≈ 130 por mes, #23) y llegó a 1.000 fabricados (#3), mientras se desplegaron 396 a un ritmo de ≈ 21 por mes (cifras maestras C-21). Amazon mismo dice que ajusta la producción a la disponibilidad de lanzadores (#23).
→ Base: #23, #3, #2. Supuestos: (a) la capacidad declarada es alcanzable; (b) "1.000 fabricados" incluye los ya lanzados. **Ojo:** Riesgos descartó a propósito una inferencia sobre "satélites fabricados sin lanzar" por débil. Si se usa la diferencia 1.000 − 396, hay que presentarla como cota con supuestos, no como stock confirmado.

## 6. Coherencia con otras secciones

| Sección | Qué debe coincidir |
|---|---|
| Acta | Objetivo SMART y exclusiones iguales a la sección 2. |
| Tiempos | Los hitos del cronograma maestro salen de los entregables de la WBS (1.2.2, 1.9.2). |
| Costos | El presupuesto se arma por elemento de la WBS (estimación bottom-up o análoga, Clase 4). |
| Riesgos | Cada riesgo apunta a un elemento: R-01/R-02 → 1.5; R-03 → 1.9; R-04/R-05 → 1.2; R-06 → 1.9.3; R-07 → 1.2.4. |
| Valor Ganado | BAC = 3.232 = entregable 1.6. |

## 7. Preguntas probables de defensa

1. ¿Por qué Gen2, D2D y Globalstar quedan afuera? → Programa contra proyecto; línea base medible; rolling wave.
2. ¿Dónde está el cuello de botella del despliegue? → En 1.5 (lanzamientos), con evidencia de capacidad contra ritmo.
3. ¿Su WBS es por entregables o por actividades? → Por entregables (Clase 2); las actividades van en el cronograma.
4. ¿Qué parte de la WBS está sostenida por evidencia y qué parte es reconstrucción? → Tabla de evidencia de la sección 3.
