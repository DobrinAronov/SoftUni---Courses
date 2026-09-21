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

DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

tea_bags = 0

while tea_bags < 10:
    dr, dc = DIRECTIONS[input()]
    a_row, a_col = a_row + dr, a_col + dc

    if not(0 <= a_row < size and 0 <= a_col < size):
        break

    current_cell = wonderland[a_row][a_col]
    wonderland[a_row][a_col] = "*"

    if current_cell == "R":
        break

    if current_cell.isdigit():
        tea_bags += int(current_cell)

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(*row) for row in wonderland]