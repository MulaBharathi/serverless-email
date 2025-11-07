import json
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

def send_email(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        receiver_email = body.get('receiver_email')
        subject = body.get('subject')
        body_text = body.get('body_text')

        if not receiver_email or not subject or not body_text:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "receiver_email, subject, and body_text are required"})
            }

        message = MIMEMultipart()
        message['From'] = EMAIL_USER
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body_text, 'plain'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(message)

        return {
            "statusCode": 200,
            "body": json.dumps({"message": f"Email sent successfully to {receiver_email}"})
        }

    except smtplib.SMTPAuthenticationError:
        return {
            "statusCode": 401,
            "body": json.dumps({"message": "Authentication failed. Check email credentials."})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": f"Internal Server Error: {str(e)}"})
        }

def root(event, context):
    return {
        "statusCode": 200,
        "body": "Serverless Email API is running!"
    }

