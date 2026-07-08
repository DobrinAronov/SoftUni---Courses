def rage_quit(some_text: str) -> str:
    unique_symbols = ''
    output_string = ''
    current_string = ''
    current_digits = ''

    for index in range(len(some_text)):
        max_index = len(some_text) - 1
        symbol = some_text[index]

        if not symbol.isdigit():
            symbol_uppercase = symbol.upper()
            if symbol_uppercase not in unique_symbols:
                unique_symbols += symbol_uppercase
            current_string += symbol_uppercase
            if current_digits:
                current_digits = ''
        else:
            current_digits += symbol
            # Checking if next symbol is out of range or if index is last
            if (index < max_index and not some_text[index + 1].isdigit()) or \
                    index == max_index:
                current_string = current_string * int(current_digits)
                output_string += current_string
                current_string = ''

    return f"Unique symbols used: {len(unique_symbols)}\n{output_string}"


input_string = input()
print(rage_quit(input_string))
