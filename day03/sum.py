def sum (): 
    numbers = input("Please enter an integer: ")
    numbers_list = numbers.split(" ")  
    for number in numbers_list:
        for char in number:
            if char not in "0123456789-.": # супер!-
                print ("Error: invalid input")
                return

    sum = 0 
    for number in numbers_list:  
         sum += float(number) 
         
    print (sum) 

sum () 