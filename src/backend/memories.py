from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from backend.sentences import Sentence

class Memory:
    def __init__(self) -> None:
        self.log = []

    def add(self, sentence: Sentence) -> None:
        self.log.append(sentence)