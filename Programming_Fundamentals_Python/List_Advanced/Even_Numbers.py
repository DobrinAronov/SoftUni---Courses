def find_even_numbers_indices(lst: list) -> list[int]:
    list_with_indices = []

    for index in range(len(lst)):
        if lst[index] % 2 == 0:
            list_with_indices.append(index)
    return list_with_indices


list_of_numbers = [int(number) for number in input().split(', ')]

print(find_even_numbers_indices(list_of_numbers))
