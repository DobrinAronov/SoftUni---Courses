SIZE = int(input())
CAR_NUMBER = input()

r_row, r_col = 0, 0

tunel_coordinates = []

race_route = []
for row in range(SIZE):
    race_route.append(list(input().split()))
    for col in range(SIZE):
        if race_route[row][col] == 'T':
            tunel_coordinates.append((row, col))

ALL_DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

kilometers_passed = 0
is_finish_car = False
while True:
    command = input()
    if command == "End":
        break

    r_row += ALL_DIRECTIONS[command][0]
    r_col += ALL_DIRECTIONS[command][1]

    cell = race_route[r_row][r_col]

    if cell == 'F':
        kilometers_passed += 10
        is_finish_car = True
        print(f"Racing car {CAR_NUMBER} finished the stage!")
        break

    if cell == 'T':
        race_route[r_row][r_col] = '.'
        for pair in tunel_coordinates:
            if (r_row, r_col) != pair:
                r_row, r_col = pair
        kilometers_passed += 30
        race_route[r_row][r_col] = '.'

    elif cell == '.':
        kilometers_passed += 10

if not is_finish_car:
    print(f"Racing car {CAR_NUMBER} DNF.")

print(f"Distance covered {kilometers_passed} km.")

race_route[r_row][r_col] = 'C'
[print(*row, sep='') for row in race_route]
