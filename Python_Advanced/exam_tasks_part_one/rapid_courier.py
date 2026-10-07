from collections import deque

packages_stack = [int(num) for num in input().split()]
couriers_dqu = deque(int(num) for num in input().split())

total_weight = 0
while packages_stack and couriers_dqu:
    curr_package = packages_stack.pop()
    curr_courier = couriers_dqu.popleft()

    if curr_courier >= curr_package:
        total_weight += curr_package
        curr_courier -= curr_package * 2
        if curr_courier > 0:
            couriers_dqu.append(curr_courier)
    else:
        total_weight += curr_courier
        curr_package -= curr_courier
        packages_stack.append(curr_package)

print(f"Total weight: {total_weight} kg")
if not packages_stack and not couriers_dqu:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif packages_stack and not couriers_dqu:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages:"
          f" {', '.join(map(str, packages_stack))}")
elif couriers_dqu and not packages_stack:
    print(f"Couriers are still on duty:"
          f" {', '.join(map(str, couriers_dqu))} but there are no more packages to deliver.")
