import os

DATA_PATH = os.path.join("data", "wellness_knowledge.txt")


def load_docs():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return f.readlines()


def retrieve_context(query: str):
    docs = load_docs()

    query = query.lower()

    # simple keyword-based retrieval (safe + reliable for students)
    matched = []

    for doc in docs:
        if any(word in doc.lower() for word in query.split()):
            matched.append(doc.strip())

    # if nothing matches, still return useful fallback
    if not matched:
        return "Try breathing exercises, hydration, sleep routine, and journaling for emotional balance."

    return "\n".join(matched[:5])