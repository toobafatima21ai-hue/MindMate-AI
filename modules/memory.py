import os
import sqlite3

# ==================================================
# DATABASE PATH
# ==================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "mindmate.db")

# ==================================================
# INIT DATABASE
# ==================================================
def init_db():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS emotions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        emotion TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

# ==================================================
# SAVE EMOTION
# ==================================================
def save_message(emotion):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO emotions (emotion) VALUES (?)",
        (emotion,)
    )

    conn.commit()
    conn.close()

# ==================================================
# LOAD HISTORY (FIXED FOR STREAMLIT ANALYTICS)
# ==================================================
def load_history():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cur = conn.cursor()

    cur.execute("""
    SELECT emotion, timestamp
    FROM emotions
    ORDER BY id ASC
    """)

    rows = cur.fetchall()
    conn.close()

    return rows

# ==================================================
# RESET DATABASE (OPTIONAL BUT VERY USEFUL)
# ==================================================
def clear_history():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cur = conn.cursor()

    cur.execute("DELETE FROM emotions")

    conn.commit()
    conn.close()

# ==================================================
# TOTAL CONVERSATIONS
# ==================================================
def get_total_conversations():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM emotions")

    total = cur.fetchone()[0]

    conn.close()
    return total

# ==================================================
# MOST COMMON EMOTION
# ==================================================
def get_top_emotion():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cur = conn.cursor()

    cur.execute("""
    SELECT emotion, COUNT(*)
    FROM emotions
    GROUP BY emotion
    ORDER BY COUNT(*) DESC
    LIMIT 1
    """)

    result = cur.fetchone()
    conn.close()

    if result:
        return result[0]

    return "No Data"
