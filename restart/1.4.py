def reverse_words(sentence):
    sentence = sentence.split()
    sentence.reverse()
    return " ".join(sentence)


print(reverse_words("я люблю python"))
print(reverse_words("hello world"))