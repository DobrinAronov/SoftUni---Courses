def rest(data: dict, num: int):
    add_power = 0
    if data['energy'] < 100:
        add_power += min(num, 100 - data['energy'])
        data['energy'] += add_power

    return f"You gained {add_power} energy.\nCurrent energy: {data['energy']}."


def order(data: dict, num: int):
    if data['energy'] >= 30:
        data['coins'] += num
        data['energy'] -= 30
        return f"You earned {num} coins."
    else:
        data['energy'] += 50
        return "You had to rest!"


def ingredient(item: str, data: dict, num: int):
    if data['coins'] >= num:
        data['coins'] -= num
        return False, f"You bought {item}."
    else:
        return True, f"Closed! Cannot afford {item}."


working_day_events = input().split('|')

resources = {
    'coins': 100,
    'energy': 100
}

for event in working_day_events:
    have_break = False
    event = event.split('-')
    event_name, number = event[0], int(event[1])

    if event_name == 'rest':
        print(rest(resources, number))

    elif event_name == 'order':
        print(order(resources, number))

    else:
        stop, message = ingredient(event_name, resources, number)
        print(message)

        if stop:
            break

else:
    print("Day completed!")
    print(f"Coins: {resources['coins']}")
    print(f"Energy: {resources['energy']}")