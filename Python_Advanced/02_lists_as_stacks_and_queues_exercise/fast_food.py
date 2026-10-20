from collections import deque

food = int(input())
orders = deque(int(order) for order in input().split())

print(max(orders))

while orders:
    if orders[0] <= food:
        food -= orders.popleft()
    else:
        print(f"Orders left: {' '.join(map(str, orders))}")
        break

else:
    print("Orders complete")