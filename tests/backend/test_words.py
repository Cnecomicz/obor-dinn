from fixtures import test_word

from backend.words import Role, Topic

# A Word can be created with required metadata
def test_word_creation(test_word):
    assert test_word.name == "test_word"
    assert Role.OBJECT in test_word.roles
    assert test_word.ideology_vector == (-1, -1)
    assert Topic.TEST in test_word.topics