a, b = map(int, input().split())

def my_func(a, b) :
    if b < 30 and  a == 0 :
        a = 23
        b += 30
        print(a, b)
        return 
    elif b < 30 :
        a -= 1
        b += 30
        print(a, b)
        return 
    
    b -= 30
    print(a, b)
    return 

r = my_func(a, b)

