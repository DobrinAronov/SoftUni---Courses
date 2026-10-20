def cookbook(*recipe_info):
    recipes_list = {}
    for current_data in recipe_info:
        recipe_name, cuisine, ingredients = current_data
        if cuisine not in recipes_list:
            recipes_list[cuisine] = {}
        recipes_list[cuisine].update({recipe_name: ingredients})

    recipes_list = sorted(recipes_list.items(), key=lambda x: (-len(x[1]), x[0]))

    output = []

    for cuisine_name, recipies_data in recipes_list:
        output.append(f"{cuisine_name} cuisine contains {len(recipies_data)} recipes:")
        for recipe_name, ingredients in sorted(recipies_data.items()):
            output.append(f"  * {recipe_name} -> Ingredients: {', '.join(ingredients)}")

    return '\n'.join(output)


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
))
