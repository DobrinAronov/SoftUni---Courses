import re


def find_all_locations(some_string: str) -> list:
    locations = []

    pattern = r"(=|\/)(?P<location>[A-Z][A-Za-z]{2,})\1"
    destinations = re.finditer(pattern, locations_on_the_map)
    for match in destinations:
        location = match.group('location')
        locations.append(location)
    return locations


locations_on_the_map = input()

all_locations = find_all_locations(locations_on_the_map)

print(f"Destinations: {', '.join(all_locations)}")
travel_points = sum([len(place) for place in all_locations])
print(f"Travel Points: {travel_points}")
