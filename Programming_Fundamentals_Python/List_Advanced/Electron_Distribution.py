def electron_distribution(num_of_electrons: int) -> list:
    list_of_electrons = []
    number_of_shells = 0

    while num_of_electrons != 0:
        number_of_shells += 1
        added_electrons = 2 * (number_of_shells ** 2)

        if added_electrons > num_of_electrons:
            added_electrons = num_of_electrons
        num_of_electrons -= added_electrons
        list_of_electrons.append(added_electrons)

    return list_of_electrons



number_of_electrons = int(input())

print(electron_distribution(number_of_electrons))