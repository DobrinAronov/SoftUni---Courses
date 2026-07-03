def check_the_stock(lst: list, checking_products: list) -> list:
    stock = {}
    messages = []

    for idx in range(0, len(lst), 2):
        stock[lst[idx]] = int(lst[idx + 1])

    for product in checking_products:
        if product in stock.keys():
            messages.append(f"We have {stock[product]} of {product} left")
        else:
            messages.append(f"Sorry, we don't have {product}")
    return messages


data = input().split()
client_require = input().split()

messages_for_print = check_the_stock(data, client_require)
for message in messages_for_print:
    print(message)