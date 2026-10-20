def shop_from_grocery_list(budget: int, *grocery_list) -> str:
    shopping = []
    shopping_list = grocery_list[0]
    price_list = grocery_list[1:]

    for product, price in price_list:
        if product not in shopping_list:
            continue

        if budget >= price:
            if product not in shopping:
                budget -= price
                shopping.append(product)
        else:
            break

    if len(shopping) == len(shopping_list):
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    missing_product = [product for product in shopping_list if product not in shopping]
    return f"You did not buy all the products. Missing products: {', '.join(missing_product)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
