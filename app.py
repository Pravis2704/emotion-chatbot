import streamlit as st
from transformers import pipeline
import sqlite3
import pandas as pd
from datetime import datetime
from utils.responder import generate_response

# Load model (once)
@st.cache_resource
def load_emotion_model():
    return pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=1)

emotion_model = load_emotion_model()

# SQLite setup
conn = sqlite3.connect("data/emotions.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        message TEXT,
        emotion TEXT,
        response TEXT,
        timestamp TEXT
    )
''')
conn.commit()

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🧠 Emotion-Aware Chatbot")
st.write("I understand your feelings and respond empathetically. Keep chatting!")

# Display chat history
for chat in st.session_state.messages:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**Bot ({chat['emotion']}):** {chat['bot']}")

# New user input
user_input = st.text_input("You:", key="user_input")

if st.button("Send"):
    if user_input.strip() != "":
        # Predict emotion
        try:
            result = emotion_model(user_input)
            emotion = result[0][0]['label']
        except Exception:
            emotion = "neutral"

        # Generate reply
        bot_reply = generate_response(emotion, user_input)


        # Add to chat history
        st.session_state.messages.append({
            "user": user_input,
            "emotion": emotion,
            "bot": bot_reply
        })

        # Save to DB
        cursor.execute('''
            INSERT INTO logs (message, emotion, response, timestamp)
            VALUES (?, ?, ?, ?)
        ''', (user_input, emotion, bot_reply, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()

        # Clear input box after sending
        st.rerun()


# Developer tools
st.sidebar.subheader("🛠️ Developer Tools")
if st.sidebar.checkbox("Show Logs"):
    df_logs = pd.read_sql_query("SELECT * FROM logs ORDER BY id DESC", conn)
    st.sidebar.dataframe(df_logs)
