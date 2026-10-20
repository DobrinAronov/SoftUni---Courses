def accommodate_new_pets(capacity: int, max_weight: float, *pets_info) -> str:
    accommodated_pets = {}
    unaccommodated_pets = False

    for pet_type, pet_weight in pets_info:
        if capacity == 0:
            unaccommodated_pets = True
            break
        if pet_weight > max_weight:
            continue

        if pet_type not in accommodated_pets:
            accommodated_pets[pet_type] = 0
        accommodated_pets[pet_type] += 1
        capacity -= 1

    output = []
    if not unaccommodated_pets:
        output.append(f"All pets are accommodated! Available capacity: {capacity}.")
    else:
        output.append("You did not manage to accommodate all pets!")
    output.append("Accommodated pets:")
    for pet_type, quantity in sorted(accommodated_pets.items()):
        output.append(f"{pet_type}: {quantity}")

    return '\n'.join(output)


print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
