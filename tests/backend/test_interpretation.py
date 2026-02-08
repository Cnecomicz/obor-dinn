from fixtures import test_statement, test_word

from backend.interpretations import Interpretation
from backend.words import Topic

# Sentence is evaluated to be on topic
def test_statements_matching_conversation_topic_have_high_relevance(
    test_statement
):
    result = Interpretation(sentence=test_statement, topics={Topic.TEST})
    assert result.relevance > 0.75
