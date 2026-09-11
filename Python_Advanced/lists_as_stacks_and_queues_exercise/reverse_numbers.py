def reverse_numbers(nums: list):
    result = []
    for _ in range (len(nums)):
        result.append(nums.pop())
    return ' '.join(result)


numbers = input().split()
print(reverse_numbers(numbers))