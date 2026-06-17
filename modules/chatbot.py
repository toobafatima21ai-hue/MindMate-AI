from transformers import pipeline

# Load a SMALL stable model (works on laptop)
generator = pipeline(
    "text-generation",
    model="google/flan-t5-base"
)

SYSTEM_PROMPT = """
You are MindMate AI, a supportive mental health assistant.

Rules:
- Be empathetic and calm
- Do NOT diagnose medical conditions
- Do NOT give medical prescriptions
- Encourage positive coping strategies
"""

def generate_response(user_input, emotion):

    prompt = f"""
{SYSTEM_PROMPT}

Emotion: {emotion}
User: {user_input}

Give a supportive response:
"""

    result = generator(
        prompt,
        max_new_tokens=150,
        do_sample=True,
        temperature=0.7
    )

    return result[0]["generated_text"]