SIZE = int(input())

mines_field = [['.' for _ in range(SIZE)] for _ in range(SIZE)]

for _ in range(int(input())):
    bomb = input().split(', ')
    b_row, b_col = \
        int(bomb[0].lstrip('(')), int(bomb[1].rstrip(')'))

    mines_field[b_row][b_col] = "*"

ALL_DIRECTIONS = {(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)}

for row in range(SIZE):
    for col in range(SIZE):
        if mines_field[row][col] == ".":
            mine_count = 0
            for pair in ALL_DIRECTIONS:
                new_row = row + pair[0]
                new_col = col + pair[1]

                if not (0 <= new_row < SIZE and 0 <= new_col < SIZE):
                    continue

                if mines_field[new_row][new_col] == "*":
                    mine_count += 1

            mines_field[row][col] = mine_count

[print(*row) for row in mines_field]
