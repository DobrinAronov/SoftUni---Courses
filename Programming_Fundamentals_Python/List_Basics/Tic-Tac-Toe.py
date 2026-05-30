def check_winner(a: int, b: int, c: int):
    if a == b == c == 1:
        return 'First'
    elif a == b == c == 2:
        return 'Second'
    else:
        return None

all_rows = []

for number_of_row in range(3):
    current_row = [int(number) for number in input().split()]
    all_rows.append(current_row)

winner = ''

# Checking The rows
for row in all_rows:
    winner = check_winner(row[0], row[1], row[2])
    if winner:
        break

if not winner:
    # Checking The Columns
    for column in range(0, 3):
        winner = check_winner(all_rows[0][column], all_rows[1][column], all_rows[2][column])
        if winner:
            break

if not winner:
    winner = check_winner(all_rows[0][0], all_rows[1][1], all_rows[2][2])  # Check left diagonal
    if not winner:
        winner = check_winner(all_rows[0][2], all_rows[1][1], all_rows[2][0])  # Check right diagonal

if winner == 'First':
    print("First player won")
elif winner == 'Second':
    print("Second player won")
else:
    print("Draw!")