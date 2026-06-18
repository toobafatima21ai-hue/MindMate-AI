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
# CUSTOM CSS
# ==================================================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #E3F2FD,
        #F8F9FA
    );
}

/* Title */
h1 {
    color: #1565C0 !important;
    text-align: center;
    font-weight: 800;
}

/* Text */
p, label, div {
    color: #212121 !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(
        90deg,
        #42A5F5,
        #1E88E5
    ) !important;

    color: white !important;
    border-radius: 12px !important;
    border: none !important;
    font-weight: bold !important;
}

/* Metric Cards */
[data-testid="metric-container"] {
    background-color: white;
    border-radius: 12px;
    padding: 15px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: white;
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
# DISPLAY CHAT HISTORY
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
• Mental Health Professional
• Trusted Friend or Family Member

You are not alone.
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
        # KNOWLEDGE RETRIEVAL
        # ==================================================
        context = retrieve_context(user_input)

        with st.expander(
            "📚 Wellness Knowledge Used"
        ):
            st.write(context)

        # ==================================================
        # AI RESPONSE
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
    # SAVE CHAT HISTORY
    # ==================================================
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

# ==================================================
# ANALYTICS SECTION
# ==================================================
st.divider()

st.header("📊 Mood Analytics Dashboard")

history = load_history()

if history:

    df = pd.DataFrame(
        history,
        columns=["Emotion", "Timestamp"]
    )

    # ==================================================
    # SUMMARY METRICS
    # ==================================================
    total_conversations = len(df)

    latest_emotion = df.iloc[-1]["Emotion"]

    emotion_counts = (
        df["Emotion"]
        .value_counts()
        .reset_index()
    )

    emotion_counts.columns = [
        "Emotion",
        "Count"
    ]

    metric1, metric2, metric3 = st.columns(3)

    with metric1:
        st.metric(
            "Total Conversations",
            total_conversations
        )

    with metric2:
        st.metric(
            "Latest Emotion",
            latest_emotion
        )

    with metric3:
        st.metric(
            "Unique Emotions",
            len(emotion_counts)
        )

    st.divider()

    # ==================================================
    # CHARTS
    # ==================================================
    col1, col2 = st.columns(2)

    with col1:

        fig_bar = px.bar(
            emotion_counts,
            x="Emotion",
            y="Count",
            color="Emotion",
            text="Count",
            title="Emotion Distribution"
        )

        st.plotly_chart(
            fig_bar,
            use_container_width=True
        )

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

    # ==================================================
    # MOOD TREND
    # ==================================================
    st.subheader("📈 Mood Trend")

    emotion_scores = {
        "joy": 10,
        "love": 9,
        "optimism": 8,
        "happy": 8,
        "neutral": 6,
        "fear": 4,
        "sadness": 3,
        "anger": 2
    }

    trend_df = df.copy()

    trend_df["Score"] = trend_df["Emotion"].apply(
        lambda x: emotion_scores.get(
            str(x).lower(),
            5
        )
    )

    trend_df["Timestamp"] = pd.to_datetime(
        trend_df["Timestamp"]
    )

    fig_line = px.line(
        trend_df.sort_values("Timestamp"),
        x="Timestamp",
        y="Score",
        markers=True,
        title="Mood Trend Over Time"
    )

    st.plotly_chart(
        fig_line,
        use_container_width=True
    )

    # ==================================================
    # WELLNESS SCORE
    # ==================================================
    avg_score = int(
        trend_df["Score"].mean() * 10
    )

    st.subheader("🌟 Wellness Score")

    st.progress(avg_score / 100)

    st.success(
        f"Current Wellness Score: {avg_score}/100"
    )

else:

    st.info(
        "No emotion history available yet."
    )
