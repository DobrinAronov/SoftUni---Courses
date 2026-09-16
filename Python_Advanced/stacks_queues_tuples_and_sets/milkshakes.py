from collections import deque

chocolates = [int(c) for c in input().split(', ')]
milk = deque(int(m) for m in input().split(', '))

count_milkshake = 0
while chocolates and milk:
    if chocolates[-1] <= 0:
        chocolates.pop()
    if milk[0] <= 0:
        milk.popleft()

    if milk and chocolates and milk[0] > 0 and chocolates[-1] > 0:
        curr_chocolate = chocolates.pop()
        curr_milk = milk.popleft()

        if curr_chocolate == curr_milk:
            count_milkshake += 1
            if count_milkshake == 5:
                print("Great! You made all the chocolate milkshakes needed!")
                break
        else:
            milk.append(curr_milk)
            curr_chocolate -= 5
            if curr_chocolate > 0:
                chocolates.append(curr_chocolate)

else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join(map(str, chocolates))}")
else:
    print("Chocolate: empty")

if milk:
    print(f"Milk: {', '.join(map(str, milk))}")
else:
    print("Milk: empty")
