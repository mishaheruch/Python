def most_frequent_word(text):
    words = text.split()
    words_count = {}
    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1
    return max(words_count, key=words_count.get)

print(most_frequent_word("кіт спить кіт їсть кіт грає"))
print(most_frequent_word("a b a c b a"))