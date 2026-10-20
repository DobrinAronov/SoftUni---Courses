from collections import deque

potion = {
    "Brew of Immortality": 110,
    "Essence of Resilience": 100,
    "Draught of Wisdom": 90,
    "Potion of Agility": 80,
    "Elixir of Strength": 70
}

MIN_ENERGY = 70
substances_stack = [int(num) for num in input().split(', ')]
crystal_energy_dqu = deque(int(num) for num in input().split(', '))

crafted_potions = []
while substances_stack and crystal_energy_dqu:
    substance = substances_stack.pop()
    crystal = crystal_energy_dqu.popleft()
    result = substance + crystal

    if result < MIN_ENERGY:
        crystal -= 5
        if crystal > 0:
            crystal_energy_dqu.append(crystal)
        continue

    for potion_name, energy in potion.items():
        if result == energy:
            if potion_name not in crafted_potions:
                crafted_potions.append(potion_name)
                break

    else:
        for potion_name, energy in potion.items():
            if energy < result and potion_name not in crafted_potions:
                crafted_potions.append(potion_name)

                crystal -= 20
                if crystal > 0:
                    crystal_energy_dqu.append(crystal)
                break
        else:
            crystal -= 5
            if crystal > 0:
                crystal_energy_dqu.append(crystal)
            continue

    if len(crafted_potions) == 5:
        print("Success! The alchemist has forged all potions!")
        break

else:
    print("The alchemist failed to complete his quest.")

if crafted_potions:
    print(f"Crafted potions: {', '.join(crafted_potions)}")
if substances_stack:
    print(f"Substances: {', '.join(map(str, reversed(substances_stack)))}")
if crystal_energy_dqu:
    print(f"Crystals: {', '.join(map(str, crystal_energy_dqu))}")
