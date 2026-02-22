from __future__ import annotations
from random import choice
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from backend.npcs import Npc
    from backend.sentences import Sentence

class ResponseSelector:
    def __init__(self, npc: Npc, sentence: Sentence) -> None:
        self.npc = npc
        self.sentence = sentence

    @property
    def selected_response(self) -> str:
        if self.sentence.coherence < self.npc.min_coherence:
            for key, value in self.npc.incoherent_responses.items():
                if key[0] < self.npc.sentiment < key[1]:
                    return choice(value)
