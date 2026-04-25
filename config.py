import os
from dotenv import load_dotenv

load_dotenv()

INPUT_FOLDER = os.getenv("INPUT_FOLDER", "data/incoming_files")
OUTPUT_FOLDER = os.getenv("OUTPUT_FOLDER", "data/output")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")