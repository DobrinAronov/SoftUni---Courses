def bakery(lst: list) -> dict:
    food_data = {}
    for idx in range(0, len(lst), 2):
        food_data[lst[idx]] = int(lst[idx + 1])
    return food_data


data = input().split()
print(bakery(data))