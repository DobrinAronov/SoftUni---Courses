def team_lineup(*football_players_data: tuple[str, str]) -> str:
    country_players = {}
    for player, country in football_players_data:
        if country not in country_players:
            country_players[country] = []
        country_players[country].append(player)

    output = []
    for country, players in sorted(country_players.items(), key=lambda x: (-len(x[1]), x[0])):
        output.append(f"{country}:")
        for player in players:
            output.append(f"  -{player}")

    return '\n'.join(output)


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))



