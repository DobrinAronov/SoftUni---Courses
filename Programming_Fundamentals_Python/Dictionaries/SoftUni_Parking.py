def register(base: dict, user: str, car_number: str) -> tuple[str, dict]:
    if user in base:
        return f"ERROR: already registered with plate number {car_number}", base
    base[user] = car_number
    return f"{user} registered {car_number} successfully", base


def unregister(base: dict, user: str) -> tuple[str, dict]:
    if user not in base:
        return f"ERROR: user {user} not found", base
    del base[user]
    return f"{user} unregistered successfully", base


database = {}

number_of_commands = int(input())

for number in range(number_of_commands):
    current_list = input().split()
    command = current_list[0]
    message = ''

    if command == 'register':
        name, license_plate_number = current_list[1], current_list[2]
        message, database = register(database, name, license_plate_number)

    elif command == 'unregister':
        name = current_list[1]
        message, database = unregister(database, name)

    print(message)

for user_name, license_plate_number in database.items():
    print(f"{user_name} => {license_plate_number}")
