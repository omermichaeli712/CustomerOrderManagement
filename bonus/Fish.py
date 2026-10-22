
from bonus.Animal import Animal
from bonus.Pet import Pet


class Fish(Animal, Pet):

    def __init__(self):
        super().__init__(0)
        self.name = ""

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def play(self):
        print(f"{self.name} is playing in the water")

    def walk(self):
        print("Fish cannot walk")

    def eat(self):
        print(f"{self.name} eats fish food")
