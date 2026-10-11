SIZE = int(input())
initial_money = 100
PENALTY = 200
PROFIT = 100

board = []

g_row, g_col = 0, 0

for row in range(SIZE):
    board.append(list(input()))
    for col in range(SIZE):
        if board[row][col] == "G":
            board[row][col] = "-"
            g_row, g_col = row, col

ALL_DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

is_lost = False
while (command := input()) != "end":

    new_row = g_row + ALL_DIRECTIONS[command][0]
    new_col = g_col + ALL_DIRECTIONS[command][1]

    if not (0 <= new_row < SIZE and 0 <= new_col < SIZE):
        is_lost = True
        break

    g_row, g_col = new_row, new_col
    cell = board[new_row][new_col]

    if cell == "J":
        initial_money += 100000
        print("You win the Jackpot!")
        print(f"End of the game. Total amount: {initial_money}$")
        board[new_row][new_col] = "-"
        break
    elif cell == "P":
        board[new_row][new_col] = "-"
        initial_money -= PENALTY
        if initial_money <= 0:
            is_lost = True
            break
    elif cell == "W":
        initial_money += PROFIT
        board[new_row][new_col] = "-"

else:
    print(f"End of the game. Total amount: {initial_money}$")

if is_lost:
    print("Game over! You lost everything!")

if initial_money > 0:
    board[g_row][g_col] = "G"
    [print(*row, sep='') for row in board]
