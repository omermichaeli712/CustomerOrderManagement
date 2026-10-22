
from bonus.Animal import Animal
from bonus.Pet import Pet


class Cat(Animal, Pet):

    def __init__(self, name=""):
        super().__init__(4)
        self.name = name

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def play(self):
        print(f"{self.name} is playing")

    def eat(self):
        print(f"{self.name} eats cat food")
