times_per_each_car = [int(digit) for digit in input().split()]

finish = len(times_per_each_car) // 2

left_side_car_times = times_per_each_car[:finish]
right_side_car_times = times_per_each_car[finish + 1:]

total_left_racer_time = 0
total_right_racer_time = 0

for time in left_side_car_times:
    if time == 0:
        if total_left_racer_time > 0:
            total_left_racer_time -= total_left_racer_time * 0.20
    total_left_racer_time += time

for time in right_side_car_times[:: -1]:
    if time == 0:
        if total_right_racer_time > 0:
            total_right_racer_time -= total_right_racer_time * 0.20
    total_right_racer_time += time

winner = ''
winner_time = 0.0

if total_left_racer_time < total_right_racer_time:
    winner = 'left'
    winner_time = total_left_racer_time

elif total_left_racer_time > total_right_racer_time:
    winner = 'right'
    winner_time = total_right_racer_time

print(f"The winner is {winner} with total time: {winner_time:.1f}")
