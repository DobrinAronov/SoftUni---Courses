number_of_guests = int(input())

registration_numbers = set()

for _ in range(number_of_guests):
    registration_numbers.add(input())

while (current_quest := input()) != "END":
    if current_quest in registration_numbers:
        registration_numbers.remove(current_quest)

print(len(registration_numbers))

for number in sorted(registration_numbers):
    print(number)