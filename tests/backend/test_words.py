from fixtures import word

# A Word can be created with required metadata
def test_word_creation(word):
    assert word.id == "testword"
    assert "object" in word.roles
    assert word.ideology_vector == (-1, -1)
    assert "testrhetoric2" in word.rhetoric
    assert "testtopic1" in word.topic