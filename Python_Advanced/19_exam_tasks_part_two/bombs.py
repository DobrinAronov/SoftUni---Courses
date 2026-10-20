from collections import deque

bomb_effects_dqe = deque(int(num) for num in input().split(', '))
bomb_casing_stack = [int(num) for num in input().split(', ')]

BOMBS = {
    "Datura Bombs": 40,
    "Cherry Bombs": 60,
    "Smoke Decoy Bombs": 120,
}

created_bombs = {"Datura Bombs": 0, "Cherry Bombs": 0, "Smoke Decoy Bombs": 0}
while bomb_effects_dqe and bomb_casing_stack:
    effect = bomb_effects_dqe[0]
    casing = bomb_casing_stack[-1]
    result = effect + casing

    for bomb_name, materials in BOMBS.items():
        if result == materials:
            created_bombs[bomb_name] += 1
            bomb_effects_dqe.popleft()
            bomb_casing_stack.pop()
            break
    else:
        bomb_casing_stack[-1] -= 5

    if all([value >= 3 for value in created_bombs.values()]):
        print("Bene! You have successfully filled the bomb pouch!")
        break

else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects_dqe:
    print(f"Bomb Effects: {', '.join(map(str, bomb_effects_dqe))}")
else:
    print("Bomb Effects: empty")
if bomb_casing_stack:
    print(f"Bomb Casings: {', '.join(map(str, bomb_casing_stack))}")
else:
    print("Bomb Casings: empty")

for bomb_name, count in sorted(created_bombs.items()):
    print(f"{bomb_name}: {count}")
