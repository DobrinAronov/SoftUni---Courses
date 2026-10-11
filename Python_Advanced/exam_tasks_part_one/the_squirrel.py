SIZE = int(input())
TARGET_HAZELNUTS = 3

commands = input().split(', ')

s_row, s_col = 0, 0

field = []

for row in range(SIZE):
    field.append(list(input()))
    for col in range(SIZE):
        if field[row][col] == "s":
            s_row, s_col = row, col
            field[row][col] = "*"

ALL_DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

hazelnuts = 0

for command in commands:
    s_row += ALL_DIRECTIONS[command][0]
    s_col += ALL_DIRECTIONS[command][1]

    if not (0 <= s_row < SIZE and 0 <= s_col < SIZE):
        print("The squirrel is out of the field.")
        break

    cell = field[s_row][s_col]

    if cell == "h":
        field[s_row][s_col] = "*"
        hazelnuts += 1
        if hazelnuts == TARGET_HAZELNUTS:
            print("Good job! You have collected all hazelnuts!")
            break

    elif cell == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        break

else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")
