def accommodate(*waiting_groups, **rooms) -> str:
    rooms_data = {int(room_number.split('_')[1]): capacity for room_number, capacity in rooms.items()}
    rooms_data = dict(sorted(rooms_data.items(), key=lambda x: (x[1], x[0])))

    accommodated_groups = {}
    unaccommodated_guests = 0
    for group in waiting_groups:
        for room_num, capacity in rooms_data.items():
            if group == capacity and room_num not in accommodated_groups:
                accommodated_groups[room_num] = group
                break
            elif group < capacity and room_num not in accommodated_groups:
                accommodated_groups[room_num] = group
                break
        else:
            unaccommodated_guests += group

    output = []
    if accommodated_groups:
        output.append(f"A total of {len(accommodated_groups)} accommodations were completed!")
        for room_num, guests in sorted(accommodated_groups.items()):
            output.append(f"<Room {room_num} accommodates {guests} guests>")
    else:
        output.append("No accommodations were completed!")

    if unaccommodated_guests > 0:
        output.append(f"Guests with no accommodation: {unaccommodated_guests}")
    if len(rooms_data) > len(accommodated_groups):
        free_rooms = len(rooms_data) - len(accommodated_groups)
        output.append(f"Empty rooms: {free_rooms}")

    return '\n'.join(output)


print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))
