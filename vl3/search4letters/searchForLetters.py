
class Search4Letters:

    def search_for_consonants(self, phrase:str) -> set:
        resultset = self.search_for_letters(phrase, "aeiou")
        return resultset

    def search_for_letters(self, phrase:str, letters:str) -> set:
        resultset = set(letters).intersection(set(phrase))
        return resultset

