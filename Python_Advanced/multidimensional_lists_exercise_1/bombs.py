mine_field = [[int(el) for el in input().split()] for _ in range(int(input()))]

mines = input().split()

all_directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

for mine in mines:
    r, c = map(int, mine.split(','))
    bomb_value = mine_field[r][c]

    if bomb_value <= 0:
        continue

    mine_field[r][c] -= bomb_value

    for direction in all_directions:
        dr, dc = direction
        new_row = r + dr
        new_col = c + dc

        if 0 <= new_row < len(mine_field) and 0 <= new_col < len(mine_field):
            if mine_field[new_row][new_col] > 0:
                mine_field[new_row][new_col] -= bomb_value

alive_cells = [el for row in mine_field for el in row if el > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

[print(*row) for row in mine_field]
