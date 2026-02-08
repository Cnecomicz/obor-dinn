from pytest import fixture

from backend.words import Word

@fixture
def test_word():
    return Word(name="test_word")