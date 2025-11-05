import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_path="generated_strings.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self._create_table()

    def _create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS generated_strings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    value TEXT NOT NULL,
                    length INTEGER NOT NULL,
                    created_at TEXT DEFAULT (datetime('now'))
                );
            """)

    def insert_string(self, value, length):
        with self.conn:
            self.conn.execute(
                "INSERT INTO generated_strings (value, length) VALUES (?, ?);",
                (value, length)
            )

    def get_recent_strings(self, ):
        cur = self.conn.cursor()
        cur.execute(
            "SELECT value, length, created_at FROM generated_strings" \
            ";",
        
        )
        return cur.fetchall()

    def close(self):
        if self.conn:
            self.conn.close()

       
