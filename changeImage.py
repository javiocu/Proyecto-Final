#!/usr/bin/env python3

### Script para procesar las imágenes del suplier:
###     - Size --> 3000x2000 a 600x400 pixeles
###     - Format --> .TIFF a .JPEJ
import os
import re
from PIL import Image

# Cambiar el directorio del proyecto en función del que se vaya a usar
DIRECTORIO_PROY = "/home/javiocu/Proyecto-Final/Proyecto-Final/Imagenes"

# Procesar imagenes
#   - Identificar los nombres de las imágenes que se tienen en la carpeta origen:

def get_images_list():
    """Captura todas las imágenes con formato TIFF.
    
    Recorre el directorio de trabajo en busca de ellas. Busca imágenes formato 
    .tiff o .TIFF (insensible a mayúsculas o minúsculas) en el directorio 
    proporcionado en la variable global 'DIRECTORIO_PROY'.

    Returns:
        list[str]: Lista de nombres de archivos TIFF encontrados. 
                  Devuelve lista vacía si no hay archivos o el directorio no existe.
    
    Raises:
        FileNotFoundError: Si el directorio especificado no existe, se captura 
                          internamente y se devuelve lista vacía.
    """
    try:
        # Creo lista vacía para rellenarla con los nombres de los archivos de
        # imagen
        todas_las_imagenes = []
        todas_los_archivos = os.listdir(DIRECTORIO_PROY)
        for archivo in todas_los_archivos:
            # Itero sobre todos los archivos de imagen para generar la lista con
            # los nombres, ignora mayúsculas y minúsculas
            if re.search(r"\w+\.tiff$", archivo, re.IGNORECASE):
                todas_las_imagenes.append(archivo)
        return todas_las_imagenes
    # Se maneja el error de FileNotFoundError
    except FileNotFoundError as error:
        print(f"{error}: Quillo el archivo no está ahí, comprueba la ruta")
        return []

# - Convertir archivos .TIFF de alta resolución a imágenes JPEG optimizadas

def convertir_a_jpeg(get_images_list=get_images_list):
    """Recibe una lista de nombres de imágenes tipo TIFF que convierte en RGB
    y pasa a formato JPEG
    
    Utiliza el método 'get_images_list' para obtener una lista de imágenes
    existentes en el directorio proporcionado por la variable global
    'DIRECTORIO_PROY', y las convierte al 'JPEG' guardando las imágenes salientes
    en el mismo directorio

    Args:
        get_images_list (str): Captura todas las imágenes con formato TIFF.
        El método entra como una str.
    Returns:
        None: No devuelve nada, guarda la imagen JPEG en el mismo directorio
        'DIRECTORIO_PROY'
    
    Raises:
        FileNotFoundError: Devuelve este error cuando alguna de las imágenes no 
        se detectan en el directorio 'DIRECTORIO_PROY'.        
    """
    try:
        for nombre in get_images_list():
            # Por si no encuentra el archivo para poder manejarlo asociamos cada
            # nuevo elemento de la lista a una variable
            noencontrado = nombre
            # Spliteamos el nombre para obtener el nuevo nombre del archivo final
            # con jpeg
            nombrejpg = nombre.split(".")[0] + ".jpeg"
            # Creamos la instancia de la imagen:
            imagen = Image.open(os.path.join(DIRECTORIO_PROY, nombre))
            # Convertimos la imagen a RGB y redimensionamos, guardamos la nueva
            # imagen en el directorio del proyecto con el nombre .jpeg
            imagen.convert("RGB").resize((600, 400)).save(os.path.join(DIRECTORIO_PROY, nombrejpg),
                                    "jpeg")
    except FileNotFoundError as error:
        print(f"{error}: Hay un archivo que no se ha podido encontrar: {noencontrado}")
        return None
