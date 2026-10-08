from collections import deque

money_stack = [int(num) for num in input().split()]
prices_of_food_dqu = deque(map(int, input().split()))

foods = 0
while money_stack and prices_of_food_dqu:

    curr_money = money_stack.pop()
    curr_price = prices_of_food_dqu.popleft()

    if curr_money == curr_price:
        foods += 1

    elif curr_money > curr_price:
        curr_money -= curr_price
        foods += 1
        if money_stack:
            money_stack[-1] += curr_money
        else:
            money_stack.append(curr_money)

if foods >= 4:
    print(f"Gluttony of the day! Henry ate {foods} foods.")
elif 1 < foods < 4:
    print(f"Henry ate: {foods} foods.")
elif foods == 1:
    print(f"Henry ate: {foods} food.")
elif foods == 0:
    print("Henry remained hungry. He will try next weekend again.")
