from fixtures import test_word

from backend.words import Role

# A Word can be created with required metadata
def test_word_creation(test_word):
    assert test_word.name == "test_word"
    assert Role.OBJECT in test_word.roles
    assert test_word.ideology_vector == (-1, -1)
    assert "testrhetoric2" in test_word.rhetoric
    assert "testtopic1" in test_word.topic