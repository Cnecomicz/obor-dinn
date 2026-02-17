from enum import Enum, auto

from backend.data_store import DatabaseSingleton

class Ideology(Enum):
    LEFT = auto()
    RIGHT = auto()
    LIBERTARIAN = auto()
    AUTHORITARIAN = auto()


class Role(Enum):
    SUBJECT = auto()
    VERB = auto()
    OBJECT = auto()
    ADJECTIVE = auto()
    ANSWER = auto()


class Topic(Enum):
    ANSWER = auto()
    TEST = auto()
    todo = auto()


class Word:
    def __init__(self, name: str) -> None:
        self.name = name
        self.roles = set()
        self.ideology = {}
        self.topics = set()

        connection = DatabaseSingleton.get_connection()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT WordId FROM Word WHERE Name = ?
            """,
            (self.name,)
        )
        word_id = cursor.fetchone()[0]

        cursor.execute("""
            SELECT r.Name
            FROM Role r
            JOIN WordRole wr ON r.RoleId = wr.RoleId
            WHERE wr.WordId = ?
            """, 
            (word_id,)
        )
        self.roles = {Role[row[0]] for row in cursor.fetchall()}

        cursor.execute("""
            SELECT i.Name, wi.Value
            FROM Ideology i
            JOIN WordIdeology wi ON i.IdeologyId = wi.IdeologyId
            WHERE wi.WordId = ?
            """, 
            (word_id,)
        )
        self.ideology = {
            Ideology[name]: value
            for name, value in cursor.fetchall()
        }

        cursor.execute("""
            SELECT t.Name
            FROM Topic t
            JOIN WordTopic wt ON t.TopicId = wt.TopicId
            WHERE wt.WordId = ?
            """, 
            (word_id,)
        )
        self.topics = {Topic[row[0]] for row in cursor.fetchall()}

    @property
    def ideology_vector(self) -> tuple[float, float]:
        return (
            self.ideology.get(Ideology.RIGHT, 0)
            - self.ideology.get(Ideology.LEFT, 0),
            self.ideology.get(Ideology.AUTHORITARIAN, 0)
            - self.ideology.get(Ideology.LIBERTARIAN, 0)
        )
