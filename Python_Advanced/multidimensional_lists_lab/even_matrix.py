even_matrix = []

for row in range(int(input())):
    current_row = [int(num) for num in input().split(', ') if int(num) % 2 == 0]
    even_matrix.append(current_row)

print(even_matrix)