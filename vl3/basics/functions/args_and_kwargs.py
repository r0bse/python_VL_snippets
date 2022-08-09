def several_arguments(*args):
    """
    nimmt eine Liste von argumenten entgegn
    """
    print(args)

def several_keyword_arguments(**kwargs):
    """
    nimmt eine Vielzah "named parameters" entgegen
    """
    print(kwargs)

if __name__ == "__main__":
    several_arguments(42, "Die Antwort auf das Leben und den ganzen Rest")
    several_keyword_arguments(key1=3234234, key2="Some other value")
