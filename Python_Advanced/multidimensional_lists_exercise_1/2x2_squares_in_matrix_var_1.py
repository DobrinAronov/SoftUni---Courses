rows, cols = [int(el) for el in input().split()]

matrix = [input().split() for _ in range(rows)]

num_of_submatrix = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        submatrix = []

        for r in range(row, row + 2):
            submatrix.append(matrix[r][col: col + 2])

        flatten_submatrix = [el for sub_row in submatrix for el in sub_row]
        if all([el == flatten_submatrix[0] for el in flatten_submatrix]):
            num_of_submatrix += 1

print(num_of_submatrix)