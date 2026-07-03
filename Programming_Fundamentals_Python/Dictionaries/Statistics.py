def statistics() -> list:
    messages = []
    products_info = {}

    while (current_command := input()) != 'statistics':
        product, quantity = current_command.split(': ')
        quantity = int(quantity)

        if product not in products_info.keys():
            products_info[product] = quantity
        else:
            products_info[product] += quantity

    messages.append("Products in stock:")

    for food, quantity in products_info.items():
        messages.append(f"- {food}: {quantity}")

    count_all_products = len(products_info)
    sum_all_quantities = sum(products_info.values())
    messages.append(f"Total Products: {count_all_products}")
    messages.append(f"Total Quantity: {sum_all_quantities}")
    return messages


messages_for_print = statistics()
for message in messages_for_print:
    print(message)
