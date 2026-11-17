"""Estimación PERT (tres valores) de la duración del despliegue restante.

Cátedra: Clase 4 Estimaciones, 2da parte (te = (a + 4m + b) / 6;
sigma = (b - a) / 6). Se estima la DURACIÓN para desplegar los satélites
que faltan, a partir de tres cadencias. Los valores a, m y b son los
mismos que usa el Monte Carlo de Riesgos (§5), para que las dos
herramientas sean coherentes.

  a (optimista, "sin milagros"):   2,0 misiones/mes = 24/año (máximo del Monte Carlo; plan "20+", #23)
  m (más probable):                0,92 misiones/mes ≈ 11/año (ritmo desde 28/04/2026, #2)
  b (pesimista, "sin catástrofes"): 0,5 misiones/mes = 6/año (lanzadores clave en tierra, R-02)
  30 satélites por misión (C-26). Todo es PROPUESTA DE GESTIÓN del grupo.

Uso: python pert_despliegue.py
"""
from datetime import date, timedelta
from math import erf, sqrt

FALTAN = 3232 - 396                 # C-14
SAT_POR_MISION = 30
CORTE = date(2026, 11, 16)
HITO = date(2029, 7, 30)
CADENCIAS = {"a (optimista)": 2.0, "m (más probable)": 0.92, "b (pesimista)": 0.5}


def meses_para(cadencia):
    return FALTAN / (cadencia * SAT_POR_MISION)


def fecha(meses):
    return CORTE + timedelta(days=meses * 30.4375)


if __name__ == "__main__":
    d = {k: meses_para(v) for k, v in CADENCIAS.items()}
    for k, v in d.items():
        print(f"{k:20s} {CADENCIAS[k]:4.2f} misiones/mes -> {v:6.1f} meses (≈ {fecha(v):%m/%Y})")
    a, m, b = d["a (optimista)"], d["m (más probable)"], d["b (pesimista)"]
    te = (a + 4 * m + b) / 6
    s = (b - a) / 6
    print(f"\nte = (a + 4m + b) / 6 = {te:.1f} meses (≈ {fecha(te):%m/%Y})")
    print(f"sigma = (b - a) / 6 = {s:.1f} meses")
    disponible = (HITO - CORTE).days / 30.4375
    z = (disponible - te) / s
    p = 0.5 * (1 + erf(z / sqrt(2)))
    print(f"Meses disponibles hasta el hito: {disponible:.1f} -> z = {z:.2f} -> "
          f"P(terminar a tiempo) ≈ {p:.2%} (aprox. normal)")
    for k in (1, 2):
        print(f"te + {k}σ = {te + k * s:.1f} meses (≈ {fecha(te + k * s):%m/%Y})")
