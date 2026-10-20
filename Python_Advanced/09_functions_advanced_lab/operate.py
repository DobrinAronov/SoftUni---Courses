from functools import reduce


def operate(operator, *numbers):
    operators = {
        "+": lambda: reduce(lambda x, y: x + y, numbers),
        "-": lambda: reduce(lambda x, y: x - y, numbers),
        "*": lambda: reduce(lambda x, y: x * y, numbers),
        "/": lambda: reduce(lambda x, y: x / y, numbers)
    }

    if operator == "/" and 0 in numbers[1:]:
        return "Error"
    return operators[operator]()


print(operate("+", 1, 2, 3))
