def get_magic_triangle(number: int) -> list[list]:
    magic_triangle = [[1], [1, 1]]

    for _ in range(number - 2):
        previous_row = magic_triangle[-1]
        next_row = [1]

        for idx in range(len(previous_row) - 1):
            next_num = previous_row[idx] + previous_row[idx + 1]
            next_row.append(next_num)

        next_row.append(1)
        magic_triangle.append(next_row)

    return magic_triangle


get_magic_triangle(5)
