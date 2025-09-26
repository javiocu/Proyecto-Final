#!/usr/bin/env python3

import os
import requests
import re

# Script para subir las imagenes generadas a un servidor web
DIRECTORIO = "/home/javiocu/Proyecto-Final/Proyecto-Final/Imagenes"

def _generar_lista():
    lista_imagenes = []
    try:
        for archivo in os.listdir(DIRECTORIO):
            if re.search(r"\w+\.jpeg$", archivo, re.IGNORECASE):
                lista_imagenes.append(archivo)
    except FileNotFoundError:
        print(f"FileNotFoundError: No se ha encontrado el directorio: '{DIRECTORIO}'")
        return []
    return lista_imagenes

