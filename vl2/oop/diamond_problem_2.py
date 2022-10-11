from abc import ABC, abstractmethod

class CrabPeople(ABC):

    def __init__(self, name):
        self.name = name
        self.race = "CrabPeople"

class Bird(ABC):

    def __init__(self, name):
        self.name = name
        self.race = "Bird"

    @abstractmethod
    def fly(self):
        pass

class Alien(CrabPeople, Bird):

    def __init__(self, name):
        super().__init__(name)
        self.race = "Alien"

    @abstractmethod
    def fly(self):
        pass

class Human(CrabPeople):

    def __init__(self, name: str):
        super().__init__(name)
        self.name = name
        self.race = "Human"

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

    print("superboy is of instance \"CrabPeople\": {0}".format(isinstance(superboy, CrabPeople)))
    print("superboy is of instance \"Bird\": {0}".format(isinstance(superboy, Bird)))
    print("superboy is of instance \"Human\": {0}".format(isinstance(superboy, Human)))
    print("superboy is of instance \"Alien\": {0}".format(isinstance(superboy, Alien)))
    print("superboy is of instance \"SuperHuman\": {0}".format(isinstance(superboy, SuperHuman)))
    print(superboy.race)