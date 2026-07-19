import re


def health_calculate(some_string: str) -> int:
    pattern = r"[^0-9\+\-\*\/\.]"
    matches = re.findall(pattern, some_string)

    health = sum([ord(symbol) for symbol in matches])
    return health


def damage_calculate(some_string: str) -> float:
    pattern = r"\-?\d+(?:\.\d+)?"
    matches = re.findall(pattern, some_string)

    total_damage = sum(float(number) for number in matches)
    damage_multiplier = 1

    for symbol in some_string:
        if symbol == '*':
            damage_multiplier *= 2
        elif symbol == '/':
            damage_multiplier /= 2
    return total_damage * damage_multiplier


all_demons = [name.strip() for name in input().split(',')]

for demon_name in sorted(all_demons):
    if demon_name:
        health_points = health_calculate(demon_name)
        damage_points = damage_calculate(demon_name)
        print(f"{demon_name} - {health_points} health, {damage_points:.2f} damage")
