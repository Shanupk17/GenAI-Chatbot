from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load model & tokenizer
model_name = "microsoft/DialoGPT-medium"  # small/medium/large available
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

print("🤖 Chatbot is ready! Type 'quit' to stop.\n")

chat_history_ids = None
step = 0

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("Chatbot: Goodbye 👋")
        break

    # Encode user input
    new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')

    # Append tokens to chat history (for context)
    if chat_history_ids is not None:
        bot_input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1)
    else:
        bot_input_ids = new_input_ids

    # Generate a response
    chat_history_ids = model.generate(
        bot_input_ids, 
        max_length=1000, 
        pad_token_id=tokenizer.eos_token_id,
        temperature=0.7,
        top_p=0.9
    )

    # Decode and print response
    bot_reply = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    print(f"Chatbot: {bot_reply}")
