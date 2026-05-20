number_of_first_letters = int(input())

for first in range(0, number_of_first_letters):
    for second in range(0, number_of_first_letters):
        for tird in range(0, number_of_first_letters):
            print(f"{chr(97 + first)}{chr(97 + second)}{chr(97 + tird)}")