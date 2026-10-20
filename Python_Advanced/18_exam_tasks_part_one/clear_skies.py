SIZE = int(input())
initial_armor = 300


airspace = []

j_row, j_col = 0, 0
num_of_enemies = 4

for row in range(SIZE):
    airspace.append(list(input()))
    for col in range(SIZE):
        if airspace[row][col] == "J":
            j_row, j_col = row, col
            airspace[row][col] = "-"


ALL_DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input()

    j_row += ALL_DIRECTIONS[command][0]
    j_col += ALL_DIRECTIONS[command][1]

    cell = airspace[j_row][j_col]

    if cell == "E":
        num_of_enemies -= 1
        if num_of_enemies == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            break
        else:
            initial_armor -= 100
            if initial_armor == 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{j_row}, {j_col}]!")
                break

    elif cell == "R":
        initial_armor = 300

    airspace[j_row][j_col] = "-"

airspace[j_row][j_col] = "J"

[print(*row, sep='') for row in airspace]