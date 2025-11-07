from unittest import TestCase
from unittest.mock import patch, call

from vl3.search4letters.app import start


class Test(TestCase):

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["1", "abcdefghi", "cba"])
    def test_menu_with_search_for_letters(self, mock_input, mock_print):
        start()

        expected_print_calls = [
            call("1: search4letter"),
            call("2: search4Consonants"),
            call("3: exit"),
            call("result = abc")
        ]

        mock_print.assert_has_calls(expected_print_calls)

        expected_print_calls = [
            call("Insert Selection:"),
            call("insert phrase:"),
            call("insert letters to search for:")
        ]

        mock_input.assert_has_calls(expected_print_calls)

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["2", "abcdefghi"])
    def test_menu_with_search_for_consonants(self, mock_input, mock_print):
        start()

        expected_print_calls = [
            call("1: search4letter"),
            call("2: search4Consonants"),
            call("3: exit"),
            call("result = aei")
        ]

        mock_print.assert_has_calls(expected_print_calls)

        expected_print_calls = [
            call("Insert Selection:"),
            call("insert phrase:")
        ]

        mock_input.assert_has_calls(expected_print_calls)