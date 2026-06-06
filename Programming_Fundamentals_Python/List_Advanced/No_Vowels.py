def remove_vowels(text: str) -> list:
    vowels_list = ['a', 'o', 'u', 'e', 'i']
    return [symbol for symbol in text if symbol.lower() not in vowels_list]


input_string = input()
text_for_print = remove_vowels(input_string)

print(''.join(text_for_print))
