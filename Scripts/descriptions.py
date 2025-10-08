#!/usr/bin/env python3

# El archivo se llamará run.py
# Deberá hacer una solicitud post a la URL para subir el nombre de una fruta, 
# su peso y su descripción, lo hará de forma automática

import os
import requests

#DIRECTORIO = os.path.expanduser("~/supplier-data/descriptions/")
DIRECTORIO = "/home/javiocu/Proyecto-Final/Proyecto-Final/Descripciones/"
lista_archivos = os.listdir(DIRECTORIO)

def generar_json():
    """Función interna que genera un diccionario de json con la información necesaria
    para cada fruta.
    """
    print("Generando el json")
    dic_final = {}
    lista_frutas_archivos = []
    for i in lista_archivos:
        with open((DIRECTORIO + i), "r",encoding="UTF-8") as abierto:
            # Generamos el json y lo adjuntamos al diccionario vacío:
            lineas = abierto.read().splitlines()
            if i not in dic_final:
                dic_final[i] = {"name": lineas[0],
                                "weight": int(lineas[1].rstrip(" lbs")), 
                                "description": lineas[2], 
                                "image_name":  i.rstrip(".txt") + ".jpeg"}
    print("json generado")
    return dic_final

def subir_imagenes_desc():
    url = "http://localhost/fruits/"
    diccionario_json = generar_json()
    print("Intentando subir los elementos")
    contador = 1
    for elemento in diccionario_json.values():
        print("Subiendo elemento: " + str(contador))
        llamada = requests.post(url, json = elemento, timeout=10)
        print(llamada.status_code)
        contador += 1

if __name__ == "__main__":
    subir_imagenes_desc()
