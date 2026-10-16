from collections import deque

customers_dqe = deque(int(num) for num in input().split(', '))
taxis_stack = [int(num) for num in input().split(', ')]

total_time = 0
while customers_dqe and taxis_stack:
    customer = customers_dqe.popleft()
    taxi = taxis_stack.pop()

    if taxi >= customer:
        total_time += customer
    else:
        customers_dqe.appendleft(customer)

if not customers_dqe:
    print(f"All customers were driven to their destinations\n"
          f"Total time: {total_time} minutes")
else:
    print(f"Not all customers were driven to their destinations\n"
          f"Customers left: {', '.join(map(str, customers_dqe))}")
