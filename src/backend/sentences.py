from __future__ import annotations
from enum import Enum, auto
from itertools import product
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from backend.words import Word

from backend.words import Role

class SpeechAct(Enum):
    ASK = auto()
    ASSERT = auto()
    EXCLAIM = auto()


class Sentence:
    def __init__(
        self,
        words: list[Word],
        punctuation: str
    ) -> None:
        if 1 <= len(words) <= 3:
            self.words = words
            self.punctuation = punctuation
        else:
            raise ValueError(f"Invalid number of {words=}.")

    @property
    def coherence(self) -> float:
        sentence_roles = [word.roles for word in self.words]
        valid_patterns = (
            {Role.SUBJECT, Role.VERB, Role.OBJECT},
            {Role.SUBJECT, Role.VERB},
            {Role.ANSWER}
        )
        score = 0
        for selection in product(*sentence_roles):
            structural = max(
                len(set(selection) & pattern) / len(pattern)
                for pattern in valid_patterns
            )
            dispersion = len(set(selection)) / len(selection)
            score = max(score, structural * dispersion)
        return score

    @property
    def ideology_vector(self) -> tuple[float, float]:
        return tuple(
            map(
                sum, 
                zip(*[word.ideology_vector for word in self.words])
            )
        )

    @property
    def speech_act(self) -> str:
        match self.punctuation:
            case "?":
                return SpeechAct.ASK
            case ".":
                return SpeechAct.ASSERT
            case "!":
                return SpeechAct.EXCLAIM
