import re


def extract_furniture_information(some_string: str):
    pattern = r">>([A-Z]*[a-z]*)<<(\d+\.?\d+)!(\d+)"
    return re.finditer(pattern, some_string)


total_cost = 0

furniture_info = input()

print("Bought furniture:")

while furniture_info != 'Purchase':
    matches = extract_furniture_information(furniture_info)
    for match in matches:
        if match:
            name = match.group(1)
            price = match.group(2)
            quantity = match.group(3)
            print(name)
            total_cost += float(price) * int(quantity)

    furniture_info = input()

print(f"Total money spend: {total_cost:.2f}")
