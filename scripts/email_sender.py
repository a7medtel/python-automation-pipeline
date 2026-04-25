import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
from config import OUTPUT_FOLDER
import logging

load_dotenv()

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%d %b %Y, %H:%M:%S"
)


def send_email():
    sender_email = os.getenv("SENDER_EMAIL")
    password = os.getenv("EMAIL_PASSWORD")
    receiver_email = os.getenv("RECEIVER_EMAIL")

    # files to attach
    csv_path = os.path.join(OUTPUT_FOLDER, "department_report.csv")
    ai_path = os.path.join(OUTPUT_FOLDER, "ai_report.txt")
    users_path = os.path.join(OUTPUT_FOLDER, "users.csv")

    # read AI report content
    with open(ai_path, "r") as f:
        ai_content = f.read()

    msg = EmailMessage()
    msg["Subject"] = "Automation Report (Data + AI)"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    # content
    msg.set_content(f"""
Hello,

Here is the AI-generated analysis:

{ai_content}

Attached:
- CSV Report
- AI Report

Regards,
Automation System
""")

    # attach files
    for file_path in [csv_path, ai_path, users_path]:
        with open(file_path, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="octet-stream",
                filename=os.path.basename(file_path)
            )

    # send email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(sender_email, password)
            smtp.send_message(msg)

        print("Email sent successfully")
        logging.info("Email sent successfully")

    except Exception as e:
        print("Error sending email:", e)
        logging.error(f"Email error: {e}")