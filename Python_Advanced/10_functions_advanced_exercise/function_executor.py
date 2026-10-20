def func_executor(*args) -> str:
    output = []

    for pair in args:
        func, numbers = pair
        output.append(f"{func.__name__} - {func(*numbers)}")

    return '\n'.join(output)


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result


def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result


print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))
