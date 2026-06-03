from math import sqrt, floor


def coordinates_closest_point(some_tuple: tuple) -> tuple:
    distance_first_point = sqrt(some_tuple[0][0] ** 2 + some_tuple[0][1] ** 2)
    distance_second_point = sqrt(some_tuple[1][0] ** 2 + some_tuple[1][1] ** 2)
    x = y = None
    if distance_first_point <= distance_second_point:
        x, y = some_tuple[0][0], some_tuple[0][1]
    elif distance_second_point < distance_first_point:
        x, y = some_tuple[1][0], some_tuple[1][1]

    return x, y


def longer_line(x_1_frs: float, y_1_frs: float, x_2_frs: float, y_2_frs: float,
                x_1_sec: float, y_1_sec: float, x_2_sec: float, y_2_sec: float):
    x_frs_min = min(x_1_frs, x_2_frs)
    x_frs_max = max(x_1_frs, x_2_frs)
    y_frs_min = min(y_1_frs, y_2_frs)
    y_frs_max = max(y_1_frs, y_2_frs)
    x_sec_min = min(x_1_sec, x_2_sec)
    x_sec_max = max(x_1_sec, x_2_sec)
    y_sec_min = min(y_1_sec, y_2_sec)
    y_sec_max = max(y_1_sec, y_2_sec)

    distance_first_line = sqrt((x_frs_max - x_frs_min) ** 2 + (y_frs_max - y_frs_min) ** 2)
    distance_second_line = sqrt((x_sec_max - x_sec_min) ** 2 + (y_sec_max - y_sec_min) ** 2)

    coordinates_first_line = ((x_1_frs, y_1_frs), (x_2_frs, y_2_frs))
    coordinates_second_line = ((x_1_sec, y_1_sec), (x_2_sec, y_2_sec))

    if distance_first_line >= distance_second_line:
        the_longest_line = coordinates_first_line
    else:
        the_longest_line = coordinates_second_line

    closest_point = coordinates_closest_point(the_longest_line)

    if closest_point == the_longest_line[0]:
        closest_point = the_longest_line[0]
        farthest_point = the_longest_line[1]
    else:
        closest_point = the_longest_line[1]
        farthest_point = the_longest_line[0]

    x_1, y_1 = [floor(element) for element in closest_point]
    x_2, y_2 = [floor(element) for element in farthest_point]
    return f"({x_1}, {y_1})({x_2}, {y_2})"


x_1_first = float(input())
y_1_first = float(input())
x_2_first = float(input())
y_2_first = float(input())
x_1_second = float(input())
y_1_second = float(input())
x_2_second = float(input())
y_2_second = float(input())

print(longer_line(x_1_first, y_1_first, x_2_first, y_2_first, x_1_second, y_1_second, x_2_second, y_2_second))
