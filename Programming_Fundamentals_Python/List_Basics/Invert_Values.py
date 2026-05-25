single_string = list(map(int, input().split()))

opposite_list = []

for number in single_string:
    opposite_list.append(number * (-1))

print(opposite_list)