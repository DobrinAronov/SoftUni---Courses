def calculate_sum(nums: list, idx: int) -> int:
    if idx == len(nums) - 1:
        return nums[idx]

    return nums[idx] + calculate_sum(nums, idx + 1)


numbers = [int(num) for num in input().split()]
print(calculate_sum(numbers, 0))
