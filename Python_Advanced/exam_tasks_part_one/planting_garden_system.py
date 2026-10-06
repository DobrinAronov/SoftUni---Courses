def plant_garden(garden_space: float, *args, **planting_requests) -> str:
    allowed_plants = dict(args)
    planted_plants = {}
    is_all_planted = True

    for plant_name, quantity in sorted(planting_requests.items()):
        if plant_name not in allowed_plants:
            continue

        space_per_plant = allowed_plants[plant_name]
        max_possible_plants = int(garden_space / space_per_plant)
        planted_pieces = min(quantity, max_possible_plants)

        if planted_pieces > 0:
            planted_plants[plant_name] = planted_pieces
            garden_space -= space_per_plant * planted_pieces

        if planted_pieces < quantity:
            is_all_planted = False

    output = []

    if is_all_planted:
        output.append(f"All plants were planted! Available garden space: {garden_space:.1f} sq meters.")
    else:
        output.append("Not enough space to plant all requested plants!")

    output.append("Planted plants:")
    for plant, pieces in sorted(planted_plants.items()):
        output.append(f"{plant}: {pieces}")

    return '\n'.join(output)


print(plant_garden(20.0, ("rose", 2.0), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, sunflower=5))
