def level_up_age():
    age = int(input('Скільки тобі років: ')) 
    date = int(input('Місяць народження(числами): '))
    day = int(input('День народження: '))
    name = input('Як тебе звати: ') 
    age += 1
    print(f"Привіт, {name}! Ти народився в {2026 - age}.{date}.{day}. Тобі через рік буде {age}.")
level_up_age()