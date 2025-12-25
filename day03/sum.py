def sum (): 
    x = input("Please enter an integer: ")
    y = x.split(" ")  
    for i in y: #проверяем на число 
        if not i.isdigit():
            print("ПОМИЛКА")
            return

    x = 0 
    for i in y:  
         x = x + float(i) 
         
    print (x) 
    

sum () 