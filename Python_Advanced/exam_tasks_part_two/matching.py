from collections import deque

male_stack = [int(num) for num in input().split()]
female_dqu = deque(int(num) for num in input().split())

matches = 0
while male_stack and female_dqu:
    if male_stack[-1] <= 0 or female_dqu[0] <= 0 or \
            male_stack[-1] % 25 == 0 or female_dqu[0] % 25 == 0:

        if male_stack[-1] <= 0 or male_stack[-1] % 25 == 0:
            male_stack.pop()
        if female_dqu[0] <= 0 or female_dqu[0] % 25 == 0:
            female_dqu.popleft()
        continue

    male = male_stack.pop()
    female = female_dqu.popleft()

    if male == female:
        matches += 1
    else:
        male_stack.append(male - 2)

print(f"Matches: {matches}")

if male_stack:
    print(f"Males left: {', '.join(map(str, reversed(male_stack)))}")
else:
    print("Males left: none")
if female_dqu:
    print(f"Females left: {', '.join(map(str, female_dqu))}")
else:
    print("Females left: none")
