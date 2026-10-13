def add_songs(*songs_data: tuple[str, list]) -> str:
    song_lyrics = {}

    for song_name, lyrics in songs_data:
        if song_name not in song_lyrics:
            song_lyrics[song_name] = []
        song_lyrics[song_name].extend(lyrics)

    output = []
    for song_title, lyrics in song_lyrics.items():
        output.append(f"- {song_title}")
        if lyrics:
            for lyric in lyrics:
                output.append(f"{lyric}")

    return "\n".join(output)


print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))