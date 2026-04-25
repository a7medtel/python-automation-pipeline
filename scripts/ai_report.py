import pandas as pd
import os
from config import OUTPUT_FOLDER

def generate_ai_report():
    file_path = os.path.join(OUTPUT_FOLDER, "department_report.csv")
    df = pd.read_csv(file_path)
    print(df.columns)
    report_text = "AI Analysis Report:\n\n"

    max_salary = df["avg_salary"].max()
    min_salary = df["avg_salary"].min()

    for _, row in df.iterrows():
        dept = row["department"]
        salary = row["avg_salary"]

        if salary == max_salary:
            insight = "has the highest salary levels in the company."
        elif salary == min_salary:
            insight = "has the lowest salary levels and may need review."
        else:
            insight = "has average salary levels compared to other departments."

        report_text += f"- {dept}: {insight}\n"

    print(report_text)

    output_path = os.path.join(OUTPUT_FOLDER, "ai_report.txt")
    with open(output_path, "w") as f:
        f.write(report_text)

    print(f"\nAI report saved to {output_path}")