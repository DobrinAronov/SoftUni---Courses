from modules_lab.fibonacci_sequence.core import create_sequence, locate

fibonacci_sequence = []

while (command := input()) != "Stop":
    number = int(command.split()[-1])

    if command.startswith('Create'):
        fibonacci_sequence = create_sequence(number)
        print(*fibonacci_sequence)

    elif command.startswith('Locate'):
        print(locate(fibonacci_sequence, number))
