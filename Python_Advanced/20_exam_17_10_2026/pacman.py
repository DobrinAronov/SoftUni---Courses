SIZE = int(input())
health = 100

field = []

p_row, p_col = 0, 0
all_stars = 0

for row in range(SIZE):
    field.append(list(input()))
    for col in range(SIZE):
        if field[row][col] == 'P':
            p_row, p_col = row, col
            field[row][col] = '-'
        elif field[row][col] == '*':
            all_stars += 1

ALL_DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

hit_ghost = 0
is_freeze = False
while True:
    command = input()

    if command == "end":
        break

    p_row = (p_row + ALL_DIRECTIONS[command][0]) % SIZE
    p_col = (p_col + ALL_DIRECTIONS[command][1]) % SIZE

    cell = field[p_row][p_col]

    if cell == 'G':
        if is_freeze:
            is_freeze = False
            field[p_row][p_col] = '-'
            continue
        else:
            hit_ghost += 1
            if hit_ghost == 2:
                health = 0
            else:
                health -= 50
            if health <= 0:
                print(f"Game over! Pacman last coordinates [{p_row},{p_col}]")
                break

    if cell == '*':
        all_stars -= 1
        if all_stars == 0:
            print("Pacman wins! All the stars are collected.")
            break

    if cell == 'F':
        is_freeze = True

    field[p_row][p_col] = '-'

if health > 0 and all_stars > 0:
    print(f"Pacman failed to collect all the stars.")

print(f"Health: {health}")

if all_stars > 0:
    print(f"Uncollected stars: {all_stars}")

field[p_row][p_col] = 'P'
[print(*row, sep='') for row in field]
