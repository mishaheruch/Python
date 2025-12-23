def error():
    x = input("Please enter an integer: ")  #тут было int, а не float. Потому яка int не принимает дробные числа
    if not x.isdigit(): #проверяем на число 
        print("Це не ціле число")
        return
    x = int(x)
    if x % 2 == 0: #проверяем на четность
        print("Це парне число")
    else:
        print("Це непарне число")

error()