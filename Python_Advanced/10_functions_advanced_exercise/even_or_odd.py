def even_odd(*args) -> list:
    command = args[-1]

    if command == "even":
        return [num for num in args[:-1] if num % 2 == 0]
    return [num for num in args[:-1] if num % 2 != 0]


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
