import sys

from search4letters.SetToStringParser import SetToStringParser
from search4letters.searchForLetters import Search4Letters


class Menu:

    def __init__(self):
        self.letterSearcher = Search4Letters()
        self.setParser = SetToStringParser()

    def show_menu(self):
        print("1: search4letter")
        print("2: search4Consonants")
        print("3: exit")
        selection = int(input("Insert Selection:"))
        self.evaluate_selection(selection)

    def evaluate_selection(self, selection: int):
        match selection:
            case 1:
                phrase = input("insert phrase:")
                letters = input("insert letters to search for:")
                resultSet =  self.letterSearcher.search_for_letters(phrase, letters)
                result = self.setParser.combine_set_to_string(resultSet)
                print("result = " + result)
            case 2:
                phrase = input("insert phrase:")
                resultSet = self.letterSearcher.search_for_consonants(phrase)
                result = self.setParser.combine_set_to_string(resultSet)
                print("result = " + result)
            case 3:
                exit()
            case _:
                print("Only the values 1,2 and 3 are allowed")

    def exit(self):
        sys.exit()
        