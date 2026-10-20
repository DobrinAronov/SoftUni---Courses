number_of_present = int(input())

matrix_size = int(input())

neighborhood = []

s_row, s_col = 0, 0
nice_kids = 0

for row in range(matrix_size):
    neighborhood.append(input().split())
    for col in range(matrix_size):
        if neighborhood[row][col] == "S":
            s_row, s_col = row, col
            neighborhood[row][col] = "-"
        elif neighborhood[row][col] == "V":
            nice_kids += 1

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

nice_happy_kids = 0

while (command := input()) != "Christmas morning":
    next_row = s_row + directions[command][0]
    next_col = s_col + directions[command][1]

    if not (0 <= next_row < matrix_size and 0 <= next_col < matrix_size):
        break

    s_row, s_col = next_row, next_col
    cell = neighborhood[next_row][next_col]

    if cell == "V":
        number_of_present -= 1
        nice_happy_kids += 1

    elif cell == "C":

        for move, (dr, dc) in directions.items():
            neighbor_row = s_row + dr
            neighbor_col = s_col + dc

            if not (0 <= neighbor_row < matrix_size and 0 <= neighbor_col < matrix_size):
                continue

            neighbor = neighborhood[neighbor_row][neighbor_col]

            if neighbor == "V":
                number_of_present -= 1
                nice_happy_kids += 1

            elif neighbor == "X":
                number_of_present -= 1

            neighborhood[neighbor_row][neighbor_col] = "-"

            if number_of_present == 0:
                break

    neighborhood[next_row][next_col] = "-"

    if number_of_present == 0:
        break

if number_of_present == 0 and nice_happy_kids < nice_kids:
    print("Santa ran out of presents!")

neighborhood[s_row][s_col] = "S"

[print(*row) for row in neighborhood]

if nice_happy_kids == nice_kids:
    print(f"Good job, Santa! {nice_happy_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - nice_happy_kids} nice kid/s.")
