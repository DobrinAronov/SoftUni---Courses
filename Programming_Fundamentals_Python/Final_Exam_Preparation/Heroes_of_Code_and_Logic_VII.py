def cast_spell(some_dict: dict, name: str, mp_require: int, spell: str) -> tuple[dict, str]:
    if some_dict[name]["MP"] >= mp_require:
        some_dict[name]["MP"] -= mp_require
        mp_points = some_dict[name]["MP"]
        return some_dict, f"{name} has successfully cast {spell} and now has {mp_points} MP!"
    return some_dict, f"{name} does not have enough MP to cast {spell}!"


def take_damage(some_dict: dict, name: str, some_damage: int, attacker_name: str) -> tuple[dict, str]:
    some_dict[name]["HP"] -= some_damage
    if some_dict[name]["HP"] > 0:
        hp_points_left = some_dict[name]["HP"]
        return some_dict, (f"{name} was hit for {some_damage} HP by {attacker_name}"
                           f" and now has {hp_points_left} HP left!")
    del some_dict[name]
    return some_dict, f"{name} has been killed by {attacker_name}!"


def recharge(some_dict: dict, name: str, mp_increase: int) -> tuple[dict, str]:
    recharge_mp_points = min(mp_increase, (200 - some_dict[name]["MP"]))

    some_dict[name]["MP"] += recharge_mp_points
    return some_dict, f"{name} recharged for {recharge_mp_points} MP!"


def heal(some_dict: dict, name: str, hp_increase: int) -> tuple[dict, str]:
    recharge_hp_points = min(hp_increase, (100 - some_dict[name]["HP"]))

    some_dict[name]["HP"] += recharge_hp_points
    return some_dict, f"{name} healed for {recharge_hp_points} HP!"


number_of_heroes = int(input())

all_heroes = {}

for number in range(number_of_heroes):
    hero_name, hit_points, mana_points = input().split()

    if hero_name not in all_heroes.keys():
        all_heroes[hero_name] = {"HP": 0, "MP": 0}
    all_heroes[hero_name]["HP"] = int(hit_points)
    all_heroes[hero_name]["MP"] = int(mana_points)

while (current_command := input()) != "End":
    command, arguments = current_command.split(' - ', 1)
    message = ''

    if command == 'CastSpell':
        hero_name, mp_needed, spell_name = arguments.split(' - ')
        all_heroes, message = cast_spell(all_heroes, hero_name, int(mp_needed), spell_name)

    elif command == 'TakeDamage':
        hero_name, damage, attacker = arguments.split(' - ')
        all_heroes, message = take_damage(all_heroes, hero_name, int(damage), attacker)

    elif command == 'Recharge':
        hero_name, amount = arguments.split(' - ')
        all_heroes, message = recharge(all_heroes, hero_name, int(amount))

    elif command == 'Heal':
        hero_name, amount = arguments.split(' - ')
        all_heroes, message = heal(all_heroes, hero_name, int(amount))

    print(message)

for hero, hero_data in all_heroes.items():
    current_hp = hero_data["HP"]
    current_mp = hero_data["MP"]
    print(f"{hero}\n  HP: {current_hp}\n  MP: {current_mp}")
