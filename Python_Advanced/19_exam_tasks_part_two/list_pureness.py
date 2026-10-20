from collections import deque


def best_list_pureness(input_list: list, number: int) -> str:
    input_list = deque(input_list)
    best_pureness = 0
    number_of_rotation = 0

    current_rotation = 0
    for _ in range(number + 1):
        current_pureness = 0
        for idx, num in enumerate(input_list):
            current_pureness += num * idx

        if current_pureness > best_pureness:
            best_pureness = current_pureness
            number_of_rotation = current_rotation

        input_list.rotate(1)
        current_rotation += 1

    return f"Best pureness {best_pureness} after {number_of_rotation} rotations"


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
