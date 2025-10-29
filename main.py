from flask import Flask, request
import requests
import os

app = Flask(__name__)

# TOKEN: Put your token in Render environment variable named TOKEN
# or replace os.environ.get("TOKEN") with the actual token string (not recommended).
TOKEN = os.environ.get("7548974165:AAESQle_jQOVG7q_aoj1g0s8mQfhRDNiO9o")  # <-- keep token secret!
URL = f"https://api.telegram.org/bot{TOKEN}"

@app.route('/')
def home():
    return "Bot ishga tushdi ✅"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    if not data:
        return {"ok": False, "error": "no json received"}, 400

    # Handle messages
    message = data.get("message") or data.get("edited_message")
    if message:
        chat_id = message["chat"]["id"]
        text = message.get("text", "")
        # oddiy javob: yuborilgan matnni qaytaradi
        reply = f"Siz yubordingiz: {text}"
        requests.post(f"{URL}/sendMessage", json={"chat_id": chat_id, "text": reply})

    return {"ok": True}

if __name__ == '__main__':
    # Render default port is $PORT, but for local testing it uses 10000
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
