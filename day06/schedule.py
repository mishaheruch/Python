def lessons():
    count = int(input("Скільки уроків буде завтра? "))
    subjects = []
    for i in range(count):
        subject = input(f"Час початку уроку та назва {i + 1}: ")
        subjects.append(subject)
    for i, subject in enumerate(subjects, start=1):
        print(f"Урок {i}: {subject}")
lessons()