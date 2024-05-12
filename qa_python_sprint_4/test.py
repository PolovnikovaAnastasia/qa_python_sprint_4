import pytest
from main import BooksCollector


class TestBooksCollector:

    @pytest.fixture
    def books_collector(self):
        return BooksCollector()

    def test_add_new_book_true(self, books_collector):
        books_collector.add_new_book('Harry Potter')
        assert 'Harry Potter' in books_collector.books_genre

    def test_set_book_genre_true(self, books_collector):
        books_collector.add_new_book('Harry Potter')
        books_collector.set_book_genre('Harry Potter', 'Фантастика')
        assert books_collector.get_book_genre('Harry Potter') == 'Фантастика'

    def test_get_book_genre_true(self, books_collector):
        books_collector.add_new_book('Harry Potter')
        books_collector.set_book_genre('Harry Potter', 'Ужасы')
        assert books_collector.get_book_genre('Harry Potter') == 'Ужасы'

    def test_get_books_with_specific_genre_true(self,books_collector):
        books_collector.add_new_book('Book4')
        books_collector.set_book_genre('Book4', 'Ужасы')
        books_collector.add_new_book('Book5')
        books_collector.set_book_genre('Book5', 'Детективы')
        assert books_collector.get_books_with_specific_genre('Ужасы') == ['Book4']
        assert books_collector.get_books_with_specific_genre('Детективы') == ['Book5']

    def test_add_book_in_favorites_true(self, books_collector):
        books_collector.add_new_book('Harry Potter')
        books_collector.add_book_in_favorites('Harry Potter')
        assert 'Harry Potter' in books_collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_true(self, books_collector):
        books_collector.add_new_book('Harry Potter')
        books_collector.add_book_in_favorites('Harry Potter')
        assert 'Harry Potter' in books_collector.get_list_of_favorites_books()
        books_collector.delete_book_from_favorites('Harry Potter')
        assert 'Harry Potter' not in books_collector.get_list_of_favorites_books()

    def test_get_books_genre_true(self,books_collector):
        assert books_collector.get_books_genre() == books_collector.books_genre

    def test_get_books_for_children_true(self,books_collector):
        books_collector.add_new_book('Book6')
        books_collector.set_book_genre('Book6', 'Мультфильмы')
        books_for_children = books_collector.get_books_for_children()
        assert 'Book6' in books_for_children

    def test_get_list_of_favorites_books_true(self,books_collector):
        books_collector.add_new_book('Book7')
        books_collector.add_new_book('Book8')
        books_collector.add_book_in_favorites('Book7')
        books_list_of_favorites = books_collector.get_list_of_favorites_books()
        assert 'Book7' in books_list_of_favorites
        assert "Book8" not in books_list_of_favorites
