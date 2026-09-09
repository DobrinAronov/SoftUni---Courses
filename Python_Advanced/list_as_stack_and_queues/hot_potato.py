from collections import deque

kids = deque(input().split())
num_of_toss = int(input())

number_of_rotate = num_of_toss - 1

while len(kids) > 1:
    kids.rotate(-number_of_rotate)
    removed_kid = kids.popleft()
    print(f"Removed {removed_kid}")

print(f"Last is {kids[0]}")
