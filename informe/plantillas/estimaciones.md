# Plantilla — Estimaciones

**Etiqueta del documento:** `[PROPUESTA DE GESTIÓN]` (las estimaciones son del equipo) sobre `[DATO REAL]` (capacidades y ritmos públicos).
**Marco:** `catedra/Clase 4 Estimaciones 1ra. Parte …html` (métodos: análoga, paramétrica, juicio de expertos/Delphi, ascendente/bottom-up; concepto de **ventana**: reestimar al cerrar cada etapa) y `catedra/Clase 4 Estimaciones · Segunda Parte …html` (**PERT, tres valores**: te = (a + 4m + b) / 6; "se puede armar un cronograma asignando una distribución de probabilidad a cada tarea… con herramientas de simulación se obtienen plazos probables").

---

## 1. Qué se estima

| Variable | Unidad | Por qué importa |
|---|---|---|
| Cadencia de lanzamiento | misiones/mes | Cuello de botella (guía de alcance §5) |
| Satélites por misión | satélites | Varía por cohete (C-26) |
| Producción de satélites | satélites/semana | Capacidad declarada contra ritmo real (C-30) |
| Fecha de inicio de servicio | fecha | R-03 |
| <otra> | | |

## 2. Método elegido por variable

| Variable | Método (Clase 4) | Por qué ese método | Datos de base (`#n`) |
|---|---|---|---|
| | | | |

> Cómo completarlo: justificar con la cátedra. Por ejemplo, **análoga** (misiones ya voladas por cohete, `ev_serie.csv`), **paramétrica** (satélites por misión × misiones), **tres valores/PERT** donde hay alta incertidumbre. Ojo: el Monte Carlo de Riesgos ya usa una triangular para la cadencia; si acá se usa PERT (Beta), explicar la diferencia o unificar.

## 3. Estimación por tres valores (PERT)

| Variable | a (optimista, "sin milagros") | m (más probable) | b (pesimista, "sin catástrofes") | te = (a+4m+b)/6 | Fuente de cada valor |
|---|---|---|---|---|---|
| | | | | | |

> Cómo completarlo: cada valor con su origen (observado, declarado por Amazon o supuesto). No usar números sin fuente o sin supuesto escrito.

## 4. Ventana de estimación y reestimación

> Cómo completarlo: la Clase 4 propone estimar todo a alto nivel y en detalle la etapa siguiente, y reestimar al cerrar cada etapa. Proponer cuándo se reestima (por ejemplo, después de cada campaña de un cohete nuevo o de cada evento como LV-01).

## 5. Prejuicios y supuestos

> Cómo completarlo: la Clase 4 trata los prejuicios en las estimaciones. Aplicación: los anuncios de Amazon (capacidad, "20+ misiones") son declaraciones de la propia empresa y tienden al optimismo; la serie de promesas de servicio lo muestra (hitos §5).

**Coherencia:** cronograma (duraciones), Monte Carlo (distribuciones), costos (cantidades), cifras maestras §3.
