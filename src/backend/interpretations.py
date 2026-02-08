from __future__ import annotations
from enum import Enum, auto
from itertools import product
from typing import TYPE_CHECKING

from backend.words import Role

if TYPE_CHECKING:
    from backend.sentences import Sentence

class SpeechAct:
    ASK = auto()
    ASSERT = auto()
    EXCLAIM = auto()


class Interpretation:
    def __init__(self, sentence: Sentence):
        self.sentence = sentence

    @property
    def coherence(self) -> float:
        sentence_roles = [word.roles for word in self.sentence.words]
        valid_patterns = (
            {Role.SUBJECT, Role.VERB, Role.OBJECT},
            {Role.SUBJECT, Role.VERB}
        )
        for roles in product(*sentence_roles):
            if any(pattern.issubset(set(roles)) for pattern in valid_patterns):
                return 1 
        return 0

    @property
    def ideology_vector(self) -> tuple[int, int]:
        return tuple(
            map(
                sum, 
                zip(*[word.ideology_vector for word in self.sentence.words])
            )
        )

    @property
    def speech_act(self) -> str:
        match self.sentence.punctuation:
            case "?":
                return SpeechAct.ASK
            case ".":
                return SpeechAct.ASSERT
            case "!":
                return SpeechAct.EXCLAIM

