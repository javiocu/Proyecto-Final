import changeImage as ch
import pytest

@pytest.fixture
def directorio_proyecto():
    return "changeImage.os.listdir"

@pytest.fixture
def lista_imagenes():
    return ["foto1.tiff", "foto2.tiff", "foto3.tiff", "foto34.tiff"]

@pytest.fixture
def mock_mocks_lista_imagenes(directorio_proyecto, lista_imagenes, mocker):
    mock_todos_archivos = mocker.patch(directorio_proyecto)
    mock_todos_archivos.return_value = lista_imagenes
    return mock_todos_archivos

def test_get_images_list_mock(mock_mocks_lista_imagenes, lista_imagenes):
    resultado = ch.get_images_list()

    assert resultado == lista_imagenes
    assert len(resultado) == len(lista_imagenes)
    assert all(img.endswith(".tiff") for img in resultado)
    assert mock_mocks_lista_imagenes.called

def test_get_images_list_file_not_found(mocker, capsys):
    mock_list_dir = mocker.patch("changeImage.os.listdir")
    mock_list_dir.side_effect = FileNotFoundError("No such file or directory")

    resultado = ch.get_images_list()
    mock_list_dir.assert_called_once()
    assert resultado == []
    assert len(resultado) == 0

    captured = capsys.readouterr()
    assert "No such file or directory" in captured.out
    assert "Quillo el archivo no está ahí, comprueba la ruta" in captured.out

def test_convertir_a_jpeg_mock(mocker, lista_imagenes):
    # Definimos mocks previos
    mock_image_instance = mocker.Mock()
    mock_image_rgb = mocker.Mock()
    mock_image_instance.convert.return_value = mock_image_rgb


    mock_get_images_list = mocker.patch("changeImage.get_images_list")
    mock_get_images_list.return_value = lista_imagenes
    mock_image_open = mocker.patch("changeImage.Image.open")
    mock_image_open.return_value = mock_image_instance

    ch.convertir_a_jpeg(mock_get_images_list)

    assert mock_image_open.called
    assert mock_get_images_list.called
    assert mock_image_open.call_count == len(lista_imagenes)
    mock_image_instance.convert.assert_called_with("RGB")

def test_convertir_a_jpeg_filenotfound(mocker, capsys):
    mock_get_images_list = mocker.patch("changeImage.get_images_list")
    mock_get_images_list.return_value = ["lista.tiff"]
    mock_image_open = mocker.patch("changeImage.Image.open")
    mock_image_open.side_effect = FileNotFoundError("No such file or directory")

    resultado = ch.convertir_a_jpeg(mock_get_images_list)

    assert resultado is None
    mock_image_open.assert_called_once()
    mock_get_images_list.assert_called_once()

    salida = capsys.readouterr()
    assert "No such file or directory" in salida.out
    assert "Hay un archivo que no se ha podido encontrar" in salida.out