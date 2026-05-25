coins = list(map(int, input().split(', ')))
number_of_beggars = int(input())

coins_per_beggar = []

for beggar in range(number_of_beggars):
    beggar_profit = []
    for index in range(beggar, len(coins), number_of_beggars):
        beggar_profit.append(coins[index])
    coins_per_beggar.append(sum(beggar_profit))

print(coins_per_beggar)