from backend.words import Ideology, Word

# A Word can be created with required metadata
def test_word_creation():
    word = Word(
        id="testword",
        roles={"subject", "verb", "object", "other"},
        ideology={Ideology.LEFT: 1, Ideology.LIBERTARIAN: 1},
        rhetoric={"testrhetoric1", "testrhetoric2"},
        topic={"testtopic1", "testtopic2"}
    )

    assert word.id == "testword"
    assert "object" in word.roles
    assert word.ideology_vector == (-1, -1)
    assert "testrhetoric2" in word.rhetoric
    assert "testtopic1" in word.topic