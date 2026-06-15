def shooting_to_win(count_shot: int, targets: list, index: int) -> tuple[int, list]:
    if index in range(len(targets)):
        if targets[index] != -1:
            target_value = targets[index]
            count_shot += 1
            targets[index] = -1

            for idx in range(len(targets)):
                if targets[idx] != -1:
                    if targets[idx] > target_value:
                        targets[idx] -= target_value
                    else:
                        targets[idx] += target_value

            return count_shot, targets
    return count_shot, targets


the_targets_sequence = [int(target) for target in input().split()]

count_shot_targets = 0

while (command := input()) != "End":
    target_index = int(command)

    count_shot_targets, the_targets_sequence = shooting_to_win(count_shot_targets, the_targets_sequence, target_index)

the_targets_str = [str(target) for target in the_targets_sequence]
print(f"Shot targets: {count_shot_targets} -> {' '.join(the_targets_str)}")
