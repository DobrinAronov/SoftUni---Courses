def calculations(some_operator : str, num_1 : int, num_2 : int) -> int:
    result = 0
    if some_operator == 'multiply':
        result = num_1 * num_2
    elif some_operator == 'divide':
        result = int(num_1 / num_2)
    elif some_operator == 'add':
        result = num_1 + num_2
    elif some_operator == 'subtract':
        result = num_1 - num_2
    return result


operator = input()
number_1 = int(input())
number_2 = int(input())

print(calculations(operator, number_1, number_2))