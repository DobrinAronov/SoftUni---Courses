def selection_sort(nums: list) -> list:
    for i in range(len(nums)):
        min_idx = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        if min_idx != i:
            nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return nums


numbers = [int(n) for n in input().split()]
print(*selection_sort(numbers))
