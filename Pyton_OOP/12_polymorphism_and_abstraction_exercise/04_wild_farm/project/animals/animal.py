from abc import ABC, abstractmethod

from project.food import Food


class Animal(ABC):
    ANIMAL_FOOD = ()
    WEIGHT_COEFFICIENT = 0.00

    def __init__(self, name: str, weight: float, food_eaten=0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @abstractmethod
    def make_sound(self) -> str:
        pass

    def feed(self, food: Food) -> str | None:
        if food.__class__.__name__ not in self.ANIMAL_FOOD:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * self.WEIGHT_COEFFICIENT
        self.food_eaten += food.quantity
        return None


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__} [{self.name},"
                f" {self.wing_size}, {self.weight}, {self.food_eaten}]")


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__} [{self.name},"
                f" {self.weight}, {self.living_region}, {self.food_eaten}]")
