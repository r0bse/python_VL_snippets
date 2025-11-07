from unittest import TestCase

from vl3.search4letters.searchForLetters import Search4Letters
import string


class TestSearch4Letters(TestCase):
    def setUp(self):
        self.searcher = Search4Letters()

    def test_search_for_a(self):
        result = self.searcher.search_for_letters("aaaa", "a")
        self.assertEqual(set("a"), result)

    def test_search_for_empty(self):
        result = self.searcher.search_for_letters("aaaa", "")
        self.assertEqual(set(""), result)

    def test_search_for_empty(self):
        result = self.searcher.search_for_consonants("abcdefghi")
        self.assertEqual(set("aei"), result)

    def test_search_for_all_chars(self):
        result = self.searcher.search_for_consonants(string.ascii_letters)
        self.assertEqual(set("aeiou"), result)