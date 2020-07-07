N = int(input())


def myfunc(n) :
    if n < 3 :
        return 1
    else :
        return myfunc(n-1) + myfunc(n-2)


r = myfunc(N)
print(r)