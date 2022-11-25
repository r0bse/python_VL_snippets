
import string


def hello(name):
    print('Hello ', name)

from unittest.mock import patch

@patch('builtins.print')
def test_greet(mock_print):
    hello('World')
    mock_print.assert_called_with('Hello ', 'World')
    hello('Umweltinformatik')
    mock_print.assert_called_with('Hello ', 'Umweltinformatik')

