"""Valor ganado en unidades físicas (satélites) - Amazon Leo.

Aplica las fórmulas de la cátedra (Clase 6, Seguimiento y Valor Ganado)
usando satélites desplegados como medida de avance (output, no input).

  BAC = 3.232 satélites (hito final FCC)          [DATO REAL]  #8 ¶3
  EV  = satélites lanzados acumulados              [INFERENCIA] suma de #2
  PV  = lo planificado a la fecha, según 2 líneas base:
        A) Regulatoria: 1.616 al 30/07/2026 y 3.232 al 30/07/2029 (#8 ¶3)
        B) Plan de Amazon a la FCC: ~700 al 30/07/2026 (#8 ¶8)
  AC  = costo real: NO PÚBLICO -> CPI no calculable.

Entre hitos, la línea base A se interpola linealmente: es una PROPUESTA
DE GESTIÓN del grupo (la FCC solo fija los dos puntos).

Uso: python valor_ganado.py   (genera ev_serie.csv en esta carpeta)
"""
from datetime import date
from pathlib import Path
import csv

# --- Misiones (evidencia/hitos.md §1, fuente #2; LV-01 fallida, #11) ---
MISIONES = [
    ("KA-01", date(2025, 4, 28), "Atlas V", 27),
    ("KA-02", date(2025, 6, 23), "Atlas V", 27),
    ("KF-01", date(2025, 7, 16), "Falcon 9", 24),
    ("KF-02", date(2025, 8, 11), "Falcon 9", 24),
    ("KA-03", date(2025, 9, 25), "Atlas V", 27),
    ("KF-03", date(2025, 10, 14), "Falcon 9", 24),
    ("LA-04", date(2025, 12, 16), "Atlas V", 27),
    ("LE-01", date(2026, 2, 12), "Ariane 64", 32),
    ("LA-05", date(2026, 4, 4), "Atlas V", 29),
    ("LA-06", date(2026, 4, 28), "Atlas V", 29),
    ("LE-02", date(2026, 4, 30), "Ariane 64", 32),
    ("LA-07", date(2026, 5, 29), "Atlas V", 29),
    ("LE-03", date(2026, 6, 17), "Ariane 64", 36),
    ("LA-08", date(2026, 7, 2), "Atlas V", 29),
    ("LV-01", date(2026, 11, 15), "Vulcan", 0),   # 40 perdidos: no suma EV
]

BAC = 3232
HITO_50 = (date(2026, 7, 30), 1616)
HITO_100 = (date(2029, 7, 30), 3232)
PLAN_AMAZON_2026 = 700            # ~700 al 30/07/2026 (#8 ¶8)
CORTE = date(2026, 11, 16)        # fecha de corte propuesta


def ev(fecha):
    return sum(s for _, d, _, s in MISIONES if d <= fecha)


def pv_regulatoria(fecha):
    """Línea base A. Antes del hito 50% solo se usa en esa fecha."""
    (d1, v1), (d2, v2) = HITO_50, HITO_100
    if fecha <= d1:
        return v1 if fecha == d1 else None
    if fecha >= d2:
        return v2
    return v1 + (v2 - v1) * (fecha - d1).days / (d2 - d1).days


def meses(d1, d2):
    return (d2 - d1).days / 30.4375


def fila(nombre, fecha, pv):
    e = ev(fecha)
    vcr = e - pv
    return {
        "corte": nombre, "fecha": fecha.strftime("%d/%m/%Y"),
        "PV": round(pv), "EV": e, "Vcr": round(vcr),
        "%Vcr": f"{vcr / pv:.0%}", "SPI": f"{e / pv:.2f}",
    }


if __name__ == "__main__":
    print(f"BAC = {BAC} satélites · EV al {CORTE:%d/%m/%Y} = {ev(CORTE)} "
          f"({ev(CORTE) / BAC:.1%} de avance físico)\n")

    filas = [
        fila("Hito 50% · línea base A (FCC)", HITO_50[0], HITO_50[1]),
        fila("Hito 50% · línea base B (plan Amazon)", HITO_50[0], PLAN_AMAZON_2026),
        fila("Corte · línea base A (interpolada)", CORTE, pv_regulatoria(CORTE)),
    ]
    print(f"{'Corte':40s} {'Fecha':>10s} {'PV':>6s} {'EV':>5s} {'Vcr':>6s} {'%Vcr':>6s} {'SPI':>5s}")
    for f in filas:
        print(f"{f['corte']:40s} {f['fecha']:>10s} {f['PV']:>6} {f['EV']:>5} "
              f"{f['Vcr']:>6} {f['%Vcr']:>6s} {f['SPI']:>5s}")

    # Proyección: ¿cuándo termina? (ritmo observado y plan de Amazon)
    inicio = MISIONES[0][1]
    ritmo = ev(CORTE) / meses(inicio, CORTE)        # satélites/mes observados
    faltan = BAC - ev(CORTE)
    print(f"\nRitmo observado: {ritmo:.1f} sat/mes desde {inicio:%d/%m/%Y}")
    for nombre, r in [("ritmo observado", ritmo),
                      ("plan Amazon (20 misiones/año x 30)", 20 * 30 / 12),
                      ("ritmo necesario", faltan / meses(CORTE, HITO_100[0]))]:
        m = faltan / r
        anio = CORTE.year + (CORTE.month - 1 + m) / 12
        print(f"  A {nombre:36s} {r:5.1f} sat/mes -> faltan {m:5.1f} meses "
              f"(≈ {anio:.1f})")

    # Serie EV acumulada para el dashboard
    out = Path(__file__).with_name("ev_serie.csv")
    with out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["mision", "fecha", "cohete", "satelites_desplegados",
                    "ev_acumulado", "pv_lineabase_A"])
        for m, d, c, s in MISIONES:
            pva = pv_regulatoria(d)
            w.writerow([m, d.isoformat(), c, s, ev(d),
                        "" if pva is None else round(pva)])
    print(f"\nSerie guardada en {out.name}")
