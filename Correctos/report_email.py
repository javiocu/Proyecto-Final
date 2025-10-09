#!/usr/bin/env python3

import os
from datetime import date
import reports
import emails


DIRECTORIO = os.path.expanduser("~/supplier-data/descriptions/")


def main():
    """Genera PDF y envía email con reporte de frutas."""
    
    # PASO 1: Leer archivos y generar texto del reporte
    texto_reporte = ""
    
    try:
        archivos = sorted(os.listdir(DIRECTORIO))
        
        for archivo in archivos:
            if archivo.endswith('.txt'):
                ruta = os.path.join(DIRECTORIO, archivo)
                
                with open(ruta, 'r', encoding='UTF-8') as f:
                    lineas = f.read().splitlines()
                    
                    if len(lineas) >= 2:
                        # Formato con <br/> para ReportLab
                        texto_reporte += f"name: {lineas[0]}<br/>"
                        texto_reporte += f"weight: {lineas[1]}<br/><br/>"
    
    except FileNotFoundError:
        print(f"Error: Directorio {DIRECTORIO} no encontrado")
        return
    
    # PASO 2: Crear título con fecha actual
    fecha_hoy = date.today().strftime("%B %d, %Y")
    titulo = f"Processed Update on {fecha_hoy}"
    
    # PASO 3: Generar PDF
    ruta_pdf = "/tmp/processed.pdf"
    reports.generate_report(ruta_pdf, titulo, texto_reporte)
    print(f"✓ PDF generado: {ruta_pdf}")
    
    # PASO 4: Crear email con adjunto
    mensaje = emails.generate_email(
        sender="automation@example.com",
        to="student@example.com",
        subject="Upload Completed - Online Fruit Store",
        body="All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
        attachment=ruta_pdf
    )
    
    # PASO 5: Enviar email
    emails.send_email(mensaje)
    print("✓ Email enviado correctamente")


if __name__ == "__main__":
    main()
