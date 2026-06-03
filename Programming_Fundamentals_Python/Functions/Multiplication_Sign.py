def multiplication_sign(first_num: int, second_num: int, tird_num: int) -> str:
    count_of_negative = 0
    list_numbers = [first_num, second_num, tird_num]
    for number in list_numbers:
        if number == 0:
            return "zero"
        if number < 0:
            count_of_negative += 1
    if count_of_negative % 2 != 0:
        return "negative"
    return "positive"


first_number, second_number, tird_number = [int(input()) for _ in range(3)]

print(multiplication_sign(first_number, second_number, tird_number))