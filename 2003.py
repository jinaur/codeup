n = int(input())

def my_func(a, b, c) :
    for i in range(0, n) :
        print(n*a+n*b+n*c)
    
    return

a = "*"
b = "x"
c = "*"
r = my_func(a, b, c)    

a = " "
c = "x"
r = my_func(a, b, c)    

a = "*"
b = " "
c = "*"
r = my_func(a, b, c)    

