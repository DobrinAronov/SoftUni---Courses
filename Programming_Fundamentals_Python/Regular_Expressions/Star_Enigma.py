import re


def extract_info(some_string: str):
    pattern = r"@(?P<planet_name>[A-Za-z]+)(?:[^@\-!:>]*):(?P<planet_population>\d+)(?:[^@\-!:>]*)!(?P<attack_type>[AD])!(?:[^@\-!:>]*)->(?P<soldier_count>\d+)"
    matches = re.finditer(pattern, some_string)

    name_of_planet = population = type_of_attack = soldiers = ''
    for match in matches:
        name_of_planet = match.group('planet_name')
        population = match.group('planet_population')
        type_of_attack = match.group('attack_type')
        soldiers = match.group('soldier_count')
    return name_of_planet, population, type_of_attack, soldiers


number_of_messages = int(input())

planet_data = {
    'A': [],
    'D': []
}

for num in range(number_of_messages):
    encrypt_message = input()
    count_star_letters = 0

    for symbol in encrypt_message:
        if symbol.lower() in ('s', 't', 'a', 'r'):
            count_star_letters += 1

    decrypt_message = ''
    for symbol in encrypt_message:
        decrypt_message += chr(ord(symbol) - count_star_letters)
    planet_name, planet_population, attack_type, soldier_count = extract_info(decrypt_message)
    if planet_name and planet_population and attack_type and soldier_count:
        planet_data[attack_type].append(planet_name)

for attack, planet in planet_data.items():
    if attack == 'A':
        print(f"Attacked planets: {len(planet)}")
        for name in sorted(planet):
            print(f"-> {name}")
    else:
        print(f"Destroyed planets: {len(planet)}")
        for name in sorted(planet):
            print(f"-> {name}")
