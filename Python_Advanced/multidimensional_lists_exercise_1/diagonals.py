matrix = [[int(num) for num in input().split(', ')] for _ in range(int(input()))]

primary_diagonal = [matrix[idx][idx] for idx in range(len(matrix))]
secondary_diagonal = [matrix[idx][-1 - idx] for idx in range(len(matrix))]

print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}")