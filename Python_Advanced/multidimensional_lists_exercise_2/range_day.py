def validate_coordinates(check_r: int, check_c: int, some_size: int) -> bool:
    if 0 <= check_r < some_size and 0 <= check_c < some_size:
        return True
    return False


def move(matrix: list[list], direct: str, r: int, c: int, moves: dict, some_steps: int) -> tuple[int, int]:

    next_row = r + moves[direct][0] * some_steps
    next_col = c + moves[direct][1] * some_steps

    if validate_coordinates(next_row, next_col, len(matrix)):
        if matrix[next_row][next_col] == ".":
            r, c = next_row, next_col

    return r, c


def shoot(matrix: list[list], direct: str, r: int, c: int, moves: dict) -> tuple[int, list]:
    target = 0
    tar_coordinates = []

    for _ in range(len(matrix) - 1):
        r += moves[direct][0]
        c += moves[direct][1]
        if validate_coordinates(r, c, len(matrix)):
            if matrix[r][c] == "x":
                matrix[r][c] = "."
                target += 1
                tar_coordinates = [r, c]
                break
        else:
            break
    return target, tar_coordinates


size = 5

shooting_range = []

my_row, my_col = (0, 0)
num_of_targets = 0

for row in range(size):
    shooting_range.append(input().split())
    for col in range(size):
        if shooting_range[row][col] == "A":
            my_row, my_col = row, col
            shooting_range[row][col] = "."
        elif shooting_range[row][col] == "x":
            num_of_targets += 1

all_directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

targets_shot = 0
shot_targets = []

for _ in range(int(input())):
    action, direction, *steps = input().split()

    if action == "move":
        steps = int(steps[0])
        my_row, my_col = \
            move(shooting_range, direction, my_row, my_col, all_directions, steps)

    elif action == "shoot":
        curr_targets_shot, curr_targets = \
            shoot(shooting_range, direction, my_row, my_col, all_directions)

        targets_shot += curr_targets_shot
        shot_targets.append(curr_targets) if curr_targets else None

        if targets_shot == num_of_targets:
            print(f"Training completed! All {targets_shot} targets hit.")
            break

else:
    print(f"Training not completed! {num_of_targets - targets_shot} targets left.")

print(*shot_targets, sep="\n") if shot_targets else None
