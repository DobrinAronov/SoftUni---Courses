SIZE = int(input())

TARGET_STARS = 10
initial_stars = 2

field = []

p_row, p_col = 0, 0

for row in range(SIZE):
    field.append(input().split())
    for col in range(SIZE):
        if field[row][col] == "P":
            p_row, p_col = row, col
            field[row][col] = '.'

ALL_DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input()
    new_row = p_row + ALL_DIRECTIONS[command][0]
    new_col = p_col + ALL_DIRECTIONS[command][1]

    if not (0 <= new_row < SIZE and 0 <= new_col < SIZE):
        new_row, new_col = 0, 0

    cell = field[new_row][new_col]

    if cell == '#':
        initial_stars -= 1
        if initial_stars == 0:
            print("Game over! You are out of any stars.")
            break

    elif cell == '*':
        field[new_row][new_col] = '.'
        initial_stars += 1
        p_row, p_col = new_row, new_col
        if initial_stars == TARGET_STARS:
            print("You won! You have collected 10 stars.")
            break

    else:
        p_row, p_col = new_row, new_col

print(f"Your final position is [{p_row}, {p_col}]")
field[p_row][p_col] = 'P'

[print(*row) for row in field]
