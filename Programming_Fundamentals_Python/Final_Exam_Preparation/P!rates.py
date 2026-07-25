def plunder(city_info: dict, part_for_split: str) -> tuple[dict, str]:
    town, people, city_gold = part_for_split.split('=>')
    people, city_gold = int(people), int(city_gold)

    city_info[town]['population'] -= people
    city_info[town]['gold'] -= city_gold
    if city_info[town]['population'] == 0 or city_info[town]['gold'] == 0:
        del city_info[town]
        return city_info, (f"{town} plundered! {city_gold} gold stolen, {people} citizens killed."
                           f"\n{town} has been wiped off the map!")
    return city_info, f"{town} plundered! {city_gold} gold stolen, {people} citizens killed."


def prosper(city_info: dict, part_for_split: str) -> tuple[dict, str]:
    town, gold_amount = part_for_split.split('=>')
    gold_amount = int(gold_amount)
    if gold_amount < 0:
        return city_info, "Gold added cannot be a negative number!"
    city_info[town]['gold'] += gold_amount
    total_gold = city_info[town]['gold']
    return city_info, f"{gold_amount} gold added to the city treasury. {town} now has {total_gold} gold."


cities = {}

while (targeted_city := input()) != "Sail":
    city, population, gold = targeted_city.split("||")

    if city not in cities.keys():
        cities[city] = {'population': 0, 'gold': 0}
    cities[city]['population'] += int(population)
    cities[city]['gold'] += int(gold)

while (events := input()) != "End":
    command, arguments = events.split('=>', 1)
    message = ''

    if command == 'Plunder':
        cities, message = plunder(cities, arguments)
    elif command == 'Prosper':
        cities, message = prosper(cities, arguments)

    print(message)

if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city_name, city_status in cities.items():
        number_of_people = city_status['population']
        gold_kg = city_status['gold']
        print(f"{city_name} -> Population: {number_of_people} citizens, Gold: {gold_kg} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
