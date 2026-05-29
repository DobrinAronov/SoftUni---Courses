list_of_integer = list(map(int, input().split()))
count_of_numbers_to_remove = int(input())

for number in range(count_of_numbers_to_remove):
    min_number = min(list_of_integer)
    list_of_integer.remove(min_number)

result = map(str, list_of_integer)
print(', '.join(result))
