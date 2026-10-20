from collections import deque


def stock_availability(cupcakes: list, *args):
    cupcakes = deque(cupcakes)
    command = args[0]

    if command == "delivery":
        cupcakes.extend(args[1:])

    elif command == "sell":
        if len(args) == 1:
            cupcakes.popleft()
        elif isinstance(args[1], int):
            for _ in range(args[1]):
                cupcakes.popleft()
        else:
            for flavor in args[1:]:
                if flavor in cupcakes:
                    new_list = []
                    for cupcake in cupcakes:
                        if cupcake != flavor:
                            new_list.append(cupcake)
                    cupcakes = deque(new_list)

    return list(cupcakes)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
