students = {}

current_command = input()
while ':' in current_command:
    name, id_num, course = current_command.split(':')
    if course not in students:
        students[course] = {}
        students[course][name] = id_num
    else:
        students[course][name] = id_num

    current_command = input()

if '_' in current_command:
    current_command = current_command.split('_')
    current_command = ' '.join(current_command)

for key, value in students.items():
    if key == current_command:
        for inner_key, inner_value in value.items():
            print(f"{inner_key} - {inner_value}")
        break
