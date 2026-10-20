def calculate_factorial(num: int) -> int:
    if num == 0:
        return 1

    return num * calculate_factorial(num - 1)


number = int(input())
print(calculate_factorial(number))
