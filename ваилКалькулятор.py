p = input("введите операцию +,-,/,*,exit.")
while p != "exit": 
        if p =="+" :
            y = int(input("Введите первое слагаемое"))
            u = int(input("Введите второе слагаемое"))
            c = u+y
            print(c)
        elif p =="-":
            y = int(input("Введите  уменьшаемое"))
            u = int(input("Введите  вычитаемое"))
            c = y-u
            print(c)
        elif p =="*":
            y = int(input("Введите первый множитель"))
            u = int(input("Введите второй множитель "))
            c = y*u
            print(c)
        elif p =="/":
            y = int(input("Введите делимое"))
            u = int(input("Введите делитель"))
            c = y/u
            print(c)
        p = input("введите операцию +,-,/,*,exit.")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
