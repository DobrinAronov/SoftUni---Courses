rows, cols = map(int, input().split())

matrix = [[int(el) for el in input().split()] for _ in range(rows)]

max_sum = -float("inf")
max_submatrix = []

for row in range(rows - 2):
    for col in range(cols - 2):
        submatrix = [sub_row[col:col + 3] for sub_row in matrix[row:row + 3]]
        submatrix_sum = sum(num for s_row in submatrix for num in s_row)
        if submatrix_sum > max_sum:
            max_sum = submatrix_sum
            max_submatrix = submatrix

print(f"Sum = {max_sum}")
[print(*row) for row in max_submatrix]