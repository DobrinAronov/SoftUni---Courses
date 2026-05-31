def sum_numbers(a: int, b: int) ->int:
    return a + b


def subtract(calculate_sum: int, c: int) -> int:
    return calculate_sum - c


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

def add_and_subtract():
    sum_first_two_numbers = sum_numbers(number_1, number_2)
    return subtract(sum_first_two_numbers, number_3)

print(add_and_subtract())