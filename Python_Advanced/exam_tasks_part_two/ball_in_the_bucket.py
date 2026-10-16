SIZE = 6

board = [input().split() for _ in range(SIZE)]

PRIZE = {
    "Football": range(100, 200),
    "Teddy Bear": range(200, 300),
    "Lego Construction Set": range(300, 999999)
}

MIN_POINTS = 100
total_points = 0
collected_prize = ''

for hit in range(3):
    row, col = input().split(', ')
    row, col = int(row.lstrip('(')), int(col.rstrip(')'))

    if not (0 <= row < SIZE and 0 <= col < SIZE) or \
            board[row][col] != "B":
        continue

    if board[row][col] == "B":
        board[row][col] = '.'
        for r in range(SIZE):
            if board[r][col].isdigit():
                total_points += int(board[r][col])

for prize_name, prize_range in PRIZE.items():
    if total_points in prize_range:
        collected_prize = prize_name

if collected_prize:
    print(f"Good job! You scored {total_points} points, and you've won {collected_prize}.")
else:
    needed_points = MIN_POINTS - total_points
    print(f"Sorry! You need {needed_points} points more to win a prize.")
