# Python Automation Pipeline 🐍

A production-ready automation pipeline built with Python that fetches live data from APIs, analyzes it with pandas, generates AI-powered insights, and delivers automated email reports — all running on a daily schedule with smart change detection.

## Features
- Fetches live user data from REST APIs automatically
- Analyzes and groups data by city using pandas
- Generates AI-style insight reports from raw data
- Sends automated email reports with CSV and text attachments
- Smart change detection — skips execution if data hasn't changed
- Logs all operations to a persistent log file
- Organized file management by extension type

## Tech Stack
- **Python 3** — core language
- **pandas** — data analysis and processing
- **requests** — REST API integration
- **smtplib** — automated email delivery
- **python-dotenv** — secure environment variable management
- **Windows Task Scheduler** — daily automated execution

## Project Structure
```
automation/
├── main.py                  # Entry point
├── config.py                # Configuration and env variables
├── requirements.txt         # Dependencies
├── .env.example             # Environment variables template
├── .gitignore
├── scripts/
│   ├── api_fetcher.py       # Fetches data from REST API
│   ├── csv_analyzer.py      # Analyzes and groups data
│   ├── ai_report.py         # Generates insight reports
│   ├── email_sender.py      # Sends email with attachments
│   ├── change_detector.py   # Detects new data before running
│   └── file_organizer.py    # Organizes files by extension
├── data/
│   ├── incoming_files/      # Input files
│   └── output/              # Generated reports
├── logs/
│   └── app.log              # Execution logs
└── tests/
└── test_file_organizer.py
```
## How It Works
API (Internet) → Fetch Data → Change Detection → CSV Analysis → AI Report → Email Delivery

1. Fetches 150 users from a live API
2. Checks if data has changed since last run
3. If new data → runs the full pipeline
4. If no change → skips and logs "No new data"

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/a7medtel/python-automation-pipeline.git
cd python-automation-pipeline
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

```bash
cp .env.example .env
```

Edit `.env` with your values:

```env
SENDER_EMAIL=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
RECEIVER_EMAIL=receiver@gmail.com
INPUT_FOLDER=data/incoming_files
OUTPUT_FOLDER=data/output
```

> **Note:** Use a Gmail App Password, not your regular password. Generate one at: https://myaccount.google.com/apppasswords

### 4. Run the pipeline
```bash
python main.py
```

### 5. Automate with Task Scheduler (Windows)
- Open Task Scheduler
- Create Basic Task
- Set trigger: Daily at 9:00 AM
- Action: `python main.py`
- Start in: project directory

## Key Concepts Demonstrated
- **Separation of Concerns** — each script has one responsibility
- **Environment Variables** — secure credential management
- **Error Handling** — try/except with logging
- **Change Detection** — smart execution using JSON snapshots
- **Data Normalization** — cleaning column names before processing
- **Logging** — persistent operation history

## Author
**Ahmed El-Telbani**
Automation Engineer | Python | n8n | AI Workflows

[![GitHub](https://img.shields.io/badge/GitHub-a7medtel-black?logo=github)](https://github.com/a7medtel)
