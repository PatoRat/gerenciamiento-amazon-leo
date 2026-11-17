"""Genera el dashboard autónomo a partir de los datos del equipo.

Lee dashboard/datos/kpis.json, lo embebe en dashboard/plantilla-dashboard.html
y escribe dashboard/amazon-leo-dashboard.html (un único archivo, sin
dependencias de red: funciona sin internet).

Uso:  python dashboard/build_dashboard.py
Para cambiar un número: editar kpis.json (y antes informe/cifras-maestras.md) y volver a correr.
"""
from pathlib import Path
import json
import re

D = Path(__file__).resolve().parent
datos = json.loads((D / "datos" / "kpis.json").read_text(encoding="utf-8"))
plantilla = (D / "plantilla-dashboard.html").read_text(encoding="utf-8")
assert "/*__DATA__*/null" in plantilla, "falta el marcador de datos en la plantilla"

js = json.dumps(datos, ensure_ascii=False).replace("</", "<\\/")
html = plantilla.replace("/*__DATA__*/null", js)

# Control: sin recursos externos (el namespace SVG no es una descarga)
externos = [u for u in re.findall(r"""(?:src|href)\s*=\s*["'](https?:[^"']+)""", html)]
assert not externos, f"recursos externos no permitidos: {externos}"

out = D / "amazon-leo-dashboard.html"
out.write_text(html, encoding="utf-8", newline="\n")
print(f"OK  {out.name}  ({len(html) / 1024:.0f} KB, sin dependencias de red)")
