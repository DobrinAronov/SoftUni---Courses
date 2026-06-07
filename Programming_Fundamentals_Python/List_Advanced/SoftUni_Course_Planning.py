def add(some_list: list[str], title: str) -> list:
    if title not in some_list:
        some_list.append(title)
    return some_list


def insert(some_list: list[str], title: str, idx: int) -> list:
    if title not in some_list:
        some_list.insert(idx, title)
    return some_list


def remove(some_list: list[str], title: str) -> list:
    if title in some_list:
        some_list.remove(title)
    if f"{title}-Exercise" in some_list:
        some_list.remove(f"{title}-Exercise")
    return some_list


def swap(some_list: list[str], title_1: str, title_2: str) -> list:
    if title_1 in some_list and title_2 in some_list:
        index_lesson_1 = some_list.index(title_1)
        index_lesson_2 = some_list.index(title_2)
        some_list[index_lesson_1], some_list[index_lesson_2] = some_list[index_lesson_2], some_list[index_lesson_1]
    if f"{title_1}-Exercise" in some_list:
        index_exercise_1 = some_list.index(title_1) + 1
        some_list.remove(f"{title_1}-Exercise")
        some_list.insert(index_exercise_1, f"{title_1}-Exercise")
    if f"{title_2}-Exercise" in some_list:
        index_exercise_2 = some_list.index(title_2) + 1
        some_list.remove(f"{title_2}-Exercise")
        some_list.insert(index_exercise_2, f"{title_2}-Exercise")
    return some_list


def exercise(some_list: list[str], title: str) -> list:
    if title in some_list and f"{title}-Exercise" not in some_list:
        index_title = some_list.index(title)
        some_list.insert(index_title + 1, f"{title}-Exercise")
    elif title not in some_list:
        some_list.append(title)
        some_list.append(f"{title}-Exercise")

    return some_list


schedule_lessons_exercises = input().split(', ')

while (current_command := input()) != 'course start':

    split_command = current_command.split(':')
    command = split_command[0]

    if command == "Add":
        lesson_title = split_command[1]
        schedule_lessons_exercises = add(schedule_lessons_exercises, lesson_title)

    elif command == "Insert":
        lesson_title = split_command[1]
        index = int(split_command[2])
        schedule_lessons_exercises = insert(schedule_lessons_exercises, lesson_title, index)

    elif command == "Remove":
        lesson_title = split_command[1]
        schedule_lessons_exercises = remove(schedule_lessons_exercises, lesson_title)

    elif command == "Swap":
        lesson_title_first = split_command[1]
        lesson_title_second = split_command[2]
        schedule_lessons_exercises = swap(schedule_lessons_exercises, lesson_title_first, lesson_title_second)

    elif command == "Exercise":
        lesson_title = split_command[1]
        schedule_lessons_exercises = exercise(schedule_lessons_exercises, lesson_title)

for index in range(len(schedule_lessons_exercises)):
    print(f"{index + 1}.{schedule_lessons_exercises[index]}")
