SIZE = 7
first_player_score = second_player_score = 501
first_throws = second_throws = 0

first_player, second_player = input().split(', ')

dartboard = [input().split() for _ in range(SIZE)]

turn = 0
while True:
    row, col = map(int, input().strip('()').split(', '))

    turn += 1

    if turn % 2 != 0:
        current_player = first_player
        first_throws += 1
    else:
        current_player = second_player
        second_throws += 1

    if not (0 <= row < SIZE and 0 <= col < SIZE):
        continue

    cell = dartboard[row][col]
    current_throws = first_throws if turn % 2 != 0 else second_throws

    if cell == "B":
        print(f"{current_player} won the game with {current_throws} throws!")
        break

    if cell.isdigit():
        if current_player == first_player:
            first_player_score -= int(cell)
        else:
            second_player_score -= int(cell)

    elif cell == "D" or cell == "T":
        sum_all_corners = sum([int(dartboard[row][0]), int(dartboard[row][SIZE - 1]),
                               int(dartboard[0][col]), int(dartboard[SIZE - 1][col])])
        if cell == "D":
            if current_player == first_player:
                first_player_score -= sum_all_corners * 2
            else:
                second_player_score -= sum_all_corners * 2

        elif cell == "T":
            if current_player == first_player:
                first_player_score -= sum_all_corners * 3
            else:
                second_player_score -= sum_all_corners * 3

    if first_player_score <= 0 or second_player_score <= 0:
        print(f"{current_player} won the game with {current_throws} throws!")
        break
