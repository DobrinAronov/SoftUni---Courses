unique_chemical = set()

for _ in range(int(input())):
    for compound in input().split():
        unique_chemical.add(compound)

print(*unique_chemical, sep="\n")