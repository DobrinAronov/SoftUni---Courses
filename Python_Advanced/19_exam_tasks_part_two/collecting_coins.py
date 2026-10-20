from math import floor

SIZE = int(input())
TARGET_COINS = 100

field = []

player_path = []
p_row, p_col = 0, 0

for row in range(SIZE):
    field.append(input().split())
    for col in range(SIZE):
        if field[row][col] == "P":
            p_row, p_col = row, col
            player_path.append([p_row, p_col])

ALL_DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

total_coins = 0
while True:
    command = input()
    if command not in ALL_DIRECTIONS:
        continue

    p_row = (p_row + ALL_DIRECTIONS[command][0]) % SIZE
    p_col = (p_col + ALL_DIRECTIONS[command][1]) % SIZE

    cell = field[p_row][p_col]
    player_path.append([p_row, p_col])

    if cell == "X":
        total_coins = floor(total_coins / 2)
        print(f"Game over! You've collected {total_coins} coins.")
        break

    if cell.isdigit():
        total_coins += int(cell)
        field[p_row][p_col] = "."
        if total_coins >= TARGET_COINS:
            print(f"You won! You've collected {total_coins} coins.")
            break

print("Your path:")
for path in player_path:
    print(path)
