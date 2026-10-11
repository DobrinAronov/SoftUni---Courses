SIZE = int(input())

s_row, s_col = 0, 0

fishing_area = []

for row in range(SIZE):
    fishing_area.append(list(input()))
    for col in range(SIZE):
        if fishing_area[row][col] == "S":
            fishing_area[row][col] = "-"
            s_row, s_col = row, col

ALL_DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

FISHING_QUOTA = 20
catch = 0

while (command := input()) != "collect the nets":

    s_row = (s_row + ALL_DIRECTIONS[command][0]) % SIZE
    s_col = (s_col + ALL_DIRECTIONS[command][1]) % SIZE

    cell = fishing_area[s_row][s_col]

    if cell == "W":
        catch = 0
        print(f"You fell into a whirlpool!"
              f" The ship sank and you lost the fish you caught."
              f" Last coordinates of the ship: [{s_row},{s_col}]")
        exit()

    if cell.isdigit():
        catch += int(cell)
        fishing_area[s_row][s_col] = '-'

if catch >= FISHING_QUOTA:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota!"
          f" You need {FISHING_QUOTA - catch} tons of fish more.")
if catch > 0:
    print(f"Amount of fish caught: {catch} tons.")

fishing_area[s_row][s_col] = "S"
[print(*row, sep='') for row in fishing_area]
