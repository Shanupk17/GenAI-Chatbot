import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key
load_dotenv("key.env")
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in key.env!")

# Configure Gemini
genai.configure(api_key=api_key)

# List available models
models = genai.list_models()
print("Available models for this API key:")
for m in models:
    print(f"- {m.name} (supports: {m.supported_generation_methods})")
