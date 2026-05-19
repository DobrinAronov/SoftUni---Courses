lost_fights_count = int(input())

gladiator_equipment = {
    'helmet_price' : float(input()),
    'sword_price' : float(input()),
    'shield_price' : float(input()),
    'armor_price' : float(input())
    }

expenses = 0
count_shield_breaks = 0

for lost_battle in range(1, lost_fights_count + 1):

    if  lost_battle % 2 == 0 and lost_battle % 3 == 0:
        expenses += gladiator_equipment['helmet_price'] + \
                    gladiator_equipment['sword_price'] + \
                    gladiator_equipment['shield_price']

        count_shield_breaks += 1
        if  count_shield_breaks % 2 == 0:
            expenses += gladiator_equipment['armor_price']

    elif  lost_battle % 2 == 0:
        expenses += gladiator_equipment['helmet_price']

    elif  lost_battle % 3 == 0:
        expenses += gladiator_equipment['sword_price']

print(f"Gladiator expenses: {expenses:.2f} aureus")