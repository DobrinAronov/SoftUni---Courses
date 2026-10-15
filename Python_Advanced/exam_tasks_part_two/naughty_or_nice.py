def naughty_or_nice_list(santa_list: list, *child_data, **check_dict) -> str:
    nice = []
    naughty = []
    not_found = []

    grades_dict = {}
    for pair in child_data:
        grade, child_type = pair.split('-')
        grades_dict[int(grade)] = child_type

    for num, child_type in grades_dict.items():
        num_matches_pairs = [pair for pair in santa_list if pair[0] == num]
        if len(num_matches_pairs) == 1:
            name = num_matches_pairs[0][1]
            if grades_dict[num] == "Nice":
                nice.append(name)
                santa_list.remove((num, name))
            elif grades_dict[num] == "Naughty":
                naughty.append(name)
                santa_list.remove((num, name))

    for name, child_type in check_dict.items():
        name_matches_pairs = [pair for pair in santa_list if pair[1] == name]
        if len(name_matches_pairs) == 1:
            if child_type == "Nice":
                nice.append(name)
            elif child_type == "Naughty":
                naughty.append(name)
            santa_list.remove(*name_matches_pairs)

    if santa_list:
        for pair in santa_list:
            not_found.append(pair[1])

    output = []
    if nice:
        output.append(f"Nice: {', '.join(nice)}")
    if naughty:
        output.append(f"Naughty: {', '.join(naughty)}")
    if not_found:
        output.append(f"Not found: {', '.join(not_found)}")

    return '\n'.join(output)


print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
