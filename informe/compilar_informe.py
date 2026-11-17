"""Compila el informe completo de Amazon Leo en un solo archivo.

Une, en el orden de informe/00-estructura.md, las secciones 00 a 14 (la 11
se reemplaza por la sección completa de Riesgos) y los anexos A a D, y
genera:
  - informe/Informe_Amazon_Leo.md
  - informe/Informe_Amazon_Leo.docx (si pandoc está instalado)

Uso (desde la raíz del repo o desde informe/):  python informe/compilar_informe.py
"""
from pathlib import Path
import re
import shutil
import subprocess

INF = Path(__file__).resolve().parent
RAIZ = INF.parent

SECCIONES = [
    "00-resumen-ejecutivo.md", "01-introduccion-y-metodo.md",
    "02-ubicacion-del-proyecto.md", "03-evidencia-y-fuentes.md",
    "04-actores-e-interesados.md", "05-caso-de-negocio.md",
    "06-acta-de-constitucion.md", "07-alcance-y-wbs.md",
    "08-cronograma-maestro.md", "09-estimaciones.md",
    "10-costos-y-presupuesto.md",
    ("riesgos/gestion-de-riesgos-amazon-leo.md", "11. Gestión de riesgos"),
    "12-seguimiento-y-valor-ganado.md", "13-integracion-y-coherencia.md",
    "14-conclusiones-y-limitaciones.md",
]
ANEXOS = [
    ("A", "Registro de fuentes", RAIZ / "evidencia/registro-fuentes.md"),
    ("B", "Cronología de hitos", RAIZ / "evidencia/hitos.md"),
    ("C", "Mapa de actores", RAIZ / "evidencia/actores.md"),
    ("D", "Cifras maestras", INF / "cifras-maestras.md"),
]


def bajar_titulos(texto):
    """Baja un nivel todos los títulos (# -> ##) fuera de bloques de código."""
    out, en_codigo = [], False
    for linea in texto.splitlines():
        if linea.startswith("```"):
            en_codigo = not en_codigo
        if not en_codigo and re.match(r"^#{1,5} ", linea):
            linea = "#" + linea
        out.append(linea)
    return "\n".join(out)


def main():
    partes = []
    for s in SECCIONES:
        if isinstance(s, tuple):
            ruta, titulo = s
            texto = (INF / ruta).read_text(encoding="utf-8")
            texto = re.sub(r"^# .*$", f"# {titulo}", texto, count=1, flags=re.M)
            texto = bajar_titulos(texto).replace(f"## {titulo}", f"# {titulo}", 1)
        else:
            texto = (INF / s).read_text(encoding="utf-8")
        partes.append(texto.strip())
    for letra, nombre, ruta in ANEXOS:
        texto = bajar_titulos(ruta.read_text(encoding="utf-8"))
        partes.append(f"# Anexo {letra}. {nombre}\n\n{texto.strip()}")
    partes.append("# Anexo E. Código\n\nScripts reproducibles (Python 3, sin dependencias externas):\n\n"
                  "- `informe/riesgos/analisis_cuantitativo.py`: Monte Carlo (Riesgos §5).\n"
                  "- `informe/estimaciones/pert_despliegue.py`: estimación PERT (sección 9).\n"
                  "- `informe/seguimiento/valor_ganado.py`: valor ganado y serie EV (sección 12).\n\n"
                  "# Anexo F. Verificación contra fuentes primarias\n\nVer `evidencia/verificacion-i1-2026-11-16.md`.")

    md = INF / "Informe_Amazon_Leo.md"
    md.write_text("\n\n---\n\n".join(partes) + "\n", encoding="utf-8", newline="\n")
    print(f"OK  {md.relative_to(RAIZ)}  ({len(md.read_text(encoding='utf-8').split()):,} palabras)")

    if shutil.which("pandoc"):
        docx = INF / "Informe_Amazon_Leo.docx"
        ref = INF / "riesgos/Gestion_de_Riesgos_Amazon_Leo.docx"
        cmd = ["pandoc", str(md), "-o", str(docx), "--toc", "--toc-depth=1",
               "--metadata", "title=Amazon Leo — Informe de investigación"]
        if ref.exists():
            cmd += ["--reference-doc", str(ref)]
        subprocess.run(cmd, check=True)
        print(f"OK  {docx.relative_to(RAIZ)}")
    else:
        print("pandoc no está instalado: se generó solo el .md")


if __name__ == "__main__":
    main()
