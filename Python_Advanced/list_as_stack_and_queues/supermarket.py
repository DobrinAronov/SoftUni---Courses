<<<<<<< HEAD
from collections import deque

customers = deque()

while (command := input()) != "End":

    if command != "Paid":
        customers.append(command)

    else:
        for _ in range(len(customers)):
            print(customers.popleft())

=======
from collections import deque

customers = deque()

while (command := input()) != "End":

    if command != "Paid":
        customers.append(command)

    else:
        for _ in range(len(customers)):
            print(customers.popleft())

>>>>>>> b6c84b4 (Add Python Advanced stack and queues)
print(f"{len(customers)} people remaining.")