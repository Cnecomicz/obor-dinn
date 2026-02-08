from __future__ import annotations
from enum import Enum, auto
from typing import TYPE_CHECKING

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
    def speech_act(self) -> str:
        match self.sentence.punctuation:
            case "?":
                return SpeechAct.ASK
            case ".":
                return SpeechAct.ASSERT
            case "!":
                return SpeechAct.EXCLAIM

