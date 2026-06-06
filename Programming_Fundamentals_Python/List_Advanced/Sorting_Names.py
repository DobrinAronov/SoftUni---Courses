def sorting_names(lst: list) -> list[str]:
    sorted_list = sorted(lst, key=lambda word: (-len(word), word))
    return sorted_list


list_with_names = [name for name in input().split(', ')]

print(sorting_names(list_with_names))
