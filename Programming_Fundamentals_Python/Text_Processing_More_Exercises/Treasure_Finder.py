def decrypts_a_message(key: list, some_string: str) -> tuple[str, str]:
    decrypts_message = ''

    while True:
        is_break = False
        for index in range(len(key)):
            decrypt_symbol = chr(ord(some_string[index]) - key[index])
            decrypts_message += decrypt_symbol
            if index == len(key) - 1:
                some_string = some_string[index + 1:]
                if not some_string:
                    is_break = True
                    break
            elif index == len(some_string) - 1:
                is_break = True
                break
        if is_break:
            break

    treasure = ''
    place = ''
    find_treasure = False
    find_place = False

    for symbol in decrypts_message:
        # Finding treasure
        if symbol == '&' and not find_treasure:
            find_treasure = True
        elif find_treasure:
            if symbol != '&':
                treasure += symbol
            else:
                find_treasure = False
            continue
        # Finding treasure's coordinates
        if symbol == '<':
            find_place = True
        elif find_place:
            if symbol != '>':
                place += symbol
            else:
                find_place = False

    return treasure, place


key_list = [int(element) for element in input().split()]

while (current_string := input()) != "find":
    type_treasure, coordinates = decrypts_a_message(key_list, str(current_string))
    print(f"Found {type_treasure} at {coordinates}")
