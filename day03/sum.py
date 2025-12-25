def sum (): 
    dodat = input("Please enter an integer: ")
    sum = dodat.split(" ")  
    for i in sum: #проверяем на числої
        for ch in i:
            if ch not in "0123456789-.":
                print ("Error: invalid input")
                return

    dodat = 0 
    for i in sum:  
         dodat = dodat + float(i) 
         
    print (dodat) 


sum () 