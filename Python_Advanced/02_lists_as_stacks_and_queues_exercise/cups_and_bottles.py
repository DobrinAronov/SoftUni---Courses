from collections import deque

cups = deque(list(map(int, input().split())))
bottles = list(map(int, input().split()))

wasted_water = 0

while cups and bottles:
    if cups[0] < bottles[-1]:
        wasted_water += bottles.pop() - cups.popleft()
    else:
        cups[0] -= bottles.pop()
        if cups[0] == 0:
            cups.popleft()

if bottles:
    print("Bottles:", *bottles)
if cups:
    print("Cups:", *cups)
print(f"Wasted litters of water: {wasted_water}")