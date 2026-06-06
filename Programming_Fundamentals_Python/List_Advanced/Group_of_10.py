def group_tens(lst: list) -> list:
    max_number = max(lst)
    if max_number % 10 != 0:
        max_number = (max_number // 10) + 1
    else:
        max_number = max_number // 10

    messages = [[] for _ in range(max_number)]

    range_0 = range(0, 11)
    range_1 = range(11, 21)
    range_2 = range(21, 31)
    range_3 = range(31, 41)
    range_4 = range(41, 51)
    range_5 = range(51, 61)
    range_6 = range(61, 71)
    range_7 = range(71, 81)
    range_8 = range(81, 91)
    range_9 = range(91, 101)

    for number in lst:
        if number in range_0:
            messages[0].append(number)
        elif number in range_1:
            messages[1].append(number)
        elif number in range_2:
            messages[2].append(number)
        elif number in range_3:
            messages[3].append(number)
        elif number in range_4:
            messages[4].append(number)
        elif number in range_5:
            messages[5].append(number)
        elif number in range_6:
            messages[6].append(number)
        elif number in range_7:
            messages[7].append(number)
        elif number in range_8:
            messages[8].append(number)
        elif number in range_9:
            messages[9].append(number)

    return messages


numbers = [int(number) for number in input().split(', ')]

tens_list = group_tens(numbers)

for tens_group in range(len(tens_list)):
    tens = (tens_group + 1) * 10
    print(f"Group of {tens}'s: {tens_list[tens_group]}")
