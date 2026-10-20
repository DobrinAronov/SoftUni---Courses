rows, cols = map(int, input().split())

lair = []

p_row, p_col = 0, 0

bunnies = []

for row in range(rows):
    lair.append(list(input()))
    for col in range(cols):
        if lair[row][col] == "P":
            lair[row][col] = "."
            p_row, p_col = row, col
        elif lair[row][col] == "B":
            bunnies.append((row, col))

all_directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

commands = input()

escape = False
dead = False

for command in commands:
    new_row = p_row + all_directions[command][0]
    new_col = p_col + all_directions[command][1]

    if not (0 <= new_row < rows and 0 <= new_col < cols):
        lair[p_row][p_col] = '.'
        escape = True

    elif lair[new_row][new_col] == "B":
        dead = True
        p_row, p_col = new_row, new_col

    elif lair[new_row][new_col] == ".":
        lair[p_row][p_col] = "."
        lair[new_row][new_col] = "P"
        p_row, p_col = new_row, new_col

    new_bunnies = []

    for bunny in bunnies:
        b_row, b_col = bunny
        for direction in all_directions.values():
            new_b_r = b_row + direction[0]
            new_b_c = b_col + direction[1]
            if not (0 <= new_b_r < rows and 0 <= new_b_c < cols):
                continue
            if lair[new_b_r][new_b_c] == "P":
                dead = True
            lair[new_b_r][new_b_c] = "B"
            new_bunnies.append((new_b_r, new_b_c))
    bunnies = new_bunnies

    if escape or dead:
        break

[print(*row, sep='') for row in lair]

print(f"won: {p_row} {p_col}") if escape else None
print(f"dead: {p_row} {p_col}") if dead else None
