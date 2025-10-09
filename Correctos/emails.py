#!/usr/bin/env python3

import os
from email.message import EmailMessage
from mimetypes import guess_type
import smtplib


def generate_email(sender="automation@example.com",
                   to="student@example.com",
                   subject="Upload Completed - Online Fruit Store",
                   body="All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
                   attachment=None):
    """Genera un objeto EmailMessage listo para enviarse.
    
    Args:
        sender (str): Dirección de correo del remitente
        to (str): Dirección de correo del destinatario
        subject (str): Asunto del email
        body (str): Cuerpo del mensaje
        attachment (str): Ruta del archivo a adjuntar (opcional)
    
    Returns:
        EmailMessage: email completo
    """
    mail = EmailMessage()
    mail["From"] = sender
    mail["To"] = to
    mail["Subject"] = subject
    mail.set_content(body)
    
    if attachment is not None:
        path_absolute = os.path.expanduser(attachment)
        name_adjunto = os.path.basename(path_absolute)
        
        with open(path_absolute, "rb") as file:
            content = file.read()
        
        mimetype, _ = guess_type(name_adjunto)
        
        if mimetype is None:
            mimetype = "application/octet-stream"
        
        mime_type, mime_subtype = mimetype.split("/", 1)
        
        mail.add_attachment(content,
                          maintype=mime_type,
                          subtype=mime_subtype,
                          filename=name_adjunto)
    
    return mail


def send_email(message):
    """Envía un email a través del servidor SMTP en localhost."""
    server = smtplib.SMTP("localhost")
    server.send_message(message)
    server.quit()
