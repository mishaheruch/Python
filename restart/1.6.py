def most_common_letter(text):
    letter = {}
    for let in text:
        if let != " ":
            if let in letter:
                letter[let] += 1
            else:
                letter[let] = 1
    return max(letter, key=letter.get)

print(most_common_letter("привіт світ"))
print(most_common_letter("banana"))