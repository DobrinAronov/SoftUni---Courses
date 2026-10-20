SIZE = 6

field = []

r_row, r_col = 0, 0

for row in range(SIZE):
    field.append(input().split())
    for col in range(SIZE):
        if field[row][col] == "E":
            r_row, r_col = row, col
            field[row][col] = '-'

ALL_DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

RESOURCES = {
    "W": "Water",
    "M": "Metal",
    "C": "Concrete",
}

collected_resources = {"W": 0, "M": 0, "C": 0}

for command in input().split(', '):
    r_row = (r_row + ALL_DIRECTIONS[command][0]) % SIZE
    r_col = (r_col + ALL_DIRECTIONS[command][1]) % SIZE

    cell = field[r_row][r_col]

    if cell == "R":
        print(f"Rover got broken at ({r_row}, {r_col})")
        break

    if cell in RESOURCES:
        collected_resources[cell] += 1
        print(f"{RESOURCES[cell]} deposit found at ({r_row}, {r_col})")

if all([resource > 0 for resource in collected_resources.values()]):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
