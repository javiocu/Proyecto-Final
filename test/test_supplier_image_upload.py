import pytest
import os
import Imagenes.supplier_image_upload as sp

@pytest.fixture
def directorio_imagenes():
    return "/home/javiocu/Proyecto-Final/Proyecto-Final/Imagenes/"

@pytest.fixture
def lista_img_completa():
    return ["imagen.tiff", "imagen2.TIFF", "imagen.png", "imagen4.jpeg", "imagen5.jpeg"]

# ------------------------ TESTS GENERAR LISTA ------------------------

def test_generar_lista(mocker, lista_img_completa):
    """Test para comprobar que el método privado genera la lista de nombres con
    las imágenes a subir"""

    mock_lista_img = mocker.patch("supplier_image_upload.os.listdir", return_value = lista_img_completa)

    lista = sp._generar_lista()

    assert isinstance(lista, list)
    assert len(lista) == 2
    assert mock_lista_img.called


def test_filenotfound(mocker, capsys, directorio_imagenes):
    mock_lista = mocker.patch("supplier_image_upload.os.listdir")
    mock_directorio = mocker.patch("supplier_image_upload.DIRECTORIO", directorio_imagenes)

    mock_lista.side_effect = FileNotFoundError("No se ha encontrado el directorio")

    resul = sp._generar_lista()
    salida = capsys.readouterr()
    
    assert resul == []
    assert isinstance(resul, list)
    assert "No se ha encontrado el directorio" in salida.out
    assert f"No se ha encontrado el directorio: '{directorio_imagenes}'" in salida.out


# ------------------------ TESTS SUBIR ARCHIVOS ------------------------

# Parchear mock_os_listdir y completar el mock de open
def test_subida_imagenes(mocker):
    mock_generar = mocker.patch("supplier_image_upload._generar_lista",
                                return_value = ["imagen.jpeg", "imagen2.jpeg"])
    mock_open = mocker.patch("builtins.open", mocker.mock_open())
    mock_respuesta_falsa = mocker.Mock(status_code = 200)
    mock_request = mocker.patch("supplier_image_upload.requests.post", 
                                return_value = mock_respuesta_falsa)

    sp.subir_imagenes()

    mock_generar.assert_called_once()
