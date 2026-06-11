def battle_ships(field: list[list], attacks: list[list]) -> int:
    count_destroyed_ships = 0

    for pair in attacks:
        row, col = pair
        if field[row][col] > 0:
            field[row][col] -= 1
            if field[row][col] == 0:
                count_destroyed_ships += 1

    return count_destroyed_ships


number_of_rows = int(input())

field_of_ships = []

for number in range(number_of_rows):
    row_of_ships = [int(ship_health) for ship_health in input().split()]
    field_of_ships.append(row_of_ships)

square = input().split()
square_attacks = []

for pair_attack in square:
    some_row, some_col = [int(element) for element in pair_attack.split('-')]
    square_attacks.append([some_row, some_col])

result = battle_ships(field_of_ships, square_attacks)
print(result)
