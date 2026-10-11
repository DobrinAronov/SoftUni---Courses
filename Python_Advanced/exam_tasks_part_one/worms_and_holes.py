from collections import deque

worms_stack = [int(num) for num in input().split()]
holes_dqu = deque(int(num) for num in input().split())

worm_count = len(worms_stack)
matches = 0
while worms_stack and holes_dqu:
    curr_worm = worms_stack.pop()
    curr_hole = holes_dqu.popleft()

    if curr_hole == curr_worm:
        matches += 1
    else:
        curr_worm -= 3
        if curr_worm > 0:
            worms_stack.append(curr_worm)

if matches > 0:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if not worms_stack and worm_count == matches:
    print("Every worm found a suitable hole!")
elif not worms_stack and worm_count > matches:
    print("Worms left: none")
elif worms_stack:
    print(f"Worms left: {', '.join(map(str, worms_stack))}")

if not holes_dqu:
    print("Holes left: none")
elif holes_dqu:
    print(f"Holes left: {', '.join(map(str, holes_dqu))}")
