import sqlite3
import os

DB_PATH = "data/memory.db"

def init_db():

    os.makedirs("data", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS emotions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            emotion TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_message(emotion):

    conn = sqlite3.connect(DB_PATH)

    cur = conn.cursor()

    cur.execute(
        "INSERT INTO emotions (emotion) VALUES (?)",
        (emotion,)
    )

    conn.commit()
    conn.close()


def load_history():

    conn = sqlite3.connect(DB_PATH)

    cur = conn.cursor()

    cur.execute(
        "SELECT emotion FROM emotions"
    )

    data = cur.fetchall()

    conn.close()

    return data