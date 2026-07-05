def reverse_string(some_string: str) -> str:
    return some_string[::-1]


while (current_string := input()) != "end":
    print(f"{current_string} = {reverse_string(current_string)}")
