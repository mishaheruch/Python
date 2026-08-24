def count_vowels(text):
    total = 0
    vowels = "aeiou"
    for char in text:
        if char in vowels:
            total += 1
    return total

print(count_vowels("hello"))
print(count_vowels("python"))