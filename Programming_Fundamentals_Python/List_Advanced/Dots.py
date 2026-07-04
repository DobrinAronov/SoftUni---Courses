def dots(matrix: list[list], all_moves: list[tuple[int, int]]) -> int:
    rows = len(matrix)
    columns = len(matrix[0])

    def checking_all_moves(row_: int, column_: int) -> int:
        #print(f"Влизам в {row_}, {column_}")
        current_count_of_dots = 1
        matrix[row_][column_] = 'v'

        for some_row, some_column in all_moves:
            i, j = (row_ + some_row), (column_ + some_column)
            is_coordinates_valid = (0 <= i < rows) and (0 <= j < columns)

            if is_coordinates_valid and matrix[i][j] == '.':
                current_count_of_dots += checking_all_moves(i, j)
        #print(f"Излизам от {row_}, {column_}")
        return current_count_of_dots

    max_count = 0
    for row in range(rows):
        for column in range(columns):
            if matrix[row][column] == '.':
                count = checking_all_moves(row, column)
                if count > max_count:
                    max_count = count

    return max_count


number_of_rows = int(input())

board_of_dots_and_dashes = []
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), ]

for number in range(number_of_rows):
    current_row = input().split()
    board_of_dots_and_dashes.append(current_row)

result = dots(board_of_dots_and_dashes, directions)
print(result)
