def product_info(products_dict: dict, product: str, cost: float, number: int) -> dict:
    if product not in products_dict:
        products_dict[product] = {
            'price': cost,
            'quantity': number
        }
    else:
        if products_dict[product]['price'] != cost:
            products_dict[product]['price'] = cost
        products_dict[product]['quantity'] += number
    return products_dict


orders = {}

while (current_command := input()) != "buy":
    name, price, quantity = current_command.split()
    price, quantity = float(price), int(quantity)

    orders = product_info(orders, name, price, quantity)

for product_name, inner_dict in orders.items():
    total_price = inner_dict['price'] * inner_dict['quantity']
    print(f"{product_name} -> {total_price:.2f}")
