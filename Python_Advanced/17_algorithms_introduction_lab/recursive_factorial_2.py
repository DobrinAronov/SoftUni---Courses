def calculate_factorial(n: int, num: int) -> int:
    if n == num:
        return num

    return n * calculate_factorial(n + 1, num)


number = int(input())
print(calculate_factorial(1, number))
