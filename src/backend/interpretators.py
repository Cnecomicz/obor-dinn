from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from backend.sentences import Sentence
    from backend.words import Topic


class Interpretator:
    def __init__(self, sentence: Sentence, topics: set[Topic]):
        self.sentence = sentence
        self.topics = topics

    @property
    def relevance(self) -> float:
        if not self.topics:
            return 0
        matches = 0
        for word in self.sentence.words:
            if self.topics & word.topics:
                matches += 1
        return matches / len(self.sentence.words)
        
# flow:
# X say a sentence 
# X score it on metrics like ideology, coherence
# X it evaluates relevance for the given conversation moment
# it logs and can remember statements
# it selects a response as a function of above data
# repeat