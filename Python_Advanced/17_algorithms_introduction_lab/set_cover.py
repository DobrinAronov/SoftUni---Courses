def set_cover(uni: list, some_sets: list[list]):
    uni_set = set(uni)
    chosen_sets = []
    remining_sets = some_sets.copy()
    while uni_set:
        best_sets = max(remining_sets, key=lambda s: len(uni_set.intersection(s)))
        if not uni_set.intersection(best_sets):
            break

        chosen_sets.append(best_sets)
        uni_set -= set(best_sets)
        remining_sets.remove(best_sets)

    if uni_set:
        return None
    return len(chosen_sets), chosen_sets


universe = input().split(', ')
number_of_sets = int(input())

sets = []
for n in range(number_of_sets):
    current_set = input().split(', ')
    sets.append(current_set)

num_of_subset, found_sets = set_cover(universe, sets)
print(f"Sets to take ({num_of_subset}):")
for f in found_sets:
    str_to_print = '{ ' + f"{', '.join(f)}" + ' }'
    print(str_to_print)