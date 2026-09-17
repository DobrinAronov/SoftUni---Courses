matriz_size = int(input())

matrix = [[int(num) for num in input().split()] for r in range(matriz_size)]

sum_prime_diagonal = 0
for row in range(matriz_size):
    for col in range(matriz_size):
        if row == col:
            sum_prime_diagonal += matrix[row][col]

print(sum_prime_diagonal)