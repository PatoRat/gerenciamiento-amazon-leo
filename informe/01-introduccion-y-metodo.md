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
| 5. Defender | Tablero ejecutivo y guion de preguntas probables | Tablero ejecutivo |

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

## 1.5 Limitaciones generales

- Amazon es una empresa privada y no publica su cronograma, su WBS ni su presupuesto. Casi toda la información de la empresa es **declaración propia**.
- Algunas fuentes no pudieron leerse por bloqueo o paywall (SpaceNews, fcc.gov en lectura automática, entre otras; ver Anexo A).
- El proyecto está en curso: la falla de la misión LV-01 ocurrió un día antes de la fecha de corte.
