class Singleton(object):

    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


class AnySingletonObject(Singleton):
    """
    A class for a Singleton Object.
    """

    # class methods and attributes ...

if __name__ == "__main__":
    print(AnySingletonObject())
    print(AnySingletonObject())
