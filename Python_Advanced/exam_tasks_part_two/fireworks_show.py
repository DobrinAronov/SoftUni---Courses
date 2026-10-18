from collections import deque

effects_dqu = deque(int(num) for num in input().split(', '))
power_stack = [int(num) for num in input().split(', ')]

collected_effects = {"Palm Fireworks": 0, "Willow Fireworks": 0, "Crossette Fireworks": 0}
while effects_dqu and power_stack:
    if effects_dqu[0] <= 0 or power_stack[-1] <= 0:
        if effects_dqu[0] <= 0:
            effects_dqu.popleft()
        if power_stack[-1] <= 0:
            power_stack.pop()

        continue

    effect = effects_dqu.popleft()
    power = power_stack.pop()
    result = effect + power

    if result % 3 == 0 and result % 5 != 0:
        collected_effects["Palm Fireworks"] += 1

    elif result % 5 == 0 and result % 3 != 0:
        collected_effects["Willow Fireworks"] += 1

    elif result % 5 == 0 and result % 3 == 0:
        collected_effects["Crossette Fireworks"] += 1

    else:
        effects_dqu.append(effect - 1)
        power_stack.append(power)

    if all([value >= 3 for value in collected_effects.values()]):
        print("Congrats! You made the perfect firework show!")
        break

else:
    print("Sorry. You can't make the perfect firework show.")

if effects_dqu:
    print(f"Firework Effects left: {', '.join(map(str, effects_dqu))}")
if power_stack:
    print(f"Explosive Power left: {', '.join(map(str, power_stack))}")

for effect_name, count in collected_effects.items():
    print(f"{effect_name}: {count}")
