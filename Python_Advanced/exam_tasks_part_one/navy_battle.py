SIZE = int(input())

s_row, s_col = 0, 0

battlefield = []

for row in range(SIZE):
    battlefield.append(list(input()))
    for col in range(SIZE):
        if battlefield[row][col] == "S":
            battlefield[row][col] = "-"
            s_row, s_col = row, col

ALL_DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

blow_mines = 3
battle_cruisers = 3

while True:
    command = input()

    s_row += ALL_DIRECTIONS[command][0]
    s_col += ALL_DIRECTIONS[command][1]

    cell = battlefield[s_row][s_col]

    if cell == "*":
        battlefield[s_row][s_col] = "-"
        blow_mines -= 1
        if blow_mines == 0:
            print(f"Mission failed, U-9 disappeared!"
                  f" Last known coordinates [{s_row}, {s_col}]!")
            break
    elif cell == "C":
        battlefield[s_row][s_col] = "-"
        battle_cruisers -= 1
        if battle_cruisers == 0:
            print("Mission accomplished,"
                  " U-9 has destroyed all battle cruisers of the enemy!")
            break

battlefield[s_row][s_col] = "S"
[print(*row, sep='') for row in battlefield]
