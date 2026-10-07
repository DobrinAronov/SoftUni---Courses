from collections import deque

bees_dqu = deque(int(num) for num in input().split())
bee_eaters_stack = [int(num) for num in input().split()]

while bees_dqu and bee_eaters_stack:
    group_bees = bees_dqu.popleft()
    group_bee_eaters = bee_eaters_stack.pop()

    if group_bee_eaters > group_bees / 7:
        group_bee_eaters -= group_bees // 7
        bee_eaters_stack.append(group_bee_eaters)

    elif group_bee_eaters < group_bees / 7:
        group_bees -= group_bee_eaters * 7
        bees_dqu.append(group_bees)

print("The final battle is over!")
if not bees_dqu and not bee_eaters_stack:
    print("But no one made it out alive!")
if bees_dqu:
    print(f"Bee groups left: {', '.join(map(str, bees_dqu))}")
if bee_eaters_stack:
    print(f"Bee-eater groups left: {', '.join(map(str, bee_eaters_stack))}")
