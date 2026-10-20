ROWS, COLUMNS = [int(num) for num in input().split()]
OPPONENT_COUNT = 3

b_row, b_col = 0, 0

playground = []

for row in range(ROWS):
    playground.append(input().split())
    for col in range(COLUMNS):
        if playground[row][col] == "B":
            b_row, b_col = row, col
            playground[row][col] = "-"

ALL_DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

moves_count = 0
touched_opponent = 0

while (command := input()) != "Finish":

    new_row = b_row + ALL_DIRECTIONS[command][0]
    new_col = b_col + ALL_DIRECTIONS[command][1]

    if not (0 <= new_row < ROWS and 0 <= new_col < COLUMNS):
        continue

    if playground[new_row][new_col] == "O":
        continue

    moves_count += 1
    b_row, b_col = new_row, new_col

    cell = playground[new_row][new_col]

    if cell == "P":
        playground[new_row][new_col] = "-"
        touched_opponent += 1
        if touched_opponent == OPPONENT_COUNT:
            break

print("Game over!")
print(f"Touched opponents: {touched_opponent} Moves made: {moves_count}")
