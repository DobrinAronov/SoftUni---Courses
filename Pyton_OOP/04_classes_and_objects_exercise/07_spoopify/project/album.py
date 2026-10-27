from project.song import Song


class Album:
    def __init__(self, name: str, *songs: Song):
        self.name = name
        self.songs: list[Song] = list(songs)
        self.published: bool = False

    def add_song(self, song: Song) -> str:
        if song in self.songs:
            return f"Song is already in the album."
        if self.published:
            return "Cannot add songs. Album is published."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        if self.published:
            return "Cannot remove songs. Album is published."
        s = next((s for s in self.songs if s.name == song_name), None)
        if s:
            self.songs.remove(s)
            return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."

    def publish(self) -> str:
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self) -> str:
        output = [f"Album {self.name}"]
        for s in self.songs:
            output.append(f"== {s.get_info()}")
        return '\n'.join(output)
