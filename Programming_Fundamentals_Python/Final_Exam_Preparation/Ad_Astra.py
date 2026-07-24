import re


text = input()
pattern = r"([|#])(?P<food_name>[A-Za-z\s]+)\1(?P<expiration_date>\d{2}/\d{2}/\d{2})\1(?P<calories>\d{1,5})\1"

matches = list(re.finditer(pattern, text))
total_calories = sum([int(match.group('calories')) for match in matches])
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")

for match in matches:
    food_name = match.group('food_name')
    expiration_date = match.group('expiration_date')
    calories = match.group('calories')
    print(f"Item: {food_name}, Best before: {expiration_date}, Nutrition: {calories}")