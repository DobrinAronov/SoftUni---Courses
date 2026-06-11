def social_distribution(lst: list, min_border: int) -> list | str:
    differences = [number - min_border for number in lst]

    if sum(differences) < 0:
        return "No equal distribution possible"

    for index in range(len(lst)):
        if lst[index] < min_border:

            while lst[index] < min_border:

                max_num = max(lst)
                max_num_idx = lst.index(max_num)

                add_value = min_border - lst[index]
                if (max_num - add_value) >= min_border:
                    lst[max_num_idx] -= add_value
                    lst[index] += add_value
                else:
                    add_value = max_num - min_border
                    lst[max_num_idx] -= add_value
                    lst[index] += add_value

    return lst


population = [int(element) for element in input().split(', ')]
minimum_wealth = int(input())

result = social_distribution(population, minimum_wealth)
print(result)
