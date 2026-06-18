def loot(lst: list, some_items: str) -> tuple[list, str]:
    items = some_items.split()
    for item in items:
        if item not in lst:
            lst.insert(0, item)
    return lst, ''


def drop(lst: list, some_items: str) -> tuple[list, str]:
    index = int(some_items)
    if index in range(len(lst)):
        move_item = lst.pop(index)
        lst.append(move_item)
    return lst, ''


def steal(lst: list, some_items: str) -> tuple[list, str]:
    count_stolen_item = int(some_items)
    stolen_items = []
    for number in range(count_stolen_item):
        if lst:
            stolen = lst.pop()
            stolen_items.append(stolen)
        else:
            break
    return lst, f"{', '.join(reversed(stolen_items))}"


all_commands = {
    "Loot": loot,
    "Drop": drop,
    "Steal": steal
}

treasure_chest = input().split('|')

while (current_command := input()) != "Yohoho!":

    split_command = current_command.split(' ', 1)
    command, parameters = split_command[0], split_command[1]

    treasure_chest, message = all_commands[command](treasure_chest, parameters)
    if message:
        print(message)

if not treasure_chest:
    print("Failed treasure hunt.")
else:
    treasure_length = [len(element) for element in treasure_chest]
    average_gain = sum(treasure_length) / len(treasure_chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
