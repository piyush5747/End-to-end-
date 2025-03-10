from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Facebook Graph API settings
PAGE_ACCESS_TOKEN = "YOUR_PAGE_ACCESS_TOKEN"  # 🔥 Yahan apna page token daalo
GRAPH_API_URL = "https://graph.facebook.com/v18.0/me/messages"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        recipient_id = request.form["recipient_id"]  # Facebook UID
        message = request.form["message"]  # Message text

        payload = {
            "recipient": {"id": recipient_id},
            "message": {"text": message},
            "messaging_type": "RESPONSE",
        }

        headers = {
            "Authorization": f"Bearer {PAGE_ACCESS_TOKEN}",
            "Content-Type": "application/json",
        }

        response = requests.post(GRAPH_API_URL, json=payload, headers=headers)
        
        if response.status_code == 200:
            return "Message Sent Successfully!"
        else:
            return f"Error: {response.text}"

    return """
    <h2>Facebook Messenger Auto-Sender</h2>
    <form method="post">
        <label>Recipient Facebook ID:</label><br>
        <input type="text" name="recipient_id" required><br><br>
        
        <label>Message:</label><br>
        <textarea name="message" required></textarea><br><br>
        
        <button type="submit">Send Message</button>
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True, port=5000)