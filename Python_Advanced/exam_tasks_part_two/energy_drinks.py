from collections import deque

MAX_CAFFEINE = 300
total_coffeine = 0

caffeine_stack = [int(num) for num in input().split(', ')]
drinks_dqu = deque([int(num) for num in input().split(', ')])

while caffeine_stack and drinks_dqu:
    caffeine = caffeine_stack.pop()
    drink = drinks_dqu.popleft()
    result = caffeine * drink

    if result + total_coffeine <= MAX_CAFFEINE:
        total_coffeine += result
    else:
        drinks_dqu.append(drink)
        if total_coffeine - 30 > 0:
            total_coffeine -= 30

if drinks_dqu:
    print(f"Drinks left: {', '.join(map(str, drinks_dqu))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_coffeine} mg caffeine.")
