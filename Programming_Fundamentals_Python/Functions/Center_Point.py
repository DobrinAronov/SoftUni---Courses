from math import floor, sqrt


def coordinates_closest_point(x_first: float, y_first: float, x_second: float, y_second: float) -> str:
    distance_first_point = sqrt(x_first ** 2 + y_first ** 2)
    distance_second_point = sqrt(x_second ** 2 + y_second ** 2)

    if distance_first_point < distance_second_point:
        x, y = x_first, y_first
    elif distance_second_point < distance_first_point:
        x, y = x_second, y_second
    else:
        x, y = x_first, y_first

    return f"({floor(x)}, {floor(y)})"

if __name__ == "__main__":

    x_1 = float(input())
    y_1 = float(input())
    x_2 = float(input())
    y_2 = float(input())

    print(coordinates_closest_point(x_1, y_1, x_2, y_2))
