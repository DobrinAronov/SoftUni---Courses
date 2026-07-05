def repeat_string(some_list: list) -> str:
    repeat_list = []

    for word in some_list:
        repeat_word = word * len(word)
        repeat_list.append(repeat_word)
    return f"{''.join(repeat_list)}"


input_string = input().split()

print(repeat_string(input_string))
