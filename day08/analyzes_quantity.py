import os
import csv
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(BASE_DIR, "data")
TARGET_DATE = datetime(2020, 3, 1)

hired_after_count = 0
state_counts = {}

def parse_date(date_str):
    for fmt in ["%Y-%m-%d", "%m/%d/%Y"]:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None

for filename in os.listdir(DATA_FOLDER):
    if filename.endswith(".csv"):
        file_path = os.path.join(DATA_FOLDER, filename)

        for encoding in ["utf-8-sig", "utf-16", "latin-1"]:
            try:
                with open(file_path, newline="", encoding=encoding) as csvfile:
                    reader = csv.DictReader(csvfile)

                    for row in reader:
                        hire_date_str = row["Hire Date"].strip()

                        if not hire_date_str:
                            continue

                        hire_date = parse_date(hire_date_str)

                        if hire_date is None:
                            continue

                        if hire_date > TARGET_DATE:
                            hired_after_count += 1

                        state = row["State"]
                        state_counts[state] = state_counts.get(state, 0) + 1
                break
            except (UnicodeDecodeError, KeyError):
                continue

print("Результат аналізу даних:")
print(f"{hired_after_count} осіб було найнято на роботу після 1 березня 2020 року")
print("Розподіл за штатом проживання:")

for state in sorted(state_counts):
    print(f"{state}: {state_counts[state]}")