# tests.py -- for simple_request.py

from unittest import TestCase
from unittest.mock import patch

from simple_request import do_hello, URL

class FakeResult:
    text = '<title>Google</title>'

class TestSimpleRequest(TestCase):
    
    @patch('requests.get')
    def test_simplerequest(self, mock_get):
        mock_get.return_value = FakeResult()

        do_hello()
        mock_get.assert_called_with(URL)

if __name__ == '__main__':
    from unittest import main
    main()