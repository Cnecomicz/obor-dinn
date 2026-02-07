from backend.words import Word

# A Word can be created with required metadata
def test_word_creation():
    word = Word(
        id="testword",
        roles={"subject", "verb", "object", "other"},
        ideology={"left-right": 1, "libertarian-authoritarian": 1},
        rhetoric={"testrhetoric1", "testrhetoric2"},
        topic={"testtopic1", "testtopic2"}
    )

    assert word.id == "testword"
    assert "object" in word.roles
    assert word.ideology["libertarian-authoritarian"] == 1
    assert "testrhetoric2" in word.rhetoric
    assert "testtopic1" in word.topic