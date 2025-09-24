#!/usr/bin/env python3

### Script para procesar las imágenes del suplier:
###     - Size --> 3000x2000 a 600x400 pixeles
###     - Format --> .TIFF a .JPEJ
import os
import re
import pytest
from PIL import Image

directorio_proy = "/home/javiocu/Proyecto-Final/Proyecto-Final/Imagenes"

# Procesar imagenes
#   - Identificar los nombres de las imágenes que se tienen en la carpeta origen:

def get_images_list():
    """Obtiene los nombres de todas las imágenes con formato .TIFF del directorio del proyecto.

    Returns:
        list[str]: Lista de nombres de archivos TIFF encontrados. 
                  Devuelve lista vacía si no hay archivos o el directorio no existe.
    
    Raises:
        FileNotFoundError: Si el directorio especificado no existe, se captura 
                          internamente y se devuelve lista vacía.
    """
    try:
        todas_las_imagenes = []
        todas_los_archivos = os.listdir(directorio_proy)
        for archivo in todas_los_archivos:
            if re.search(r"\w+\.tiff$", archivo, re.IGNORECASE):
                todas_las_imagenes.append(archivo)
        return todas_las_imagenes
    except FileNotFoundError as error:
        print(f"{error}: Quillo el archivo no está ahí, comprueba la ruta")
        return []

# - Convertir archivos .TIFF de alta resolución a imágenes JPEG optimizadas

def convertir_a_jpeg(directorio_proy, get_images_list):
    try:
        for nombre in get_images_list():
            noencontrado = nombre
            nombrejpg = nombre.split(".")[0] + ".jpeg"
            imagen = Image.open(os.path.join(directorio_proy, nombre))
            imagen.convert("RGB").save(os.path.join(directorio_proy, nombrejpg),
                                    "jpeg")
    except FileNotFoundError as error:
        print(f"{error}: Hay un archivo que no se ha podido encontrar: {noencontrado}")
        return None
        

# - Redimensionar automáticamente las imágenes para web

