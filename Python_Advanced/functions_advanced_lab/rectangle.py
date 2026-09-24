def rectangle(length: int, width: int ) -> str:
    if type(length) != int or type(width) != int:
        return "Enter valid values!"

    output = []

    def area():
        return length * width
    def perimeter():
        return 2 * (length + width)

    output.append(f"Rectangle area: {area()}")
    output.append(f"Rectangle perimeter: {perimeter()}")

    return '\n'.join(output)


print(rectangle('2', 10))