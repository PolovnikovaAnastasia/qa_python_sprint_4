import pytest
from main import BooksCollector


class TestBooksCollector:
    @pytest.fixture
    def books_collector(self):
        return BooksCollector()

    def test_add_new_book_true(self, books_collector):
        books_collector.add_new_book('Harry Potter')
        assert 'Harry Potter' in books_collector.books_genre

    @pytest.mark.parametrize('name, genre', [('Harry Potter', 'Фантастика'),
                                             ('Sherlock Holmes', 'Детективы')])
    def test_set_book_genre_true(self, books_collector, name, genre):
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert books_collector.get_book_genre(name) == genre

    @pytest.mark.parametrize('name', ['Alice in Wonderland', 'Dracula'])
    def test_get_book_genre_true(self, books_collector, name):
        genre = books_collector.get_book_genre(name)
        assert genre is None

    def test_get_books_with_specific_genre_true(self, books_collector):
        books_collector.add_new_book('Dracula')
        books_collector.set_book_genre('Dracula', 'Ужасы')
        books_collector.add_new_book('Sherlock Holmes')
        books_collector.set_book_genre('Sherlock Holmes', 'Детективы')
        assert books_collector.get_books_with_specific_genre('Ужасы') == ['Dracula']
        assert books_collector.get_books_with_specific_genre('Детективы') == ['Sherlock Holmes']

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

    def test_get_books_genre_true(self, books_collector):
        assert books_collector.get_books_genre() == books_collector.books_genre

    def test_get_books_for_children_true(self, books_collector):
        books_collector.add_new_book('Alice in Wonderland')
        books_collector.set_book_genre('Alice in Wonderland', 'Мультфильмы')
        books_for_children = books_collector.get_books_for_children()
        assert 'Alice in Wonderland' in books_for_children

    def test_get_list_of_favorites_books_true(self, books_collector):
        books_collector.add_new_book('Alice in Wonderland')
        books_collector.add_new_book('Dracula')
        books_collector.add_book_in_favorites('Alice in Wonderland')
        books_list_of_favorites = books_collector.get_list_of_favorites_books()
        assert 'Alice in Wonderland' in books_list_of_favorites
        assert "Dracula" not in books_list_of_favorites