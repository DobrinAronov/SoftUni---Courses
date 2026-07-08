def string_explosion(some_string: str) -> str:
    output_string = ''
    number_of_explosions = 0

    for idx in range(len(some_string)):
        if some_string[idx] == '>':
            output_string += some_string[idx]
            number_of_explosions += int(some_string[idx + 1])

        elif number_of_explosions > 0:
            number_of_explosions -= 1

        else:
            output_string += some_string[idx]

    return output_string


input_string = input()
print(string_explosion(input_string))
