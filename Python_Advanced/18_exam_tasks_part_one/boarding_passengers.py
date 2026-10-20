def boarding_passengers(ship_capacity: int, *passenger_groups) -> str:
    accommodated_groups = {}

    for guests, benefit_group in passenger_groups:
        if ship_capacity >= guests:
            ship_capacity -= guests
            if benefit_group not in accommodated_groups:
                accommodated_groups[benefit_group] = 0
            accommodated_groups[benefit_group] += guests

        if ship_capacity == 0:
            break

    output = ["Boarding details by benefit plan:"]
    for benefit_plan, passengers in sorted(accommodated_groups.items(), key=lambda x: (-x[1], x[0])):
        output.append(f"## {benefit_plan}: {passengers} guests")

    total_quest = sum([group[0] for group in passenger_groups])
    accommodated_passengers = sum([passengers for passengers in accommodated_groups.values()])

    if total_quest == accommodated_passengers:
        output.append("All passengers are successfully boarded!")

    elif ship_capacity == 0 and accommodated_passengers < total_quest:
        output.append("Boarding unsuccessful. Cruise ship at full capacity.")

    if ship_capacity > 0 and accommodated_passengers < total_quest:
        output.append(f"Partial boarding completed. Available capacity: {ship_capacity}.")

    return '\n'.join(output)


print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))
