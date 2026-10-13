from collections import deque

seats = input().split(', ')
first_num_dqe = deque(input().split(', '))
second_num_stack = deque(input().split(', '))

seat_matches = 0
rotations = 0
occupation_seats = []
while True:
    first = first_num_dqe.popleft()
    second = second_num_stack.pop()
    rotations += 1
    letter = chr(int(first) + int(second))

    for seat_number in [first + letter, second + letter]:
        if seat_number in seats and seat_number not in occupation_seats:
            occupation_seats.append(seat_number)
            seat_matches += 1
            break
    else:
        first_num_dqe.append(first)
        second_num_stack.appendleft(second)

    if seat_matches == 3 or rotations == 10:
        break

print(f"Seat matches: {', '.join(occupation_seats)}")
print(f"Rotations count: {rotations}")