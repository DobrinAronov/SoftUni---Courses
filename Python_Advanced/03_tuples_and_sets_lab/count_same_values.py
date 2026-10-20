numbers = tuple(map(float, input().split()))

count_numbers = []

for number in numbers:
    if number not in count_numbers:
        count_numbers.append(number)
        print(f"{number:.1f} - {numbers.count(number)} times")