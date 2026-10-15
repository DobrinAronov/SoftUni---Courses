def start_spring(**object_data):
    type_objects = {}

    for name, type_object in object_data.items():
        if type_object not in type_objects.keys():
            type_objects[type_object] = []
        type_objects[type_object].append(name)

    output = []
    for type_obj, names_obj in \
            sorted(type_objects.items(), key=lambda x: (-len(x[1]), x[0])):
        output.append(f"{type_obj}:")
        for name in sorted(names_obj):
            output.append(f"-{name}")

    return "\n".join(output)


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
