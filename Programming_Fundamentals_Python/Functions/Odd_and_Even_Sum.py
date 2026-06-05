def odd_and_even_sum(some_number: str) -> str:
    odd_sum = 0
    even_sum = 0
    for symbol in some_number:
        digit = int(symbol)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = input()
print(odd_and_even_sum(number))