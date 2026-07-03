resource = {}
resource_lst = []
current_command = input()

while current_command != "stop":
    resource_lst.append(current_command)

    current_command = input()

for index in range(0, len(resource_lst), 2):
    if resource_lst[index] not in resource:
        resource[resource_lst[index]] = int(resource_lst[index + 1])
    else:
        resource[resource_lst[index]] += int(resource_lst[index + 1])

for key, value in resource.items():
    print(f"{key} -> {value}")