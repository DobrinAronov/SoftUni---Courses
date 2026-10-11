def movie_organizer(*movie_data) -> str:
    sorted_movies = {}

    for movie_name, genre in movie_data:
        if genre not in sorted_movies:
            sorted_movies[genre] = []
        sorted_movies[genre].append(movie_name)

    output = []
    for genre, movie_names in sorted(sorted_movies.items(), key=lambda x: (-len(x[1]), x[0])):
        output.append(f"{genre} - {len(movie_names)}")
        for movie_name in sorted(movie_names):
            output.append(f"* {movie_name}")

    return '\n'.join(output)


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
