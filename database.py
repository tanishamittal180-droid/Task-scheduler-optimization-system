import sqlite3
import os

DB_PATH = "database/scheduler.db"


def get_connection():

    os.makedirs(
        "database",
        exist_ok=True
    )

    conn = sqlite3.connect(
        DB_PATH,
        check_same_thread=False
    )

    return conn


def create_tables():

    conn = get_connection()

    cursor = conn.cursor()

    # Users

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)

    # Tasks
    cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id TEXT,
    task_name TEXT,
    duration INTEGER,
    deadline INTEGER,
    priority INTEGER,
    profit INTEGER,
    dependency TEXT,
    skill_required TEXT,
    assigned_resource TEXT,
    start_time INTEGER,
    finish_time INTEGER,
    status TEXT
)
""")

   

    # Resources

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resources(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        resource_id TEXT,
        resource_name TEXT,
        skill TEXT,
        capacity INTEGER
    )
    """)

    conn.commit()
    conn.close()


create_tables()