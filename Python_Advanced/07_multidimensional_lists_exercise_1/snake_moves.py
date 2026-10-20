from collections import deque

rows, cols = map(int, input().split())
text = deque(input())

snake_moves = []

for row in range(1, rows + 1):
    current_row = ''

    for col in range(cols):
        current_row += text[0]
        text.rotate(-1)

    if row % 2 != 0:
        snake_moves.append(current_row)
    else:
        snake_moves.append(reversed(current_row))

for row in snake_moves:
    print(''.join(row))
