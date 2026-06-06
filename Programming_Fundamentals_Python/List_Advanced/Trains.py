def add(lst: list, people: int) -> list:
    lst[-1] += people
    return lst


def insert(lst: list, idx: int, people: int) -> list:
    lst[idx] += people
    return lst


def leave(lst: list, idx: int, people: int) -> list:
    lst[idx] -= people
    return lst


number_of_wagons = int(input())

train = [0 for num in range(number_of_wagons)]

while (current_command := input()) != 'End':

    split_command = current_command.split()
    command = split_command[0]

    if command == 'add':
        number_of_people = int(split_command[1])
        train = add(train, number_of_people)

    elif command == 'insert':
        index, number_of_people = int(split_command[1]), int(split_command[2])
        train = insert(train, index, number_of_people)

    elif command == 'leave':
        index, number_of_people = int(split_command[1]), int(split_command[2])
        train = leave(train, index, number_of_people)

print(train)
