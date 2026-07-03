def adding_students_by_average_grade(base: dict, student_name: str, current_grade: float) -> dict:
    if student_name not in base:
        base[student_name] = [current_grade]
    else:
        base[student_name].append(current_grade)
    return base


good_students = {}

number_of_pairs = int(input())

for number in range(number_of_pairs):
    name = input()
    grade = float(input())

    number_of_pairs = adding_students_by_average_grade(good_students, name, grade)

for name, grades in good_students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")
