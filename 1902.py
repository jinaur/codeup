N = int(input())

def myfunc(n) :
    print(n)
    if n == 1 :
        return
    myfunc(n-1)

myfunc(N)