def smallest_number(a: int, b: int, c : int) -> int:
    return min(a, b, c)


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(smallest_number(number_1, number_2, number_3))