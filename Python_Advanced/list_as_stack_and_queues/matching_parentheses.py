<<<<<<< HEAD
expression = input()

parentheses = []

for i in range(len(expression)):
    if expression[i] == '(':
        parentheses.append(i)
    elif expression[i] == ')':
        start_idx = parentheses.pop()
        end_idx = i + 1
=======
expression = input()

parentheses = []

for i in range(len(expression)):
    if expression[i] == '(':
        parentheses.append(i)
    elif expression[i] == ')':
        start_idx = parentheses.pop()
        end_idx = i + 1
>>>>>>> b6c84b4 (Add Python Advanced stack and queues)
        print(expression[start_idx: end_idx])