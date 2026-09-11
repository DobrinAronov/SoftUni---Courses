clothes = [int(c) for c in input().split()]
rack = int(input())

number_of_racks = 1
current_rack = rack

while clothes:
    if clothes[-1] <= current_rack:
        current_rack -= clothes.pop()
    else:
        number_of_racks += 1
        current_rack = rack

print(number_of_racks)