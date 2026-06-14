def find_a_place(lift: list, people: int) -> str:
    for index in range(len(lift)):
        if lift[index] < 4:
            add_people = min((4 - lift[index]), people)
            lift[index] += add_people
            people -= add_people

    empty_spot = False
    for wagon in lift:
        if wagon < 4:
            empty_spot = True
            break
    lift_str = [str(element) for element in lift]
    if empty_spot and people == 0:
        return f"The lift has empty spots!\n{' '.join(lift_str)}"
    elif not empty_spot and people > 0:
        return f"There isn't enough space! {people} people in a queue!\n{' '.join(lift_str)}"
    else:
        return f"{' '.join(lift_str)}"


number_of_people = int(input())
lift_wagons = [int(element) for element in input().split()]

message = find_a_place(lift_wagons, number_of_people)
print(message)
