def binary_search(nums: list, target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


numbers = [int(n) for n in input().split()]
number = int(input())
print(binary_search(numbers, number))
