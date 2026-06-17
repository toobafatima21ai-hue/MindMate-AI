def check_crisis(text):
    keywords = ["suicide", "kill myself", "die", "end my life", "self harm"]

    text = text.lower()

    return any(k in text for k in keywords)