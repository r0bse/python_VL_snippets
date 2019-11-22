
class Stringify:

    name = ""

    def __init__(self, value):
        self.name = value

    def __str__(self):
        return "name: {0}".format(self.name)

if __name__ == "__main__":
    print(str(Stringify("foo")))
    print(Stringify("bar"))


