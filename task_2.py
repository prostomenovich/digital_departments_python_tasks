BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    """Класс, описывающий книгу"""
    def __init__(self, id_: int, name: str, pages: int):
        """
        Конструктор экземпляра класса.

        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        """
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f"Книга \"{self.name}\""

    def __repr__(self):
        return f"Book(id_={self.id_}, name={self.name!r}, pages={self.pages})"


# TODO написать класс Library
class Library:
    """Класс, описывающий библиотеку с книгами."""
    def __init__(self, books: list = None):
        """
        Конструктор экземпляра класса.

        :param books: список книг, если параметр не задан, то будет создан пустой список
        """
        if books is None:
            books = list()
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Получает идентификатор следующей книги, которая будет добавлена в библиотеку.

        :return: идентификатор (идентификатор последней книги в списке + 1 или 1, если список пуст)
        """
        if self.books:
            return self.books[-1].id_ + 1
        return 1

    def get_index_by_book_id(self, id_: int):
        """
        Поиск индекса книги в списке books по идентификатору (id_)

        :param id_: идентификатор книги
        :return: индекс книги в списке, если она в нём присутствует, иначе ValueError
        """
        for index, book in enumerate(self.books):
            if book.id_ == id_:
                return index

        return ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1

