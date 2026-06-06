def find_next_version(lst: list[str]) -> str:
    number_in_str = ''.join(lst)
    real_number = int(number_in_str)

    next_version = real_number + 1
    next_version_str = str(next_version)
    return '.'.join(next_version_str)


soft_version = [number for number in input().split('.')]

print(find_next_version(soft_version))
