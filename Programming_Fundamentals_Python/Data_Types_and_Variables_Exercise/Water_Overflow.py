number_of_lines = int(input())

tank_capacity = 0

for number in range(number_of_lines):
    pour_tank_litters = int(input())
    if  pour_tank_litters + tank_capacity <= 255:
        tank_capacity += pour_tank_litters
    else:
        print("Insufficient capacity!")

print(tank_capacity)