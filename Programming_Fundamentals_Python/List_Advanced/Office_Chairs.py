def office_chair(lst: list) -> str:
    messages = []
    total_free_chairs = 0
    for room in range(len(lst)):

        chair, visitors = lst[room].split()
        num_of_chairs = len(chair)
        visitors = int(visitors)

        if visitors > num_of_chairs:
            need_chairs = visitors - num_of_chairs
            messages.append(f"{need_chairs} more chairs needed in room {room + 1}")  # + 1 because rooms started from 1!
        else:
            total_free_chairs += num_of_chairs - visitors
    if not messages:
        return f"Game On, {total_free_chairs} free chairs left"
    return '\n'.join(messages)


number_of_rooms = int(input())
chair_visitors_info = []

for room_info in range(number_of_rooms):
    chair_visitors_info.append(input())

print(office_chair(chair_visitors_info))
