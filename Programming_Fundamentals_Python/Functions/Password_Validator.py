def check_length(input_str: str) -> bool:
    if 6 <= len(input_str) <= 10:
        return True
    return False


def only_letters_and_digit(input_str: str) -> bool:
    for symbol in input_str:
        if not (symbol.isdigit() or symbol.isalpha()):
            return False
    return True


def least_two_digits(input_str: str) -> bool:
    number_of_digits = []
    for symbol in input_str:
        if symbol.isdigit():
            number_of_digits.append(symbol)
    if len(number_of_digits) < 2:
        return False
    return True


password = input()

condition_1 = check_length(password)
condition_2 = only_letters_and_digit(password)
condition_3 = least_two_digits(password)

if condition_1 and condition_2 and condition_3:
    print("Password is valid")
else:
    if not condition_1:
        print("Password must be between 6 and 10 characters")
    if not condition_2:
        print("Password must consist only of letters and digits")
    if not condition_3:
        print("Password must have at least 2 digits")