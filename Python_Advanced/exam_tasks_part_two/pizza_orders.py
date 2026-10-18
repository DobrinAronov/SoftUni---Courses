from collections import deque

pizza_orders_dqu = deque(int(num) for num in input().split(', '))
employees_stack = [int(num) for num in input().split(', ')]

MAX_ORDERS = 10
total_pizzas = 0

while pizza_orders_dqu and employees_stack:
    if pizza_orders_dqu[0] <= 0 or pizza_orders_dqu[0] > MAX_ORDERS:
        pizza_orders_dqu.popleft()
        continue

    order = pizza_orders_dqu.popleft()
    employee = employees_stack.pop()

    if order <= employee:
        total_pizzas += order
    else:
        total_pizzas += employee
        pizza_orders_dqu.appendleft(order - employee)

if not pizza_orders_dqu:
    print(f"All orders are successfully completed!\n"
          f"Total pizzas made: {total_pizzas}\n"
          f"Employees: {', '.join(map(str, employees_stack))}")
else:
    print(f"Not all orders are completed.\n"
          f"Orders left: {', '.join(map(str, pizza_orders_dqu))}")