def even(lst: list, ) -> list:
    return [x for x in lst if x % 2 == 0]


def odd(lst: list, ) -> list:
    return [x for x in lst if x % 2 != 0]


def negative(lst: list, ) -> list:
    return [x for x in lst if x < 0]


def positive(lst: list, ) -> list:
    return [x for x in lst if x >= 0]


number_of_integers = int(input())
all_integers = []

for num in range(number_of_integers):
    current_number = int(input())
    all_integers.append(current_number)

command = input()

all_commands = {
    'even' : even,
    'odd' : odd,
    'negative' : negative,
    'positive' : positive
}

print(all_commands[command](all_integers))