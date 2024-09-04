from app.book import Book


class BookProcessor:
    def __init__(self, book: Book):
        self.book = book

    def display(self, display_strategy) -> None:
        display_strategy.display(self.book.content)

    def print_book(self, print_strategy) -> None:
        print_strategy.print_book(self.book.title, self.book.content)

    def serialize(self, serialize_strategy) -> str:
        return serialize_strategy.serialize(self.book.title, self.book.content)
