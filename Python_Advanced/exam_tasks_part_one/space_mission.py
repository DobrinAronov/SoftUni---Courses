SIZE = int(input())
RESOURCES = 100

space = []

s_row, s_col = 0, 0

for row in range(SIZE):
    space.append(input().split())
    for col in range(SIZE):
        if space[row][col] == "S":
            space[row][col] = "."
            s_row, s_col = row, col

ALL_DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

is_won = False
while True:
    command = input()

    RESOURCES -= 5

    new_row = s_row + ALL_DIRECTIONS[command][0]
    new_col = s_col + ALL_DIRECTIONS[command][1]

    if not (0 <= new_row < SIZE and 0 <= new_col < SIZE):
        print("Mission failed! The spaceship was lost in space.")
        break

    s_row, s_col = new_row, new_col

    cell = space[new_row][new_col]

    if cell == "P":
        is_won = True
        print(f"Mission accomplished! The spaceship reached "
              f"Planet B with {RESOURCES} resources left.")
        break

    if cell == "M":
        RESOURCES -= 5
        space[s_row][s_col] = "."

    elif cell == "R":
        add_resources = min(10, 100 - RESOURCES)
        RESOURCES += add_resources

    if RESOURCES < 5:
        print("Mission failed! The spaceship was stranded in space.")
        break

if not is_won:
    space[s_row][s_col] = "S"

for row in space:
    print(*row)
