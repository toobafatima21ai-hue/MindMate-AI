import streamlit as st
import pandas as pd
import plotly.express as px

from modules.llm import generate_response
from modules.emotion import detect_emotion
from modules.crisis import check_crisis
from modules.memory import init_db, save_message, load_history
from modules.rag import retrieve_context

# ==================================================
# INIT DATABASE
# ==================================================
init_db()

# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="MindMate AI",
    page_icon="💛🧘",
    layout="wide"
)

# ==================================================
# CUSTOM CSS (LIGHT & CLEAN UI)
# ==================================================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #E3F2FD, #F8F9FA);
}

/* Title */
h1 {
    color: #1565C0 !important;
    text-align: center;
    font-weight: 800;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #42A5F5, #1E88E5) !important;
    color: white !important;
    border-radius: 12px !important;
    border: none !important;
    font-weight: bold !important;
}

/* Metrics */
[data-testid="metric-container"] {
    background-color: white;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# HEADER
# ==================================================
st.markdown("""
<h1>💛🧘 MindMate AI</h1>
<h4 style='text-align:center;color:#555;'>
Your Emotional Support & Wellness Companion
</h4>
""", unsafe_allow_html=True)

# ==================================================
# SESSION STATE (IMPORTANT FIX)
# ==================================================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "emotion_history" not in st.session_state:
    st.session_state.emotion_history = []

# ==================================================
# 🔥 NEW CHAT RESET BUTTON
# ==================================================
if st.button("🆕 New Chat / Reset Session"):
    st.session_state.messages = []
    st.session_state.emotion_history = []
    st.rerun()

# ==================================================
# DASHBOARD CARDS
# ==================================================
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Mood Status", "Active")

with col2:
    st.metric("Support Mode", "Empathetic")

with col3:
    st.metric("AI Assistant", "Online")

st.divider()

# ==================================================
# CHAT HISTORY
# ==================================================
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ==================================================
# CHAT INPUT
# ==================================================
user_input = st.chat_input("How are you feeling today?")

if user_input:

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    # ==================================================
    # CRISIS CHECK
    # ==================================================
    if check_crisis(user_input):

        response = """
⚠️ Crisis Detected

Please contact:
- Emergency Services
- Mental Health Professional
- Trusted Person

You are not alone 💛
"""

        with st.chat_message("assistant"):
            st.error(response)

    else:

        # ==================================================
        # EMOTION DETECTION
        # ==================================================
        emotion_data = detect_emotion(user_input)

        emotion = emotion_data["emotion"]
        confidence = emotion_data["confidence"]

        st.info(f"Detected Emotion: {emotion} ({confidence:.2f}%)")

        # store for analytics (SESSION ONLY = RESET WORKS)
        st.session_state.emotion_history.append(emotion)

        # ==================================================
        # RAG CONTEXT
        # ==================================================
        context = retrieve_context(user_input)

        with st.expander("📚 Wellness Knowledge Used"):
            st.write(context)

        # ==================================================
        # AI RESPONSE
        # ==================================================
        response = generate_response(user_input, emotion, context)

        with st.chat_message("assistant"):
            st.write(response)

        # OPTIONAL: database storage (comment if you want full reset only)
        save_message(emotion)

    # Save assistant message
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

# ==================================================
# ANALYTICS DASHBOARD
# ==================================================
st.divider()
st.header("📊 Mood Analytics Dashboard")

history = st.session_state.emotion_history

if history:

    df = pd.DataFrame(history, columns=["Emotion"])

    emotion_counts = df["Emotion"].value_counts().reset_index()
    emotion_counts.columns = ["Emotion", "Count"]

    col1, col2 = st.columns(2)

    # BAR CHART
    with col1:
        fig_bar = px.bar(
            emotion_counts,
            x="Emotion",
            y="Count",
            color="Emotion",
            title="Emotion Distribution"
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    # PIE CHART
    with col2:
        fig_pie = px.pie(
            emotion_counts,
            names="Emotion",
            values="Count",
            title="Emotion Breakdown"
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    # ==================================================
    # WELLNESS SCORE
    # ==================================================
    positive_emotions = ["joy", "happy", "love", "optimism"]

    positive_count = sum(
        1 for e in history if e.lower() in positive_emotions
    )

    score = min(positive_count * 10, 100)

    st.subheader("🌟 Wellness Score")
    st.progress(score / 100)
    st.success(f"Current Wellness Score: {score}/100")

else:
    st.info("No emotion history available yet.")
