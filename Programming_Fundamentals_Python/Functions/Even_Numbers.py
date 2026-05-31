def only_the_even_numbers(lst: list) -> list:
    result = list(filter(lambda x : x % 2 == 0, lst))
    return result


numbers = [int(element) for element in input().split()]

print(only_the_even_numbers(numbers))