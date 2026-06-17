import streamlit as st
import pandas as pd
import plotly.express as px

from modules.llm import generate_response
from modules.emotion import detect_emotion
from modules.crisis import check_crisis
from modules.memory import init_db, save_message, load_history
from modules.rag import retrieve_context

# ==================================================
# DATABASE INITIALIZATION
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
# CUSTOM CSS
# ==================================================
st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(
        135deg,
        #E3F2FD,
        #F8F9FA
    );
}

/* Titles */
h1 {
    color: #1565C0 !important;
    text-align: center;
    font-weight: 800;
}

h2, h3 {
    color: #0D47A1 !important;
}

/* Text */
p, label {
    color: #212121 !important;
}

/* Chat Input */
textarea {
    background-color: white !important;
    color: black !important;
    border-radius: 12px !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(
        90deg,
        #42A5F5,
        #1E88E5
    ) !important;

    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: bold !important;
}

/* Metric Cards */
[data-testid="metric-container"] {
    background-color: white;
    border-radius: 12px;
    padding: 15px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #ffffff;
}

/* Charts */
.js-plotly-plot {
    background-color: white;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# HEADER
# ==================================================
st.markdown("""
<h1>💛🧘 MindMate AI</h1>

<h4 style='text-align:center;color:#555;'>
Your Emotional Support & Wellness Companion 💙
</h4>
""", unsafe_allow_html=True)

# ==================================================
# SESSION STATE
# ==================================================
if "messages" not in st.session_state:
    st.session_state.messages = []

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
user_input = st.chat_input(
    "How are you feeling today?"
)

if user_input:

    # USER MESSAGE
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.write(user_input)

    # ==================================================
    # CRISIS DETECTION
    # ==================================================
    if check_crisis(user_input):

        response = """
⚠️ Crisis Detected

Please contact:

• Emergency Services
• A Mental Health Professional
• A Trusted Friend or Family Member

You do not need to handle this alone.
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

        st.info(
            f"Detected Emotion: {emotion} ({confidence:.2f}%)"
        )

        # ==================================================
        # RAG KNOWLEDGE RETRIEVAL
        # ==================================================
        context = retrieve_context(user_input)

        with st.expander(
            "📚 Wellness Knowledge Used"
        ):
            st.write(context)

        # ==================================================
        # RESPONSE GENERATION
        # ==================================================
        response = generate_response(
            user_input,
            emotion,
            context
        )

        with st.chat_message("assistant"):
            st.write(response)

        # ==================================================
        # SAVE TO DATABASE
        # ==================================================
        save_message(emotion)

    # ==================================================
    # SAVE CHAT
    # ==================================================
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

# ==================================================
# ANALYTICS
# ==================================================
st.divider()

st.header("📊 Mood Analytics Dashboard")

history = load_history()

if history:

    df = pd.DataFrame(
        history,
        columns=["Emotion"]
    )

    emotion_counts = (
        df["Emotion"]
        .value_counts()
        .reset_index()
    )

    emotion_counts.columns = [
        "Emotion",
        "Count"
    ]

    col1, col2 = st.columns(2)

    # =====================================
    # BAR CHART
    # =====================================
    with col1:

        fig_bar = px.bar(
            emotion_counts,
            x="Emotion",
            y="Count",
            color="Emotion",
            title="Emotion Distribution"
        )

        st.plotly_chart(
            fig_bar,
            use_container_width=True
        )

    # =====================================
    # PIE CHART
    # =====================================
    with col2:

        fig_pie = px.pie(
            emotion_counts,
            names="Emotion",
            values="Count",
            title="Emotion Breakdown"
        )

        st.plotly_chart(
            fig_pie,
            use_container_width=True
        )

    # =====================================
    # WELLNESS SCORE
    # =====================================
    positive_emotions = [
        "joy",
        "happy",
        "love",
        "optimism"
    ]

    positive_count = sum(
        1
        for item in history
        if item[0].lower() in positive_emotions
    )

    score = min(
        positive_count * 10,
        100
    )

    st.subheader("🌟 Wellness Score")

    st.progress(score / 100)

    st.success(
        f"Current Wellness Score: {score}/100"
    )

else:

    st.info(
        "No emotion history available yet."
    )