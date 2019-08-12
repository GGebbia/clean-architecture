from unittest.mock import patch

from fileinfo.logger import Logger

@patch('fileinfo.logger.datetime.datetime')
def test_log(mock_datetime):
    time_now = 123
    test_message = 'This is a test'
    mock_datetime.now.return_value = time_now

    test_logger = Logger()
    test_logger.log(test_message)
    assert test_logger.messages == [(time_now, test_message)]
