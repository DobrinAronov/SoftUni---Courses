def even_odd_filter(**kwargs: dict) -> dict:
    for key, value in kwargs.items():
        if key == "even":
            kwargs[key] = [num for num in value if num % 2 == 0]
        else:
            kwargs[key] = [num for num in value if num % 2 != 0]

    sorted_dict = dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))
    return sorted_dict


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
