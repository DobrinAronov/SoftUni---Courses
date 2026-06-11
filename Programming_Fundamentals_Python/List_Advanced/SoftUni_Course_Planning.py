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
    name_exercise_1 = f"{title_1}-Exercise"
    name_exercise_2 = f"{title_2}-Exercise"

    if title_1 in some_list and title_2 in some_list:
        index_lesson_1 = some_list.index(title_1)
        index_lesson_2 = some_list.index(title_2)
        # Swap the lesson's title
        some_list[index_lesson_1], some_list[index_lesson_2] = some_list[index_lesson_2], some_list[index_lesson_1]

    if name_exercise_1 in some_list:
        index_exercise_1 = some_list.index(title_1) + 1
        some_list.remove(name_exercise_1)
        some_list.insert(index_exercise_1, name_exercise_1)

    if name_exercise_2 in some_list:
        index_exercise_2 = some_list.index(title_2) + 1
        some_list.remove(name_exercise_2)
        some_list.insert(index_exercise_2, name_exercise_2)

    return some_list


def exercise(some_list: list[str], title: str) -> list:
    exercise_name = f"{title}-Exercise"

    if title in some_list and exercise_name not in some_list:
        index_title = some_list.index(title)
        some_list.insert(index_title + 1, exercise_name)

    elif title not in some_list:
        some_list.append(title)
        some_list.append(exercise_name)

    return some_list


schedule_lessons_exercises = input().split(', ')

while (current_command := input()) != 'course start':

    split_command = current_command.split(':')
    command = split_command[0]
    lesson_title = split_command[1]

    if command == "Add":
        schedule_lessons_exercises = add(schedule_lessons_exercises, lesson_title)

    elif command == "Insert":
        index = int(split_command[2])
        schedule_lessons_exercises = insert(schedule_lessons_exercises, lesson_title, index)

    elif command == "Remove":
        schedule_lessons_exercises = remove(schedule_lessons_exercises, lesson_title)

    elif command == "Swap":
        lesson_title_second = split_command[2]
        schedule_lessons_exercises = swap(schedule_lessons_exercises, lesson_title, lesson_title_second)

    elif command == "Exercise":
        schedule_lessons_exercises = exercise(schedule_lessons_exercises, lesson_title)

for index in range(len(schedule_lessons_exercises)):
    print(f"{index + 1}.{schedule_lessons_exercises[index]}")
