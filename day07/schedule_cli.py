import sys
import json
from pathlib import Path


FILE = "schedule.json"

def load_schedule():
    if not Path(FILE).exists():
        return []

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)
    
def save_schedule(schedule):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(schedule, f, indent=2, ensure_ascii=False)
        
def add_lesson(time, title):
    schedule = load_schedule()
    lesson = {
        "time": time,
        "title": title
    }
    schedule.append(lesson) # Додаємо новий урок до розкладу
    save_schedule(schedule) # Зберігаємо оновлений розклад
    print(f"Урок {len(schedule)} успішно додано: {title}, час {time}")

def list_lessons():
    schedule = load_schedule()
    if not schedule:
        print("Розклад порожній.")
        return

    print(f"Розклад уроків (усього {len(schedule)} уроків)")
    for i, lesson in enumerate(schedule, start=1):
        print(f"Урок {i} – {lesson['title']}, час {lesson['time']}")
        
def main():
    if len(sys.argv) < 2:
        print("  python3 schedule_cli.py add ЧАС НАЗВА_УРОКУ")
        print("  python3 schedule_cli.py list")
        return

    command = sys.argv[1]
    if command == "add":
        if len(sys.argv) < 4:
            print("Використання: python3 schedule_cli.py add ЧАС НАЗВА_УРОКУ")
            return
        time = sys.argv[2]
        title = " ".join(sys.argv[3:])
        add_lesson(time, title)
    elif command == "list":
        list_lessons()
    else:
        print(f"Невідома команда: {command}")
        
if __name__ == "__main__":
    main()
