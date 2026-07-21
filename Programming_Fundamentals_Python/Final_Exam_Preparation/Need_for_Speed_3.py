def drive(car_dict: dict, name: str, some_distance: int, some_fuel: int) -> tuple:
    if name in car_dict.keys():
        if car_dict[name]['fuel'] < some_fuel:
            return car_dict, "Not enough fuel to make that ride"
        car_dict[name]['mileage'] += some_distance
        car_dict[name]['fuel'] -= some_fuel

        if car_dict[name]['mileage'] > 100000:
            del car_dict[name]
            return car_dict, (f"{name} driven for {some_distance} kilometers. {some_fuel} liters of fuel consumed."
                              f"\nTime to sell the {name}!")
        return car_dict, f"{name} driven for {some_distance} kilometers. {some_fuel} liters of fuel consumed."
    return car_dict, ''


def refuel(car_dict: dict, name: str, some_fuel: int) -> tuple:
    if name in car_dict.keys():
        refuel_quantity = min(some_fuel, (75 - car_dict[name]['fuel']))
        car_dict[name]['fuel'] += refuel_quantity
        return car_dict, f"{name} refueled with {refuel_quantity} liters"
    return car_dict, ''


def revert(car_dict: dict, name: str, some_kilometers: int) -> tuple:
    if name in car_dict.keys():
        car_dict[name]['mileage'] -= some_kilometers
        if car_dict[name]['mileage'] < 10000:
            car_dict[name]['mileage'] = 10000
            return car_dict, ''
        return car_dict, f"{name} mileage decreased by {some_kilometers} kilometers"
    return car_dict, ''


number_of_cars = int(input())

car_information = {}

for number in range(number_of_cars):
    car_name, mileage, fuel = input().split('|')
    if car_name not in car_information:
        car_information[car_name] = {
            'mileage': int(mileage),
            'fuel': int(fuel)
        }

while (current_command := input()) != "Stop":
    command = current_command.split(' : ')
    action = command[0]
    message = ''

    if action == "Drive":
        car, distance, fuel = command[1], int(command[2]), int(command[3])
        car_information, message = drive(car_information, car, distance, fuel)

    elif action == "Refuel":
        car, fuel = command[1], int(command[2])
        car_information, message = refuel(car_information, car, fuel)

    elif action == "Revert":
        car, kilometers = command[1], int(command[2])
        car_information, message = revert(car_information, car, kilometers)

    if message:
        print(message)

for car, info in car_information.items():
    print(f"{car} -> Mileage: {info['mileage']} kms, Fuel in the tank: {info['fuel']} lt.")
