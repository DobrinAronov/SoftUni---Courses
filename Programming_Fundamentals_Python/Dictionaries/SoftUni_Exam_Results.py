def adding_students_points(base: dict, all_sub: dict, name: str, some_course: str, some_points: int) -> None:
    if some_course not in base:
        base[some_course] = {}
    if name not in base[some_course]:
        base[some_course][name] = some_points
    else:
        if base[some_course][name] < points:
            base[some_course][name] = points

    if some_course not in all_sub:
        all_sub[some_course] = []
    all_sub[some_course].append(name)


def banned(base: dict, name: str) -> None:
    for dictionary in base.values():
        if name in dictionary.keys():
            dictionary[name] = 'banned'


exam_results = {}
all_submissions = {}

while (current_command := input()) != "exam finished":

    command_split = current_command.split('-')

    if len(command_split) == 2:
        user_name = command_split[0]
        banned(exam_results, user_name)

    else:
        user_name, language, points = command_split[0], command_split[1], int(command_split[2])
        adding_students_points(exam_results, all_submissions, user_name, language, points)

print("Results:")
for course, students_grades in exam_results.items():
    for student, grade in students_grades.items():
        if grade != 'banned':
            print(f"{student} | {grade}")

print("Submissions:")
for course, students_submissions in all_submissions.items():
    print(f"{course} - {len(students_submissions)}")
