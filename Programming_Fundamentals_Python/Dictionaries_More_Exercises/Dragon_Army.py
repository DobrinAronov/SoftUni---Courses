def calculate_average(matrix: list[list], idx: int) -> float:
    total_sum = 0
    number_of_elements = len(matrix)

    for row in matrix:
        total_sum += row[idx]

    average = total_sum / number_of_elements
    return average


default_values = {
    'damage': 45,
    'health': 250,
    'armor': 10
}

dragons = {}

numbers_of_dragons = int(input())

for num in range(numbers_of_dragons):
    dragon_type, name, damage, health, armor = input().split()

    damage = default_values['damage'] if damage == 'null' else int(damage)
    health = default_values['health'] if health == 'null' else int(health)
    armor = default_values['armor'] if armor == 'null' else int(armor)

    if dragon_type not in dragons:
        dragons[dragon_type] = {}

    dragons[dragon_type][name] = [damage, health, armor]

for key, inner_dict in dragons.items():
    average_damage = calculate_average(inner_dict.values(), 0)
    average_health = calculate_average(inner_dict.values(), 1)
    average_armor = calculate_average(inner_dict.values(), 2)

    print(f"{key}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")

    for inner_key, inner_data in sorted(inner_dict.items(), key=lambda x: x[0]):
        print(f"-{inner_key} -> damage: {inner_data[0]}, health: {inner_data[1]}, armor: {inner_data[2]}")
