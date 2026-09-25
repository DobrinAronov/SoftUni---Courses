def math_operations(*float_numbers: tuple[float], **operations) -> str:
    for index, num in enumerate(float_numbers):
        idx = index % 4

        if idx == 0:
            operations["a"] += num
        elif idx == 1:
            operations["s"] -= num
        elif idx == 2:
            if num != 0:
                operations["d"] /= num
        else:
            operations["m"] *= num

    output = []

    for key, value in sorted(operations.items(), key=lambda x: (-x[1], x[0])):
        output.append(f"{key}: {value:.1f}")

    return '\n'.join(output)


print(math_operations(6.0, a=0, s=0, d=5, m=0))
