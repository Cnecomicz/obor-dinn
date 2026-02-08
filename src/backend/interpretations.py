from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from backend.sentences import Sentence


class Interpretation:
    def __init__(self, sentence: Sentence):
        self.sentence = sentence

    @property
    def speech_act(self) -> str:
        if self.sentence.punctuation == "?":
            return "ASK"
