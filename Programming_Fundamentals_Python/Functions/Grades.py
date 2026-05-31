def grade_in_words(number : float) -> str:
    grade = ''
    if 2.00 <= number <= 2.99:
        grade = 'Fail'
    elif  3.00 <= number <= 3.49:
        grade = 'Poor'
    elif  3.50 <= number <= 4.49:
        grade = 'Good'
    elif  4.50 <= number <= 5.49:
        grade = 'Very Good'
    elif  5.50 <= number <= 6.00:
        grade = 'Excellent'
    return grade


grade_in_number = float(input())
print(grade_in_words(grade_in_number))