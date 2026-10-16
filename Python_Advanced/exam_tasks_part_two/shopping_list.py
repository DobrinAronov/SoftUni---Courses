def shopping_list(budget: float, **product_data) -> str:
    if budget < 100:
        return "You do not have enough budget."

    bought_products = {}
    for product, product_info in product_data.items():
        price, quantity = product_info
        total_price = price * quantity
        if budget >= total_price:
            if product not in bought_products:
                bought_products[product] = 0
            bought_products[product] += total_price
            budget -= total_price

        if len(bought_products) == 5:
            break

    output = []
    for product, total in bought_products.items():
        output.append(f"You bought {product} for {total:.2f} leva.")

    return '\n'.join(output)


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
