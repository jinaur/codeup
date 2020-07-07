n = int(input())

def my_func(n) :
    a = n % 2
    b = n // 2

    if b == 0 :
        return(str(a))

    return my_func(b) + str(a)

r = my_func(n)
print(r) 