from pytest import fixture

from backend.npcs import Npc
from backend.sentences import Sentence
from backend.words import Word

@fixture
def test_word():
    return Word(name="test_word")

@fixture
def test_statement(test_word):
    return Sentence([test_word], ".")

@fixture
def test_question(test_word):
    return Sentence([test_word, test_word, test_word], "?")

@fixture
def test_exclamation(test_word):
    return Sentence([test_word, test_word], "!")

@fixture
def incoherent_sentence():
    return Sentence([Word("adjective")], ".")

@fixture
def left_authoritarian_libertarian():
    return Sentence(
        [Word("left"), Word("authoritarian"), Word("libertarian")], "."
    )

@fixture
def subject_verb_object():
    return Sentence([Word("subject"), Word("verb"), Word("object")], ".")

@fixture
def subject_verb():
    return Sentence([Word("subject"), Word("verb")], ".")

@fixture
def yes():
    return Sentence([Word("yes")], ".")

@fixture
def left():
    return Sentence([Word("left")], ".")

@fixture
def right():
    return Sentence([Word("right")], ".")

@fixture
def test_npc():
    return Npc(name="test_npc")