from collections import deque

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

points = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

presents = {}

while materials and magic:
    result = magic[0] * materials[-1]

    if result in points:
        magic.popleft()
        materials.pop()
        if points[result] not in presents:
            presents[points[result]] = 0
        presents[points[result]] += 1

    elif result > 0:
        magic.popleft()
        materials[-1] += 15
    elif result < 0:
        result = magic.popleft() + materials.pop()
        materials.append(result)
    else:
        if magic[0] == 0:
            magic.popleft()
        if materials[-1] == 0:
            materials.pop()

if ("Doll" in presents and "Wooden train" in presents) or ("Teddy bear" in presents and "Bicycle" in presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

print(f"Materials left: {', '.join(map(str, reversed(materials)))}") if materials else None
print(f"Magic left: {', '.join(map(str, magic))}") if magic else None

for toy_name, quantity in sorted(presents.items()):
    print(f"{toy_name}: {quantity}")
