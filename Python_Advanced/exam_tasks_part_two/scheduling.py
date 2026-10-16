clock_cycles  = list(map(int, input().split(', ')))
index = int(input())

target_task = clock_cycles[index]

total_cycles = 0
for num in sorted(clock_cycles):
    if num <= target_task:
        total_cycles += num

print(total_cycles)