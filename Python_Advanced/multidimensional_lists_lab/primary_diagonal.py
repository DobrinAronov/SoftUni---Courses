matriz_size = int(input())

matrix = [[int(num) for num in input().split()] for r in range(matriz_size)]

sum_prime_diagonal = 0
for idx in range(matriz_size):
    sum_prime_diagonal += matrix[idx][idx]

print(sum_prime_diagonal)