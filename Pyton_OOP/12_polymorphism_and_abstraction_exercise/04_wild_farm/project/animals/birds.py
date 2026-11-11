from project.animals.animal import Bird


class Owl(Bird):
    ANIMAL_SOUND = "Hoot Hoot"
    ANIMAL_FOOD = ("Meat",)
    WEIGHT_COEFFICIENT = 0.25

    def make_sound(self) -> str:
        return self.ANIMAL_SOUND


class Hen(Bird):
    ANIMAL_SOUND = "Cluck"
    ANIMAL_FOOD = ("Vegetable", "Fruit", "Seed", "Meat")
    WEIGHT_COEFFICIENT = 0.35

    def make_sound(self) -> str:
        return self.ANIMAL_SOUND