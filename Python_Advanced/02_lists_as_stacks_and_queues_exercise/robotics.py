from collections import deque


def add_time(some_current_time):
    # Split hour, minutes, seconds
    hours, minutes, seconds = map(int, some_current_time.split(":"))

    # Converting current time in seconds
    total_seconds = hours * 3600 + minutes * 60 + seconds

    # Adding seconds
    total_seconds = total_seconds % (24 * 3600)
    return total_seconds


def convert_time_in_format(total_time_seconds: int):
    total_time_seconds %= 24 * 3600

    hours = total_time_seconds // 3600
    minutes = (total_time_seconds % 3600) // 60
    seconds = total_time_seconds % 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


products = deque()
robots = deque()

for robot_info in input().split(';'):
    name, time = robot_info.split('-')
    current_dict = {'Name': name, 'Time': int(time), 'Finish': 0}
    robots.append(current_dict)

start_time = input()

while (command := input()) != "End":
    product = command
    products.append(product)

add_second = 0
current_time = add_time(start_time)

while products:
    current_time += 1
    product = products[0]

    for robot in robots:
        if robot['Finish'] <= current_time:
            print(f"{robot['Name']} - {product} [{convert_time_in_format(current_time)}]")
            products.popleft()
            robot_time = robot['Time']
            robot['Finish'] = current_time + robot_time
            break
        else:
            continue

    else:
        products.rotate(-1)
