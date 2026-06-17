def check_crisis(text):
    keywords = [
        "suicide", "kill myself", "end my life",
        "self harm", "want to die", "hopeless"
    ]

    text = text.lower()
    return any(k in text for k in keywords)