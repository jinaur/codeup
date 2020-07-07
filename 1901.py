N = int(input())

def myfunc(n) :
    print(n)
    if n == N :
        return
    myfunc(n-1)

myfunc(1)