def adding_side_and_force_user(base: dict, name: str, some_side: str) -> dict:
    if some_side not in base.keys():
        base[some_side] = []

    is_found = False
    for force_list in base.values():
        if name in force_list:
            is_found = True
            break
    if not is_found:
        base[some_side].append(name)
    return base


def change_side(base: dict, name: str, other_side: str) -> tuple[str, dict]:
    same_side = ''
    some_message = ''
    is_name = False
    is_message = False

    if other_side not in base.keys():
        base[other_side] = []

    # Checking if the name exists in the dictionary and determine same_side
    for force_side, force_list in base.items():
        for force_user in force_list:
            if force_user == name:
                is_name = True
                same_side = force_side
                break
        if is_name:
            break

    # if name doesn't exist, we adding it in other_side
    if not is_name:
        base[other_side].append(name)
        is_message = True

    else:
        if name in base[same_side] and name not in base[other_side]:
            base[same_side].remove(name)
            base[other_side].append(name)
            is_message = True

    if is_message:
        some_message = f"{name} joins the {other_side} side!"
    return some_message, base


force_users_by_side = {}

while (current_command := input()) != "Lumpawaroo":

    message = ''

    if '|' in current_command:
        side, user = current_command.split(' | ')

        force_users_by_side = adding_side_and_force_user(force_users_by_side, user, side)

    elif '->' in current_command:
        user, side = current_command.split(' -> ')

        message, force_users_by_side = change_side(force_users_by_side, user, side)

    if message:
        print(message)

for side, users_list in force_users_by_side.items():
    if users_list:
        print(f"Side: {side}, Members: {len(users_list)}")
        for user in users_list:
            print(f"! {user}")
    else:
        continue
