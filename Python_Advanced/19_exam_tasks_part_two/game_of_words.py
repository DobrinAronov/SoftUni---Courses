initial_string = input()
SIZE = int(input())

field = []

p_row, p_col = 0, 0

for row in range(SIZE):
    field.append(list(input()))
    for col in range(SIZE):
        if field[row][col] == "P":
            p_row, p_col = row, col
            field[row][col] = "-"

ALL_DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for _ in range(int(input())):
    command = input()

    new_row = p_row + ALL_DIRECTIONS[command][0]
    new_col = p_col + ALL_DIRECTIONS[command][1]

    if not (0 <= new_row < SIZE and 0 <= new_col < SIZE):
        if initial_string:
            initial_string = initial_string[:-1]
        continue

    p_row, p_col = new_row, new_col
    cell = field[new_row][new_col]

    if cell.isalpha():
        initial_string += cell
        field[new_row][new_col] = "-"

print(initial_string)

field[p_row][p_col] = "P"
[print(*row, sep='') for row in field]
