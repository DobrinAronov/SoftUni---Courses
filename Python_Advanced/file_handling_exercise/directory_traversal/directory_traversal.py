import os

sorted_files = {}
directory = "../"


def get_files(folder, level=float("inf")):
    if level < 0:
        return

    for element in os.listdir(folder):
        path = os.path.join(folder, element)

        if os.path.isfile(path):
            _, ext = os.path.splitext(element)
            if ext:
                if ext not in sorted_files:
                    sorted_files[ext] = []
                sorted_files[ext].append(element)

        elif os.path.isdir(path):
            get_files(path, level - 1)


get_files(directory, 2)

with open("report.txt", "w") as output:
    for ext, file_names in sorted(sorted_files.items()):
        output.write(f"{ext}\n")
        for file_name in sorted(file_names):
            output.write(f"- - - {file_name}\n")
