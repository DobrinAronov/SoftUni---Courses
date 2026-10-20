from collections import deque

textiles_dqu = deque(int(num) for num in input().split())
medicaments_stack = [int(num) for num in input().split()]

HEALING_ITEM = {
    "Patch": 30,
    "Bandage": 40,
    "MedKit": 100,
}


MAX_RESOURCE = HEALING_ITEM["MedKit"]

collected_items = {}
while textiles_dqu and medicaments_stack:
    textile = textiles_dqu.popleft()
    medicament = medicaments_stack.pop()
    item = textile + medicament

    if item > MAX_RESOURCE:
        if "MedKit" not in collected_items:
            collected_items["MedKit"] = 0
        collected_items["MedKit"] += 1

        reminder = item - MAX_RESOURCE

        if medicaments_stack:
            medicaments_stack[-1] += reminder
        else:
            medicaments_stack.append(reminder)

    elif item in HEALING_ITEM.values():
        for name, resources in HEALING_ITEM.items():
            if item == resources:
                if name not in collected_items:
                    collected_items[name] = 0
                collected_items[name] += 1
                break

    else:
        medicaments_stack.append(medicament + 10)

if not textiles_dqu and not medicaments_stack:
    print("Textiles and medicaments are both empty.")
elif not textiles_dqu:
    print("Textiles are empty.")
elif not medicaments_stack:
    print("Medicaments are empty.")

if collected_items:
    for item_name, count in sorted(collected_items.items(), key=lambda x: (-x[1], x[0])):
        print(f"{item_name} - {count}")

print(f"Medicaments left: {', '.join(map(str, reversed(medicaments_stack)))}")\
    if medicaments_stack else None
print(f"Textiles left: {', '.join(map(str, textiles_dqu))}") if textiles_dqu else None