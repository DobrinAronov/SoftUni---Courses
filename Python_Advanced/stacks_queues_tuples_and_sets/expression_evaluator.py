from functools import reduce

expression = input().split()

result = []

for char in expression:

    if char in "*+-/":

        operators = {
            "*": reduce(lambda x, y: x * y, result) if result else None,
            "+": reduce(lambda x, y: x + y, result) if result else None,
            "-": reduce(lambda x, y: x - y, result) if result else None,
            "/": reduce(lambda x, y: x // y, result) if result else None
        }

        curr_result = operators[char]
        result.clear()
        result.append(curr_result)

    else:
        result.append(int(char))

print(*result)
