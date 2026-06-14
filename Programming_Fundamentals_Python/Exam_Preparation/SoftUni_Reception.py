def calculate_time_to_services_all_students(first: int, second: int, tird: int, num_of_students: int) -> int:
    hours = 0
    while num_of_students > 0:
        hours += 1
        if hours % 4 != 0:
            num_of_students -= (first + second + tird)
    return hours



first_employee = int(input())
second_employee = int(input())
tird_employee = int(input())
number_of_students = int(input())

time_needed = calculate_time_to_services_all_students(
    first_employee, second_employee, tird_employee, number_of_students)
print(f"Time needed: {time_needed}h.")