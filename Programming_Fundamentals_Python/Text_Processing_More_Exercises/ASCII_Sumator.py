def ascii_sumator(first_symbol: str, second_symbol: str, some_string: str) -> int:
    ascii_sum = 0
    for symbol in some_string:
        if ord(first_symbol) < ord(symbol) < ord(second_symbol):
            ascii_sum += ord(symbol)
    return ascii_sum


first_character = input()
second_character = input()
random_string = input()

print(ascii_sumator(first_character, second_character, random_string))
