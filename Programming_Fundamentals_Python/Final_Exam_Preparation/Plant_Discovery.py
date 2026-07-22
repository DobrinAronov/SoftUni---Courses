def rate(plants_dict: dict, rest_part: str) -> tuple[dict, str]:
    plant_name, rating = rest_part.split(' - ')
    if plant_name in plants_dict.keys():
        plants_dict[plant_name]['rating'].append(float(rating))
        return plants_dict, ''
    return plants_dict, 'error'


def update(plants_dict: dict, rest_part: str) -> tuple[dict, str]:
    plant_name, new_rarity = rest_part.split(' - ')
    if plant_name in plants_dict.keys():
        plants_dict[plant_name]['rarity'] = new_rarity
        return plants_dict, ''
    return plants_dict, 'error'


def reset(plants_dict: dict, rest_part: str) -> tuple[dict, str]:
    plant_name = rest_part
    if plant_name in plants_dict.keys():
        plants_dict[plant_name]['rating'] = []
        return plants_dict, ''
    return plants_dict, 'error'


all_plants = {}

all_commands = {
    'Rate': rate,
    'Update': update,
    'Reset': reset
}

number_of_information_lines = int(input())

for line in range(number_of_information_lines):
    plant, rarity = input().split('<->')
    if plant not in all_plants:
        all_plants[plant] = {'rarity': rarity, 'rating': []}
    else:
        all_plants[plant]['rarity'] = rarity

while (current_command := input()) != "Exhibition":
    command, other_part = current_command.split(': ')
    all_plants, message = all_commands[command](all_plants, other_part)
    if message:
        print(message)

print("Plants for the exhibition:")
for plant, info in all_plants.items():
    average_rating = 0.00
    if info['rating']:
        average_rating = sum(info['rating']) / len(info['rating'])
    print(f"- {plant}; Rarity: {info['rarity']}; Rating: {average_rating:.2f}")
