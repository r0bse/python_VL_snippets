class Dto:
    def __init__(self, value: str):
        self.string = value

    def __repr__(self):
        return "Dto({0})".format(self.string)


