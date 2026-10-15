SIZE = 8

RANKS = {0: "8", 1: "7", 2: "6", 3: "5", 4: "4", 5: "3", 6: "2", 7: "1"}

COLUMNS = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}

WHITE_MOVES = {
    "up_left": (-1, -1),
    "up_right": (-1, 1),
    "up": (-1, 0)
}

BLACK_MOVES = {
    "down_left": (1, -1),
    "down_right": (1, 1),
    "down": (1, 0)
}

w_row, w_col = 0, 0
b_row, b_col = 0, 0

chessboard = []

for row in range(SIZE):
    chessboard.append(input().split())
    for col in range(SIZE):
        if chessboard[row][col] == "w":
            w_row, w_col = row, col
        elif chessboard[row][col] == "b":
            b_row, b_col = row, col

turn = 0
while True:
    turn += 1

    current_figure = "w" if turn % 2 != 0 else "b"
    won_figure = ''

    if current_figure == "w":
        for coordinates in WHITE_MOVES.values():
            dr, dc = coordinates[0], coordinates[1]
            w_new_row, w_new_col = w_row + dr, w_col + dc

            if not (0 <= w_new_col < SIZE):
                continue

            if chessboard[w_new_row][w_new_col] == "b":
                won_figure = "White"
                print(f"Game over! {won_figure} "
                      f"win, capture on {COLUMNS[w_new_col] + RANKS[w_new_row]}.")
                exit()
        else:
            chessboard[w_row][w_col] = "-"
            dr, dc = WHITE_MOVES["up"]
            w_row, w_col = w_row + dr, w_col + dc
            chessboard[w_row][w_col] = current_figure

    elif current_figure == "b":
        for coordinates in BLACK_MOVES.values():
            dr, dc = coordinates[0], coordinates[1]
            b_new_row, b_new_col = b_row + dr, b_col + dc

            if not (0 <= b_new_col < SIZE):
                continue

            if chessboard[b_new_row][b_new_col] == "w":
                won_figure = "Black"
                print(f"Game over! {won_figure} "
                      f"win, capture on {COLUMNS[b_new_col] + RANKS[b_new_row]}.")
                exit()
        else:
            chessboard[b_row][b_col] = "-"
            dr, dc = BLACK_MOVES["down"]
            b_row, b_col = b_row + dr, b_col + dc
            chessboard[b_row][b_col] = current_figure

    if w_row == 0 or b_row == SIZE - 1:
        won_figure = "White" if w_row == 0 else "Black"
        if current_figure == "w":
            print(f"Game over! {won_figure} pawn is promoted"
                  f" to a queen at {COLUMNS[w_col] + RANKS[w_row]}.")
        else:
            print(f"Game over! {won_figure} pawn is promoted"
                  f" to a queen at {COLUMNS[b_col] + RANKS[b_row]}.")
        break
