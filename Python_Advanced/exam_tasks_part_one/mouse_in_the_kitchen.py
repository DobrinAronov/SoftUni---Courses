ROWS, COLUMNS = map(int, input().split(','))

m_row, m_col = 0, 0

cupboard_area = []
cheeses_count = 0

for row in range(ROWS):
    cupboard_area.append(list(input()))
    for col in range(COLUMNS):
        if cupboard_area[row][col] == "M":
            m_row, m_col = row, col
            cupboard_area[row][col] = "*"
        elif cupboard_area[row][col] == "C":
            cheeses_count += 1

ALL_DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while (command := input()) != "danger":

    new_row = m_row + ALL_DIRECTIONS[command][0]
    new_col = m_col + ALL_DIRECTIONS[command][1]

    if not (0 <= new_row < ROWS and 0 <= new_col < COLUMNS):
        print("No more cheese for tonight!")
        break

    cell = cupboard_area[new_row][new_col]

    if cell == "@":
        continue

    m_row, m_col = new_row, new_col

    if cell == "T":
        print("Mouse is trapped!")
        break

    elif cell == "C":
        cupboard_area[new_row][new_col] = "*"
        cheeses_count -= 1
        if cheeses_count == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            break

else:
    if cheeses_count > 0:
        print("Mouse will come back later!")

cupboard_area[m_row][m_col] = "M"

[print(*row, sep='') for row in cupboard_area]
