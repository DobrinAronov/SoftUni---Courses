class PhotoAlbum:
    PAGE_CAPACITY = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos: list[list[str]] = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        count_pages = photos_count // cls.PAGE_CAPACITY
        if (photos_count % cls.PAGE_CAPACITY) > 0:
            count_pages += 1
        return cls(count_pages)

    def add_photo(self, label: str) -> str:
        for page_num, page_photos in enumerate(self.photos, start=1):
            if len(page_photos) < self.PAGE_CAPACITY:
                page_photos.append(label)
                return (f"{label} photo added successfully"
                        f" on page {page_num} slot {len(page_photos)}")
        return "No more free slots"

    def display(self) -> str:
        output = ["-----------"]
        for page in range(self.pages):
            output.append(' '.join(["[]" for _ in self.photos[page]]))
            output.append("-----------")

        return '\n'.join(output)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
