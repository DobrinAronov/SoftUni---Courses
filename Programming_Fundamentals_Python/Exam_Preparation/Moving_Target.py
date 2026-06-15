def shoot(targets: list, idx: int, power: int) -> tuple[list, str]:
    if idx in range(len(targets)):
        targets[idx] -= power
        if targets[idx] <= 0:
            del targets[idx]
    return targets, ''


def add(targets: list, idx: int, value: int) -> tuple[list, str]:
    if idx in range(len(targets)):
        targets.insert(idx, value)
        return targets, ''
    return targets, "Invalid placement!"


def strike(targets: list, idx: int, radius: int) -> tuple[list, str]:
    start_idx = idx - radius
    end_idx = idx + radius
    index_range = range(len(targets))

    if start_idx in index_range and end_idx in index_range:
        targets = targets[:start_idx] + targets[end_idx + 1:]
        return targets, ''
    return targets, "Strike missed!"


all_commands = {
    "Shoot": shoot,
    "Add": add,
    "Strike": strike
}

sequence_of_targets = [int(target) for target in input().split()]

while (current_command := input()) != "End":

    command, index, parameter = current_command.split()
    index, parameter = int(index), int(parameter)

    sequence_of_targets, message = all_commands[command](sequence_of_targets, index, parameter)

    if message:
        print(message)

sequence_of_targets_str = [str(number) for number in sequence_of_targets]
print(f"{'|'.join(sequence_of_targets_str)}")
