n = int(input())

def my_func(n) :
    e = "prime"
    for i in range(2, n) :
        if n%i == 0 :
            e = "composite"
            return e
    return e        

print(my_func(n))

