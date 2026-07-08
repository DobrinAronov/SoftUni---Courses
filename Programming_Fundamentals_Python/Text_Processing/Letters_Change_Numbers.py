def calculate_total_sum(str_list: list) -> str:
    total = 0

    for some_str in str_list:
        current_number = int(some_str[1:-1])
        current_sum = 0
        # (ord(some_str[index].lower()) - 96) is letter's position in the alphabet (starting from 1)
        if some_str[0].isupper():
            current_sum += current_number / (ord(some_str[0].lower()) - 96)
        elif some_str[0].islower():
            current_sum += current_number * (ord(some_str[0].lower()) - 96)

        if some_str[-1].isupper():
            current_sum -= ord(some_str[-1].lower()) - 96
        elif some_str[-1].islower():
            current_sum += ord(some_str[-1].lower()) - 96

        total += current_sum

    return f"{total:.2f}"


string_list = input().split()
print(calculate_total_sum(string_list))
