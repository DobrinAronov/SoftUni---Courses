from collections import deque

times_dqu = deque(int(num) for num in input().split())
tasks_stack = [int(num) for num in input().split()]

RUBBER_DUCKS = {
    "Darth Vader Ducky": range(0, 61),
    "Thor Ducky": range(61, 121),
    "Big Blue Rubber Ducky": range(121, 181),
    "Small Yellow Rubber Ducky": range(181, 241)
}

HIGHEST_RANGE = 240
collected_ducks = {"Darth Vader Ducky": 0, "Thor Ducky": 0,
                   "Big Blue Rubber Ducky": 0, "Small Yellow Rubber Ducky": 0}

while times_dqu and tasks_stack:
    time = times_dqu.popleft()
    task = tasks_stack.pop()
    result = time * task

    if result > HIGHEST_RANGE:
        tasks_stack.append(task - 2)
        times_dqu.append(time)
    else:
        for duck_type, points in RUBBER_DUCKS.items():
            if result in points:
                collected_ducks[duck_type] += 1
                break

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for duck, count in collected_ducks.items():
    print(f"{duck}: {count}")
