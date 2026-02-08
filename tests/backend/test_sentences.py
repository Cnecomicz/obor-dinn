from pytest import raises

from fixtures import test_word

from backend.sentences import Sentence

# A Sentence stores at most three words
def test_sentence_word_count(test_word):
    sentence1 = Sentence([test_word, test_word, test_word], ".")
    assert len(sentence1.words) == 3
    sentence2 = Sentence([test_word, test_word], "?")
    assert len(sentence2.words) == 2
    sentence3 = Sentence([test_word], "!")
    assert len(sentence3.words) == 1
    with raises(ValueError):
        Sentence([test_word, test_word, test_word, test_word], ".")
    with raises(ValueError):
        Sentence([], ".")