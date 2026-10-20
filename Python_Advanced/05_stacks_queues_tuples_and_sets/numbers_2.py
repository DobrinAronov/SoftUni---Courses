first = {int(num) for num in input().split()}
second = {int(num) for num in input().split()}

mapper = {
    "Add First": lambda *args: first.update(numbers),
    "Add Second": lambda *args: second.update(numbers),
    "Remove First": lambda *args: first.difference_update(numbers),
    "Remove Second": lambda *args: second.difference_update(numbers),
    "Check Subset": lambda *args: print(any([first.issubset(second), second.issubset(first)]))
}

for _ in range(int(input())):
    command = input().split()
    action = ' '.join(command[:2])
    numbers = {int(n) for n in command[2:]}

    mapper[action](first, second, numbers)

print(', '.join(map(str, sorted(first))))
print(*sorted(second), sep=", ")
