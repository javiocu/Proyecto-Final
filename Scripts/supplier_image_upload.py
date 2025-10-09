#!/usr/bin/env python3

import os
import requests
import re

# Módulo para subir las imagenes generadas a un servidor web
#DIRECTORIO = "/home/javiocu/Proyecto-Final/Proyecto-Final/Imagenes"
DIRECTORIO = os.path.expanduser("~/supplier-data/images/")

def _generar_lista():
    """Método privado para generar la lista de nombres de los archivos que se
    subirán al servidor. Filtra archivos para seleccionar solo las 'JPEG'.
    Ignora mayúsculas y minúsculas. Maneja el error del directorio no encontrado.

    Returns:
        List[str]: Devuelve una lista de str, con los nombres de los archivos
                ya filtrados para jpeg que se subirán al servidor
    
    Raises:
        FileNotFoundError: 
    """
    lista_imagenes = []
    try:
        for archivo in os.listdir(DIRECTORIO):
            if re.search(r"\w+\.jpeg$", archivo, re.IGNORECASE):
                lista_imagenes.append(archivo)
    except FileNotFoundError:
        print(f"FileNotFoundError: No se ha encontrado el directorio: '{DIRECTORIO}'")
        return []
    return lista_imagenes


def subir_imagenes():
    url = "http://localhost/upload/"
    for archivo in _generar_lista():
        try:
            with open(os.path.join(DIRECTORIO, archivo), "rb") as abierto:
                llamada = requests.post(url, files={"file": abierto}, timeout=10)
                print(llamada.status_code)
        except TimeoutError:
            print(f"TimeoutError: Han pasado 10 segundos y no se sube")
            
            
if __name__ == "__main__":
    subir_imagenes()
