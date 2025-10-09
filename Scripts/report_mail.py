#!/usr/bin/env python3

## Script para generar automáticamente un pdf reporte

import datetime as dt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from descriptions import generar_json
from emails import generate_email, send_email
import health_check

DIRECTORIO = os.path.expanduser("~/supplier-data/descriptions/")
#DIRECTORIO = "/home/javiocu/Proyecto-Final/Proyecto-Final/Descripciones/"

def generate_report(title="processed.pdf"):
    pdf = SimpleDocTemplate(title, pagesize = letter)
    story = []
    fecha = dt.datetime.now().strftime("%B %d, %Y")
    titulo = Paragraph("Processed Update on " + fecha, style=getSampleStyleSheet()["Title"])

    story.append(titulo)

    salto_grande = Spacer(0, 0.2 * inch)
    salto_pequeño = Spacer(0, 0.1 * inch)

    story.append(salto_grande)

    for elemento in generar_json().values():
        name = elemento["name"]
        weight = elemento["weight"]
        cuerpo_texto = Paragraph(f"name: {name}")
        story.append(cuerpo_texto)
        cuerpo_texto = Paragraph(f"weight: {weight} lbs")
        story.append(cuerpo_texto)
        story.append(salto_pequeño)


    pdf.build(story)



if __name__ == "__main__":
    generate_report()