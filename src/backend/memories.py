from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from backend.sentences import Sentence

class Memory:
    def __init__(self) -> None:
        self.log = []
        self.ideology_vector = (0, 0)
        half_life = 10
        self.decay_factor = 1 - 2 ** (-1 / half_life)

    def add(self, sentence: Sentence) -> None:
        self.log.append(sentence)
        self.ideology_vector = (
            self.decay_factor * sentence.ideology_vector[0]
            + (1 - self.decay_factor) * self.ideology_vector[0],
            self.decay_factor*sentence.ideology_vector[1] 
            + (1 - self.decay_factor) * self.ideology_vector[1]
        )