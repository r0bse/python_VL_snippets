from unittest.mock import patch
from unittest import TestCase


def answer():
    ans = input('enter yes or no')
    if ans == 'yes':
        return 'you entered yes'
    if ans == 'no':
        return 'you entered no'


class Test(TestCase):

    # get_input will return 'yes' during this test
    @patch('builtins.input', return_value='yes')
    def test_answer_yes(self, input):
        self.assertEqual(answer(), 'you entered yes')

    @patch('builtins.input', return_value='no')
    def test_answer_no(self, input):
        self.assertEqual(answer(), 'you entered no')
