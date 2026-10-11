from collections import deque

armor_due = deque(int(num) for num in input().split(','))
strike_stack = list(map(int, input().split(',')))

killed_monsters = 0
while armor_due and strike_stack:
    curr_armor = armor_due.popleft()
    curr_strike = strike_stack.pop()

    if curr_strike >= curr_armor:
        curr_strike -= curr_armor
        killed_monsters += 1
        if curr_strike > 0:
            if strike_stack:
                strike_stack[-1] += curr_strike
            else:
                strike_stack.append(curr_strike)
    else:
        curr_armor -= curr_strike
        if curr_armor > 0:
            armor_due.append(curr_armor)

print("All monsters have been killed!") if not armor_due else None
print("The soldier has been defeated.") if not strike_stack else None
print(f"Total monsters killed: {killed_monsters}")
