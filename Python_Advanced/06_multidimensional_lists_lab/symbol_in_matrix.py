n = int(input())

matrix = [list(input()) for row in range(n)]
searching_symbol = input()

for row in range(n):
    for col in range(n):
        if matrix[row][col] == searching_symbol:
            is_found = True
            print(f"({row}, {col})")
            exit()

print(f"{searching_symbol} does not occur in the matrix")