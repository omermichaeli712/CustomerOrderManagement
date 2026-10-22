
from bonus.Animal import Animal
from bonus.Pet import Pet
from bonus.Spider import Spider
from bonus.Cat import Cat
from bonus.Fish import Fish


def main():
    spider = Spider()
    cat = Cat("Milo")
    fish = Fish()
    fish.setName("Nemo")

    animals = [spider, cat, fish]

    for animal in animals:
        animal.walk()
        animal.eat()

    pets = [cat, fish]

    for pet in pets:
        print("Pet name:", pet.getName())
        pet.play()


if __name__ == "__main__":
    main()
