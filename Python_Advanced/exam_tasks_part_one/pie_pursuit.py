from collections import deque

contestants_dqu = deque(int(num) for num in input().split())
pies_stack = [int(num) for num in input().split()]

while pies_stack and contestants_dqu:
    curr_pie = pies_stack.pop()
    curr_contestant = contestants_dqu.popleft()

    if curr_contestant >= curr_pie:
        curr_contestant -= curr_pie
        if curr_contestant > 0:
            contestants_dqu.append(curr_contestant)

    elif curr_pie > curr_contestant:
        curr_pie -= curr_contestant
        if curr_pie == 1 and len(pies_stack) > 1:
            pies_stack[-1] += curr_pie
        else:
            pies_stack.append(curr_pie)

if not pies_stack and contestants_dqu:
    print("We will have to wait for more pies to be baked!")
    print(f"Contestants left: {', '.join(map(str, contestants_dqu))}")

elif not pies_stack and not contestants_dqu:
    print("We have a champion!")

elif not contestants_dqu and pies_stack:
    print(f"Our contestants need to rest!")
    print(f"Pies left: {', '.join(map(str, pies_stack))}")
