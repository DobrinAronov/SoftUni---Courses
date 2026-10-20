from collections import deque

bowls_stack = [int(num) for num in input().split(', ')]
customers_dqe = deque(int(num) for num in input().split(', '))

while bowls_stack and customers_dqe:
    bowl = bowls_stack.pop()
    customer = customers_dqe.popleft()

    if bowl == customer:
        continue
    if bowl > customer:
        bowls_stack.append(bowl - customer)
    elif customer > bowl:
        customers_dqe.appendleft(customer - bowl)

if not customers_dqe:
    print("Great job! You served all the customers.")
    if bowls_stack:
        print(f"Bowls of ramen left: {', '.join(map(str, bowls_stack))}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(map(str, customers_dqe))}")
