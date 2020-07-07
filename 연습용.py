N = int(input())


def myfunc(n) :
    if n <= 2 :
        return 1
    else :
        return myfunc(n-1) + myfunc(n-2)
        
r = myfunc(N)
r = r%10009
print(r)