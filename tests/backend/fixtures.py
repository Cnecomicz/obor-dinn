from pytest import fixture

from backend.words import Ideology, Role, Word

@fixture
def test_word():
    return Word(name="test_word")