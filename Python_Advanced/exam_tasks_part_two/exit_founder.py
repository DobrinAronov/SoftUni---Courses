first_player, second_player = input().split(', ')

SIZE = 6

maze = [input().split() for _ in range(SIZE)]

turn = 0
players_hit_wall = []
while True:
    coordinates = input().split(', ')
    row, col = \
        int(coordinates[0].lstrip('(')), int(coordinates[1].rstrip(')'))
    turn += 1

    current_player = first_player if turn % 2 != 0 else second_player

    if current_player in players_hit_wall:
        players_hit_wall.remove(current_player)
        continue

    cell = maze[row][col]

    if cell == "E":
        print(f"{current_player} found the Exit and wins the game!")
        break

    if cell == "T":
        winner = first_player if current_player == second_player else second_player
        print(f"{current_player} is out of the game! The winner is {winner}.")
        break

    if cell == "W":
        players_hit_wall.append(current_player)
        print(f"{current_player} hits a wall and needs to rest.")
