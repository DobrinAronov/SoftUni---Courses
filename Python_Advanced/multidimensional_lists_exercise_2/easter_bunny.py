size_of_field = int(input())

field = []

b_row, b_col = 0, 0

for row in range(size_of_field):
    current_row = input().split()
    for col in range(size_of_field):
        if current_row[col] == "B":
            b_row, b_col = row, col
    field.append(current_row)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

right_direction = ''
positions = []
max_eggs = float("-inf")

for move in directions:
    eggs_in_direction = 0
    moves_in_directions = []
    # We overwrite the bunny's starting position.
    b_i_row, b_i_col = b_row, b_col

    for time in range(size_of_field - 1):
        new_row = b_i_row + directions[move][0]
        new_col = b_i_col + directions[move][1]
        # If the bunny goes outside the field
        if not (0 <= new_row < size_of_field and
                0 <= new_col < size_of_field):
            break
        # If the bunny gets caught in a trap
        elif field[new_row][new_col] == "X":
            break
        # The bunny is collecting eggs.
        else:
            eggs_in_direction += int(field[new_row][new_col])
            moves_in_directions.append([new_row, new_col])
            b_i_row, b_i_col = new_row, new_col

    # Check for the maximum number of eggs if there are available moves.
    if eggs_in_direction > max_eggs and moves_in_directions:
        right_direction = move
        positions = moves_in_directions
        max_eggs = eggs_in_direction

print(right_direction)
[print(position) for position in positions]
print(max_eggs)
