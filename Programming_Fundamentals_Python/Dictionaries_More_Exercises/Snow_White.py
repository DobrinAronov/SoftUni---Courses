dwarfs_info = {}

while (dwarf_data := input()) != "Once upon a time":
    name, hat_color, physics = dwarf_data.split(' <:> ')
    physics = int(physics)

    if name not in dwarfs_info:
        dwarfs_info[name] = {}
        dwarfs_info[name][hat_color] = physics
    elif hat_color not in dwarfs_info[name]:
        dwarfs_info[name][hat_color] = physics
    else:
        dwarfs_info[name][hat_color] = max(dwarfs_info[name][hat_color], physics)

dwarfs_info_tuples = []

for key, value in dwarfs_info.items():
    for inner_key, inner_value in value.items():
        row = (key, inner_key, inner_value)
        dwarfs_info_tuples.append(row)

color_count = {}

for info in dwarfs_info_tuples:
    if info[1] not in color_count:
        color_count[info[1]] = 1
    else:
        color_count[info[1]] += 1

dwarfs_sorted = sorted(dwarfs_info_tuples, key=lambda x: (-x[2], -color_count[x[1]]))

for elements in dwarfs_sorted:
    print(f"({elements[1]}) {elements[0]} <-> {elements[2]}")
