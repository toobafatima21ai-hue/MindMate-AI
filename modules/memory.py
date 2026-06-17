import os
import sqlite3

# ===============================
# DATABASE PATH (SAFE FOR CLOUD)
# ===============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "mindmate.db")


# ===============================
# INIT DATABASE
# ===============================
def init_db():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS emotions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        emotion TEXT
    )
    """)

    conn.commit()
    conn.close()


# ===============================
# SAVE EMOTION
# ===============================
def save_message(emotion):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO emotions (emotion) VALUES (?)",
        (emotion,)
    )

    conn.commit()
    conn.close()


# ===============================
# LOAD HISTORY
# ===============================
def load_history():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cur = conn.cursor()

    cur.execute("SELECT emotion FROM emotions")
    rows = cur.fetchall()

    conn.close()

    return rows
