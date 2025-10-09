#!/usr/bin/env python3

from emails import generate_email, send_email
from reports import generate_report

if __name__ == "__main__":
    generate_report()
    send_email(generate_email())