row, col = [int(n) for n in input().split(', ')]

matrix = [[int(num) for num in input().split()]for r in range(row)]

for c in range(col):
    sum_column = 0
    for r in range(row):
        sum_column += matrix[r][c]
    print(sum_column)