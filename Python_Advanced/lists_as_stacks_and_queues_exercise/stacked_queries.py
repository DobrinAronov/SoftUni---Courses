stack = []

number_of_lines = int(input())

functions = {
    "1" : lambda x: stack.append(int(x)),
    "2" : lambda: stack.pop() if stack else None,
    "3" : lambda: print(max(stack)) if stack else None,
    "4" : lambda: print(min(stack)) if stack else None
}

for _ in range(number_of_lines):
    current_command = input().split()
    functions[current_command[0]](*current_command[1:])
stack.reverse()
print(*reversed(stack), sep=', ')