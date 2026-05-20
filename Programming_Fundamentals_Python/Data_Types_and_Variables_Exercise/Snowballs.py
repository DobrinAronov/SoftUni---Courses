number_of_snowballs =int(input())

max_grade = 0
max_weight = 0
max_time = 0
max_quality = 0

for snowball in range(number_of_snowballs):

    weight_of_the_snowball  = int(input())
    time_needed  = int(input())
    snowball_quality = int(input())

    current_grade = (weight_of_the_snowball // time_needed) ** snowball_quality
    if  current_grade > max_grade:
        max_grade = current_grade
        max_weight = weight_of_the_snowball
        max_time = time_needed
        max_quality = snowball_quality

print(f"{max_weight} : {max_time} = {max_grade} ({max_quality})")