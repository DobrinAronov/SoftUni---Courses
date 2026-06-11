def number_classification(lst: list[int]) -> tuple:
    positive = []
    negative = []
    even = []
    odd = []

    for number in lst:
        if number % 2 == 0:
            even.append(str(number))
        elif number % 2 != 0:
            odd.append(str(number))
        if number >= 0:
            positive.append(str(number))
        elif number < 0:
            negative.append(str(number))
    return positive, negative, even, odd


numbers = [int(number) for number in input().split(', ')]

positive_numbers, negative_numbers, even_numbers, odd_numbers = number_classification(numbers)

print(f"Positive: {', '.join(positive_numbers)}")
print(f"Negative: {', '.join(negative_numbers)}")
print(f"Even: {', '.join(even_numbers)}")
print(f"Odd: {', '.join(odd_numbers)}")
