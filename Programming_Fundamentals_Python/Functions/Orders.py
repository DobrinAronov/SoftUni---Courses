def calculate_total_price(data: dict, product: str, count: int) -> float:
        total_price = data[product] * count
        return total_price


product_prices = {
    'coffee' : 1.50,
    'water' : 1.00,
    'coke' : 1.40,
    'snacks' : 2.00
}

product_name = input()
quantity = int(input())

result = calculate_total_price(product_prices, product_name, quantity)
print(f"{result:.2f}")