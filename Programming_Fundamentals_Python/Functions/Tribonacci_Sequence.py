def tribonacci_sequence(first_num: int, second_num: int, tird_num: int) -> int:
    if first_num == 0 and second_num == 0:
        return 1
    return first_num + second_num + tird_num


def print_tribonacci_numbers(lst: list) -> str:
    list_str = [str(element) for element in lst]
    return f"{' '.join(list_str)}"


number = int(input())

tribonacci_list = []

first_number = 0
second_number = 0
tird_number = 0

for num in range(number):
    result = tribonacci_sequence(first_number, second_number, tird_number)
    tribonacci_list.append(result)
    first_number = second_number
    second_number = tird_number
    tird_number = result

print(print_tribonacci_numbers(tribonacci_list))
