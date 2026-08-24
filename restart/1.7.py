def first_unique_char(text):
    total = {}
    for word in text:
        if word not in total:
            total[word] = 1
        else:
            total[word] += 1
    return min(total)
print(first_unique_char("swiss"))
print(first_unique_char("aabbcc"))