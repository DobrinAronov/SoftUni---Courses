def digits_letters_and_others(some_string: str) ->tuple[str, str, str]:
    some_digits = ''
    some_letters = ''
    some_others = ''
    for symbol in some_string:
        if symbol.isdigit():
            some_digits += symbol
        elif symbol.isalpha():
            some_letters += symbol
        else:
            some_others += symbol

    return some_digits, some_letters, some_others


input_string = input()

digits, letters, others = digits_letters_and_others(input_string)
print(f"{digits}\n{letters}\n{others}")