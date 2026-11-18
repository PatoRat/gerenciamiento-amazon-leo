"""Ajusta el formato del Word resumido (el estilo por defecto de pandoc deja 10 pt
después de cada párrafo, también dentro de las tablas, y suma varias páginas).

Uso, desde informe/resumido/:
    pandoc Informe_Amazon_Leo_resumido.md -o Informe_Amazon_Leo_resumido.docx --toc --toc-depth=1 \
        --reference-doc ../riesgos/Gestion_de_Riesgos_Amazon_Leo.docx
    python ajustar_word.py
Requiere: python-docx.
"""
from docx import Document
from docx.shared import Pt, Cm

ARCHIVO = "Informe_Amazon_Leo_resumido.docx"
d = Document(ARCHIVO)
for s in d.sections:  # A4 con márgenes de 2 cm
    s.page_width, s.page_height = Cm(21.0), Cm(29.7)
    s.left_margin = s.right_margin = s.top_margin = s.bottom_margin = Cm(2.0)

def fmt(p, despues, interlineado):
    p.paragraph_format.space_after = Pt(despues)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.line_spacing = interlineado

for p in d.paragraphs:
    if p.style.name.startswith("Heading"):
        continue
    fmt(p, 2, 1.0) if p.style.name.startswith("TOC") else fmt(p, 5, 1.08)
for t in d.tables:  # celdas sin espacio extra y con texto de 9 pt
    for fila in t.rows:
        for celda in fila.cells:
            for p in celda.paragraphs:
                fmt(p, 0, 1.0)
                for r in p.runs:
                    r.font.size = Pt(9)
d.save(ARCHIVO)
