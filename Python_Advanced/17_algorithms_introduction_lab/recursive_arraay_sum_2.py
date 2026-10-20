def calculate_sum(nums: list, idx: int) -> int:
    if idx == 0:
        return nums[idx]

    return nums[idx] + calculate_sum(nums, idx - 1)


numbers = [int(num) for num in input().split()]
print(calculate_sum(numbers, len(numbers) - 1))
