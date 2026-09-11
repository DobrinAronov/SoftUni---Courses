parentheses = input()

open_parentheses = []

for char in parentheses:
    if char in ["(", "[", "{"]:
        open_parentheses.append(char)
    else:
        if not open_parentheses:
            print("NO")
            break
        else:
            if open_parentheses[-1] == "(" and char == ")":
                open_parentheses.pop()
            elif open_parentheses[-1] == "[" and char == "]":
                open_parentheses.pop()
            elif open_parentheses[-1] == "{" and char == "}":
                open_parentheses.pop()
            else:
                print("NO")
                break
else:
    print("YES")