from collections import deque

customers = deque()

while (command := input()) != "End":

    if command != "Paid":
        customers.append(command)

    else:
        for _ in range(len(customers)):
            print(customers.popleft())

print(f"{len(customers)} people remaining.")