from datetime import datetime


def generate_response(user_input, emotion, context):

    # simple system time (no pytz → avoids errors)
    current_time = datetime.now().strftime("%I:%M %p")

    emotion_responses = {

        "joy": f"""
💙 MindMate AI Support

That's wonderful to hear 😊

Positive emotions are very important for mental well-being.

📚 Wellness Insight:
{context}

🌱 Challenge:
Write down one thing you're grateful for today.

🕒 Time: {current_time}
""",

        "fear": f"""
💙 MindMate AI Support

It sounds like you're feeling anxious or uncertain.

Fear is a natural response, but it can be managed step by step.

📚 Wellness Insight:
{context}

🌱 Challenge:
Focus on one small thing you can control today.

🕒 Time: {current_time}
""",

        "sadness": f"""
💙 MindMate AI Support

I'm really sorry you're feeling low right now.

It's okay to feel this way — emotions are temporary.

📚 Wellness Insight:
{context}

🌱 Challenge:
Talk to someone you trust or write your thoughts down.

🕒 Time: {current_time}
""",

        "anger": f"""
💙 MindMate AI Support

It sounds like you're feeling upset or frustrated.

Take a moment before reacting — breathe slowly.

📚 Wellness Insight:
{context}

🌱 Challenge:
Step away for a few minutes and relax your mind.

🕒 Time: {current_time}
"""
    }

    return emotion_responses.get(
        emotion.lower(),
        f"""
💙 MindMate AI Support

Thank you for sharing your feelings.

📚 Wellness Insight:
{context}

🌱 Small Action:
Take care of yourself today — one step at a time.

🕒 Time: {current_time}
"""
    )
