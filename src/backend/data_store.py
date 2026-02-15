from __future__ import annotations
from os import path, remove
from sqlite3 import connect
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sqlite3 import Connection

class DatabaseDONOTIMPORT:
    def __init__(self) -> None:
        self.connection = None
        self.db_path = "data/backend/words_and_responses.db"

    def close(self) -> None:
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def execute_sql_file(self, sql_path: str) -> None:
        with open(sql_path, "r", encoding="utf-8") as file:
            sql_script = file.read()
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.executescript(sql_script)
        connection.commit()

    def get_connection(self) -> Connection:
        if self.connection is None:
            self.connection = connect(self.db_path)
            self.connection.execute("PRAGMA foreign_keys = ON;")
        return self.connection

    def reset(self) -> None:
        self.close()
        if path.exists(self.db_path):
            remove(self.db_path)
        self.execute_sql_file("data/backend/generate_schema.sql")
        print("Database created.")
        self.execute_sql_file("data/backend/populate_tables.sql")
        print("Database populated.")
        

DatabaseSingleton = DatabaseDONOTIMPORT()
 
if __name__ == "__main__":
    DatabaseSingleton.reset()

