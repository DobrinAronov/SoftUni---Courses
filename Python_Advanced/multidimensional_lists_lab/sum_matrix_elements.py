rows, cols = [int(x) for x in input().split(', ')]
matrix = []

total_sum = 0
for r in range(rows):
    current_row = [int(num) for num in input().split(', ')]
    total_sum += sum(current_row)
    matrix.append(current_row)

print(total_sum)
print(matrix)