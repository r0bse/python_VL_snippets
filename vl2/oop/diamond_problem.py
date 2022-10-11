from abc import ABC, abstractmethod

class Alien(ABC):

    @abstractmethod
    def fly(self):
        pass

class Human():

    def __init__(self, name: str):
        self.name = name

    def walk(self):
        print("walking")

class SuperHuman(Human, Alien):

    def __init__(self, name: str):
        super().__init__(name)

    def fly(self):
        print("flying")

if __name__ == "__main__":
    superboy = SuperHuman("superboy")
    superboy.walk()
    superboy.fly()