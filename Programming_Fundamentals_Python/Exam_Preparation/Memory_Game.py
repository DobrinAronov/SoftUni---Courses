def memory_game(lst: list, idx_1: int, idx_2: int, num_moves: int) -> tuple[bool, list, int, str]:
    num_moves += 1
    index_range = range(0, len(lst))

    if idx_1 == idx_2 or (idx_1 not in index_range or idx_2 not in index_range):
        middle_idx = len(lst) // 2
        lst.insert(middle_idx, f"-{num_moves}a")
        lst.insert(middle_idx, f"-{num_moves}a")
        return False, lst, num_moves, "Invalid input! Adding additional elements to the board"

    elif lst[idx_1] != lst[idx_2]:
        return False, lst, num_moves, "Try again!"

    # Case when we have equal indexes
    first_remove_idx = max(idx_1, idx_2)
    second_remove_idx = min(idx_1, idx_2)

    remove_element = lst.pop(first_remove_idx)
    lst.pop(second_remove_idx)

    if lst:
        return False, lst, num_moves, f"Congrats! You have found matching elements - {remove_element}!"
    return True, lst, num_moves, f"Congrats! You have found matching elements - {remove_element}!"


elements = input().split()
number_of_moves = 0

while (current_command := input()) != 'end':

    index_1, index_2 = current_command.split()
    index_1, index_2 = int(index_1), int(index_2)

    stop, elements, number_of_moves, massage = memory_game(elements, index_1, index_2, number_of_moves)
    print(massage)

    if stop:
        print(f"You have won in {number_of_moves} turns!")
        break

else:
    if elements:
        print(f"Sorry you lose :(\n{' '.join(elements)}")
