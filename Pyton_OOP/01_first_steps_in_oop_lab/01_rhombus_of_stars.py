def prinf_line(num: int, n: int):
    print(" " * (num - n) + "* " * n)


def print_rhombus_down_side(num: int):
    for row in range(num, -1, -1):
        prinf_line(num, row)


def print_rhombus_up_side(num: int):
    for row in range(num):
        prinf_line(num, row)


def print_rhombus(num: int):
    print_rhombus_up_side(num)
    print_rhombus_down_side(num)


number = int(input())
print_rhombus(number)
