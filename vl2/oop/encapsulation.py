
class Encapsulation:

    def __init__(self, a, b, c):
        self.public = a
        self._protected = b
        self.__private = c


e = Encapsulation("public", "protected", "private")

print(e.public)
print(e._protected)
print(e.__private)


