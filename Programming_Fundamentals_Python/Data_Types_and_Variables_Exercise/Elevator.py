number_of_people = int(input())
capacity_of_elevator = int(input())

count_courses = 0

while number_of_people > 0:

    if number_of_people <= capacity_of_elevator:
        number_of_people -= min(number_of_people, capacity_of_elevator)
        count_courses += 1

    else:
        number_of_people -= capacity_of_elevator
        count_courses += 1

print(count_courses)