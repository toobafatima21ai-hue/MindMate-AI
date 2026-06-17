import sqlite3
import os

# make sure data folder exists
os.makedirs("data", exist_ok=True)

DB_PATH = "data/mindmate.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_text TEXT,
            emotion TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_message(user_text, emotion):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO messages (user_text, emotion) VALUES (?, ?)",
        (user_text, emotion)
    )

    conn.commit()
    conn.close()


def load_history():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT emotion FROM messages")
    data = cur.fetchall()

    conn.close()
    return data
