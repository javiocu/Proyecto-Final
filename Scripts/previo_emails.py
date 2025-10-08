import os
from email.message import EmailMessage
import mimetypes
import smtplib
import getpass



def generate_email():
    ruta_adjunto = "/home/javiocu/Proyecto-Final/Proyecto-Final/processed.pdf"
    nombre_adjunto = os.path.basename(ruta_adjunto)
    mimetype, _ = mimetypes.guess_type(nombre_adjunto)
    mime_type, mime_subtype = mimetype.split("/", 1)

    mensaje = EmailMessage()
    sender = "automation@example.com"
    recipient = "student@example.com"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    subject = "Upload Completed - Online Fruit Store"

    mensaje["From"] = sender
    mensaje["To"] = recipient
    mensaje["Subject"] = subject
    mensaje.set_content(body)

    with open(ruta_adjunto, "rb") as ap:
        mensaje.add_attachment(ap.read(),
                               maintype = mime_type,
                               subtype = mime_subtype,
                               filename = nombre_adjunto)
    return mensaje

def send():
  """Sends the message to the configured SMTP server."""
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(generate_email())
  mail_server.quit()




if __name__ == "__main__":
    mail_server = smtplib.SMTP_SSL('smtp.example.com')

    sender = 'tu_email@gmail.com'
    mail_pass = getpass.getpass('Password? ')
    mail_server.login(sender, mail_pass)

    print(mail_pass)