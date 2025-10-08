#!/usr/bin/env python3

import os
from email.message import EmailMessage
from mimetypes import guess_type
import smtplib


def generate_email(sender = "automation@example.com",
                  to = "student@example.com",
                  subject = "Upload Completed - Online Fruit Store",
                  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email",
                  attachment = None):
  """Genera un mail que puede usarse para enviarse mediante el segundo método.
  Este método solo genera el mail y maneja un posible adjunto.

  Args:
      sender (str, optional): _description_. Defaults to "automation@example.com".
      to (str, optional): _description_. Defaults to "student@example.com".
      subject (str, optional): _description_. Defaults to "Upload Completed - Online Fruit Store".
      body (str, optional): _description_. Defaults to "All fruits are uploaded to our website successfully. A detailed list is attached to this email".
      attachment (optional): _description_. Defaults to None.

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
      mime_type, mime_subtype = mimetype.split("/", 1)
      mail.add_attachment(content,
                          maintype = mime_type,
                          subtype = mime_subtype,
                          filename = name_adjunto)
  return mail



def send_email(message):
  server = smtplib.SMTP("localhost")
  server.send_message(message)
  server.quit()