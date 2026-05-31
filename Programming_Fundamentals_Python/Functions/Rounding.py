def rounds(lst: list) -> list:
    return [round(element) for element in lst]


input_string = [float(element) for element in input().split()]

print(rounds(input_string))