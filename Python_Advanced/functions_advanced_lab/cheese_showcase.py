def sorting_cheeses(**cheeses: dict) -> str:
    output = []
    for cheese_name, quantity in sorted(cheeses.items(), key=lambda x: (-len(x[1]), x[0])):
        output.append(cheese_name)
        for number in sorted(quantity, reverse=True):
            output.append(number)

    return '\n'.join(map(str, output))


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
