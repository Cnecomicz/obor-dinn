from fixtures import test_statement, test_word

from backend.memories import Memory

# The game logs your statements
def test_sentences_are_recorded(test_statement):
    memory = Memory()
    memory.add(test_statement)
    assert memory.log[0] == test_statement