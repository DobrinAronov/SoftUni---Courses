from collections import deque

bullet_price = int(input())
barrel_size = int(input())

bullets = list(map(int, input().split()))
locks = deque(map(int, input().split()))

money = int(input())

shots = 0

while bullets and locks:
    bullet = bullets.pop()
    money -= bullet_price

    if bullet <= locks[0]:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")

    shots += 1

    if shots == barrel_size:
        if bullets:
            print("Reloading!")
        shots = 0

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${money}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")