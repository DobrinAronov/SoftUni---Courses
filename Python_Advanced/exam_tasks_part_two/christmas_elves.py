from collections import deque

elf_energy_dqu = deque(int(num) for num in input().split())
materials_stack = [int(num) for num in input().split()]

MIN_ENERGY = 5
COOKIE = 1

total_energy = 0
number_of_toys = 0
turn = 0
is_not_enough_energy = False

while elf_energy_dqu and materials_stack:
    energy = elf_energy_dqu.popleft()
    if energy < MIN_ENERGY:
        continue

    turn += 1
    material = materials_stack.pop()

    if turn % 3 == 0:
        if energy >= material * 2:
            total_energy += material * 2
            energy -= material * 2
            if turn % 5 == 0:
                # The elf does not eat a cookie
                # and does not make toys.
                elf_energy_dqu.append(energy)
            else:
                number_of_toys += 2
                # elf eat cookie and increase energy by 1
                elf_energy_dqu.append(energy + COOKIE)
        else:
            is_not_enough_energy = True

    elif turn % 5 == 0:
        if energy >= material:
            total_energy += material
            # elf don't eat a cookie !!!
            elf_energy_dqu.append(energy - material)
        else:
            is_not_enough_energy = True

    else:
        if energy >= material:
            total_energy += material
            number_of_toys += 1
            # elf eat cookie and increase energy by 1
            elf_energy_dqu.append(energy - material + COOKIE)
        else:
            is_not_enough_energy = True

    if is_not_enough_energy:
        # elf drink hot chocolate which doubles his energy
        elf_energy_dqu.append(energy * 2)
        materials_stack.append(material)
        is_not_enough_energy = False

print(f"Toys: {number_of_toys}")
print(f"Energy: {total_energy}")
print(f"Elves left: {', '.join(map(str, elf_energy_dqu))}")\
    if elf_energy_dqu else None
print(f"Boxes left: {', '.join(map(str, materials_stack))}")\
    if materials_stack else None