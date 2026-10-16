SIZE = 8

chess_board = []

k_row, k_col = 0, 0

queens = []
for row in range(SIZE):
    chess_board.append(input().split())
    for col in range(SIZE):
        if chess_board[row][col] == "K":
            k_row, k_col = row, col
        elif chess_board[row][col] == "Q":
            queens.append((row, col))

ALL_MOVES = {
    "horizontally_left": (0, -1),
    "horizontally_right": (0, 1),
    "vertically_up": (-1, 0),
    "vertically_down": (1, 0),
    "prime_up": (-1, -1),
    "prime_down": (1, 1),
    "secondary_up": (-1, 1),
    "secondary_down": (1, -1),
}

attacked_queens = []
for queen in queens:
    q_row, q_col = queen
    for move in ALL_MOVES.values():
        is_found = False
        q_ini_row, q_ini_col = q_row, q_col
        while True:
            q_new_row = q_ini_row + move[0]
            q_new_col = q_ini_col + move[1]

            if not (0 <= q_new_row < SIZE and 0 <= q_new_col < SIZE):
                break

            cell = chess_board[q_new_row][q_new_col]

            if cell == "Q":
                break

            if cell == "K":
                is_found = True
                attacked_queens.append((q_row, q_col))
                break

            q_ini_row, q_ini_col = q_new_row, q_new_col

        if is_found:
            break

if attacked_queens:
    for queen in attacked_queens:
        print(f"[{queen[0]}, {queen[1]}]")
else:
    print("The king is safe!")
