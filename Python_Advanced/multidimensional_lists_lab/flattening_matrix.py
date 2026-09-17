matrix = []

for row in range(int(input())):
    current_row = [int(num) for num in input().split(', ')]
    matrix.append(current_row)

flattened_matrix = [num for row in matrix for num in row]
print(flattened_matrix)