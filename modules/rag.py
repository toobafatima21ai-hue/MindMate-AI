def retrieve_context(query):

    query = query.lower()

    knowledge = {

        "stress": """
Break large tasks into smaller goals.
Use the Pomodoro technique.
Take regular short breaks.
""",

        "anxiety": """
Focus on what you can control.
Practice deep breathing exercises.
Challenge catastrophic thinking.
""",

        "future": """
Uncertainty about the future is normal.
Focus on short-term achievable goals.
Take one step at a time.
""",

        "sad": """
Talk to someone you trust.
Spend time outdoors.
Maintain healthy routines.
""",

        "lonely": """
Reach out to a friend or family member.
Join communities with similar interests.
Remember that loneliness is temporary.
""",

        "happy": """
Celebrate your achievements.
Share your happiness with others.
Practice gratitude journaling.
"""
    }

    for keyword, value in knowledge.items():

        if keyword in query:
            return value

    return """
Maintain healthy sleep habits.
Exercise regularly.
Stay hydrated.
Practice mindfulness.
"""
