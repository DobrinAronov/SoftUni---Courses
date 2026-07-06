def encrypt_text(input_str: str) -> str:
    encrypt_string = ''

    for symbol in input_str:
        encrypt_string += chr(ord(symbol) + 3)

    return encrypt_string


input_text = input()

print(encrypt_text(input_text))
