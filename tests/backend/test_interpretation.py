from fixtures import test_word, test_question

from backend.interpretation import interpret


# Punctuation determines speech act
def test_question_mark_creates_ask_speech_act(test_question):
    result = interpret(sentence=test_question, topic=None, state=None)
    assert result.speech_act == "ASK"
