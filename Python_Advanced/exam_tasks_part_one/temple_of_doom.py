from collections import deque

tools_dqu = deque(int(num) for num in input().split())
substances_stack = [int(num) for num in input().split()]
challenges = [int(num) for num in input().split()]

while tools_dqu and substances_stack:
    tool = tools_dqu.popleft()
    substance = substances_stack.pop()
    result = tool * substance

    if result in challenges:
        challenges.remove(result)
    else:
        tools_dqu.append(tool + 1)
        substance -= 1
        if substance > 0:
            substances_stack.append(substance)

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

[print(f"Tools: {', '.join(map(str, tools_dqu))}") if tools_dqu else None]
[print(f"Substances: {', '.join(map(str, substances_stack))}") if substances_stack else None]
[print(f"Challenges: {', '.join(map(str, challenges))}") if challenges else None]
