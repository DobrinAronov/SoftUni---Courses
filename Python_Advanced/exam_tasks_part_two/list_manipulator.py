from collections import deque


def list_manipulator(input_list: list, *commands) -> list:
    input_list = deque(input_list)
    command = commands[:2]
    numbers = commands[2:]

    if command == ("add", "beginning"):
        for num in reversed(numbers):
            input_list.appendleft(num)

    elif command == ("add", "end"):
        input_list += numbers

    elif command == ("remove", "beginning"):
        if numbers:
            for _ in range(int(numbers[0])):
                input_list.popleft()
        else:
            if input_list:
                input_list.popleft()

    elif command == ("remove", "end"):
        if numbers:
            for _ in range(int(numbers[0])):
                input_list.pop()
        else:
            if input_list:
                input_list.pop()

    return list(input_list)


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
