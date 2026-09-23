SIZE = int(input())
moves = input().split()

matrix = []

s_row, s_col = 0, 0
num_of_coils = 0

for row in range(SIZE):
    matrix.append(input().split())
    for col in range(SIZE):
        if matrix[row][col] == "s":
            s_row, s_col = row, col
        elif matrix[row][col] == "c":
            num_of_coils += 1

all_directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for move in moves:
    dr, dc = all_directions[move]
    new_row, new_col = s_row + dr, s_col + dc

    if not (0 <= new_row < SIZE and 0 <= new_col < SIZE):
        continue
    s_row, s_col = new_row, new_col

    if matrix[new_row][new_col] == "e":
        print(f"Game over! ({s_row}, {s_col})")
        break
    if matrix[new_row][new_col] == "c":
        matrix[new_row][new_col] = "*"
        num_of_coils -= 1
        if num_of_coils == 0:
            print(f"You collected all coal! ({s_row}, {s_col})")
            break

else:
    print(f"{num_of_coils} pieces of coal left. ({s_row}, {s_col})")
