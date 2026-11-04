from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: list[Room] = []

    @property
    def guests(self):
        return sum(r.guests for r in self.rooms)

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def find_room(self, room_num: int):
        return next((r for r in self.rooms if r.number == room_num), None)

    def take_room(self, room_number: int, people: int):
        searched_room = self.find_room(room_number)
        if searched_room:
            return searched_room.take_room(people)

    def free_room(self, room_number: int):
        searched_room = self.find_room(room_number)
        if searched_room:
            return searched_room.free_room()

    def status(self) -> str:
        return (f"Hotel {self.name} has {self.guests} total guests\n"
                f"Free rooms: {', '.join([str(r.number) for r in self.rooms if not r.is_taken])}\n"
                f"Taken rooms: {', '.join([str(r.number) for r in self.rooms if r.is_taken])}")
