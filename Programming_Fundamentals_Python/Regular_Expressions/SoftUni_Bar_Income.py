import re

total_income = 0
while (current_string := input()) != "end of shift":
    pattern = r"%(?P<customer>[A-Z][a-z]+)%([^\|\$%\.]*)<(?P<product>\w+)>([^\|\$%\.]*)\|(?P<count>\d+)\|([^\|\$%\.\d]*)(?P<price>\d+(?:\.\d+)?)\$"
    matches = re.finditer(pattern, current_string)

    for match in matches:
        customer = match.group('customer')
        product = match.group('product')
        count = match.group('count')
        price = match.group('price')

        total_price = int(count) * float(price)
        total_income += total_price
        print(f"{customer}: {product} - {total_price:.2f}")


print(f"Total income: {total_income:.2f}")
