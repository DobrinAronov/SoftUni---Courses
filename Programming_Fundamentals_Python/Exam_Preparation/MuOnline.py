def potion(health: int, bitcoins: int, some_value: int) -> tuple:
    added_health = min(some_value, 100 - health)
    health += added_health
    return health, bitcoins, f"You healed for {added_health} hp.\nCurrent health: {health} hp."


def chest(health: int, bitcoins: int, some_value: int) -> tuple:
    bitcoins += some_value
    return health, bitcoins, f"You found {some_value} bitcoins."


def fight_with_monster(health: int, some_monster: str, monster_power: int) -> tuple:
    health -= monster_power
    if health > 0:
        return False, health, f"You slayed {some_monster}."
    return True, health, f"You died! Killed by {some_monster}."


all_commands = {

    "potion": potion,
    "chest": chest,
    "fight_with_monster": fight_with_monster

}

initial_health = 100
initial_bitcoins = 0

dungeon_rooms = input().split('|')

for room in range(len(dungeon_rooms)):
    command, value = dungeon_rooms[room].split()
    value = int(value)

    if command == "potion" or command == "chest":
        initial_health, initial_bitcoins, message = all_commands[command](initial_health, initial_bitcoins, value)
    else:
        monster = command
        stop, initial_health, message = all_commands["fight_with_monster"](initial_health, monster, value)
        if stop:
            print(message)
            print(f"Best room: {room + 1}")
            break

    print(message)
else:
    print(f"You've made it!\nBitcoins: {initial_bitcoins}\nHealth: {initial_health}")
