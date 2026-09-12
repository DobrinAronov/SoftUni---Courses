import time

numbers = [int(num) for num in input().split()]
target = int(input())

start = time.time()

pairs = {}

for value in numbers:
    if value not in pairs:
        result = target - value
        pairs[result] = value
    else:
        print(f"{pairs[value]} + {value} = {target}")
        del pairs[value]

end = time.time()
print(f"Time range: {end - start}")