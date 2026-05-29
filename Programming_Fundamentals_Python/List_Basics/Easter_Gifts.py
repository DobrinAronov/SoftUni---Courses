gifts = input().split()

while (current_command := input()) != 'No Money':
    current_command = current_command.split()
    command = current_command[0]
    gift = current_command[1]

    if command == "OutOfStock":
        if gift in gifts:
            for index in range(len(gifts)):
                if gifts[index] == gift:
                    gifts[index] = None

    elif command == "Required":
        index = int(current_command[2])
        if index in range(len(gifts)):
            gifts[index] = gift

    elif command == "JustInCase":
        gifts.pop()
        gifts.append(gift)

result = [gift for gift in gifts if gift is not None]
print(' '.join(result))
