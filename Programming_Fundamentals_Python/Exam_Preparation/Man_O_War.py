def fire(war_ship: list, idx: int, some_damage: int) -> tuple[bool, list, str]:
    if idx in range(len(war_ship)):
        war_ship[idx] -= some_damage
        if war_ship[idx] <= 0:
            return True, war_ship, "You won! The enemy ship has sunken."
    return False, war_ship, ''


def defend(pirate_ship: list, start_idx: int, end_idx: int, some_damage: int) -> tuple[bool, list, str]:
    valid_range = range(len(pirate_ship))

    if start_idx in valid_range and end_idx in valid_range:
        finish = max(start_idx, end_idx)
        start = min(start_idx, end_idx)

        for attack in range(start, finish + 1):
            pirate_ship[attack] -= some_damage
            if pirate_ship[attack] <= 0:
                return True, pirate_ship, "You lost! The pirate ship has sunken."
    return False, pirate_ship, ''


def repair(pirate_ship: list, idx: int, some_health: int, max_health: int) -> list:
    if idx in range(len(pirate_ship)):
        added_health = min(some_health, (max_health - pirate_ship[idx]))
        pirate_ship[idx] += added_health
        return pirate_ship
    return pirate_ship


def status(pirate_ship: list, max_health: int) -> str:
    count_sections_for_repair = 0

    for section in pirate_ship:
        if section < max_health * 0.2:
            count_sections_for_repair += 1
    return f"{count_sections_for_repair} sections need repair."


pirate_ship_sections = [int(element) for element in input().split('>')]
war_ship_sections = [int(element) for element in input().split('>')]
maximum_health = int(input())

while (current_command := input()) != "Retire":

    command_split = current_command.split()
    command = command_split[0]
    message = ''
    stop = False

    if command == "Fire":
        index, damage = int(command_split[1]), int(command_split[2])
        stop, war_ship_sections, message = fire(war_ship_sections, index, damage)
    elif command == "Defend":
        start_index, end_index, damage = int(command_split[1]), int(command_split[2]), int(command_split[3])
        stop, pirate_ship_sections, message = defend(pirate_ship_sections, start_index, end_index, damage)
    elif command == "Repair":
        index, health = int(command_split[1]), int(command_split[2])
        pirate_ship_sections = repair(pirate_ship_sections, index, health, maximum_health)
    elif command == "Status":
        message = status(pirate_ship_sections, maximum_health)

    if message:
        print(message)
    if stop:
        break
else:
    print(f"Pirate ship status: {sum(pirate_ship_sections)}")
    print(f"Warship status: {sum(war_ship_sections)}")
