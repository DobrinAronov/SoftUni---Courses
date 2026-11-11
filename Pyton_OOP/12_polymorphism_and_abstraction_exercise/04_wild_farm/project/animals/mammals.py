from project.animals.animal import Mammal


class Mouse(Mammal):
    ANIMAL_SOUND = "Squeak"
    ANIMAL_FOOD = ("Vegetable", "Fruit")
    WEIGHT_COEFFICIENT = 0.10

    def make_sound(self) -> str:
        return self.ANIMAL_SOUND


class Dog(Mammal):
    ANIMAL_SOUND = "Woof!"
    ANIMAL_FOOD = ("Meat",)
    WEIGHT_COEFFICIENT = 0.40

    def make_sound(self) -> str:
        return self.ANIMAL_SOUND


class Cat(Mammal):
    ANIMAL_SOUND = "Meow"
    ANIMAL_FOOD = ("Vegetable", "Meat")
    WEIGHT_COEFFICIENT = 0.30

    def make_sound(self) -> str:
        return self.ANIMAL_SOUND


class Tiger(Mammal):
    ANIMAL_SOUND = "ROAR!!!"
    ANIMAL_FOOD = ("Meat",)
    WEIGHT_COEFFICIENT = 1.00

    def make_sound(self) -> str:
        return self.ANIMAL_SOUND
