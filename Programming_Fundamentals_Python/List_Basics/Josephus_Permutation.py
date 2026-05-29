people_in_circle = input().split()
number = int(input())

executed = []
step = number - 1

index = 0

while people_in_circle:

    index += step

    while index >= len(people_in_circle):
        index = index - len(people_in_circle)

    executed.append(people_in_circle[index])
    del people_in_circle[index]

print(f"[{','.join(executed)}]")
