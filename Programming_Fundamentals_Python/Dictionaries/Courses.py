def adding_student_in_course(base: dict, course: str, name: str) -> dict:
    if course not in base:
        base[course] = [name]
    else:
        base[course].append(name)
    return base


courses_students = {}

while (current_command := input()) != "end":
    course_name, student_name = current_command.split(" : ")

    courses_students = adding_student_in_course(courses_students, course_name, student_name)

for course, students in courses_students.items():
    print(f"{course}: {len(students)}")
    for student_name in students:
        print(f"-- {student_name}")
