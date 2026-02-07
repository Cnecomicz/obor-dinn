from pytest import fixture

from backend.words import Ideology, Word

@fixture
def word():
    return Word(
        id="testword",
        roles={"subject", "verb", "object", "other"},
        ideology={Ideology.LEFT: 1, Ideology.LIBERTARIAN: 1},
        rhetoric={"testrhetoric1", "testrhetoric2"},
        topic={"testtopic1", "testtopic2"}
    )