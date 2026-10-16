SIZE = int(input())
TARGET_FOOD = 10

territory = []

s_row, s_col = 0, 0

burrows = []

for row in range(SIZE):
    territory.append(list(input()))
    for col in range(SIZE):
        if territory[row][col] == "S":
            territory[row][col] = '.'
            s_row, s_col = row, col
        elif territory[row][col] == "B":
            burrows.append((row, col))

ALL_DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

eaten_food = 0
while True:
    command = input()

    new_row = s_row + ALL_DIRECTIONS[command][0]
    new_col = s_col + ALL_DIRECTIONS[command][1]

    if not (0 <= new_row < SIZE and 0 <= new_col < SIZE):
        print("Game over!")
        break

    cell = territory[new_row][new_col]
    s_row, s_col = new_row, new_col

    if cell == "*":
        territory[new_row][new_col] = "."
        eaten_food += 1
        if eaten_food == TARGET_FOOD:
            territory[new_row][new_col] = "S"
            print("You won! You fed the snake.")
            break

    if cell == "B":
        territory[new_row][new_col] = "."
        other_burrow = [pair for pair in burrows if pair != (new_row, new_col)]
        s_row, s_col = other_burrow[0]
        territory[s_row][s_col] = "."

    territory[new_row][new_col] = "."

print(f"Food eaten: {eaten_food}")
[print(*row, sep='') for row in territory]
