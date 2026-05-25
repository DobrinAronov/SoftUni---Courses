fires_in_cells  = input().split('#')
water = int(input())

total_effort = 0.00
extinguished_cells = []

for fire in fires_in_cells:
    is_valid = False
    fire = fire.split(' = ')
    fire_level = fire[0]
    cell_value = int(fire[1])

    if  fire_level == 'High':
        if  81 <= cell_value <= 125:
            is_valid = True

    elif    fire_level == 'Medium':
        if  51 <= cell_value <= 80:
            is_valid = True

    elif    fire_level == 'Low':
        if  1 <= cell_value <= 50:
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