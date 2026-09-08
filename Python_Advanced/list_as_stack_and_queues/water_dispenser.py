from collections import deque

quantity_of_water = int(input())
people_queue = deque()

while (command := input()) != "Start":
    people_queue.append(command)

while (command := input()) != "End":

    if command.isdigit():
        client = people_queue.popleft()
        if quantity_of_water >= int(command):
            quantity_of_water -= int(command)
            print(f"{client} got water")
        else:
            print(f"{client} must wait")

    elif command.startswith("refill "):
        quantity_of_water += int(command.split()[1])

print(f"{quantity_of_water} liters left")
