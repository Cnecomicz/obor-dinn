from collections import defaultdict
from enum import Enum, auto

from backend.data_store import WORDS_CACHE

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
    def __init__(self, name: str) -> None:
        self.name = name
        word_data = WORDS_CACHE[name]
        self.roles = {
            Role[role] 
            for role in word_data["roles"]
        }
        self.ideology = {          
            Ideology[ideology]: value
            for ideology, value in word_data["ideology"].items()
        }
        self.rhetoric = word_data["rhetoric"]
        self.topic = word_data["topic"]

    @property
    def ideology_vector(self) -> tuple[int, int]:
        return (
            self.ideology.get(Ideology.RIGHT, 0)
            - self.ideology.get(Ideology.LEFT, 0),
            self.ideology.get(Ideology.AUTHORITARIAN, 0)
            - self.ideology.get(Ideology.LIBERTARIAN, 0)
        )
