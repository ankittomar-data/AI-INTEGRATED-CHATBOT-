"""AI Integrated Chatbot - Flask backend using the Anthropic API."""
import os
from flask import Flask, jsonify, render_template, request
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = Anthropic()  # reads ANTHROPIC_API_KEY from environment
MODEL = os.getenv("CLAUDE_MODEL", "claude-sonnet-5-5")
SYSTEM_PROMPT = (
    "You are a friendly study assistant for college students. "
    "Explain things clearly and keep answers concise."
)
MAX_TURNS = 20  # keep only the last N messages to limit cost


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    messages = data.get("messages", [])
    if not messages:
        return jsonify(error="No messages provided."), 400
    try:
        reply = client.messages.create(
            model=MODEL,
            max_tokens=1000,
            system=SYSTEM_PROMPT,
            messages=messages[-MAX_TURNS:],
        )
        return jsonify(reply=reply.content[0].text)
    except Exception as e:
        return jsonify(error=f"AI request failed: {e}"), 500


if __name__ == "__main__":
    app.run(debug=True)
