from transformers import pipeline

classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

def detect_emotion(text):
    result = classifier(text)

    best = max(result, key=lambda x: x["score"])

    return {
        "emotion": best["label"],
        "confidence": round(best["score"] * 100, 2)
    }