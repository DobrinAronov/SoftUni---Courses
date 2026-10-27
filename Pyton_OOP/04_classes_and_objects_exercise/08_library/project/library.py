from project.user import User


class Library:
    def __init__(self):
        self.user_records: list[User] = []
        self.books_available: dict[str, list[str]] = {}
        self.rented_books: dict[str, dict[str, int]] = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str | None:
        for book_info in self.rented_books.values():
            if book_name in book_info:
                return (f'The book "{book_name}"'
                        f' is already rented and will be available in {book_info[book_name]} days!')

        for book_author, books in self.books_available.items():
            if book_author == author and book_name in books:
                books.remove(book_name)
                if book_name not in user.books:
                    user.books.append(book_name)
                if user not in self.user_records:
                    self.user_records.append(user)
                if user.username not in self.rented_books:
                    self.rented_books[user.username] = {}
                self.rented_books[user.username][book_name] = days_to_return
                return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author: str, book_name: str, user: User) -> None | str:
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"

        user.books.remove(book_name)
        if author not in self.books_available:
            self.books_available[author] = []
        if book_name not in self.books_available[author]:
            self.books_available[author].append(book_name)

        if user.username in self.rented_books and book_name in self.rented_books[user.username]:
            del self.rented_books[user.username][book_name]
