class Sentence:
    def __init__(
        self,
        words: list[str],
        punctuation: str
    ):
        if 1 <= len(words) <= 3:
            self.words = words
            self.punctuation = punctuation
        else:
            raise ValueError(f"Invalid number of {words=}.")
