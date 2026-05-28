all_movies = []

for _ in range(3):
    current_game = [int(number) for number in input().split()]
    all_movies.append(current_game)

winner = ''
# Checking The rows
for row in all_movies:
    if row == [1, 1, 1]:
        winner = 'First'
        break
    elif row == [2, 2, 2]:
        winner = 'Second'
        break

# Checking The Columns

if  all_movies[0][0] == 1 and all_movies[1][0] == 1 and all_movies[2][0] == 1:
    winner = 'First'

elif  all_movies[0][0] == 2 and all_movies[1][0] == 2 and all_movies[2][0] == 2:
    winner = 'Second'

if all_movies[0][1] == 1 and all_movies[1][1] == 1 and all_movies[2][1] == 1:
    winner = 'First'

elif all_movies[0][1] == 2 and all_movies[1][1] == 2 and all_movies[2][1] == 2:
    winner = 'Second'

if all_movies[0][2] == 1 and all_movies[1][2] == 1 and all_movies[2][2] == 1:
    winner = 'First'

elif all_movies[0][2] == 2 and all_movies[1][2] == 2 and all_movies[2][2] == 2:
    winner = 'Second'

# Checking The diagonals
if  all_movies[0][0] == 1 and all_movies[1][1] == 1 and all_movies[2][2] == 1:
    winner = 'First'                                                                # Check left diagonal
elif  all_movies[0][0] == 2 and all_movies[1][1] == 2 and all_movies[2][2] == 2:
    winner = 'Second'

if  all_movies[0][2] == 1 and all_movies[1][1] == 1 and all_movies[2][0] == 1:
    winner = 'First'                                                                # Check right diagonal
elif  all_movies[0][2] == 2 and all_movies[1][1] == 2 and all_movies[2][0] == 2:
    winner = 'Second'

if winner == 'First':
    print("First player won")

elif    winner == 'Second':
    print("Second player won")
else:
    print("Draw!")