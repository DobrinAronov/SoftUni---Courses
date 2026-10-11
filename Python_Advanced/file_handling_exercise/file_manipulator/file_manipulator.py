import os

while True:
    command = input()

    if command == "End":
        break

    action, file_name, *args = command.split('-')

    if action == "Create":
        new_file = open(file_name, "w").close()

    elif action == "Add":
        content = args[0]
        if os.path.exists(file_name):
            with open(file_name, "a") as f:
                f.write(f"{content}\n")
        else:
            with open(file_name, "w") as f:
                f.write(f"{content}\n")

    elif action == "Replace":
        old_str, new_str = args
        if os.path.exists(file_name):
            with open(file_name, "r+") as f:
                text = f.read()
                text = text.replace(old_str, new_str)
                f.seek(0)
                f.truncate()
                f.write(text)
        else:
            print("An error occurred")

    elif action == "Delete":
        try:
            os.remove(file_name)

        except FileNotFoundError:
            print("An error occurred")
