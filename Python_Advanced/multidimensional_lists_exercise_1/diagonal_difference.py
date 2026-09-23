matrix = [[int(num) for num in input().split()] for _ in range(int(input()))]

primary_diagonal_sum = sum([matrix[idx][idx] for idx in range(len(matrix))])
secondary_diagonal_sum = sum([matrix[idx][-1 - idx] for idx in range(len(matrix))])

print(f"{abs(primary_diagonal_sum - secondary_diagonal_sum)}")
