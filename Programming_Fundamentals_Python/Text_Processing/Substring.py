def substring(some_string: str, sub_str: str) -> str:
    while sub_str in some_string:
        some_string = some_string.replace(sub_string, '')
    return some_string


sub_string = input()
input_string = input()

print(substring(input_string, sub_string))