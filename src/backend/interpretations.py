from __future__ import annotations
from enum import Enum, auto
from itertools import product
from typing import TYPE_CHECKING

from backend.words import Role, Topic

if TYPE_CHECKING:
    from backend.sentences import Sentence

class SpeechAct:
    ASK = auto()
    ASSERT = auto()
    EXCLAIM = auto()


class Interpretation:
    def __init__(self, sentence: Sentence, topics: set[Topic]):
        self.sentence = sentence
        self.topics = topics

    @property
    def coherence(self) -> float:
        sentence_roles = [word.roles for word in self.sentence.words]
        valid_patterns = (
            {Role.SUBJECT, Role.VERB, Role.OBJECT},
            {Role.SUBJECT, Role.VERB}
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
    def ideology_vector(self) -> tuple[int, int]:
        return tuple(
            map(
                sum, 
                zip(*[word.ideology_vector for word in self.sentence.words])
            )
        )

    @property
    def relevance(self) -> float:
        if not self.topics:
            return 0
        matches = 0
        for word in self.sentence.words:
            if self.topics & word.topics:
                matches += 1
        return matches / len(self.sentence.words)

    @property
    def speech_act(self) -> str:
        match self.sentence.punctuation:
            case "?":
                return SpeechAct.ASK
            case ".":
                return SpeechAct.ASSERT
            case "!":
                return SpeechAct.EXCLAIM
        
