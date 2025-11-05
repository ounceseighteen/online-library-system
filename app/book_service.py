class BookService:
    def search_books(self, query):
        return f"Поиск книг: {query}"

    def get_book_details(self, book_id):
        return f"Информация о книге {book_id}"