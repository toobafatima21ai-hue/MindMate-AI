from datetime import datetime

def generate_response(user_input, emotion, context):

    emotion = emotion.lower()

    responses = {
        "sadness": (
            "I'm sorry you're feeling this way. "
            "It may help to talk with someone you trust, take a short break, "
            "or write down what is bothering you."
        ),

        "anger": (
            "It sounds like you're frustrated. "
            "Taking a few deep breaths or stepping away from the situation "
            "for a short time may help."
        ),

        "fear": (
            "Feeling worried or afraid can be overwhelming. "
            "Try focusing on what is within your control and take things one step at a time."
        ),

        "joy": (
            "It's wonderful that you're feeling positive. "
            "Take a moment to appreciate what contributed to this feeling."
        ),

        "love": (
            "Strong positive connections can be very meaningful. "
            "Nurturing supportive relationships often improves well-being."
        ),

        "surprise": (
            "Unexpected situations can bring many emotions. "
            "Take some time to process what happened."
        )
    }

    base_response = responses.get(
        emotion,
        "Thank you for sharing how you're feeling. "
        "Your emotions are valid, and it's important to take care of yourself."
    )

    final_response = f"""
💙 MindMate AI Support

I understand that you may be experiencing **{emotion}**.

{base_response}

📚 Wellness Insight:
{context}

🌱 Small Action for Today:
Take 5 minutes to focus on yourself, whether through deep breathing,
stretching, journaling, or a short walk.

⚠️ Reminder:
MindMate AI provides emotional support and wellness guidance only.
It is not a substitute for professional mental health care.

Time: {datetime.now().strftime("%H:%M")}
"""

    return final_response