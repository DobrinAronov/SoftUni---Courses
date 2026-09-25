def positive_vs_negative(nums: list) -> str:
    positive_sum = sum(num for num in nums if num > 0)
    negative_sum = sum(num for num in nums if num < 0)

    output = [negative_sum, positive_sum]

    if abs(negative_sum) > positive_sum:
        output.append("The negatives are stronger than the positives")
    else:
        output.append("The positives are stronger than the negatives")

    return '\n'.join(map(str, output))


numbers = [int(n) for n in input().split()]
print(positive_vs_negative(numbers))
