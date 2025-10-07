from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import traceback

app = Flask(__name__)
CORS(app)

# 🔑 Get credentials from environment variables (set these in Render dashboard)
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))

# 👇 All form messages will be sent to your inbox
MY_INBOX = os.getenv("MY_INBOX", "codis1723@gmail.com")


# 🏠 Root route for testing
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "✅ Flask Email API is running"}), 200


# 📬 Function to send email
def send_email(subject, body):
    try:
        if not SENDER_EMAIL or not SENDER_PASSWORD:
            return {"success": False, "error": "Email credentials not configured."}

        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = MY_INBOX
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)

        return {"success": True, "message": f"✅ Email sent successfully to {MY_INBOX}"}
    except Exception as e:
        traceback.print_exc()
        return {"success": False, "error": str(e)}


# 📩 API endpoint for frontend contact form
@app.route("/sendemail", methods=["POST"])
def api_send_email():
    try:
        data = request.get_json()
        user_email = data.get("email")
        subject = data.get("subject", "New Form Submission")
        message = data.get("message", "")

        if not user_email:
            return jsonify({"success": False, "error": "User email is required"}), 400

        # Nicely formatted email body
        body = f"""
You received a new message from your website contact form:

From: {user_email}
Subject: {subject}

Message:
{message}
"""

        result = send_email(subject, body)
        return jsonify(result), (200 if result["success"] else 500)

    except Exception as e:
        traceback.print_exc()
        return jsonify({"success": False, "error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
