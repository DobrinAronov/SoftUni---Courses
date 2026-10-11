from collections import deque

fuel_stack = [int(num) for num in input().split()]
consumption_idx_que = deque(int(num) for num in input().split())

needed_fuel = deque(list(map(int, input().split())))

altitude_count = 0
altitude_pass = []

while needed_fuel:
    fuel = fuel_stack.pop()
    consumption_idx = consumption_idx_que.popleft()

    altitude_count += 1
    current_altitude = f"Altitude {altitude_count}"

    if fuel - consumption_idx >= needed_fuel[0]:
        needed_fuel.popleft()
        altitude_pass.append(current_altitude)
        print(f"John has reached: {current_altitude}")
    else:
        print(f"John did not reach: {current_altitude}")
        break
else:
    print("John has reached all the altitudes and managed to reach the top!")
    exit()

print("John failed to reach the top.")

if needed_fuel and altitude_pass:
    print(f"Reached altitudes: {', '.join(altitude_pass)}")
elif not altitude_pass:
    print("John didn't reach any altitude.")
