def retrieve_context(query):

    query = query.lower()

    knowledge_base = {

        "stress": [
            "Break large tasks into smaller achievable goals.",
            "Use Pomodoro technique (25 min focus, 5 min break).",
            "Take regular breaks and avoid overload."
        ],

        "anxiety": [
            "Focus on things you can control right now.",
            "Try deep breathing: inhale 4s, hold 4s, exhale 6s.",
            "Challenge negative thoughts with logical reasoning."
        ],

        "future": [
            "Uncertainty about the future is normal.",
            "Focus on small daily improvements.",
            "Set short-term realistic goals instead of overthinking."
        ],

        "sad": [
            "Talk to someone you trust.",
            "Spend time in nature or sunlight.",
            "Maintain healthy sleep and routine."
        ],

        "lonely": [
            "Reach out to friends or family.",
            "Join online/offline communities.",
            "Remember: loneliness is temporary, not permanent."
        ],

        "happy": [
            "Celebrate your achievements.",
            "Share positivity with others.",
            "Practice gratitude journaling."
        ]
    }

    matched_points = []

    # ==================================================
    # SMART MATCHING (MULTI KEYWORD SUPPORT)
    # ==================================================
    for keyword, points in knowledge_base.items():
        if keyword in query:
            matched_points.extend(points)

    # ==================================================
    # IF MATCH FOUND → RETURN VARIED OUTPUT
    # ==================================================
    if matched_points:
        return "\n".join(f"• {point}" for point in matched_points)

    # ==================================================
    # DEFAULT FALLBACK (IMPORTANT)
    # ==================================================
    return """
• Maintain a healthy sleep schedule  
• Exercise regularly to improve mood  
• Stay hydrated throughout the day  
• Practice mindfulness and deep breathing  
"""
