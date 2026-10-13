def forecast(*weather_info) -> str:
    forcast_data = {'Sunny': [], 'Cloudy': [], 'Rainy': []}

    for location, weather in weather_info:
        if weather == 'Sunny':
            forcast_data['Sunny'].append(location)
        elif weather == 'Cloudy':
            forcast_data['Cloudy'].append(location)
        elif weather == 'Rainy':
            forcast_data['Rainy'].append(location)

    output = []

    for weather, locations in forcast_data.items():
        for location in sorted(locations):
            output.append(f"{location} - {weather}")

    return '\n'.join(output)


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
