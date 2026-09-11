number_of_students = int(input())

students_grades = {}

for student in range(number_of_students):
    name, grade = input().split()
    if name not in students_grades:
        students_grades[name] = []
    students_grades[name].append(float(grade))

for student, grades in students_grades.items():
    average = sum(grades) / len(grades)
    grades_str = [str(f"{el:.2f}") for el in grades]
    print(f"{student} -> {' '.join(grades_str)} (avg: {average:.2f})")
