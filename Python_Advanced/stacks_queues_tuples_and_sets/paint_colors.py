from collections import deque

substrings = deque(input().split())

main_colors = {"red", "yellow", "blue"}

secondary_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"}
}

found_colors = []

while substrings:
    first_sub = substrings.popleft()
    last_sub = substrings.pop() if substrings else ''

    for color in (first_sub + last_sub, last_sub + first_sub):
        if color in main_colors or color in secondary_colors:
            found_colors.append(color)
            break
    else:
        if len(first_sub) > 1:
            substrings.insert(len(substrings) // 2, first_sub[:-1])
        if len(last_sub) > 1:
            substrings.insert(len(substrings) // 2, last_sub[:-1])

valid_colors = []
for color in found_colors:
    if color in main_colors:
        valid_colors.append(color)
    elif color in secondary_colors:
        if all(c in found_colors for c in secondary_colors[color]):
            valid_colors.append(color)

print(valid_colors)