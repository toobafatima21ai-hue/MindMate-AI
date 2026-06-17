def get_recommendation(emotion):

    recommendations = {
        "joy": "Keep doing what makes you happy! Try journaling positive moments.",
        "sadness": "Try deep breathing or talking to a friend.",
        "anger": "Take a short walk or practice 4-7-8 breathing.",
        "fear": "Ground yourself using the 5-4-3-2-1 technique.",
        "neutral": "Maintain routine and hydration.",
        "stress": "Try mindfulness or a 10-minute break."
    }

    return recommendations.get(emotion.lower(), "Take care of yourself today.")