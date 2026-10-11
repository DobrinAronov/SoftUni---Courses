ROWS, COLUMNS = [int(num) for num in input().split()]

b_initial_row, b_initial_col = 0, 0

neighborhood = []

for row in range(ROWS):
    neighborhood.append(list(input()))
    for col in range(COLUMNS):
        if neighborhood[row][col] == "B":
            b_initial_row, b_initial_col = row, col

ALL_DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

b_row, b_col = b_initial_row, b_initial_col
while True:
    command = input()

    new_row = b_row + ALL_DIRECTIONS[command][0]
    new_col = b_col + ALL_DIRECTIONS[command][1]

    if not (0 <= new_row < ROWS and 0 <= new_col < COLUMNS):
        neighborhood[b_initial_row][b_initial_col] = ' '
        print("The delivery is late. Order is canceled.")
        break

    cell = neighborhood[new_row][new_col]

    if cell == "*":
        continue

    b_row, b_col = new_row, new_col

    if cell == "A":
        neighborhood[new_row][new_col] = "P"
        print("Pizza is delivered on time! Next order...")
        break

    elif cell == "P":
        neighborhood[new_row][new_col] = "R"
        print("Pizza is collected. 10 minutes for delivery.")

    elif cell == "-":
        neighborhood[new_row][new_col] = "."

[print(*row, sep='') for row in neighborhood]
