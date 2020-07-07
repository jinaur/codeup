import sys
sys.setrecursionlimit(100000)
N = int(input())


def myfunc(n) :
    if n == N :
        return n
    return n + myfunc(n+1) 


x = myfunc(1)
print(x)