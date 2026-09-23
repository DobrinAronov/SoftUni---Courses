rows, cols = map(int, input().split())

matrix = [input().split() for _ in range(rows)]

while (current_command := input()) != "END":
    has_invalid_command = False

    if current_command.startswith("swap"):
        command = current_command.split()
        if len(command) == 5:
            action = command[0]
            row_1, col_1, row_2, col_2 = map(int, command[1:])
            if (0 <= row_1 < rows and 0 <= row_2 < rows
                    and 0 <= col_1 < cols and 0 <= col_2 < cols):

                matrix[row_1][col_1], matrix[row_2][col_2] = \
                    matrix[row_2][col_2], matrix[row_1][col_1]

                [print(*row) for row in matrix]

            else:
                has_invalid_command = True
        else:
            has_invalid_command = True
    else:
        has_invalid_command = True

    if has_invalid_command:
        print("Invalid input!")
