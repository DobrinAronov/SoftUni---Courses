def grocery_store(**kwargs: dict) -> str:
    output = []

    recipe = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    for product, quantity in recipe:
        output.append(f"{product}: {quantity}")

    return '\n'.join(output)


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))