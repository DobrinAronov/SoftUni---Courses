def calculate_pig_resources(some_food: float, some_hay: float, some_cover: float, weight: float) -> tuple:
    for day in range(1, 31):
        some_food -= 300
        if day % 2 == 0:
            some_hay -= some_food * 0.05
        if day % 3 == 0:
            some_cover -= weight / 3
        if some_food <= 0 or some_hay <= 0 or some_cover <= 0:
            return True, some_food, some_hay, some_cover

    return False, some_food, some_hay, some_cover


food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
pig_wight = float(input()) * 1000

stop, food, hay, cover = calculate_pig_resources(food, hay, cover, pig_wight)

if stop:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {food/1000:.2f}, Hay: {hay/1000:.2f}, Cover: {cover/1000:.2f}.")
