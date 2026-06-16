from math import ceil


def calculate_bonus_points(max_bonus: int, max_attendance: int, students: int, all_lectures: int, add_bonus: int,
                           attendance: int) -> tuple:
    if max_attendance < attendance:
        max_attendance = attendance

    total_bonus = attendance / all_lectures * (5 + add_bonus)

    if max_bonus < total_bonus:
        max_bonus = total_bonus

    return ceil(max_bonus), max_attendance


number_of_the_students = int(input())
number_of_the_lectures = int(input())
the_additional_bonus = int(input())

maximum_bonus = 0
maximum_attendance = 0

for i in range(number_of_the_students):
    attendance_of_each_student = int(input())

    maximum_bonus, maximum_attendance = (calculate_bonus_points
                                         (maximum_bonus, maximum_attendance, number_of_the_students,
                                          number_of_the_lectures, the_additional_bonus, attendance_of_each_student))

print(f"Max Bonus: {maximum_bonus}.")
print(f"The student has attended {maximum_attendance} lectures.")
