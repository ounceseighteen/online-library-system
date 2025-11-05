class BookService:
    def search_books(self, query):
        return f"Поиск книг: {query}"

    def get_book_details(self, book_id):
        return f"Информация о книге {book_id}"

    def get_book_status(self, book_id):
        return f"Статус книги {book_id}"