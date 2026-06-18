from datetime import datetime
 

def generate_response(user_input, emotion, context):

    pakistan = pytz.timezone("Asia/Karachi")

    current_time = datetime.now(
        pakistan
    ).strftime("%I:%M %p")

    emotion_responses = {

        "joy":
        f"""
💙 MindMate AI Support

That's wonderful to hear.

Positive moments deserve recognition and appreciation.

📚 Wellness Insight:
{context}

🌱 Challenge:
Write down one thing you're grateful for today.

🕒 Time: {current_time}
""",

        "fear":
        f"""
💙 MindMate AI Support

It sounds like uncertainty is weighing on your mind.

Fear often grows when we focus on outcomes we cannot fully control.

📚 Wellness Insight:
{context}

🌱 Challenge:
Focus on one small action you can take today.

🕒 Time: {current_time}
""",

        "sadness":
        f"""
💙 MindMate AI Support

I'm sorry you're having a difficult time.

Remember that difficult emotions are temporary.

📚 Wellness Insight:
{context}

🌱 Challenge:
Reach out to someone you trust.

🕒 Time: {current_time}
""",

        "anger":
        f"""
💙 MindMate AI Support

It sounds like something has frustrated or upset you.

Taking a pause before reacting can help.

📚 Wellness Insight:
{context}

🌱 Challenge:
Take a 5-minute walk or breathing break.

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
Take care of yourself today.

🕒 Time: {current_time}
"""
    )
