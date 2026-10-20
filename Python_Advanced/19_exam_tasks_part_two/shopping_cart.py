def shopping_cart(*meals_product: tuple[str, str]) -> str:
    soup = 3
    pizza = 4
    dessert = 2
    bought_meals = {"Soup": [], "Pizza": [], "Dessert": []}

    for pair in meals_product:
        if pair == "Stop":
            break

        meal, product = pair
        if meal == 'Soup' and len(bought_meals["Soup"]) < soup:
            if product not in bought_meals["Soup"]:
                bought_meals["Soup"].append(product)

        elif meal == 'Pizza' and len(bought_meals["Pizza"]) < pizza:
            if product not in bought_meals["Pizza"]:
                bought_meals["Pizza"].append(product)

        elif meal == 'Dessert' and len(bought_meals["Dessert"]) < dessert:
            if product not in bought_meals["Dessert"]:
                bought_meals["Dessert"].append(product)

    output = []

    if all([products == [] for products in bought_meals.values()]):
        output.append("No products in the cart!")
    else:
        for meal_type, products in sorted(bought_meals.items(), key=lambda x: (-len(x[1]), x[0])):
            output.append(f"{meal_type}:")
            for product in sorted(products):
                output.append(f" - {product}")

    return '\n'.join(output)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
