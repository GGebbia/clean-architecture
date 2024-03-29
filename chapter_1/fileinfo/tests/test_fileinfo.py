from fileinfo.fileinfo import FileInfo
from unittest.mock import patch

def test_init():
    filename = 'hola.txt'
    fi = FileInfo(filename)
    assert fi.filename == filename

def test_init_relative_path():
    filename = 'hola.txt'
    relative_path = '../{}'.format(filename)

    fi = FileInfo(relative_path)
    assert fi.filename == filename

@patch('os.path.getsize')
@patch('os.path.abspath')
def test_get_info(abspath_mock, getsize_mock):
    filename = 'hola.txt'
    original_path = '../{}'.format(filename)
    
    test_abspath = 'some/abs/path'
    abspath_mock.return_value = test_abspath

    test_size = 1234
    getsize_mock.return_value = test_size
    fi = FileInfo(original_path)

    assert fi.get_info() == (filename, original_path, test_abspath, test_size)


