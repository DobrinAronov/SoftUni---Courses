def check_rows(matrix: list[list], sign: str) -> bool:
    search_sign = f" {sign} "

    for row in matrix:
        if row.count(search_sign) == len(matrix):
            return True
    return False


def check_columns(matrix: list[list], sign: str) -> bool:
    search_sign = f" {sign} "

    for col in range(len(matrix)):
        count = 0
        for row in range(len(matrix)):
            if matrix[row][col] == search_sign:
                count += 1
        if count == len(matrix):
            return True
    return False


def check_diagonals(matrix: list[list], sign: str) -> bool:
    search_sign = f" {sign} "

    prime_count = 0
    secondary_count = 0
    for idx in range(len(matrix)):
        if matrix[idx][idx] == search_sign:
            prime_count += 1
        if matrix[idx][-1 - idx] == search_sign:
            secondary_count += 1
    if prime_count == len(matrix) or secondary_count == len(matrix):
        return True
    return False


def check_for_winner(matrix: list[list], sign: str) -> bool:
    if check_rows(matrix, sign) or check_columns(matrix, sign) or check_diagonals(matrix, sign):
        return True
    return False


def print_board(matrix: list[list]):
    print()
    for row in matrix:
        print('|' + '|'.join(row) + '|')
    print()


first_player = input("Please, enter the name of the first player: ")
second_player = input("Please, enter the name of the second player: ")
first_sign = ''
second_sign = ''

while True:

    first_sign = input(f"\n{first_player}, would you like to play with 'X' or 'O'?").upper()
    if first_sign not in "XO":
        print(f"{first_player}, you need to choose between 'X' and 'O' if you want to play.")
        continue
    else:
        second_sign = "X" if first_sign == "O" else "O"
        print(f"{second_player}, you will play with {second_sign}")
        break

print("\nThis is the numeration of the board\n")
board_view = [
    ['| 1 | 2 | 3 |'],
    ['| 4 | 5 | 6 |'],
    ['| 7 | 8 | 9 |'],
]

[print(*row) for row in board_view]

board = [['   '] * 3 for row in range(3)]

mapper = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2)
}

turn = 1
while turn <= 9:

    current_player = first_player if turn % 2 != 0 else second_player
    current_sign = first_sign if turn % 2 != 0 else second_sign

    try:
        current_number = int(input(f"\n{current_player}, please enter a digit between [1 - 9]"))

    except ValueError:
        print("You must enter an integer.")
        continue

    if not (1 <= current_number <= 9):
        print(f"{current_player}, you must enter a digit between 1 and 9")
        continue

    b_row, b_col = mapper[current_number]

    if board[b_row][b_col] != '   ':
        print(f"{current_player}, this position is occupied! Try to play on another position")
        continue

    board[b_row][b_col] = f" {current_sign} "
    print_board(board)

    if turn >= 5 and check_for_winner(board, current_sign):
        winner = current_player
        loser = second_player if winner == first_player else first_player

        print(f"\nCongratulations {current_player}, you are the winner!\n"
              f"Sorry {loser}, but you lost this game")
        break

    turn += 1

else:
    print("\nDraw, no winner.")
