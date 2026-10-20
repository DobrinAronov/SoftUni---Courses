ROWS, COLS = [int(num) for num in input().split(', ')]
DEFUSE_TIME = 4

time_to_explosion = 16

map_layout = []

c_row, c_col = 0, 0

for row in range(ROWS):
    current_row = list(input())
    for col in range(COLS):
        if current_row[col] == "C":
            c_row, c_col = row, col
    map_layout.append(current_row)

ALL_DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

is_lost = False
while True:
    command = input()

    if command == "defuse":
        if map_layout[c_row][c_col] == "B":
            time_to_explosion -= DEFUSE_TIME
            if time_to_explosion >= 0:
                map_layout[c_row][c_col] = "D"
                print("Counter-terrorist wins!")
                print(f"Bomb has been defused: {time_to_explosion}"
                      f" second/s remaining.")
                break
            else:
                map_layout[c_row][c_col] = "X"
                is_lost = True
                break
        else:
            time_to_explosion -= 2
            if time_to_explosion <= 0:
                is_lost = True
                break
            else:
                continue

    if time_to_explosion > 0:
        time_to_explosion -= 1

        new_row = c_row + ALL_DIRECTIONS[command][0]
        new_col = c_col + ALL_DIRECTIONS[command][1]

        if not (0 <= new_row < ROWS and 0 <= new_col < COLS):
            continue

        c_row, c_col = new_row, new_col
        cell = map_layout[new_row][new_col]

        if cell == "T":
            map_layout[new_row][new_col] = "*"
            print("Terrorists win!")
            break
    else:
        is_lost = True
        break

if is_lost:
    print("Terrorists win!")
    print("Bomb was not defused successfully!")
    print(f"Time needed: {abs(time_to_explosion)} second/s.")

[print(*row, sep='') for row in map_layout]
