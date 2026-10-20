row, col = [int(n) for n in input().split(', ')]

matrix = [[int(num) for num in input().split(', ')] for _ in range(row)]

biggest_sum = float("-inf")
max_matrix = []

for r in range(row - 1):
    for c in range(col - 1):
        element = matrix[r][c]
        next_to = matrix[r][c + 1]
        below = matrix[r + 1][c]
        diagonal = matrix[r + 1][c + 1]

        current_matrix = [[element, next_to], [below, diagonal]]
        current_sum = sum(sum(row) for row in current_matrix)

        if current_sum > biggest_sum:
            biggest_sum = current_sum
            max_matrix = current_matrix

for row in max_matrix:
    print(*row)

print(biggest_sum)