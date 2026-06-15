def counter_strike(count_won: int, some_energy: int, some_distance: int) -> tuple:
    if some_energy >= some_distance:
        count_won += 1
        some_energy -= some_distance
        if count_won % 3 == 0:
            some_energy += count_won
        return count_won, some_energy, False, ''
    else:
        return (count_won, some_energy, True,
                f"Not enough energy! Game ends with {count_won} won battles and {some_energy} energy")


initial_energy = int(input())
count_won_battles = 0

command = input()

while command != "End of battle":
    distance = int(command)

    count_won_battles, initial_energy, stop, message = counter_strike(count_won_battles, initial_energy, distance)

    if stop:
        print(message)
        break

    command = input()

else:
    print(f"Won battles: {count_won_battles}. Energy left: {initial_energy}")
