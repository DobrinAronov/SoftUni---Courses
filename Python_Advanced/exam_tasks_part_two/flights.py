def flights(*flights_info) -> dict:
    flights_data = {}

    for idx in range(0, len(flights_info), 2):
        if flights_info[idx] == "Finish":
            break

        destination, passengers = flights_info[idx], flights_info[idx + 1]

        if destination not in flights_data:
            flights_data[destination] = 0
        flights_data[destination] += passengers

    return flights_data


print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
