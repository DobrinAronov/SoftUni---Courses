matrix = [[int(num) for num in input().split()] for line in range(int(input()))]

while (current_command := input()) != "END":
    command, row, col, value = current_command.split()
    row, col, value = int(row), int(col), int(value)

    if not (0 <= row < len(matrix) and 0 <= col < len(matrix)):
        print("Invalid coordinates")
    else:
        if command == "Add":
            matrix[row][col] += value
        elif command == "Subtract":
            matrix[row][col] -= value

[print(*row) for row in matrix]