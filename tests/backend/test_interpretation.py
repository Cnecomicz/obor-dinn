from fixtures import test_word, test_question

from backend.interpretations import Interpretation


# Punctuation determines speech act
def test_question_mark_creates_ask_speech_act(test_question):
    result = Interpretation(sentence=test_question)
    assert result.speech_act == "ASK"
