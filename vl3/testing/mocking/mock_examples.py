from unittest.mock import patch

@patch('module.ClassB')
@patch('module.functionA')
def test_some_func(self, mock_A, mock_B):
    ...

