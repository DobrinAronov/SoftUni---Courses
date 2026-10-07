SIZE = int(input())

field = []

b_row, b_col = 0, 0

for row in range(SIZE):
    current_row = list(input())
    for col in range(SIZE):
        if current_row[col] == "B":
            current_row[col] = '-'
            b_row, b_col = row, col
    field.append(current_row)

ALL_DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

bee_energy = 15
NECTAR_FOR_HONEY = 30

current_nectar = 0
restored_energy = 0

while True:
    command = input()

    bee_energy -= 1

    new_row = (b_row + ALL_DIRECTIONS[command][0]) % SIZE
    new_col = (b_col + ALL_DIRECTIONS[command][1]) % SIZE

    b_row, b_col = new_row, new_col

    cell = field[new_row][new_col]

    if cell == "H":
        if current_nectar >= NECTAR_FOR_HONEY:
            field[new_row][new_col] = '-'
            print(f"Great job, Beesy! The hive is full. Energy left: {bee_energy}")
            break
        else:
            print("Beesy did not manage to collect enough nectar.")
            break

    elif field[new_row][new_col].isdigit():
        current_nectar += int(field[new_row][new_col])
        field[new_row][new_col] = '-'

    if bee_energy == 0:
        if current_nectar > NECTAR_FOR_HONEY and restored_energy == 0:
            add_nectar = current_nectar - NECTAR_FOR_HONEY
            bee_energy += add_nectar
            current_nectar -= add_nectar
            restored_energy += 1
        else:
            print("This is the end! Beesy ran out of energy.")
            break

field[b_row][b_col] = 'B'

[print(*row, sep='') for row in field]
