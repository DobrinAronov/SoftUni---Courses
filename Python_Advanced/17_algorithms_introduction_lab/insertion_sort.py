def insertion_sort(nums: list):
    for j in range(1, len(nums)):
        for i in range(j, 0, -1):
            if nums[i] < nums[i - 1]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]


numbers = [int(n) for n in input().split()]
insertion_sort(numbers)
print(*numbers)