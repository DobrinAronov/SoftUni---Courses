countries = input().split(', ')
capitals  = input().split(', ')

country_capital = {country : capital for country, capital in zip(countries, capitals)}

for country, capital in country_capital.items():
    print(f"{country} -> {capital}")