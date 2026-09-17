matriz_size = int(input())

matrix = [[int(num) for num in input().split()] for r in range(matriz_size)]

sum_secondary_diagonal = 0
for row in range(matriz_size):
    sum_secondary_diagonal += matrix[row][matriz_size - 1 - row]

print(sum_secondary_diagonal)