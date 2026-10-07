mapper = {
    '/': lambda x, y: x / y if y != 0 else None,
    '*': lambda x, y: x * y,
    '-': lambda x, y: x - y,
    '+': lambda x, y: x + y,
    '^': lambda x, y: x ** y
}


def calculate_result(some_expression) -> str:
    num_first, operator, num_sec = some_expression.split()
    num_first, num_sec = float(num_first), float(num_sec)

    result = mapper[operator](num_first, num_sec)

    if result is None:
        return "Error, there is no division by zero."

    return f"{result:.2f}"

