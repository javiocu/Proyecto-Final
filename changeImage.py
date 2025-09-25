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
    """Captura todas las imágenes con formato TIFF.
    
    Recorre el directorio de trabajo en busca de ellas. Busca imágenes formato 
    .tiff o .TIFF (insensible a mayúsculas o minúsculas) en el directorio 
    proporcionado en la variable global 'directorio_proy'.

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

def convertir_a_jpeg(get_images_list=get_images_list):
    """Recibe una lista de nombres de imágenes tipo TIFF que convierte en RGB
    y pasa a formato JPEG
    
    Utiliza el método 'get_images_list' para obtener una lista de imágenes
    existentes en el directorio proporcionado por la variable global
    'directorio_proy', y las convierte al 'JPEG' guardando las imágenes salientes
    en el mismo directorio

    Args:
        get_images_list (function): Captura todas las imágenes con formato TIFF.

    Returns:
        None: No devuelve nada, guarda la imagen JPEG en el mismo directorio
        'directorio_proy'
    
    Raises:
        FileNotFoundError: Devuelve este error cuando alguna de las imágenes no 
        se detectan en el directorio 'directorio_proy'.        
    """
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
        

# - Redimensionar automáticamente las imágenes para web de 3000x2000 a 600x400

imagen = Image.new("RGB",(3000, 2000), color="Red")

print(imagen.size)