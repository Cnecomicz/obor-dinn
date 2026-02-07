from collections import defaultdict
from enum import Enum, auto
from yaml import safe_load

class Ideology(Enum):
    LEFT = auto()
    RIGHT = auto()
    LIBERTARIAN = auto()
    AUTHORITARIAN = auto()


class Role(Enum):
    SUBJECT = auto()
    VERB = auto()
    OBJECT = auto()
    OTHER = auto()


class Word:
    def __init__(self, name: str):
        self.name = name
        with open("data/backend/words.yaml", "r") as file:
            word_data = safe_load(file)[name]
        self.roles = {
            Role[role] 
            for role in word_data["roles"]
            }
        self._ideology = defaultdict(
            int,
            {          
                Ideology[ideology]: value
                for ideology, value in word_data["ideology"].items()
            }
        )
        self.ideology_vector = (
            self._ideology[Ideology.RIGHT]-self._ideology[Ideology.LEFT], 
            self._ideology[Ideology.AUTHORITARIAN]-self._ideology[Ideology.LIBERTARIAN]
        )
        self.rhetoric = word_data["rhetoric"]
        self.topic = word_data["topic"]

