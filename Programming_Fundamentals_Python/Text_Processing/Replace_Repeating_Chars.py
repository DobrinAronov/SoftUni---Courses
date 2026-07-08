def replace_repeating_symbols(some_string: str) -> str:
    output_string = ''

    for idx in range(len(some_string)):
        if idx == 0:
            output_string += some_string[idx]

        elif some_string[idx] != output_string[-1]:
            output_string += some_string[idx]

    return output_string


input_string = input()
print(replace_repeating_symbols(input_string))
