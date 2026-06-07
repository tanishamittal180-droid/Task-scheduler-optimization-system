import sqlite3


class AuditLog:

    def __init__(self, db="database/scheduler.db"):

        self.db = db

    def log(self, action):

        conn = sqlite3.connect(self.db)

        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS audit(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            action TEXT
        )
        """)

        cursor.execute(
            "INSERT INTO audit(action) VALUES(?)",
            (action,)
        )

        conn.commit()

        conn.close()