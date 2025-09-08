# 🤖 GenAI Chatbot (Gemini Powered)

[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-✔️-green)](https://streamlit.io/)
[![Gemini API](https://img.shields.io/badge/Gemini-API-orange)](https://ai.google.com/)

A **Streamlit-based chatbot** powered by Google Gemini API. Chat with a Gemini language model in real-time. The project also includes a `model.py` file to list available models for your specific Gemini API key.

---

## 📂 Project Structure

```text
GenAI-Chatbot/
├── app.py               # Main Streamlit chatbot application
├── key.env.example      # Example file for Gemini API key (do NOT upload real key)
├── model.py             # Script to list available Gemini models for your API key
├── requirements.txt     # Python dependencies
├── .gitignore           # Files/folders to ignore in GitHub
└── README.md            # Project instructions and documentation
```


---

## ⚙️ Purpose of `model.py`

The `model.py` file is included to **check which Gemini models are available** for your API key. This is important because:

- Not all models are available for every account.  
- Some models support `generateContent`, while others support embeddings or audio generation.  
- Helps avoid 404 errors in your chatbot (`app.py`).
 Run:
```bash
python model.py
```

It will print all models your API key can access along with their supported methods.

**To run the project :**

# 🛠 Setup Instructions

**1. Clone the repository**
 ```bash
git clone https://github.com/Shanupk17/GenAI-Chatbot.git
cd GenAI-Chatbot
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Add your Gemini API key**

- Copy the example environment file to create your own:
```bash
cp key.env.example key.env   # Linux/macOS
copy key.env.example key.env # Windows
```
- Open key.env and add your Gemini API key:
```bash
GEMINI_API_KEY=your_actual_gemini_api_key_here
```
**Important: Never commit key.env to GitHub; it contains sensitive credentials.**

**4. Run the chatbot**
```bash
streamlit run app.py
```
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/8ae94529-673b-481d-a4ec-2a29bda2c84b" />


-A browser window will open showing the chatbot interface.

-Type your message in the input box.

-The bot responds in real-time using the Gemini API.

-All messages are stored in session state for conversation history.
```
💡 Usage Example
🧑 You: Hello
🤖 Bot: Hi! How can I help you today?

```
You can continue typing multiple messages.

The conversation will appear sequentially with your inputs and bot responses.

# ⚠️ Notes

- Free-tier API keys have daily and per-minute usage limits. Exceeding them will return 429 quota exceeded errors.

- Use model.py to confirm which models are valid for your API key.

- Only commit the example .env file (key.env.example), never your real API key.

# 📦 Dependencies

- streamlit – Web UI for the chatbot

- google-generativeai – Access Gemini API

- python-dotenv – Load environment variables from .env file

- Install all dependencies:
```
pip install -r requirements.txt
```

## ⚠️ Limitations

**1. API Key Quotas**

- Free-tier Gemini API keys have daily and per-minute usage limits.

- Exceeding these limits may return 429 quota exceeded errors, preventing further requests until the quota resets.

**2.Model Availability**

- Not all Gemini models are available to every API key.

- Use model.py to check which models your API key can access and their supported methods.

# 👨‍💻 Author

**Santha.P**

# 🔗 Useful Links

[Gemini API Key](https://aistudio.google.com/apikey)


