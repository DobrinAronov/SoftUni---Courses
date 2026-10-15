ROWS, COLUMNS = map(int, input().split(', '))

my_row, my_col = 0, 0
number_of_items = 0
workshop = []

for row in range(ROWS):
    workshop.append(input().split())
    for col in range(COLUMNS):
        if workshop[row][col] == 'Y':
            my_row, my_col = row, col
            workshop[row][col] = 'x'
        elif workshop[row][col] in ['D', 'G', 'C']:
            number_of_items += 1

ALL_DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

collected_items = {"Christmas decorations": 0, "Gifts": 0, "Cookies": 0}
is_break = False

while (command := input()) != 'End':
    direction, steps = command.split('-')

    for step in range(int(steps)):
        my_row = (my_row + ALL_DIRECTIONS[direction][0]) % ROWS
        my_col = (my_col + ALL_DIRECTIONS[direction][1]) % COLUMNS

        cell = workshop[my_row][my_col]

        if cell == 'D':
            collected_items["Christmas decorations"] += 1
            number_of_items -= 1
        elif cell == 'G':
            collected_items["Gifts"] += 1
            number_of_items -= 1
        elif cell == 'C':
            collected_items["Cookies"] += 1
            number_of_items -= 1

        workshop[my_row][my_col] = 'x'
        if number_of_items == 0:
            is_break = True
            print("Merry Christmas!")
            break
    if is_break:
        break

print("You've collected:")
for item, count in collected_items.items():
    print(f"- {count} {item}")

workshop[my_row][my_col] = 'Y'
[print(*row) for row in workshop]
