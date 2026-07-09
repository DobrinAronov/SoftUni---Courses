def extract_person_info(some_string: list) -> tuple[str, str]:
    person_name = ''
    person_age = ''
    find_name = False
    find_age = False
    for word in some_string:
        for symbol in word:
            # Case, when we find name
            if symbol == '@':
                find_name = True
            elif find_name:
                if symbol != '|':
                    person_name += symbol
                else:
                    find_name = False
            # Case, when we find age
            if symbol == '#':
                find_age = True
            elif find_age:
                if symbol != '*':
                    person_age += symbol
                else:
                    find_age = False

    return person_name, person_age


number_of_person = int(input())

for nuber in range(number_of_person):
    person_info = input().split()
    name, age = extract_person_info(person_info)
    print(f"{name} is {age} years old.")
