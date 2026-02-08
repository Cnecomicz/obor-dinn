from pytest import fixture

from backend.sentences import Sentence
from backend.words import Word

@fixture
def test_word():
    return Word(name="test_word")

@fixture
def test_statement(test_word):
    return Sentence([test_word, test_word, test_word], ".")

@fixture
def test_question(test_word):
    return Sentence([test_word,], "?")

@fixture
def test_exclamation(test_word):
    return Sentence([test_word, test_word], "!")
