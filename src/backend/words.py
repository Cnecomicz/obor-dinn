class Word:
    def __init__(
        self, 
        id: str, 
        roles: set[str], 
        ideology: dict[str, int], 
        rhetoric: set[str], 
        topic: set[str]
    ):
        self.id = id
        self.roles = roles
        self.ideology = ideology
        self.rhetoric = rhetoric
        self.topic = topic

