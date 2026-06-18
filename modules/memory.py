import os
import sqlite3

# ==========================================

# DATABASE PATH

# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(**file**))
DB_PATH = os.path.join(BASE_DIR, "mindmate.db")

# ==========================================

# INITIALIZE DATABASE

# ==========================================

def init_db():

```
conn = sqlite3.connect(
    DB_PATH,
    check_same_thread=False
)

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
```

# ==========================================

# SAVE EMOTION

# ==========================================

def save_message(emotion):

```
conn = sqlite3.connect(
    DB_PATH,
    check_same_thread=False
)

cur = conn.cursor()

cur.execute(
    """
    INSERT INTO emotions(emotion)
    VALUES(?)
    """,
    (emotion,)
)

conn.commit()
conn.close()
```

# ==========================================

# LOAD ALL HISTORY

# ==========================================

def load_history():

```
conn = sqlite3.connect(
    DB_PATH,
    check_same_thread=False
)

cur = conn.cursor()

cur.execute("""
SELECT emotion, timestamp
FROM emotions
ORDER BY id DESC
""")

rows = cur.fetchall()

conn.close()

return rows
```

# ==========================================

# GET TOTAL CONVERSATIONS

# ==========================================

def get_total_conversations():

```
conn = sqlite3.connect(
    DB_PATH,
    check_same_thread=False
)

cur = conn.cursor()

cur.execute(
    "SELECT COUNT(*) FROM emotions"
)

total = cur.fetchone()[0]

conn.close()

return total
```

# ==========================================

# GET MOST COMMON EMOTION

# ==========================================

def get_top_emotion():

```
conn = sqlite3.connect(
    DB_PATH,
    check_same_thread=False
)

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
```
