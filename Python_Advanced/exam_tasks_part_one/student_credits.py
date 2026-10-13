def students_credits(*courses_data: str) -> str:
    diploma_points = 240
    student_courses = {}

    for curr_course in courses_data:
        course_info = curr_course.split('-')
        name = course_info[0]
        course_credits, max_points, current_points = map(int, course_info[1:])

        current_credits = (current_points / max_points) * course_credits
        student_courses[name] = current_credits

    output = []
    total_credits = sum(curr_credits for curr_credits in student_courses.values())

    if total_credits >= diploma_points:
        output.append(f"Diyan gets a diploma with {total_credits:.1f} credits.")
    else:
        output.append(f"Diyan needs {(diploma_points - total_credits):.1f} credits more for a diploma.")

    for course, student_credits in sorted(student_courses.items(), key=lambda x: -x[1]):
        output.append(f"{course} - {student_credits:.1f}")

    return '\n'.join(output)


print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
