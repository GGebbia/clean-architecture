from unittest import mock

class MyObj():
    def __init__(self, repo):
        self._repo = repo
        repo.connect()
    
    def setup(self):
        self._repo.setup(cache=True, max_connections=256)   

def test_connect():
    external_obj = mock.Mock()
    MyObj(external_obj)
    external_obj.connect.assert_called_with()

def test_setup():
    external_obj = mock.Mock()
    obj = MyObj(external_obj)
    obj.setup()
    external_obj.setup.assert_called_with(cache=True, max_connections=256)


