from unittest import TestCase

from vl3.vignere.vigner_table import encrypt_vignere, calculate_key, create_matrix


class Test(TestCase):
    def test_create_matrix(self):
        matrix = create_matrix("abc")
        expected_matrix= {'a': {'a': 'a', 'b': 'b', 'c': 'c'},
                          'b': {'a': 'b', 'b': 'c', 'c': 'a'},
                          'c': {'a': 'c', 'b': 'a', 'c': 'b'}}
        self.assertEqual(matrix, expected_matrix)

    def test_calculate_key(self):
        key = calculate_key("abcdefg", "cba")
        self.assertEqual(key, "cbacbac")

        key = calculate_key("123", "1234")
        self.assertEqual(key, "123")

        # self.assertRaises(ZeroDivisionError, calculate_key("123", ""))

    def test_encrypt_vignere(self):
        matrix = {'a': {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e'},
                  'b': {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'a'},
                  'c': {'a': 'c', 'b': 'd', 'c': 'e', 'd': 'a', 'e': 'b'},
                  'd': {'a': 'd', 'b': 'e', 'c': 'a', 'd': 'b', 'e': 'c'},
                  'e': {'a': 'e', 'b': 'a', 'c': 'b', 'd': 'c', 'e': 'd'}}
        result = encrypt_vignere(matrix, "abc", "ede")
        self.assertEqual(result, "eeb")