items_to_buy_prices = input().split('|')
budget = float(input())

ticket_price = 150
spent_money = 0

prices = {
    'Clothes': 50.00,
    'Shoes': 35.00,
    'Accessories': 20.50
}

list_bought_items = []

for item_price in items_to_buy_prices:
    item_price = item_price.split('->')
    item, price = item_price[0], float(item_price[1])
    if price <= prices[item]:
        if budget >= price:
            budget -= price
            spent_money += price
            list_bought_items.append(price)

profit_after_sell = [price_sell * 1.4 for price_sell in list_bought_items]

for index in range(len(profit_after_sell)):
    if index == len(profit_after_sell) - 1:
        print(f"{profit_after_sell[index]:.2f}")
    else:
        print(f"{profit_after_sell[index]:.2f}", end=' ')

total_profit_after_sell = round(sum(profit_after_sell), 2)
profit = total_profit_after_sell - spent_money
print(f"Profit: {profit:.2f}")

if (budget + total_profit_after_sell) >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")
