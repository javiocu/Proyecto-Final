import pytest
import os
import supplier_image_upload as sp

@pytest.fixture
def directorio_imagenes():
    return "/home/javiocu/Proyecto-Final/Proyecto-Final/Imagenes/"

@pytest.fixture
def lista_img():
    return ["imagen.tiff", "imagen2.TIFF", "imagen.png", "imagen4.jpeg", "imagen5.jpeg"]

def test_generar_lista(mocker, lista_img):
    """Test para comprobar que el método privado genera la lista de nombres con
    las imágenes a subir"""

    mock_lista_img = mocker.patch("supplier_image_upload.os.listdir", return_value = lista_img)

    lista = sp._generar_lista()

    assert isinstance(lista, list)
    assert len(lista) == 2
    assert mock_lista_img.called


def test_filenotfound(mocker, capsys, lista_img, directorio_imagenes):
    mock_lista = mocker.patch("supplier_image_upload.os.listdir")
    mock_directorio = mocker.patch("supplier_image_upload.DIRECTORIO", directorio_imagenes)

    mock_lista.side_effect = FileNotFoundError("No se ha encontrado el directorio")

    resul = sp._generar_lista()
    salida = capsys.readouterr()
    
    assert resul == []
    assert isinstance(resul, list)
    assert "No se ha encontrado el directorio" in salida.out
    assert f"No se ha encontrado el directorio: '{directorio_imagenes}'" in salida.out
