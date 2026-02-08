from fixtures import left, right, test_statement, test_word

from backend.memories import Memory

# The NPC logs your statements
def test_sentences_are_recorded(test_statement):
    memory = Memory()
    memory.add(test_statement)
    assert memory.log[0] == test_statement

# The NPC keeps a running total of your ideology
def test_ideology_is_remembered_but_decays(left, right):
    memory = Memory()
    memory.add(left)
    memory.add(left)
    memory.add(left)
    assert memory.ideology_vector[0] < 0
    memory.add(right)
    memory.add(right)
    memory.add(right)
    assert memory.ideology_vector[0] > 0 # strictly greater b/c decay
