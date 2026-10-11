def softuni_students(*args, **kwargs) -> str:
    students_data = {}
    invalid_students = []
    for pair in args:
        id_course, user_name = pair
        if id_course in kwargs:
            students_data[user_name] = kwargs[id_course]

        else:
            invalid_students.append(user_name)

    output = []
    for student_name, course_name in sorted(students_data.items()):
        output.append(f"*** A student with the username {student_name}"
                      f" has successfully finished the course {course_name}!")
    if invalid_students:
        output.append(f"!!! Invalid course students: {', '.join(sorted(invalid_students))}")

    return '\n'.join(output)


print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))
