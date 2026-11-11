from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance) -> None:
        pass

    @abstractmethod
    def refuel(self, fuel) -> None:
        pass


class Car(Vehicle):
    AC_CONSUMPTION = 0.9

    def drive(self, distance: float) -> None:
        if distance > 0:
            needed_fuel = distance * (self.fuel_consumption + self.AC_CONSUMPTION)
            if needed_fuel <= self.fuel_quantity:
                self.fuel_quantity -= needed_fuel

    def refuel(self, fuel: float) -> None:
        if fuel > 0:
            self.fuel_quantity += fuel


class Truck(Vehicle):
    AC_CONSUMPTION = 1.6
    ACTUAL_REFUEL = 0.95

    def drive(self, distance: float) -> None:
        if distance > 0:
            needed_fuel = distance * (self.fuel_consumption + self.AC_CONSUMPTION)
            if needed_fuel <= self.fuel_quantity:
                self.fuel_quantity -= needed_fuel

    def refuel(self, fuel: float) -> None:
        if fuel > 0:
            self.fuel_quantity += fuel * self.ACTUAL_REFUEL


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
