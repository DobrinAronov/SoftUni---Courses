from collections import deque

green_light = int(input())
free_window = int(input())

cars = deque()

total_cars_passed = 0
is_break = False

while (command := input()) != "END":
    if command == "green":
        current_green = green_light
        current_free_windows = free_window
        while cars and current_green > 0:
            current_car = cars[0]
            if len(current_car) <= current_green:
                current_green -= len(current_car)
                cars.popleft()
                total_cars_passed += 1
            else:
                if len(current_car) <= current_green + current_free_windows:
                    current_free_windows -= (len(current_car) - current_green)
                    current_green = 0
                    cars.popleft()
                    total_cars_passed += 1
                else:
                    hit_index = current_green + current_free_windows
                    character_hit = current_car[hit_index]
                    print(f"A crash happened!\n{current_car} was hit at {character_hit}.")
                    is_break = True
                    break

    else:
        cars.append(command)

    if is_break:
        break

else:
    print(f"Everyone is safe.\n{total_cars_passed} total cars passed the crossroads.")
