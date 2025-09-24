import changeImage as ch
import pytest

@pytest.fixture
def directorio_proyecto():
    return "changeImage.os.listdir"

@pytest.fixture
def lista_imagenes():
    return ["foto1.tiff", "foto2.tiff", "foto3.tiff"]

def test_get_images_list_mock(mocker, directorio_proyecto, lista_imagenes):
    # Defino mocks necesarios
    mock_todos_archivos = mocker.patch(directorio_proyecto)
    # Defino valores finales de mocks
    mock_todos_archivos.return_value = lista_imagenes

    resultado = ch.get_images_list()
    assert resultado == lista_imagenes
    assert len(resultado) == 3
    assert all(img.endswith(".tiff") for img in resultado)

def test_convertir_a_jpeg_mock(mocker, lista_imagenes, directorio_proyecto):
    # Definimos mocks previos
    mock_image_instance = mocker.Mock()
    mock_image_rgb = mocker.Mock()
    mock_image_instance.convert.return_value = mock_image_rgb
    
    mock_get_images_list = mocker.patch("changeImage.get_images_list")
    mock_get_images_list.return_value = lista_imagenes
    mock_image_open = mocker.patch("changeImage.Image.open")
    mock_image_open.return_value = mock_image_instance
    
    directorio = directorio_proyecto
    
    ch.convertir_a_jpeg(directorio, mock_get_images_list)
    
    assert mock_image_open.called
    assert mock_get_images_list.called
    assert mock_image_open.call_count == len(lista_imagenes)