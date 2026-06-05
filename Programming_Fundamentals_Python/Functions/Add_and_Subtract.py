def sum_numbers(num_1: int, num_2: int) ->int:
    return num_1 + num_2


def subtract(received_sum: int, num_3: int) -> int:
    return received_sum - num_3


def add_and_subtract(number_1: int, number_2: int, number_3: int) -> int:
    returned_result = sum_numbers(number_1, number_2)
    return subtract(returned_result, number_3)


first_number = int(input())
second_number = int(input())
tird_number = int(input())

print(add_and_subtract(first_number, second_number, tird_number))