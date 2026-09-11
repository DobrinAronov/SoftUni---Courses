numbers_of_command = int(input())

parking_lot = set()

for _ in range(numbers_of_command):
    action, number = input().split(', ')

    if action == "IN":
        parking_lot.add(number)
    elif action == "OUT":
        if number in parking_lot:
            parking_lot.remove(number)

if not parking_lot:
    print("Parking Lot is Empty")
else:
    print(*parking_lot, sep="\n")