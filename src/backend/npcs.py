from backend.data_store import DatabaseSingleton
from backend.memories import Memory

class Npc():
    def __init__(self, name: str) -> None:
        self.name = name
        self.sentiment = 0
        connection = DatabaseSingleton.get_connection()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT NpcId, MinCoherence, IdeologyConsistency 
            FROM Npc 
            WHERE Name = ?
            """,
            (self.name,)
        )
        npc_id, self.min_coherence, self.ideology_consistency = cursor.fetchall()[0]
        cursor.execute("""
            SELECT MinSentiment, MaxSentiment, Response 
            FROM IncoherentResponse
            WHERE NpcId = ?
            """,
            (npc_id,)
        )
        self.incoherent_responses = {}
        for row in cursor.fetchall():
            if (row[0], row[1]) not in self.incoherent_responses:
                self.incoherent_responses[(row[0], row[1])] = []
            self.incoherent_responses[(row[0], row[1])].append(row[2])
        self.memory = Memory()
