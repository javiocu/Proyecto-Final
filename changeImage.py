#!/usr/bin/env python3

### Script para procesar las imágenes del suplier:
###     - Size --> 3000x2000 a 600x400 pixeles
###     - Format --> .TIFF a .JPEJ
import os
import re
from PIL import Image

directorio_proy = "/home/javiocu/coursera-docker/Module_4/"

# Procesar imagenes
#   - Identificar los nombres de las imágenes que se tienen en la carpeta origen:

def _get_images_list():
    """Método privado para obtener los nombres de todas las imágenes
    con formato .TIFF.

    Returns:
        class'list': Imagen en formato .JPEG
    """
    try:
        todas_las_imagenes = []
        todas_los_archivos = os.listdir(directorio_proy)
        for archivo in todas_los_archivos:
            if re.search(r"\w+\.tiff$", archivo):
                todas_las_imagenes.append(archivo)
        return todas_las_imagenes
    except FileNotFoundError as errior:
        print(f"{errior}: Quillo el archivo no está ahí, comprueba la ruta")

# - Convertir archivos .TIFF de alta resolución a imágenes JPEG optimizadas
lista_temporal = ["mango.tiff"]

for imagen in _get_images_list():
    imagen = Image.open(os.path.join(directorio_proy, imagen))
    imagen.convert("RGB").save(os.path.join("manguito.jpeg"))