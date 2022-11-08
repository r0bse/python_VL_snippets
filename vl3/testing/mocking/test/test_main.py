from unittest import TestCase
from unittest.mock import patch

from vl3.testing.mocking.mock_intro import SumCalculator


class TestCalculator(TestCase):

    def setUp(self):
        self.calc = SumCalculator()

    def test_sum(self):
        answer = self.calc.sum(2, 4)
        self.assertEqual(answer, 6)

    @patch('vl3.testing.mocking.mock_intro.SumCalculator.sum',
           return_value=9)
    def test_mock_sum_function(self, sum):
        self.assertEqual(sum(2,3), 9)