SIZE = 6

table = [input().split() for _ in range(SIZE)]

my_row, my_col = input().split(', ')
my_row, my_col = int(my_row.lstrip('(')), int(my_col.rstrip(')'))

ALL_DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while (command := input()) != "Stop":
    action, direction, *value = command.split(", ")

    my_row += ALL_DIRECTIONS[direction][0]
    my_col += ALL_DIRECTIONS[direction][1]

    cell = table[my_row][my_col]

    if action == "Create" and cell == '.':
        table[my_row][my_col] = value[0]

    elif action == "Update" and cell != '.':
        table[my_row][my_col] = value[0]

    elif action == "Delete" and cell != '.':
        table[my_row][my_col] = '.'

    elif action == "Read" and cell != '.':
        print(cell)

[print(*row, sep=' ') for row in table]
