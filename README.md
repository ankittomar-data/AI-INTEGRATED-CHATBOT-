# AI Integrated Chatbot

A web-based AI chatbot built with Python (Flask) and vanilla HTML/CSS/JS.

## Features
- Real-time AI chat with conversation memory
- Clean, responsive interface with dark mode
- API key kept safely on the server (never exposed to the browser)

## Tech stack
Python, Flask, HTML, CSS, JavaScript

## Setup
```bash
git clone https://github.com/ankittomar-data/ai-chatbot.git
cd ai-chatbot
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # then paste your API key into .env
python app.py
```
Open http://127.0.0.1:5000

## Project structure
```
app.py                Flask server + AI integration
templates/index.html  Chat interface
requirements.txt      Dependencies
```

## Future improvements
Streaming replies, user login, saving chat history, file upload support.

## Author
Ankit Tomar
