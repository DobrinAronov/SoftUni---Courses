def calculate_total_points(some_dict: dict) -> int:
    total = 0
    for some_value in some_dict.values():
        total += some_value
    return total


players_info = {}

while (current_command := input()) != "Season end":
    if ' -> ' in current_command:
        player, position, skill = current_command.split(' -> ')
        skill = int(skill)

        if player not in players_info:
            players_info[player] = {}
            players_info[player][position] = skill
        else:
            if position not in players_info[player]:
                players_info[player][position] = skill
            else:
                players_info[player][position] = max(players_info[player][position], skill)

    else:
        player_1, player_2 = current_command.split(' vs ')

        if player_1 in players_info.keys() and player_2 in players_info.keys():
            is_duel = False
            for position_first in players_info[player_1]:
                for position_second in players_info[player_2]:
                    if position_first == position_second:
                        is_duel = True
                        break
                if is_duel:
                    break
            if is_duel:
                # duel is happen
                total_1 = calculate_total_points(players_info[player_1])
                total_2 = calculate_total_points(players_info[player_2])
                if total_1 > total_2:
                    del players_info[player_2]
                elif total_1 < total_2:
                    del players_info[player_1]

for key, dict_data in players_info.items():
    players_info[key]['total_points'] = calculate_total_points(dict_data)

sorted_player_info = dict(sorted(players_info.items(), key=lambda x: (-x[1]['total_points'], x[0])))

for name, data in sorted_player_info.items():
    print(f"{name}: {data['total_points']} skill")
    del data['total_points']
    sorted_data = sorted(data.items(), key=lambda x: (-x[1], x[0]))
    for num in range(len(sorted_data)):
        print(f"- {sorted_data[num][0]} <::> {sorted_data[num][1]}")
