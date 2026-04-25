import pandas as pd
from config import OUTPUT_FOLDER
import os


def analyze_csv():
    file_path = os.path.join(OUTPUT_FOLDER, "users.csv")

    df = pd.read_csv(file_path)

    #  clean column names
    df.columns = df.columns.str.strip().str.lower()

    print("=== RAW DATA ===")
    print(df.head())

    # group by city
    grouped = df.groupby("city").size().reset_index(name="count")

    print("\n=== USERS PER CITY ===")
    print(grouped)

    # grouped
    report = grouped.sort_values(by="count", ascending=False)

    # save report
    report_path = os.path.join(OUTPUT_FOLDER, "city_report.csv")
    report.to_csv(report_path, index=False)

    print(f"\nReport saved to {report_path}")