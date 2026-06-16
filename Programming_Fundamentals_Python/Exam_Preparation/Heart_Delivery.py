def hard_delivery(current_position: int, lst: list, some_length: int) -> tuple:
    current_position += length
    if current_position not in range(len(lst)):
        current_position = 0
    if lst[current_position] > 0:
        lst[current_position] -= 2
        if lst[current_position] == 0:
            return current_position, lst, f"Place {current_position} has Valentine's day."
        return current_position, lst, ''
    return current_position, lst, f"Place {current_position} already had Valentine's day."


neighborhood = [int(element) for element in input().split('@')]
cupid_last_position = 0

while (current_command := input()) != "Love!":

    command_split = current_command.split()
    length = int(command_split[1])

    cupid_last_position, neighborhood, message = hard_delivery(cupid_last_position, neighborhood, length)
    if message:
        print(message)

print(f"Cupid's last position was {cupid_last_position}.")

if sum(neighborhood) == 0:
    print("Mission was successful.")
else:
    count_did_not_celebrated = 0
    for house in neighborhood:
        if house > 0:
            count_did_not_celebrated += 1
    print(f"Cupid has failed {count_did_not_celebrated} places.")
