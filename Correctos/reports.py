#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


def generate_report(attachment, title, paragraph):
    """Genera un reporte PDF.
    
    Args:
        attachment (str): Ruta donde guardar el PDF
        title (str): Título del documento
        paragraph (str): Contenido del reporte (puede contener HTML)
    """
    pdf = SimpleDocTemplate(attachment, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()
    
    # Añadir título
    titulo_pdf = Paragraph(title, styles["Title"])
    story.append(titulo_pdf)
    story.append(Spacer(1, 0.3 * inch))
    
    # Añadir contenido
    contenido = Paragraph(paragraph, styles["Normal"])
    story.append(contenido)
    
    # Construir y guardar PDF
    pdf.build(story)
