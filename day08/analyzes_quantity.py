import os
import csv
from datetime import datetime

DATA_FOLDER = "data"
TARGET_DATE = datetime(2020, 3, 1)

hired_after_count = 0
state_counts = {}

for filename in os.listdir(DATA_FOLDER):
    if filename.endswith(".csv"):
        file_path = os.path.join(DATA_FOLDER, filename)

        with open(file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                hire_date = datetime.strptime(row["Hire Date"], "%Y-%m-%d")

                if hire_date > TARGET_DATE:
                    hired_after_count += 1

                state = row["State"]
                state_counts[state] = state_counts.get(state, 0) + 1

print("Результат аналізу даних:")
print(f"{hired_after_count} осіб було найнято на роботу після 1 березня 2020 року")
print("Розподіл за штатом проживання:")

for state in sorted(state_counts):
    print(f"{state}: {state_counts[state]}")
