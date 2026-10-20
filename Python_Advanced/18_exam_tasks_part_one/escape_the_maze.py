SIZE = int(input())
traveller_health = 100
MONSTER_DAMAGE = 40
RESTORE_HEALTH = 15

p_row, p_col = 0, 0

maze = []

for row in range(SIZE):
    maze.append(list(input()))
    for col in range(SIZE):
        if maze[row][col] == "P":
            p_row, p_col = row, col
            maze[row][col] = "-"

ALL_DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input()

    new_row = p_row + ALL_DIRECTIONS[command][0]
    new_col = p_col + ALL_DIRECTIONS[command][1]

    if not (0 <= new_row < SIZE and 0 <= new_col < SIZE):
        continue

    p_row, p_col = new_row, new_col
    cell = maze[new_row][new_col]

    if cell == "X" and traveller_health > 0:
        print("Player escaped the maze. Danger passed!")
        break

    elif cell == "M":
        traveller_health -= MONSTER_DAMAGE
        if traveller_health <= 0:
            traveller_health = 0
            print("Player is dead. Maze over!")
            break

    elif cell == "H":
        traveller_health += min(RESTORE_HEALTH, 100 - traveller_health)

    maze[new_row][new_col] = "-"

print(f"Player's health: {traveller_health} units")

maze[p_row][p_col] = "P"
[print(*row, sep='') for row in maze]
