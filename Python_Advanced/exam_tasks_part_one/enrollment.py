def gather_credits(needed_credits: int, *course_info: tuple[str, int]) -> str:
    enrollment_courses = []
    gathered_credits = 0

    for course_name, course_credit in course_info:
        if gathered_credits < needed_credits:
            if course_name not in enrollment_courses:
                enrollment_courses.append(course_name)
                gathered_credits += course_credit
        else:
            break

    output = []
    if gathered_credits >= needed_credits:
        output.append(f"Enrollment finished! Maximum credits: {gathered_credits}.")
        output.append(f"Courses: {', '.join(sorted(enrollment_courses))}")
    else:
        output.append(f"You need to enroll in more courses!"
                      f" You have to gather {needed_credits - gathered_credits} credits more.")

    return '\n'.join(output)


print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
