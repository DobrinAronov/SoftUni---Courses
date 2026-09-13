n, m = [int(num) for num in input().split()]

first_set = set()
second_set = set()

for index in range(n + m):
    number = int(input())
    if 0 <= index < n:
        first_set.add(number)
    else:
        second_set.add(number)

result = first_set.intersection(second_set)
print(*result, sep='\n')