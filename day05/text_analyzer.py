from collections import Counter # Імпортуємо Counter для підрахунку слів
def analyze_text():
    text = input("Текст: ") 
    
    
    analyze_text = text.lower() # Робимо всі слова з маленькими літерами
    words = analyze_text.split() # Розбиваємо текст на слова
    slova = len(words) # Підраховуємо загальну кількість слів
    sentences = [s for s in text.split('.') if s.strip()] # Розбиваємо текст на речення за крапками
    sentence_count = len(sentences) # Підраховуємо кількість речень
    counter = Counter(words) # Підраховуємо кількість кожного слова
    word, count = counter.most_common(1)[0] # Знаходимо найпоширеніше слово та його кількість повторів
    print(f"Найпоширеніше слово: {word}, Кількість повторів: {count}, Загальна кількість слів: {slova}, Кількість речень: {sentence_count}")


analyze_text()


# я користувався chat gpt він. мені допомагав знаходити помилки у коді коли я вже не міг знайти сам 