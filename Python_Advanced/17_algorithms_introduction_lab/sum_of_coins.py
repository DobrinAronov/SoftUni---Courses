def sum_of_coins(nums: list, goal: int) -> str:
    nums.sort(reverse=True)
    collected_coins = {}

    for coin in nums:
        if coin <= goal:
            num_of_coins = goal // coin
            goal %= coin
            if coin not in collected_coins:
                collected_coins[coin] = num_of_coins

    if goal > 0:
        return "Error"

    result = f"Number of coins to take: {sum(collected_coins.values())}\n"

    for nominal, count in collected_coins.items():
        result += f"{count} coin(s) with value {nominal}\n"

    return result.strip()


numbers = [int(n) for n in input().split(', ')]
target = int(input())
print(sum_of_coins(numbers, target))
