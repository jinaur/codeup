a, b = map(int, input().split())

def myfunc(a, b) :
    if a%2 == 1 :
        print(a, end=" ")
    if a >= b :
        return
    myfunc(a+1, b)
    return


myfunc(a, b)