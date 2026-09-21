size = int(input())

wonderland = []

a_row, a_col = (0, 0)

for row in range(size):
    current_row = input().split()
    for col in range(size):
        if current_row[col] == "A":
            a_row, a_col = row, col
            current_row[col] = "*"
    wonderland.append(current_row)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

tea_bags = 0
while True:
    command = input()

    a_row += directions[command][0]
    a_col += directions[command][1]

    if not(0 <= a_row < size and 0 <= a_col < size):
        print("Alice didn't make it to the tea party.")
        break

    elif wonderland[a_row][a_col] == "R":
        wonderland[a_row][a_col] = "*"
        print("Alice didn't make it to the tea party.")
        break

    elif wonderland[a_row][a_col].isdigit():
        tea_bags += int(wonderland[a_row][a_col])
        wonderland[a_row][a_col] = "*"
        if tea_bags >= 10:
            print("She did it! She went to the party.")
            break
    else:
        wonderland[a_row][a_col] = "*"

[print(*row) for row in wonderland]