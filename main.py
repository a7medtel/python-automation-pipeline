from scripts.api_fetcher import fetch_users
from scripts.csv_analyzer import analyze_csv
from scripts.ai_report import generate_ai_report
from scripts.email_sender import send_email
from scripts.change_detector import has_new_data

count = fetch_users()

if has_new_data(count):
    print("New data detected — running pipeline...")
    analyze_csv()
    generate_ai_report()
    send_email()
else:
    print("No new data — skipping.")