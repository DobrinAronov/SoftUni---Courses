def find_hidden_message(some_string: str) -> str:
    numbers_list = []
    no_number_list = []

    for symbol in some_string:
        if symbol.isdigit():
            numbers_list.append(int(symbol))
        else:
            no_number_list.append(symbol)

    take_list = []
    skip_list = []

    for index in range(len(numbers_list)):
        if index % 2 == 0:
            take_list.append(numbers_list[index])
        else:
            skip_list.append(numbers_list[index])

    encrypted_str = ''.join(no_number_list)
    result_string = ''

    for idx in range(len(take_list)):
        take_index = take_list[idx]
        take_char = encrypted_str[:take_index]
        result_string += take_char
        skip_index = skip_list[idx]
        encrypted_str = encrypted_str[take_index + skip_index:]

    return result_string


input_string = input()

result = find_hidden_message(input_string)
print(result)
