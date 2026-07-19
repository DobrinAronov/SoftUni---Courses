import re

list_of_participants = input().split(', ')

participants_dictionary = {participant: 0 for participant in list_of_participants}

while (current_string := input()) != "end of race":
    name_pattern = r"[A-Z]|[a-z]"
    distance_patern = r"\d"
    name_matches = re.findall(name_pattern, current_string)
    name = ''.join(name_matches)
    distance_matches = re.findall(distance_patern, current_string)
    distance = sum(int(num) for num in distance_matches)
    if name in participants_dictionary.keys():
        participants_dictionary[name] += distance

sorted_dictionary = sorted(participants_dictionary.items(), key=lambda x: -x[1])

for number in range(len(sorted_dictionary[:3])):
    if number == 0:
        print(f"1st place: {sorted_dictionary[number][0]}")
    elif number == 1:
        print(f"2nd place: {sorted_dictionary[number][0]}")
    elif number == 2:
        print(f"3rd place: {sorted_dictionary[number][0]}")
