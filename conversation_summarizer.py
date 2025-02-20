import openai
import os
from dotenv import load_dotenv

# Load OpenAI API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_conversation(conversation):
    prompt = f"Summarize the following conversation succinctly:\n\n{conversation}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert summarizer."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    print("Paste your conversation transcript (end with an empty line):")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    conversation = "\n".join(lines)
    summary = summarize_conversation(conversation)
    print("\nConversation Summary:\n", summary)
