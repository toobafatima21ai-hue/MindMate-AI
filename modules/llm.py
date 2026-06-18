from datetime import datetime

# ==================================================
# RESPONSE GENERATION ENGINE (RULE-BASED LLM STYLE)
# ==================================================
def generate_response(user_input, emotion, context):

    # system time (simple, no pytz → stable for deployment)
    current_time = datetime.now().strftime("%I:%M %p")

    base_context = context if context else "Focus on general mental wellness and self-care."

    emotion_responses = {

        "joy": f"""
💙 MindMate AI Support

That's wonderful to hear 😊

It's important to acknowledge and appreciate positive emotions.

📚 Wellness Insight:
{base_context}

🌱 Reflection:
Write down 3 things you're grateful for today.

🕒 Time: {current_time}
""",

        "fear": f"""
💙 MindMate AI Support

It sounds like you're experiencing fear or anxiety.

Try to ground yourself in the present moment.

📚 Wellness Insight:
{base_context}

🌱 Exercise:
Focus on one small controllable action today.

🕒 Time: {current_time}
""",

        "sadness": f"""
💙 MindMate AI Support

I'm really sorry you're feeling this way.

Sadness is valid and temporary.

📚 Wellness Insight:
{base_context}

🌱 Support Step:
Talk to someone you trust or express your thoughts in writing.

🕒 Time: {current_time}
""",

        "anger": f"""
💙 MindMate AI Support

It seems you're feeling frustrated or angry.

Taking a pause can help regulate emotions.

📚 Wellness Insight:
{base_context}

🌱 Action Step:
Take a short break, breathe deeply, and reset your mind.

🕒 Time: {current_time}
"""
    }

    # ==================================================
    # DEFAULT RESPONSE (IMPORTANT FOR UNSEEN EMOTIONS)
    # ==================================================
    return emotion_responses.get(
        emotion.lower(),
        f"""
💙 MindMate AI Support

Thank you for sharing how you feel.

Every emotion is valid and important.

📚 Wellness Insight:
{base_context}

🌱 Small Step:
Take care of yourself today — one step at a time.

🕒 Time: {current_time}
"""
    )
