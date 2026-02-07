from collections import defaultdict
from enum import Enum

class Ideology(Enum):
    LEFT = "left"
    RIGHT = "right"
    LIBERTARIAN = "libertarian"
    AUTHORITARIAN = "authoritarian"

class Word:
    def __init__(
        self, 
        id: str, 
        roles: set[str], 
        ideology: dict[Ideology, int], 
        rhetoric: set[str], 
        topic: set[str]
    ):
        self.id = id
        self.roles = roles
        self._ideology = defaultdict(int, ideology)
        self.ideology_vector = (
            self._ideology[Ideology.RIGHT]-self._ideology[Ideology.LEFT], 
            self._ideology[Ideology.AUTHORITARIAN]-self._ideology[Ideology.LIBERTARIAN]
        )
        self.rhetoric = rhetoric
        self.topic = topic

