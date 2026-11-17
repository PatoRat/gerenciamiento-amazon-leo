# Amazon Leo

### Investigación del proyecto de constelación de satélites

Trabajo Integrador de Investigación · Dirección de Proyectos 2026 (UCA). Estado y próximos pasos: **[PROGRESO.md](PROGRESO.md)**.

## Cómo ver el trabajo

| Qué | Dónde | Cómo |
|---|---|---|
| Informe completo | `informe/Informe_Amazon_Leo.docx` (o `.md`) | Abrir en Word. Para regenerarlo: `python informe/compilar_informe.py` (requiere pandoc para el `.docx`) |
| Secciones por separado | `informe/00-…md` a `informe/14-…md` | En VS Code, `Ctrl+Shift+V` para la vista previa |
| Tablero ejecutivo | `dashboard/amazon-leo-dashboard.html` | Doble clic: se abre en el navegador, funciona sin internet. Botón "Descargar PDF". Para regenerarlo: `python dashboard/build_dashboard.py` |
| Guion de defensa | `dashboard/guion-defensa.md` | 16 preguntas probables y dónde está cada respuesta |
| Evidencia | `evidencia/` | Registro de fuentes (47), hitos, actores, verificación FCC/SEC |
| Cifras | `informe/cifras-maestras.md` | Fuente única de todos los números |

## Cálculos reproducibles (Python 3, sin dependencias)

```bash
python informe/riesgos/analisis_cuantitativo.py   # Monte Carlo: P50 ≈ 1.513 satélites al 30/07/2029
python informe/estimaciones/pert_despliegue.py    # PERT: fin ≈ 11/2035; P(2029) ≈ 0,07%
python informe/seguimiento/valor_ganado.py        # SPI 0,25 / 0,57 / 0,22; genera ev_serie.csv
```
