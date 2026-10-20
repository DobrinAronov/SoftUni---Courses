from collections import deque

eggs_dqu = deque(int(num) for num in input().split(', '))
paper_stack = deque(int(num) for num in input().split(', '))

BOX_SIZE = 50
filled_boxes = 0
while eggs_dqu and paper_stack:
    if eggs_dqu[0] <= 0 or eggs_dqu[0] == 13:
        if eggs_dqu[0] == 13:
            paper_stack[0], paper_stack[-1] = \
                paper_stack[-1], paper_stack[0]
        eggs_dqu.popleft()
        continue

    egg = eggs_dqu.popleft()
    paper = paper_stack.pop()
    result = egg + paper

    if result <= BOX_SIZE:
        filled_boxes += 1

if filled_boxes > 0:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

print(f"Eggs left: {', '.join(map(str, eggs_dqu))}") if eggs_dqu else None
print(f"Pieces of paper left: {', '.join(map(str, paper_stack))}") \
    if paper_stack else None
