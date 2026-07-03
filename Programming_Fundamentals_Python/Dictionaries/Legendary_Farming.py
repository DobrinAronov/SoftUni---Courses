def adding_key_materials(some_dict: dict, word: str, num: int) -> tuple[bool, str, dict]:
    win = ''
    if word == "shards":
        some_dict[word] += num
        if some_dict[word] >= 250:
            some_dict[word] -= 250
            win = 'Shadowmourne'
            return True, win, some_dict
        return False, win, some_dict

    elif word == "fragments":
        some_dict[word] += num
        if some_dict[word] >= 250:
            some_dict[word] -= 250
            win = 'Valanyr'
            return True, win, some_dict
        return False, win, some_dict

    elif word == "motes":
        some_dict[word] += num
        if some_dict[word] >= 250:
            some_dict[word] -= 250
            win = 'Dragonwrath'
            return True, win, some_dict
        return False, win, some_dict
    return False, win, some_dict


def adding_junk_materials(junk_dict: dict, some_word: str, some_num: int) -> dict:
    if some_word not in junk_dict:
        junk_dict[some_word] = some_num
    else:
        junk_dict[some_word] += some_num
    return junk_dict


legendary_items = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}

junk_items = {}
winner = ''
is_winner = False

while True:
    current_list = input().split()

    for idx in range(0, len(current_list), 2):
        number = int(current_list[idx])
        name = current_list[idx + 1].lower()
        is_material_won = False
        # Include key materials in dictionary legendary_items
        if name in ("shards", "fragments", "motes"):
            is_material_won, winner, legendary_items = adding_key_materials(legendary_items, name, number)
        # Include junk materials in dictionary junk_items
        else:
            junk_items = adding_junk_materials(junk_items, name, number)

        if is_material_won:
            is_winner = True
            break

    if is_winner:
        break

if winner:
    print(f"{winner} obtained!")

for material, quantity in legendary_items.items():
    print(f"{material}: {quantity}")

for junk, quantity in junk_items.items():
    print(f"{junk}: {quantity}")
