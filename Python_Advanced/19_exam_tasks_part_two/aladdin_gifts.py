from collections import deque

materials_stack = [int(num) for num in input().split()]
magic_dqu = deque(int(num) for num in input().split())

wedding_present = {
    "Gemstone": range(100, 200),
    "Porcelain Sculpture": range(200, 300),
    "Gold": range(300, 400),
    "Diamond Jewellery": range(400, 500),
}

MIN_RESULT = 100
MAX_RESULT = 499

crafting_gifts = {}
while materials_stack and magic_dqu:
    material = materials_stack.pop()
    magic = magic_dqu.popleft()
    result = material + magic

    if result < MIN_RESULT:
        if result % 2 == 0:
            result = material * 2 + magic * 3
        else:
            result *= 2

    elif result > MAX_RESULT:
        result //= 2

    for present, points in wedding_present.items():
        if result in points:
            if present not in crafting_gifts:
                crafting_gifts[present] = 0
            crafting_gifts[present] += 1
            break

if ("Gemstone" in crafting_gifts.keys() and "Porcelain Sculpture" in crafting_gifts.keys()) or \
        ("Gold" in crafting_gifts.keys() and "Diamond Jewellery" in crafting_gifts.keys()):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials_stack:
    print(f"Materials left: {', '.join(map(str, materials_stack))}")
if magic_dqu:
    print(f"Magic left: {', '.join(map(str, magic_dqu))}")
if crafting_gifts:
    for present, amount in sorted(crafting_gifts.items()):
        print(f"{present}: {amount}")
