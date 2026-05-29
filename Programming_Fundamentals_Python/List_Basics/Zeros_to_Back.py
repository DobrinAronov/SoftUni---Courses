integers = list(map(int, input().split(', ')))
integer_numbers = []
zero_list = []

for idx in range(len(integers)):
    if integers[idx] == 0:
        zero_list.append(0)
    else:
        integer_numbers.append(integers[idx])

integer_numbers += zero_list
print(integer_numbers)
