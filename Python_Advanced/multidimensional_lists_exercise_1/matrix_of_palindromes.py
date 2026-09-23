rows, cols = map(int, input().split())

matrix = []
base = 97

for row in range(rows):
    matrix_row = []
    for col in range(cols):
        matrix_row.append(chr(base + row) + chr(base + row + col) + chr(base + row))
    matrix.append(matrix_row)

[print(*row) for row in matrix]
