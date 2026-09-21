def check_for_attack_knight(matrix: list[list], knights_list: list, moves: list, size):
    max_attack = 0
    max_row, max_col = 0, 0

    for k_row, k_col in knights_list:
        knight_attack = 0
        for dr, dc in moves:
            new_row = k_row + dr
            new_col = k_col + dc
            if not (0 <= new_row < size and 0 <= new_col < size):
                continue
            else:
                if matrix[new_row][new_col] == "K":
                    knight_attack += 1
        if knight_attack > max_attack:
            max_attack = knight_attack
            max_row, max_col = k_row, k_col

    return max_attack, max_row, max_col


matrix_size = int(input())

chessboard = []

knights = []

for row in range(matrix_size):
    current_row = list(input())
    for col in range(matrix_size):
        if current_row[col] == "K":
            knights.append((row, col))
    chessboard.append(current_row)

knight_moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]

num_of_attack, m_row, m_col = (
    check_for_attack_knight(chessboard, knights, knight_moves, matrix_size))

remove_knights = 0
while num_of_attack > 0:
    chessboard[m_row][m_col] = "0"
    knights.remove((m_row, m_col))

    remove_knights += 1
    num_of_attack, m_row, m_col = (
        check_for_attack_knight(chessboard, knights, knight_moves, matrix_size))

print(remove_knights)
