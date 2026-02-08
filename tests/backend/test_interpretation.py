from fixtures import (
    left_authoritarian_libertarian, 
    subject_verb,
    subject_verb_object,
    test_exclamation, 
    test_question, 
    test_statement, 
    test_word
)

from backend.interpretations import Interpretation, SpeechAct
from backend.words import Topic

# Punctuation determines speech act
def test_speech_acts(test_exclamation, test_question, test_statement):
    result1 = Interpretation(sentence=test_question, topics=set())
    assert result1.speech_act == SpeechAct.ASK
    result2 = Interpretation(sentence=test_statement, topics=set())
    assert result2.speech_act == SpeechAct.ASSERT
    result3 = Interpretation(sentence=test_exclamation, topics=set())
    assert result3.speech_act == SpeechAct.EXCLAIM

# Ideology is aggregated from words
def test_ideology_vector_aggregates_word_values(
    left_authoritarian_libertarian
):
    result = Interpretation(
        sentence=left_authoritarian_libertarian, topics=set()
    )
    assert result.ideology_vector == (-1, 0)

# Sentence is evaluated for coherency
def test_subject_verb_object_is_highly_coherent(subject_verb_object):
    result = Interpretation(sentence=subject_verb_object, topics=set())
    assert result.coherence == 1

# Sentence is evaluated for coherency
def test_subject_verb_is_highly_coherent(subject_verb):
    result = Interpretation(sentence=subject_verb, topics=set())
    assert result.coherence == 1

# Sentence is evaluated for coherency
def test_one_word_with_all_roles_is_not_very_coherent(test_statement):
    result = Interpretation(sentence=test_statement, topics=set())
    assert result.coherence < 1

# Sentence is evaluated to be on topic
def test_statements_matching_conversation_topic_have_high_relevance(
    test_statement
):
    result = Interpretation(sentence=test_statement, topics={Topic.TEST})
    assert result.relevance > 0.75
