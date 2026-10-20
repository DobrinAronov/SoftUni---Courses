def create_sequence(num: int):
    fibonacci_seq = [0, 1]
    for _ in range(num - 2):
        next_number = fibonacci_seq[-1] + fibonacci_seq[-2]
        fibonacci_seq.append(next_number)

    return fibonacci_seq


def locate(sequence: list, num: int) -> str:
    if sequence:
        try:
            return f"The number - {num} is at index {sequence.index(num)}"
        except ValueError:
            return f"The number {num} is not in the sequence"
    else:
        return "There is no Fibonacci sequence, you have to create it first!"
