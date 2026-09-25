def age_assignment(*names: str, **kwargs: dict[str, int]) -> str:
    name_age_dict = {}

    for name in names:
        if name[0] in kwargs.keys():
            name_age_dict[name] = kwargs[name[0]]

    output = []

    for name, age in sorted(name_age_dict.items()):
        output.append(f"{name} is {age} years old.")

    return '\n'.join(output)


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
