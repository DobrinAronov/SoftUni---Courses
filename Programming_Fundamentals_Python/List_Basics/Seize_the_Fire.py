fires_in_cells = input().split('#')
water = int(input())

total_effort = 0.00
extinguished_cells = []

high = range(81, 125 + 1)
medium = range(51, 80 + 1)
low = range(1, 50 + 1)

for fire in fires_in_cells:
    is_valid = False
    fire = fire.split(' = ')
    fire_level, cell_value = fire[0], int(fire[1])

    if fire_level == 'High':
        if cell_value in high:
            is_valid = True

    elif fire_level == 'Medium':
        if cell_value in medium:
            is_valid = True

    elif fire_level == 'Low':
        if cell_value in low:
            is_valid = True

    if is_valid:
        if water >= cell_value:
            water -= cell_value
            extinguished_cells.append(cell_value)
            total_effort += cell_value * 0.25

total_fire = sum(extinguished_cells)

print("Cells:")
for cell in extinguished_cells:
    print(f" - {cell}")

print(f"Effort: {total_effort:.2f}\nTotal Fire: {total_fire}")
