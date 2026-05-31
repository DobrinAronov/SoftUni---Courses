def characters_in_range(first: str, second: str):
    return [chr(element) for element in range(ord(first) + 1, ord(second))]


first_character = input()
second_character = input()

print(' '.join(characters_in_range(first_character, second_character)))