# 🤖 GenAI Chatbot (Gemini Powered)

[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-✔️-green)](https://streamlit.io/)
[![Gemini API](https://img.shields.io/badge/Gemini-API-orange)](https://ai.google.com/)

A **Streamlit-based chatbot** powered by Google Gemini API. Chat with a Gemini language model in real-time. The project also includes a `model.py` file to list available models for your specific Gemini API key.

---

## 📂 Project Structure
'''GenAI-Chatbot/
│
├── app.py # Main Streamlit chatbot application
├── key.env.example # Example file for Gemini API key (do NOT upload real key)
├── model.py # Script to list available Gemini models for your API key
├── requirements.txt # Python dependencies
├── .gitignore # Files/folders to ignore in GitHub
└── README.md # Project instructions and documentation '''


---

## ⚙️ Purpose of `model.py`

The `model.py` file is included to **check which Gemini models are available** for your API key. This is important because:

- Not all models are available for every account.  
- Some models support `generateContent`, while others support embeddings or audio generation.  
- Helps avoid 404 errors in your chatbot (`app.py`).  

**To run:**

```bash
python model.py
🛠 Setup Instructions
1. Clone the repository
git clone https://github.com/yourusername/GenAI-Chatbot.git
cd GenAI-Chatbot

2. Install dependencies
pip install -r requirements.txt

3. Add your Gemini API key

Copy the example environment file to create your own:

cp key.env.example key.env   # Linux/macOS
copy key.env.example key.env # Windows


Open key.env and add your Gemini API key:

GEMINI_API_KEY=your_actual_gemini_api_key_here


Important: Never commit key.env to GitHub; it contains sensitive credentials.

4. Run the chatbot
streamlit run app.py


A browser window will open showing the chatbot interface.

Type your message in the input box.

The bot responds in real-time using the Gemini API.

All messages are stored in session state for conversation history.

💡 Usage Example
🧑 You: Hello
🤖 Bot: Hi! How can I help you today?


You can continue typing multiple messages.

The conversation will appear sequentially with your inputs and bot responses.

⚠️ Notes

Free-tier API keys have daily and per-minute usage limits. Exceeding them will return 429 quota exceeded errors.

Use model.py to confirm which models are valid for your API key.

Only commit the example .env file (key.env.example), never your real API key.

📦 Dependencies

streamlit – Web UI for the chatbot

google-generativeai – Access Gemini API

python-dotenv – Load environment variables from .env file

Install all dependencies:

pip install -r requirements.txt

👨‍💻 Author

Santha P.

🔗 Useful Links

Gemini API Documentation

Streamlit Documentation

