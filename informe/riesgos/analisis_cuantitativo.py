"""Análisis cuantitativo del riesgo R-04 (hito FCC del 30/07/2029) - Amazon Leo.

Pregunta: ¿cuántos satélites habría operativos el 30/07/2029 y con qué
probabilidad se llega a 3.232? Todo supuesto está en las constantes de abajo
y es una PROPUESTA del grupo, no un dato publicado.
Uso: python3 analisis_cuantitativo.py
"""
import random

random.seed(20261116)          # reproducible
N = 100_000                    # simulaciones

# --- Datos (fuentes en el informe) ---
ACTUALES = 396                 # satélites lanzados antes de LV-01 (Amazon, #2)
OBJETIVO = 3232                # hito final (FCC DA 26-553 ¶3)
MESES = 32.5                   # del 16/11/2026 al 30/07/2029

# --- Supuestos del grupo [PROPUESTA] ---
# Cadencia en misiones por mes: triangular(mín, máx, moda).
#   mín 0,5 : lanzadores clave en tierra buena parte del período (R-02)
#   moda 0,92: ritmo observado desde 28/04/2026 (≈ 11 por año, #2)
#   máx 2,0 : plan de Amazon "20+ misiones" en el año dos (#23) y un poco más
CAD = dict(low=0.5, high=2.0, mode=0.92)
# Satélites por misión: triangular(24, 40, moda 30) (rango de #2 y #3)
SAT = dict(low=24, high=40, mode=30)

def tri(p):
    return random.triangular(p["low"], p["high"], p["mode"])

def simular():
    res = []
    for _ in range(N):
        misiones = tri(CAD) * MESES
        total = ACTUALES + misiones * tri(SAT)
        res.append(total)
    res.sort()
    return res

def pct(v, p):
    return v[int(p / 100 * (len(v) - 1))]

if __name__ == "__main__":
    # 1) Escenarios determinísticos
    print("ESCENARIOS (misiones por año -> satélites al 30/07/2029, 30 por misión)")
    for nombre, por_anio in [("Ritmo observado", 11), ("Plan de Amazon (20/año)", 20),
                             ("Ritmo necesario", 35)]:
        m = por_anio / 12 * MESES
        t = ACTUALES + m * 30
        print(f"  {nombre:26s} {por_anio:>3} /año  {m:5.1f} misiones  {t:7.0f} sat  {t/OBJETIVO:5.0%} de {OBJETIVO}")
    print(f"  Necesario: {(OBJETIVO-ACTUALES)/30/MESES*12:.1f} misiones por año a 30 satélites")
    # 2) Monte Carlo
    r = simular()
    print(f"\nMONTE CARLO ({N:,} simulaciones)")
    for p in (10, 50, 90):
        print(f"  P{p}: {pct(r,p):6.0f} satélites ({pct(r,p)/OBJETIVO:4.0%})")
    print(f"  P(llegar a {OBJETIVO}): {sum(1 for x in r if x>=OBJETIVO)/N:.2%}")
    # 3) Sensibilidad: ¿y si el máximo de cadencia fuese mayor?
    print("\nSENSIBILIDAD al máximo de cadencia (misiones/mes)")
    for hi in (2.0, 2.5, 3.0, 3.5):
        CAD["high"] = hi
        rr = simular()
        print(f"  máx {hi}: P(llegar) = {sum(1 for x in rr if x>=OBJETIVO)/N:.1%}, P50 = {pct(rr,50):.0f}")
