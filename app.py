import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# -------------------
# Load API key from key.env
# -------------------
load_dotenv("key.env")  # Load environment variables from key.env
api_key = os.getenv("GEMINI_API_KEY")   # Get the key

if not api_key:
    st.error("⚠️ Please set the GEMINI_API_KEY in key.env file.")
    st.stop()

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-pro-latest")


# -------------------
# Streamlit UI
# -------------------
st.set_page_config(page_title="GenAI Chatbot", page_icon="🤖", layout="centered")
st.title("🤖 GenAI Chatbot (Gemini Powered)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.text_input("You: ", "")

if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate bot response
    response = model.generate_content(
        [{"role": m["role"], "parts": [m["content"]]} for m in st.session_state.messages]
    )

    bot_reply = response.text
    st.session_state.messages.append({"role": "model", "content": bot_reply})

# Display conversation
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"🧑 **You:** {msg['content']}")
    else:
        st.markdown(f"🤖 **Bot:** {msg['content']}")
    st.write("---")
