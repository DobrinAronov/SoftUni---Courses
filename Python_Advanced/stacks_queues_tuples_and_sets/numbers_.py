def add_numbers(sequence: set, nums: set) -> set:
    return sequence.union(nums)


def remove_numbers(sequence: set, nums: set) -> set:
    return sequence.difference(nums)


first = {int(num) for num in input().split()}
second = {int(num) for num in input().split()}

for _ in range(int(input())):
    command = input().split()
    action = ' '.join(command[0:2])
    numbers = set([int(n) for n in command[2:]])

    if action == "Add First":
        first = add_numbers(first, numbers)
    elif action == "Add Second":
        second = add_numbers(second, numbers)
    elif action == "Remove First":
        first = remove_numbers(first, numbers)
    elif action == "Remove Second":
        second = remove_numbers(second, numbers)
    elif action == "Check Subset":
        if first.issubset(second) or second.issubset(first):
            print("True")
        else:
            print("False")

print(', '.join(map(str, sorted(first))))
print(*map(str, sorted(second)), sep=", ")