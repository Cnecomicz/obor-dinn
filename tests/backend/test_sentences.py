from pytest import raises

from fixtures import (
    left_authoritarian_libertarian,
    subject_verb, 
    subject_verb_object, 
    test_exclamation, 
    test_question, 
    test_statement, 
    test_word,
    yes
)

from backend.sentences import Sentence, SpeechAct

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

# Punctuation determines speech act
def test_speech_acts(test_exclamation, test_question, test_statement):
    assert test_question.speech_act == SpeechAct.ASK
    assert test_statement.speech_act == SpeechAct.ASSERT
    assert test_exclamation.speech_act == SpeechAct.EXCLAIM

# Ideology is aggregated from words
def test_ideology_vector_aggregates_word_values(
    left_authoritarian_libertarian
):
    assert left_authoritarian_libertarian.ideology_vector == (-1, 0)

# Sentence is evaluated for coherency
def test_subject_verb_object_is_highly_coherent(subject_verb_object):
    assert subject_verb_object.coherence == 1

# Sentence is evaluated for coherency
def test_subject_verb_is_highly_coherent(subject_verb):
    assert subject_verb.coherence == 1

# Sentence is evaluated for coherency
def test_one_word_with_all_roles_is_not_very_coherent(test_statement):
    assert test_statement.coherence < 1

# Sentence is evaluated for coherency
def test_some_words_can_stand_alone(yes):
    assert yes.coherence == 1