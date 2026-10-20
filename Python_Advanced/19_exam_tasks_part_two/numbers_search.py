def numbers_searching(*numbers: tuple[int]) -> list:
    input_list = list(numbers)
    min_num = min(input_list)
    max_num = max(input_list)

    all_nums = {n for n in range(min_num, max_num + 1)}

    missing_num = all_nums.difference(set(input_list))
    repeating_nums = sorted({n for n in input_list if input_list.count(n) > 1})

    return [*missing_num, list(repeating_nums)]


print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
