from collections import deque

bees = deque(int(bee) for bee in input().split())
nectar = [int(n) for n in input().split()]
process = deque(input().split())

operators = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y if y != 0 else 0
}

total_honey = 0
while bees and nectar:
    curr_bee = bees[0]
    curr_nectar = nectar[-1]

    if curr_nectar >= curr_bee:
        honey = abs(operators[process.popleft()](bees.popleft(), nectar.pop()))
        total_honey += honey
    else:
        nectar.pop()

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")