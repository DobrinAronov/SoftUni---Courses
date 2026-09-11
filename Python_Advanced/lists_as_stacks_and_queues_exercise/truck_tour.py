from collections import deque

petrol_pumps = int(input())
circle_road = deque()

for _ in range(petrol_pumps):
    fuel, distance = input().split()
    circle_road.append((int(fuel), int(distance)))

first_station = 0

while True:
    curr_fuel, curr_dist = circle_road[0]
    if curr_fuel < curr_dist:
        first_station += 1
        circle_road.rotate(-1)
    else:
        curr_petrol = 0
        for pump in circle_road:
            petrol, kilometers = pump
            curr_petrol += petrol
            curr_petrol -= kilometers
            if curr_petrol < 0:
                first_station += 1
                circle_road.rotate(-1)
                break
        else:
            print(first_station)
            break
