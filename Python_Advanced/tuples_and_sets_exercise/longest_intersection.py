intersections = []
for _ in range(int(input())):
    first_borders, second_borders = input().split('-')
    first_start, fist_end = first_borders.split(',')
    second_start, second_end = second_borders.split(',')

    first_set = set(range(int(first_start), int(fist_end) + 1))
    second_set = set(range(int(second_start), int(second_end) + 1))

    intersections.append(first_set.intersection(second_set))

sorted_intersection =  sorted(intersections, key=lambda i: -len(i))
print(f"Longest intersection is [{', '.join(map(str, sorted_intersection[0]))}] with length {len(sorted_intersection[0])}")