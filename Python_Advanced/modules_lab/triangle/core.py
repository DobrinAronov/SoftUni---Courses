def print_top_part(num: int):
    for row in range(1, num + 1):
        for n in range(1, row + 1):
            print(n, end=' ')
        print()


def print_bottom_part(num: int):
    for row in range(1, num):
        for n in range(1, num + 1 - row):
            print(n, end=' ')
        print()