from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: list[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str) -> str:
        removed_pokemon = next((p for p in self.pokemons if p.name == pokemon_name), None)
        if removed_pokemon:
            self.pokemons.remove(removed_pokemon)
            return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self) -> str:
        output = (f"Pokemon Trainer {self.name}\n"
                  f"Pokemon count {len(self.pokemons)}\n")

        for pokemon in self.pokemons:
            output += f"- {pokemon.pokemon_details()}\n"

        return output.strip()
