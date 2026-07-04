def is_correct_data(some_dict: dict, some_contest: str, some_password: str) -> bool:
    for contest_name, check_password in some_dict.items():
        if contest_name == some_contest and some_password == check_password:
            return True
    return False


def calculate_total_points(data: dict) -> tuple[str, int]:
    winner = ''
    total_points = 0

    for student_name, points_in_course in data.items():
        current_total = 0
        for course, current_points in points_in_course.items():
            current_total += current_points
        if current_total > total_points:
            total_points = current_total
            winner = student_name
    return winner, total_points


contests_passwords = {}

while (current_command := input()) != "end of contests":
    contest, password = current_command.split(':')

    contests_passwords[contest] = password

students_submissions = {}

while (current_command := input()) != "end of submissions":
    contest, password, user_name, points = current_command.split('=>')
    points = int(points)

    if is_correct_data(contests_passwords, contest, password):
        if user_name not in students_submissions:
            students_submissions[user_name] = {}
        if contest not in students_submissions[user_name]:
            students_submissions[user_name][contest] = 0
        students_submissions[user_name][contest] = max(students_submissions[user_name][contest], points)

best_student, total = calculate_total_points(students_submissions)

print(f"Best candidate is {best_student} with total {total} points.")
print("Ranking:")
for student, course_points in sorted(students_submissions.items(), key=lambda x: x[0]):
    print(f"{student}")
    for course_name, points in sorted(course_points.items(), key=lambda x: -x[1]):
        print(f"#  {course_name} -> {points}")
