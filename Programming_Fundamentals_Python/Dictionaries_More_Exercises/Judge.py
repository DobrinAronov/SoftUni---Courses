students = {}

while (current_command := input()) != "no more time":
    user, contest, points = current_command.split(' -> ')
    points = int(points)

    if contest not in students:
        students[contest] = {}
        students[contest][user] = points
    if user not in students[contest]:
        students[contest][user] = points
    else:
        students[contest][user] = max(students[contest][user], points)

individual_scores = {}

for key, value in students.items():
    print(f"{key}: {len(value)} participants")
    sorted_points = sorted(value.items(), key=lambda x: (-x[1], x[0]))
    for num in range(len(sorted_points)):
        print(f"{num + 1}. {sorted_points[num][0]} <::> {sorted_points[num][1]}")
        name, points = sorted_points[num][0], sorted_points[num][1]
        if name not in individual_scores:
            individual_scores[name] = points
        else:
            individual_scores[name] += points

sorted_individual_scores = sorted(individual_scores.items(), key=lambda x: (-x[1], x[0]))

print("Individual standings:")
for num in range(len(sorted_individual_scores)):
    user_name, total_points = sorted_individual_scores[num][0], sorted_individual_scores[num][1]
    print(f"{num + 1}. {user_name} -> {total_points}")
