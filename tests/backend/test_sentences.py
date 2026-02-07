from pytest import raises

from fixtures import word

from backend.sentences import Sentence




# A Sentence stores at most three words
def test_sentence_word_count(word):
    sentence1 = Sentence([word, word, word], ".")
    assert len(sentence1.words) == 3
    sentence2 = Sentence([word, word], "?")
    assert len(sentence2.words) == 2
    sentence3 = Sentence([word], "!")
    assert len(sentence3.words) == 1
    with raises(ValueError):
        Sentence([word, word, word, word], ".")
    with raises(ValueError):
        Sentence([], ".")