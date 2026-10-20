def bubble_sort(nums: list) -> list:
    i = 0
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for j in range(1, len(nums) - i):
            if nums[j - 1] > nums[j]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                is_sorted = False
        i += 1

    return nums


numbers = [int(n) for n in input().split()]
print(*bubble_sort(numbers))
