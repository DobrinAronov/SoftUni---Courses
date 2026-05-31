def min_max_sum(lst: list)->tuple:
    min_num = min(lst)
    max_num = max(lst)
    sum_num = sum(lst)
    return min_num, max_num, sum_num


input_list = [int(element) for element in input().split()]

min_number, max_number, sum_number = min_max_sum(input_list)

print(f"The minimum number is {min_number}")
print(f"The maximum number is {max_number}")
print(f"The sum number is: {sum_number}")