# 📧 Flask Email API

A simple **Flask-based email API** that allows you to send emails from your frontend (e.g., a contact form on a GitHub Pages website) through Gmail’s SMTP.

The API is designed to be hosted on **Render**, while your frontend can be hosted on **GitHub** Pages (or anywhere else).

---

# 🚀 Features

- Send emails securely using Gmail SMTP

- Environment variable–based credentials (no hardcoded secrets)

- CORS enabled → can be used directly with a frontend (HTML/JS)

- Ready for deployment on Render

---

# 🛠️ Tech Stack

- Backend: Python, Flask, Flask-CORS

- Email: Gmail SMTP

- Deployment: Render (for API), GitHub Pages (for frontend)

---

# Project Files
``` bash 
flask-email-api/
│── app.py              # Main Flask app
│── requirement.txt    # Python dependencies
│── Procfile            # For Render deployment
│── README.md           # Project docs

```
---
# ⚙️ Local Setup

1. Clone Repo 
``` bash 
git clone https://github.com/BIGUDOM/flask-email-api.git
cd flask-email-api
```

2. Install dependecies 
``` bash 
pip install -r requirement.txt
```

3. Set environment variable 
``` ini 
SENDER_EMAIL=your-gmail@gmail.com
SENDER_PASSWORD=your-gmail-app-password
MY_INBOX=your-gmail@gmail.com
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

4. Run locally
```bash 
python app.py
```



