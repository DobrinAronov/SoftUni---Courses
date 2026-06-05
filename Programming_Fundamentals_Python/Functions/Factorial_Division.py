from functools import reduce


def factorial_division(first_num: int, second_num: int) -> float:
    first_factorial_list = [element for element in range(1, first_num + 1)]
    first_factorial_sum = reduce(lambda x, y: x * y, first_factorial_list)

    second_factorial_list = [element for element in range(1, second_num + 1)]
    second_factorial_sum = reduce(lambda x, y: x * y, second_factorial_list)

    return first_factorial_sum / second_factorial_sum


first_number = int(input())
second_number = int(input())

result = factorial_division(first_number, second_number)
print(f"{result:.2f}")
