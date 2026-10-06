from collections import deque

strengths_stack = [int(num) for num in input().split()]
accuracy_dqu = deque(int(num) for num in input().split())

goals = 0
while strengths_stack and accuracy_dqu:
    curr_strength = strengths_stack.pop()
    curr_accuracy = accuracy_dqu.popleft()
    result = curr_strength + curr_accuracy

    if result == 100:
        goals += 1
    elif result < 100:
        if curr_strength < curr_accuracy:
            accuracy_dqu.appendleft(curr_accuracy)
        elif curr_accuracy < curr_strength:
            strengths_stack.append(curr_strength)
        else:
            strengths_stack.append(result)
    else:
        strengths_stack.append(curr_strength - 10)
        accuracy_dqu.append(curr_accuracy)

if goals == 3:
    print("Paul scored a hat-trick!")
elif goals == 0:
    print("Paul failed to score a single goal.")
elif goals > 3:
    print("Paul performed remarkably well!")
elif 0 < goals < 3:
    print("Paul failed to make a hat-trick.")
if goals > 0:
    print(f"Goals scored: {goals}")

[print(f"Strength values left: {', '.join(map(str, strengths_stack))}") if strengths_stack else None]
[print(f"Accuracy values left: {', '.join(map(str, accuracy_dqu))}") if accuracy_dqu else None]
