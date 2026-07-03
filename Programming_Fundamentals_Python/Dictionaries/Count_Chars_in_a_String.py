def count_chars(some_string: str) -> dict:
    output_dict = {}
    for symbol in some_string:
        if symbol != ' ':
            if symbol not in output_dict:
                output_dict[symbol] = some_string.count(symbol)
    return output_dict


input_text = input()
result = count_chars(input_text)

for letter, count in result.items():
    print(f"{letter} -> {count}")
