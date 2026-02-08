from fixtures import (
    left_authoritarian_libertarian, 
    test_exclamation, 
    test_question, 
    test_statement, 
    test_word
)

from backend.interpretations import Interpretation, SpeechAct


# Punctuation determines speech act
def test_speech_acts(test_exclamation, test_question, test_statement):
    result1 = Interpretation(sentence=test_question)
    assert result1.speech_act == SpeechAct.ASK
    result2 = Interpretation(sentence=test_statement)
    assert result2.speech_act == SpeechAct.ASSERT
    result3 = Interpretation(sentence=test_exclamation)
    assert result3.speech_act == SpeechAct.EXCLAIM

# Ideology is aggregated from words
def test_ideology_vector_aggregates_word_values(left_authoritarian_libertarian):
    result = Interpretation(left_authoritarian_libertarian)
    assert result.ideology_vector == (-1, 0)

