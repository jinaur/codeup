N = int(input())


def myfunc(n) :
    if n == 1 :
        return 1
    return n * myfunc(n - 1)



r = myfunc(N)
print(r)