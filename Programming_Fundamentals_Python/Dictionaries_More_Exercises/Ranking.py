def check_contest_is_valid(etalon_list: dict, some_name: str, contest_pass: str) -> bool:
    if some_name in etalon_list.keys():
        if contest_pass == etalon_list[some_name]:
            return True
    return False


all_contests = {}

while (current_command := input()) != "end of contests":
    contest, password = current_command.split(':')
    all_contests[contest] = password

students_submissions = {}

while (contents_info := input()) != "end of submissions":
    contest_name, contest_password, user_name, points = contents_info.split('=>')
    points = int(points)

    correct_contents = check_contest_is_valid(all_contests, contest_name, contest_password)
    if not correct_contents:
        continue
    else:
        if contest_name not in students_submissions.keys():
            students_submissions[contest_name] = {
                'names': [],
                'points': []
            }
        # We add new name and points (in lists) to the keys "name" and "points" if they do not exist!
        if user_name not in students_submissions[contest_name]['names']:
            students_submissions[contest_name]['names'].append(user_name)
            students_submissions[contest_name]['points'].append(points)
        else:  # We keep the student's highest grade.
            index_name = students_submissions[contest_name]['names'].index(user_name)
            if students_submissions[contest_name]['points'][index_name] < points:
                students_submissions[contest_name]['points'][index_name] = points

student_names = []

for content in students_submissions:
    for name in students_submissions[content]['names']:
        if name not in student_names:
            student_names.append(name)
sorted_names = sorted(student_names)

final_dict = {}

for name in sorted_names:
    for item in students_submissions:
        if name in students_submissions[item]['names']:
            if name not in final_dict:
                final_dict[name] = {
                    'subject': [],
                    'points': []
                }
            index_name = students_submissions[item]['names'].index(name)
            final_dict[name]['subject'].append(item)
            final_dict[name]['points'].append(students_submissions[item]['points'][index_name])

for item in final_dict:
    pairs = sorted(zip(final_dict[item]['points'], final_dict[item]['subject']), reverse=True)
    final_dict[item]['points'], final_dict[item]['subject'] = zip(*pairs)

winner = ''
winer_points = 0

for item in final_dict:
    total_points = sum(final_dict[item]['points'])
    if total_points > winer_points:
        winer_points = total_points
        winner = item

print(f"Best candidate is {winner} with total {winer_points} points.\nRanking:")

for item in final_dict:
    print(item)
    for index in range(len(final_dict[item]['subject'])):
        print(f"#  {final_dict[item]['subject'][index]} -> {final_dict[item]['points'][index]}")
