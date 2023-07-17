import pytest
from movies import Movie, MovieSorter


@pytest.fixture
def movies():
    return [
        Movie("The Avengers", 2012, ["Action", "Adventure", "Sci-Fi"]),
        Movie("Anchorman: The Legend of Ron Burgundy", 2004, ["Comedy"]),
        Movie("The Dark Knight", 2008, ["Action", "Crime", "Drama"]),
    ]


def test_sort_by_year_descending(movies):
    sorted_movies = MovieSorter.sort_by_year_descending(movies)
    years = [movie.year for movie in sorted_movies]
    assert years == [2012, 2008, 2004]


def test_sort_alphabetically_ignoring_articles(movies):
    sorted_movies = MovieSorter.sort_alphabetically_ignoring_articles(movies)
    titles = [movie.title for movie in sorted_movies]
    assert titles == ["Anchorman: The Legend of Ron Burgundy", "The Avengers", "The Dark Knight"]
