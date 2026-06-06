def calculate_employee_happiness(lst: list[int], some_factor: int) -> str:
    list_with_factor = [number * some_factor for number in lst]
    average_happiness = sum(list_with_factor) / len(list_with_factor)

    count_happiness_employee = 0

    for happiness in list_with_factor:
        if happiness >= average_happiness:
            count_happiness_employee += 1
    if count_happiness_employee >= len(list_with_factor) // 2:
        return f"Score: {count_happiness_employee}/{len(list_with_factor)}. Employees are happy!"
    return f"Score: {count_happiness_employee}/{len(list_with_factor)}. Employees are not happy!"


list_employee_happiness = [int(number) for number in input().split()]
factor = int(input())

print(calculate_employee_happiness(list_employee_happiness, factor))
