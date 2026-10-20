even_set = set()
odd_set = set()

for idx in range(1, int(input()) + 1):
    result = sum(ord(letter) for letter in input()) // idx
    even_set.add(result) if result % 2 == 0 else odd_set.add(result)

even_sum = sum(even_set)
odd_sum = sum(odd_set)

if even_sum == odd_sum:
    print(', '.join(map(str, even_set.union(odd_set))))
elif odd_sum > even_sum:
    print(', '.join(map(str, odd_set.difference(even_set))))
elif even_sum > odd_sum:
    print(', '.join(map(str, even_set.symmetric_difference(odd_set))))
