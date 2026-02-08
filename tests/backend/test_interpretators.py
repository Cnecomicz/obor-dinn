from fixtures import test_statement, test_word

from backend.interpretators import Interpretator
from backend.words import Topic

# Sentence is evaluated to be on topic
def test_statements_matching_conversation_topic_have_high_relevance(
    test_statement
):
    result = Interpretator(sentence=test_statement, topics={Topic.TEST})
    assert result.relevance > 0.75
