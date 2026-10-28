from project.car import Car
from project.sports_car import SportsCar
from project.vehicle import Vehicle

car = Vehicle()
volvo = Car()
porshe = SportsCar()
print(car.move())
print(volvo.drive())
print(volvo.drive())
print(porshe.move())
print(porshe.drive())
print(porshe.race())
