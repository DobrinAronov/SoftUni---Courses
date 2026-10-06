def list_roman_emperors(*success_status, **length_of_rule) -> str:
    successful_emperors = {}
    unsuccessful_emperors = {}
    num_of_all_emperors = 0

    for name, status in success_status:
        if status is True:
            successful_emperors[name] = length_of_rule[name]
        elif status is False:
            unsuccessful_emperors[name] = length_of_rule[name]

        num_of_all_emperors += 1

    output = [f"Total number of emperors: {num_of_all_emperors}"]

    if successful_emperors:
        output.append("Successful emperors:")
        for name, years in sorted(successful_emperors.items(), key=lambda x: (-x[1], x[0])):
            output.append(f"****{name}: {years}")

    if unsuccessful_emperors:
        output.append("Unsuccessful emperors:")
        for name, years in sorted(unsuccessful_emperors.items(), key=lambda x: (x[1], x[0])):
            output.append(f"****{name}: {years}")

    return '\n'.join(output)


print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False),
                          ("Caligula", False), ("Pertinax", False), ("Vespasian", True),
                          Augustus=40, Trajan=19, Nero=14, Caligula=4, Pertinax=4, Vespasian=19, ))
